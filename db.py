import sqlite3
from pathlib import Path

# Path to the database file
DB_PATH = Path(__file__).parent / "planner.db"


def get_connection() -> sqlite3.Connection:
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Initialize the database with habits and completions tables."""
    conn = get_connection()
    cur = conn.cursor()

    # Create habits table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            periodicity TEXT NOT NULL CHECK (periodicity IN ('daily', 'weekly')),
            created_at TEXT NOT NULL,
            is_archived INTEGER NOT NULL DEFAULT 0
        );
        """
    )

    # Create completions table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER NOT NULL,
            completed_at TEXT NOT NULL,
            FOREIGN KEY (habit_id) REFERENCES habits (id) ON DELETE CASCADE
        );
        """
    )

    conn.commit()
    conn.close()