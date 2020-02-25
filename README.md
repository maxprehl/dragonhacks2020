# dragonhacks2020

Team:

* Max Prehl
* Corinna Hoang
* Alex Chebatarev
* Tumaris Yalkun

## Project Summary

A web application that connects people who speaks different languages.

## Getting Started

These instructions assume a Unix-like system using Bash and python3

1. Clone the repo

```console
$ git clone git@github.com:maxprehl/dragonhacks2020.git
```

2. Start a python venv and activate it

```console
$ python3 -m venv .venv

$ source .venv/bin/activate
```

3. Install our dependencies into the venv using pip

```console
$ pip install -r requirements.txt
```

4. Use these commands to initialize and fill the sqlite db

```console
$ echo "from app import init_db, fill_db; init_db(); fill_db()" | python3
```

5. Run the app??

```console
$ python3 app.py
```


