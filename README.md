# SETLOG 2.0

setlog is a personal fitness analytics tool that parses Obsidian workout logs to file sessions, track progressive overload, improve exercise selection, and visualise training progress over time.

### Features

- Parses Obsidian markdown workout logs automatically
- Models sessions, exercises and sets as structured data
- Tracks equipment and gym variants separately
- Supports custom set flags (failure, half reps, PB, unilateral etc.)
- Visualises progressive overload per exercise over time
- Identifies undertrained muscle groups and suggests improvements
- Plans future sessions and generates markdown templates
- Exercise catalogue with muscle group mapping

### Data Model

- **Gym**: name, location, notes on equipment
- **Session**: date, gym, type, list of exercises, notes
- **Split**: name, list of days, each day mapped to exercises
- **Exercise**: name, equipment type, muscle groups
- **Set**: weight, reps, flags

### Directory

```
setlog-2.0/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   └── catalogue.json
├── logs/
├── setlog/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── models.py
│   └── parser.py
└── tests/