from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class Habit:
    id: Optional[int]      # database id (None before it is saved)
    name: str              # habit name
    periodicity: str       # "daily" or "weekly"
    created_at: str        # timestamp in UTC (ISO string)
    is_archived: bool = False

    @staticmethod
    def now_utc_iso() -> str:
        """Return the current time in UTC as an ISO string."""
        return datetime.now(timezone.utc).isoformat()


@dataclass
class Completion:
    id: Optional[int]      # database id (None before it is saved)
    habit_id: int          # id of the related habit
    completed_at: str      # timestamp in UTC (ISO string)