# Fitness Tracker

A command-line fitness tracking application built in Python. Log workouts, store them persistently in Excel, and view summaries of your activity.

Built during a gap year between finishing secondary school and starting a Computer Science degree at Iowa State University.

## What it does

- Log activities with an ID, type, duration, calories burned, and date
- Update or delete existing entries
- View a full activity log
- See a summary of your most frequent activity and total workout count
- Get simple rule-based feedback on your activity level
- Automatically save all data to `fitness_data.xlsx` so nothing is lost between sessions

## Built with

- **Python 3**
- **pandas** — writing and reading the Excel data file
- **NumPy** — counting activity types to find the most frequent one
- **openpyxl** — Excel file support (used by pandas)

## Running it

Install the dependencies:

```bash
pip install pandas numpy openpyxl
```

Run the program:

```bash
python fitness_tracker.py
```

You'll get a menu with seven options. Choose `1` to log your first activity.

## How it's structured

Everything lives in a single `Fitness_Tracker` class. Activities are held in a dictionary keyed by activity ID, and written out to Excel after every change that modifies the data.

The class is organised in stages:

- **Stage 1** — Core operations: add, update, delete, view, and save
- **Stage 2** — Loading saved data on startup, and basic analysis with NumPy
- **Stage 3** — Rule-based feedback on activity level
- **Stage 4** — The menu loop that ties it together

## A note on the feedback feature

The `get_progress_feedback()` function is **not** machine learning. It checks total calories against fixed thresholds and prints a matching message. It's rule-based logic, and naming it accurately felt more useful than making it sound more advanced than it is.

## What I learned building this

**Why classes are useful.** My first version was a set of loose functions that all passed the same dictionary between them. Grouping them into a class removed that repetition.

**Why data persistence matters.** The first working version lost every entry when the program closed. Writing to Excel with pandas fixed that.

**Why input validation exists.** Entering text where the program expected a number crashed it. The `try`/`except` blocks around duration and calorie input handle that now.

## Known limitations

- Dates are stored as plain strings and aren't validated, so an invalid date will be accepted
- No unit tests
- Analysis is limited to activity frequency; there's no trend analysis over time
- Everything is in one file, which will need splitting as the project grows

## Next steps

- Validate dates properly using `datetime`
- Add trend analysis across weeks
- Split the code into separate modules
- Add unit tests

## About

Built by Melvin Vicky Kanikairaj.
B.S. Computer Science, Iowa State University (Class of 2030).

[LinkedIn](https://www.linkedin.com/in/melvin-vicky)
