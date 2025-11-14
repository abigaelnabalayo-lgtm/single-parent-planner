from datetime import datetime, timezone
from typing import Optional, List, Tuple

from models import Habit, Completion
from repository import HabitRepository
from analytics import longest_streak_for


class HabitService:
    """
    High-level logic for working with habits.
    The CLI will call this layer instead of talking to the repository directly.
    """

    def __init__(self, repo: Optional[HabitRepository] = None) -> None:
        # allow injecting a repo (useful for tests later)
        self.repo = repo or HabitRepository()

    # ---------- Habit management ----------

    def create_habit(self, name: str, periodicity: str) -> Habit:
        """Create a new habit with a valid periodicity ('daily' or 'weekly')."""
        periodicity = periodicity.lower()
        if periodicity not in ("daily", "weekly"):
            raise ValueError("Periodicity must be 'daily' or 'weekly'.")
        return self.repo.create_habit(name=name, periodicity=periodicity)

    def list_habits(
        self,
        include_archived: bool = False,
        periodicity: Optional[str] = None,
    ) -> List[Habit]:
        """List habits with optional filters."""
        if periodicity:
            periodicity = periodicity.lower()
        return self.repo.list_habits(
            include_archived=include_archived,
            periodicity=periodicity,
        )

    def archive_habit(self, habit_id: int) -> None:
        """Archive a habit so it no longer shows in the default list."""
        habit = self.repo.get_habit(habit_id)
        if habit is None:
            raise ValueError(f"Habit with id {habit_id} not found.")
        self.repo.archive_habit(habit_id)

    def delete_habit(self, habit_id: int) -> None:
        """Permanently delete a habit (and its completions)."""
        habit = self.repo.get_habit(habit_id)
        if habit is None:
            raise ValueError(f"Habit with id {habit_id} not found.")
        self.repo.delete_habit(habit_id)

    # ---------- Completions ----------

    @staticmethod
    def _now_utc_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    def add_completion_now(self, habit_id: int) -> Completion:
        """Mark a habit as completed for 'now'."""
        habit = self.repo.get_habit(habit_id)
        if habit is None:
            raise ValueError(f"Habit with id {habit_id} not found.")
        if habit.is_archived:
            raise ValueError("Cannot complete an archived habit.")

        return self.repo.add_completion(
            habit_id=habit_id,
            completed_at=self._now_utc_iso(),
        )

    def add_completion_at(self, habit_id: int, completed_at_iso: str) -> Completion:
        """
        Mark a habit as completed at a specific UTC timestamp (used for backfilling).
        The timestamp is expected as an ISO string.
        """
        habit = self.repo.get_habit(habit_id)
        if habit is None:
            raise ValueError(f"Habit with id {habit_id} not found.")
        if habit.is_archived:
            raise ValueError("Cannot complete an archived habit.")

        return self.repo.add_completion(habit_id=habit_id, completed_at=completed_at_iso)

    def list_completions_for_habit(self, habit_id: int) -> List[Completion]:
        """Return all completion records for one habit."""
        return self.repo.list_completions_for_habit(habit_id)

    def list_all_completions(self) -> List[Completion]:
        """Return all completion records for all habits."""
        return self.repo.list_all_completions()

    # ---------- Analytics helpers ----------

    def longest_streak_for_habit(self, habit_id: int) -> int:
        """Calculate the longest streak for a single habit."""
        habit = self.repo.get_habit(habit_id)
        if habit is None:
            raise ValueError(f"Habit with id {habit_id} not found.")

        completions = self.repo.list_completions_for_habit(habit_id)
        return longest_streak_for(completions, habit.periodicity)

    def longest_streak_overall(self) -> Tuple[Optional[Habit], int]:
        """
        Return (habit, streak) for the habit with the longest streak overall.
        If there are no habits/completions yet, returns (None, 0).
        """
        habits = self.repo.list_habits(include_archived=False)
        completions = self.repo.list_all_completions()

        best_habit: Optional[Habit] = None
        best_streak = 0

        for habit in habits:
            comps = [c for c in completions if c.habit_id == habit.id]
            streak = longest_streak_for(comps, habit.periodicity)
            if streak > best_streak:
                best_streak = streak
                best_habit = habit

        return best_habit, best_streak