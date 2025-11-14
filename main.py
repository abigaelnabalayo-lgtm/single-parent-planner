from db import init_db
from cli import create_parser, run_cli


def main():
    init_db()
    parser = create_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
    else:
        run_cli(args)


if __name__ == "__main__":
    main()