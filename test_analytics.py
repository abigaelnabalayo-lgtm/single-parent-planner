from datetime import datetime, timezone, timedelta
from typing import List

from analytics import longest_streak_for
from models import Completion


def make_completion(habit_id: int, days_ago: int) -> Completion:
    """Helper to create a completion 'days_ago' days before now."""
    day = datetime.now(timezone.utc).date() - timedelta(days=days_ago)
    dt = datetime.combine(day, datetime.min.time(), tzinfo=timezone.utc)
    return Completion(id=None, habit_id=habit_id, completed_at=dt.isoformat())


def test_longest_streak_for_daily_empty():
    completions: List[Completion] = []
    assert longest_streak_for(completions, "daily") == 0


def test_longest_streak_for_daily_simple():
    # Three consecutive days -> streak 3
    completions = [
        make_completion(1, 2),
        make_completion(1, 1),
        make_completion(1, 0),
    ]
    assert longest_streak_for(completions, "daily") == 3


def test_longest_streak_for_daily_with_gap():
    # Two days, gap, then one day -> longest streak 2
    completions = [
        make_completion(1, 4),
        make_completion(1, 3),
        make_completion(1, 1),
    ]
    assert longest_streak_for(completions, "daily") == 2


def test_longest_streak_for_weekly():
    # Four weeks in a row -> streak 4
    completions = [
        make_completion(1, 0),
        make_completion(1, 7),
        make_completion(1, 14),
        make_completion(1, 21),
    ]
    assert longest_streak_for(completions, "weekly") == 4