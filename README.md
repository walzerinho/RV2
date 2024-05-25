# RV2

A Django app which is used to create your tournaments depending of the format you want to give to !

## Features

- Create tournaments

  - Swiss rounds
  - Championship (multiple groups)
  - Bracket (winner + looser | winner)

- Manage tournaments

  - Add/delete games
  - Add/delete players
  - Add/delete matches

- Follow tournaments
  - Consult games
  - Consult leaderboard (swiss rounds and championships)
  - Consult brackets
  - Consult players
  - Consult created tournaments

# Installation and launch

## Installation

```bash
pip install -r requirements.txt
```

## Launch

```bash
python manage.py runserver
```

# Tournament creation

From the home page, you can create a tournament
