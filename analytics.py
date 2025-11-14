from datetime import datetime, timedelta, timezone
from typing import List

from models import Completion, Habit


# -----------------------------------------
# Helper to convert ISO string -> datetime
# -----------------------------------------
def to_dt(iso: str) -> datetime:
    return datetime.fromisoformat(iso)


# -----------------------------------------
# Longest streak for one habit
# -----------------------------------------
def longest_streak_for(completions: List[Completion], periodicity: str) -> int:
    """
    Given completions for ONE habit, return their longest streak.
    """
    if not completions:
        return 0

    # Convert timestamps to datetime, sorted
    dates = sorted([to_dt(c.completed_at).date() for c in completions])

    streak = 1
    best = 1

    for i in range(1, len(dates)):
        prev = dates[i - 1]
        curr = dates[i]

        # Daily streak
        if periodicity == "daily":
            if curr == prev + timedelta(days=1):
                streak += 1
            else:
                streak = 1

        # Weekly streak
        elif periodicity == "weekly":
            if curr.isocalendar()[1] == prev.isocalendar()[1] + 1:
                streak += 1
            else:
                streak = 1

        best = max(best, streak)

    return best


# -----------------------------------------
# Longest streak overall
# -----------------------------------------
def longest_streak_overall(all_habits: List[Habit],
                           all_completions: List[Completion]) -> int:
    best = 0

    for habit in all_habits:
        comps = [c for c in all_completions if c.habit_id == habit.id]
        streak = longest_streak_for(comps, habit.periodicity)
        best = max(best, streak)

    return best