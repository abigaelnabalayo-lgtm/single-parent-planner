import argparse
from service import HabitService


def create_parser():
    parser = argparse.ArgumentParser(description="Single Parent Planner CLI")

    subparsers = parser.add_subparsers(dest="command")

    # ------------------ habit add ------------------
    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("name", type=str, help="Name of the habit")
    add_parser.add_argument("--period", choices=["daily", "weekly"], required=True)

    # ------------------ habit list ------------------
    list_parser = subparsers.add_parser("list", help="List habits")
    list_parser.add_argument("--period", choices=["daily", "weekly"])
    list_parser.add_argument("--all", action="store_true")
    list_parser.add_argument("--archived", action="store_true")

    # ------------------ habit complete ------------------
    comp_parser = subparsers.add_parser("complete", help="Complete a habit")
    comp_parser.add_argument("id", type=int)
    comp_parser.add_argument("--at", type=str)

    # ------------------ habit archive ------------------
    archive_parser = subparsers.add_parser("archive", help="Archive a habit")
    archive_parser.add_argument("id", type=int)

    # ------------------ analytics group ------------------
    analytics_parser = subparsers.add_parser("analytics", help="Analytics commands")
    analytics_sub = analytics_parser.add_subparsers(dest="analytics_command")

    # analytics list-all
    ana_list_all = analytics_sub.add_parser(
        "list-all", help="List all habits with streak info"
    )
    ana_list_all.add_argument("--period", choices=["daily", "weekly"])

    # analytics longest-streak
    ana_longest = analytics_sub.add_parser(
        "longest-streak",
        help="Show longest streak overall or for a single habit",
    )
    ana_longest.add_argument("--habit", type=int, help="Habit id (optional)")

    # ------------------ seed fixtures ------------------
    seed_parser = subparsers.add_parser("seed", help="Load example data")
    seed_parser.add_argument("what", choices=["fixtures"], help="What to seed")

    return parser


def run_cli(args):
    service = HabitService()

    if args.command == "add":
        habit = service.create_habit(args.name, args.period)
        print(f"Habit added: {habit.id} - {habit.name}")

    elif args.command == "list":
        habits = service.list_habits(
            include_archived=args.all or args.archived,
            periodicity=args.period,
        )
        for h in habits:
            print(f"[{h.id}] {h.name} ({h.periodicity}), archived={h.is_archived}")

    elif args.command == "complete":
        # add a completion (now or at a custom time)
        if args.at:
            comp = service.add_completion_at(args.id, args.at)
        else:
            comp = service.add_completion_now(args.id)

        print(f"Completion added at {comp.completed_at}")

        # compute current longest streak for this habit
        streak = service.longest_streak_for_habit(args.id)
        if streak > 1:
            print(f"🎉 Congratulations! You're on a streak of {streak}!")

    elif args.command == "archive":
        service.archive_habit(args.id)
        print(f"Habit {args.id} archived.")

    elif args.command == "analytics":
        if args.analytics_command == "list-all":
            habits = service.list_habits(
                include_archived=False,
                periodicity=args.period,
            )
            for h in habits:
                longest = service.longest_streak_for_habit(h.id)
                print(
                    f"[{h.id}] {h.name} ({h.periodicity}) - longest streak: {longest}"
                )

        elif args.analytics_command == "longest-streak":
            if args.habit:
                streak = service.longest_streak_for_habit(args.habit)
                print(f"Longest streak for habit {args.habit}: {streak}")
            else:
                best_habit, best_streak = service.longest_streak_overall()
                if best_habit is None:
                    print("No habits/completions yet.")
                else:
                    print(
                        f"Longest streak overall: {best_streak} ({best_habit.name})"
                    )

    elif args.command == "seed":
        if args.what == "fixtures":
            from fixtures import seed_fixtures

            seed_fixtures()