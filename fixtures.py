from datetime import datetime, timedelta, timezone

from service import HabitService


def seed_fixtures() -> None:
    """
    Create the 5 predefined habits and add 4 weeks of example completions.
    This is only meant for demo/analytics screenshots.
    """
    service = HabitService()

    # If there are already habits, do not create duplicates
    existing = service.list_habits(include_archived=True)
    if existing:
        print("Habits already exist – not seeding fixtures to avoid duplicates.")
        return

    today = datetime.now(timezone.utc).date()

    # 5 predefined habits from my Phase 1
    habits_def = [
        ("Track one expense", "daily"),
        ("Check or do learning activity with child", "daily"),
        ("Self-study ≥ 30 minutes", "daily"),
        ("Save €20", "weekly"),
        ("Outdoor activity with child", "weekly"),
    ]

    created = []
    for name, period in habits_def:
        habit = service.create_habit(name, period)
        created.append((habit, period))
        print(f"Created habit [{habit.id}] {habit.name} ({period})")

    # Add completions: 28 days for daily habits, 4 weeks for weekly habits
    for habit, period in created:
        if period == "daily":
            # last 28 days -> nice daily streaks
            for i in range(28):
                day = today - timedelta(days=i)
                dt = datetime.combine(day, datetime.min.time(), tzinfo=timezone.utc)
                service.add_completion_at(habit.id, dt.isoformat())
        else:
            # last 4 weeks -> weekly streaks
            for i in range(4):
                day = today - timedelta(days=7 * i)
                dt = datetime.combine(day, datetime.min.time(), tzinfo=timezone.utc)
                service.add_completion_at(habit.id, dt.isoformat())

    print("Seeded 5 habits with 4 weeks of example completions.")