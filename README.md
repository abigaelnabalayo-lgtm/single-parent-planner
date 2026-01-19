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


