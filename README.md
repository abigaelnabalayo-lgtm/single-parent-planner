# Single Parent Planner – Habit Tracker (CLI)

This is a small command-line habit tracker designed around a “single parent” use case: a lightweight tool to keep track of a few daily and weekly routines (school-related tasks, self-study, basic budgeting, and saving).

The app is written in **Python 3.9+** and uses **SQLite** for persistence. It was developed for the IU module **Object-Oriented and Functional Programming with Python**.


## Features

- Create habits with a **daily** or **weekly** period
- List habits (optional filters: by period / include archived)
- Mark habits as completed (now or with a custom timestamp)
- Archive habits you don’t want in the main list
- Analytics:
  - longest streak per habit
  - habit with the longest streak overall
- Predefined demo data (“fixtures”): **5 habits** and **4 weeks** of completions (for testing)
- A small “congratulations” message when you’re on a streak


## Requirements

- **Python 3.9+**
- SQLite (via Python’s built-in `sqlite3` module)

Install dependencies from `requirements.txt` (currently only `pytest`).


## Project structure

- `main.py` – entry point; sets up DB and parses CLI arguments
- `cli.py` – CLI commands (`add`, `list`, `complete`, `analytics`, `seed`, …)
- `db.py` – DB connection + table creation
- `models.py` – data classes (`Habit`, `Completion`)
- `repository.py` – CRUD database access layer
- `service.py` – application logic layer
- `analytics.py` – streak calculation logic (pure functions)
- `fixtures.py` – demo habits + 4 weeks of example data
- `test_analytics.py` – unit tests for analytics


## Setup and installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abigaelnabalayo-lgtm/single-parent-planner.git
   cd single-parent-planner
   ```
   2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
The SQLite database (`planner.db`) will be created automatically the first time you run the application.
## Running the application
Start the habit tracker from the project root with:

```bash
python main.py
```
## Analytics

The application provides analytics commands to evaluate habit streaks.

### List streaks for all habits

Command:
python3 main.py analytics list-all

Example output:
[1] Track one expense (daily) – longest streak: 28
[2] Check or do learning activity with child (daily) – longest streak: 28
[3] Self-study ≥ 30 minutes (daily) – longest streak: 28
[4] Save €20 (weekly) – longest streak: 4
[5] Outdoor activity with child (weekly) – longest streak: 4

### Show longest streak overall

Command:
python3 main.py analytics longest-streak

Example output:
Longest streak overall: 28 (Track one expense)
## Tests

Basic unit tests are implemented using `pytest` to validate the analytics functionality.

To run the tests, execute the following command from the project root:

pytest

Example result:
4 tests passed successfully.


