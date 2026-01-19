# Single Parent Planner – Habit Tracker (CLI)

This project is a small command line habit tracker for single parents.  
It helps keep an eye on a few important daily and weekly routines, such as
checking school work, doing self-study, tracking expenses and saving a little
money every week.

The app is written in **Python 3.9** and uses **SQLite** to store habits and
their completion history. It was developed as part of the module
“Object-Oriented and Functional Programming with Python” at IU.


## 1. Features

- Create habits with a **daily** or **weekly** period
- List all habits, with optional filters (by period / include archived)
- Mark a habit as completed (now or at a specific timestamp)
- Archive habits you no longer want to see in the main list
- Analytics:
  - show the longest streak for each habit
  - show the habit with the longest streak overall
- Predefined demo data (“fixtures”) for 5 habits and 4 weeks of completions
- Small **congratulations message** when you are on a streak

The main use case is a single parent who wants a quick CLI tool to track a few
core routines without a big GUI application.


## 2. Requirements

- Python **3.9** (or newer)
- SQLite (comes built-in with Python’s `sqlite3` module)

Python dependencies are listed in `requirements.txt` and can be installed with
`pip` inside a virtual environment.


## 3. Project structure

At the top level the repository is organised like this:

- `main.py` – program entry point; sets up the database and parses CLI arguments
- `cli.py` – all command line commands (`add`, `list`, `complete`, `analytics`, `seed`, …)
- `db.py` – database connection and table creation (`planner.db`)
- `models.py` – `Habit` and `Completion` data classes
- `repository.py` – low-level database access (CRUD for habits and completions)
- `service.py` – application logic on top of the repository
- `analytics.py` – pure functions for streak calculations
- `fixtures.py` – helper to create example habits and four weeks of data
- `test_analytics.py` – unit tests for the analytics logic
- `requirements.txt` – Python dependencies (currently just `pytest`)
- `planner.db` – SQLite database file (created at runtime)


# Single Parent Planner – Habit Tracker (CLI)

This project is a small command line habit tracker for single parents.  
It helps keep an eye on a few important daily and weekly routines, such as
checking school work, doing self-study, tracking expenses and saving a little
money every week.

The app is written in **Python 3.9** and uses **SQLite** to store habits and
their completion history. It was developed as part of the module
“Object-Oriented and Functional Programming with Python” at IU.


## 1. Features

- Create habits with a **daily** or **weekly** period
- List all habits, with optional filters (by period / include archived)
- Mark a habit as completed (now or at a specific timestamp)
- Archive habits you no longer want to see in the main list
- Analytics:
  - show the longest streak for each habit
  - show the habit with the longest streak overall
- Predefined demo data (“fixtures”) for 5 habits and 4 weeks of completions
- Small **congratulations message** when you are on a streak

The main use case is a single parent who wants a quick CLI tool to track a few
core routines without a big GUI application.


## 2. Requirements

- Python **3.9** (or newer)
- SQLite (comes built-in with Python’s `sqlite3` module)

Python dependencies are listed in `requirements.txt` and can be installed with
`pip` inside a virtual environment.


## 3. Project structure

At the top level the repository is organised like this:

- `main.py` – program entry point; sets up the database and parses CLI arguments
- `cli.py` – all command line commands (`add`, `list`, `complete`, `analytics`, `seed`, …)
- `db.py` – database connection and table creation (`planner.db`)
- `models.py` – `Habit` and `Completion` data classes
- `repository.py` – low-level database access (CRUD for habits and completions)
- `service.py` – application logic on top of the repository
- `analytics.py` – pure functions for streak calculations
- `fixtures.py` – helper to create example habits and four weeks of data
- `test_analytics.py` – unit tests for the analytics logic
- `requirements.txt` – Python dependencies (currently just `pytest`)
- `planner.db` – SQLite database file (created at runtime)


## 4. Setup and installation

1. **Clone or copy** the project folder to your machine.

2. Open a terminal in the project folder and create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate # Single Parent Planner – Habit Tracker (CLI)

This project is a small command line habit tracker for single parents.  
It helps keep an eye on a few important daily and weekly routines, such as
checking school work, doing self-study, tracking expenses and saving a little
money every week.

The app is written in **Python 3.9** and uses **SQLite** to store habits and
their completion history. It was developed as part of the module
“Object-Oriented and Functional Programming with Python” at IU.


## 1. Features

- Create habits with a **daily** or **weekly** period
- List all habits, with optional filters (by period / include archived)
- Mark a habit as completed (now or at a specific timestamp)
- Archive habits you no longer want to see in the main list
- Analytics:
  - show the longest streak for each habit
  - show the habit with the longest streak overall
- Predefined demo data (“fixtures”) for 5 habits and 4 weeks of completions
- Small **congratulations message** when you are on a streak

The main use case is a single parent who wants a quick CLI tool to track a few
core routines without a big GUI application.


## 2. Requirements

- Python **3.9** (or newer)
- SQLite (comes built-in with Python’s `sqlite3` module)

Python dependencies are listed in `requirements.txt` and can be installed with
`pip` inside a virtual environment.


## 3. Project structure

At the top level the repository is organised like this:

- `main.py` – program entry point; sets up the database and parses CLI arguments
- `cli.py` – all command line commands (`add`, `list`, `complete`, `analytics`, `seed`, …)
- `db.py` – database connection and table creation (`planner.db`)
- `models.py` – `Habit` and `Completion` data classes
- `repository.py` – low-level database access (CRUD for habits and completions)
- `service.py` – application logic on top of the repository
- `analytics.py` – pure functions for streak calculations
- `fixtures.py` – helper to create example habits and four weeks of data
- `test_analytics.py` – unit tests for the analytics logic
- `requirements.txt` – Python dependencies (currently just `pytest`)
- `planner.db` – SQLite database file (created at runtime)


## 4. Setup and installation

1. **Clone or copy** the project folder to your machine.

2. Open a terminal in the project folder and create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate# Single Parent Planner – Habit Tracker (CLI)

This project is a small command line habit tracker for single parents.  
It helps keep an eye on a few important daily and weekly routines, such as
checking school work, doing self-study, tracking expenses and saving a little
money every week.

The app is written in **Python 3.9** and uses **SQLite** to store habits and
their completion history. It was developed as part of the module
“Object-Oriented and Functional Programming with Python” at IU.


## 1. Features

- Create habits with a **daily** or **weekly** period
- List all habits, with optional filters (by period / include archived)
- Mark a habit as completed (now or at a specific timestamp)
- Archive habits you no longer want to see in the main list
- Analytics:
  - show the longest streak for each habit
  - show the habit with the longest streak overall
- Predefined demo data (“fixtures”) for 5 habits and 4 weeks of completions
- Small **congratulations message** when you are on a streak

The main use case is a single parent who wants a quick CLI tool to track a few
core routines without a big GUI application.


## 2. Requirements

- Python **3.9** (or newer)
- SQLite (comes built-in with Python’s `sqlite3` module)

Python dependencies are listed in `requirements.txt` and can be installed with
`pip` inside a virtual environment.


## 3. Project structure

At the top level the repository is organised like this:

- `main.py` – program entry point; sets up the database and parses CLI arguments
- `cli.py` – all command line commands (`add`, `list`, `complete`, `analytics`, `seed`, …)
- `db.py` – database connection and table creation (`planner.db`)
- `models.py` – `Habit` and `Completion` data classes
- `repository.py` – low-level database access (CRUD for habits and completions)
- `service.py` – application logic on top of the repository
- `analytics.py` – pure functions for streak calculations
- `fixtures.py` – helper to create example habits and four weeks of data
- `test_analytics.py` – unit tests for the analytics logic
- `requirements.txt` – Python dependencies (currently just `pytest`)
- `planner.db` – SQLite database file (created at runtime)


# Single Parent Planner – Habit Tracker (CLI)

This project is a small command line habit tracker for single parents.  
It helps keep an eye on a few important daily and weekly routines, such as
checking school work, doing self-study, tracking expenses and saving a little
money every week.

The app is written in **Python 3.9** and uses **SQLite** to store habits and
their completion history. It was developed as part of the module
“Object-Oriented and Functional Programming with Python” at IU.


## 1. Features

- Create habits with a **daily** or **weekly** period
- List all habits, with optional filters (by period / include archived)
- Mark a habit as completed (now or at a specific timestamp)
- Archive habits you no longer want to see in the main list
- Analytics:
  - show the longest streak for each habit
  - show the habit with the longest streak overall
- Predefined demo data (“fixtures”) for 5 habits and 4 weeks of completions
- Small **congratulations message** when you are on a streak

The main use case is a single parent who wants a quick CLI tool to track a few
core routines without a big GUI application.


## 2. Requirements

- Python **3.9** (or newer)
- SQLite (comes built-in with Python’s `sqlite3` module)

Python dependencies are listed in `requirements.txt` and can be installed with
`pip` inside a virtual environment.


## 3. Project structure

At the top level the repository is organised like this:

- `main.py` – program entry point; sets up the database and parses CLI arguments
- `cli.py` – all command line commands (`add`, `list`, `complete`, `analytics`, `seed`, …)
- `db.py` – database connection and table creation (`planner.db`)
- `models.py` – `Habit` and `Completion` data classes
- `repository.py` – low-level database access (CRUD for habits and completions)
- `service.py` – application logic on top of the repository
- `analytics.py` – pure functions for streak calculations
- `fixtures.py` – helper to create example habits and four weeks of data
- `test_analytics.py` – unit tests for the analytics logic
- `requirements.txt` – Python dependencies (currently just `pytest`)
- `planner.db` – SQLite database file (created at runtime)


## 4. Setup and installation

1. Clone or copy the project folder to your machine.

2. Open a terminal in the project folder and create a virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate

3. Install the required dependencies:

   pip install -r requirements.txt

The SQLite database (planner.db) will be created automatically the first time
you run the application.


## 5. Running the application

Start the habit tracker from the project root with:

   python main.py

The application provides a command-line interface (CLI) that allows you to add,
list, complete and analyse habits using commands such as add, list, complete,
analytics and seed.

To load the predefined demo data (5 habits with 4 weeks of example completions),
run:

   python main.py seed


## 6. Running the tests

Unit tests for the analytics logic are implemented using pytest.

To run the tests, execute the following command from the project root:

   pytest

All tests should pass without errors.
