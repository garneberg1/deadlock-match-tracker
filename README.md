# Deadlock Match Tracker

A Python command-line application for recording and analyzing match statistics from **Deadlock**. Match history is saved to a local JSON file, so it is available the next time the program runs.

## Features

- Record a match's hero, win/loss result, kills, deaths, and assists.
- View all previously recorded matches.
- View overall kills, deaths, assists, wins, losses, KDA ratio, and win percentage.
- Automatically save match history after adding a valid match.
- Load saved matches at startup.
- Reject invalid win/loss entries, nonnumeric stats, and negative stats.

## Requirements

- Python 3
- No third-party packages required (uses Python's built-in `json` module).

## Getting started

1. Clone this repository, or download its files.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python tracker.py
   ```

   On some systems, use `python3 tracker.py` instead.

4. Select an option from the menu:

   ```text
   ===== DEADLOCK TRACKER =====
   1. Add a match
   2. View matches
   3. View statistics
   4. Exit
   ```

## Example

```text
Choose an option: 1
Adding a match...
Enter hero played: Haze
Enter result (Win or Loss): Win
Enter number of kills: 5
Enter number of deaths: 2
Enter number of assists: 8
Match added successfully!

Choose an option: 2
Viewing matches...
Match 1: Haze | Win | 5/2/8
```

For this match, the KDA ratio is `(5 + 8) / 2 = 6.5`. The win percentage is `100%`.

## How data is stored

The application writes match records to `matches.json` in the **current working directory**. If the file doesn't exist when the application starts, the match list starts empty and the file is created after your first successfully added match.

Each match is stored as a JSON object with the fields `Hero`, `Result`, `Kills`, `Deaths`, and `Assists`.

The program saves after each successful match entry and again when you choose Exit. Keep `matches.json` out of Git if you don't want to publish your personal match history; for example, add it to `.gitignore`.

## Project structure

```text
Deadlock Stats Tracker/
├── tracker.py     # Main application
├── README.md      # Project documentation
└── matches.json   # Local saved data; generated when a match is recorded
```

## Potential future improvements

- Hero-specific performance statistics
- Editing and deleting recorded matches
- Automated tests for calculations and input validation
- Charts or a simple interface for visualizing performance

## About

An independent Python project built to practice functions, lists, dictionaries, input validation, file handling, and basic statistics.

*This is an unofficial fan-made tracker and is not affiliated with Valve.*
