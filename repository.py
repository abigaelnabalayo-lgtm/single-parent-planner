from typing import Optional, List

from db import get_connection
from models import Habit, Completion


def row_to_habit(row) -> Habit:
    """Convert a database row into a Habit object."""
    return Habit(
        id=row["id"],
        name=row["name"],
        periodicity=row["periodicity"],
        created_at=row["created_at"],
        is_archived=bool(row["is_archived"]),
    )


def row_to_completion(row) -> Completion:
    """Convert a database row into a Completion object."""
    return Completion(
        id=row["id"],
        habit_id=row["habit_id"],
        completed_at=row["completed_at"],
    )


class HabitRepository:
    """Handles all reads and writes to the SQLite database."""

    def __init__(self) -> None:
        self.conn = get_connection()

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    # ---------- Habits ----------

    def create_habit(self, name: str, periodicity: str) -> Habit:
        """Create a new habit and save it to the database."""
        habit = Habit(
            id=None,
            name=name,
            periodicity=periodicity,
            created_at=Habit.now_utc_iso(),
            is_archived=False,
        )

        cur = self.conn.cursor()
        cur.execute(
            """
            INSERT INTO habits (name, periodicity, created_at, is_archived)
            VALUES (?, ?, ?, ?)
            """,
            (habit.name, habit.periodicity, habit.created_at, int(habit.is_archived)),
        )
        self.conn.commit()

        habit.id = cur.lastrowid
        return habit

    def list_habits(
        self,
        include_archived: bool = False,
        periodicity: Optional[str] = None,
    ) -> List[Habit]:
        """Return all habits, with optional filters."""
        cur = self.conn.cursor()

        query = "SELECT * FROM habits"
        conditions = []
        params: list = []

        if not include_archived:
            conditions.append("is_archived = 0")
        if periodicity:
            conditions.append("periodicity = ?")
            params.append(periodicity)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY id"

        cur.execute(query, params)
        rows = cur.fetchall()
        return [row_to_habit(row) for row in rows]

    def get_habit(self, habit_id: int) -> Optional[Habit]:
        """Return a single habit by id, or None if not found."""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM habits WHERE id = ?", (habit_id,))
        row = cur.fetchone()
        if row is None:
            return None
        return row_to_habit(row)

    def archive_habit(self, habit_id: int) -> None:
        """Mark a habit as archived."""
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE habits SET is_archived = 1 WHERE id = ?",
            (habit_id,),
        )
        self.conn.commit()

    def delete_habit(self, habit_id: int) -> None:
        """Permanently delete a habit (and its completions)."""
        cur = self.conn.cursor()
        cur.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        self.conn.commit()

    # ---------- Completions ----------

    def add_completion(self, habit_id: int, completed_at: str) -> Completion:
        """Add a completion record for a habit."""
        completion = Completion(
            id=None,
            habit_id=habit_id,
            completed_at=completed_at,
        )
        cur = self.conn.cursor()
        cur.execute(
            """
            INSERT INTO completions (habit_id, completed_at)
            VALUES (?, ?)
            """,
            (completion.habit_id, completion.completed_at),
        )
        self.conn.commit()
        completion.id = cur.lastrowid
        return completion

    def list_completions_for_habit(self, habit_id: int) -> List[Completion]:
        """Return all completions for one habit (ordered by time)."""
        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT * FROM completions
            WHERE habit_id = ?
            ORDER BY completed_at
            """,
            (habit_id,),
        )
        rows = cur.fetchall()
        return [row_to_completion(row) for row in rows]

    def list_all_completions(self) -> List[Completion]:
        """Return all completions for all habits."""
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM completions ORDER BY completed_at"
        )
        rows = cur.fetchall()
        return [row_to_completion(row) for row in rows]