# flask-taskmaster-webapp
Task master CRUD web app built using [Flask](https://flask.palletsprojects.com/), built upon on [this YouTube tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA). Allows users to add items a to-do list, update their descriptions, delete entries, and mark them as complete.

## Installation
These installation instructions are for Windows. Mac and Linux setup may differ slightly.

Install the latest version of Python 3, found [here](https://www.python.org/downloads/). Your current Python installation version can be checked using:

```
python --version
```

Install virtualenv using:

```
pip install virtualenv
```

and set it up in the project folder using:

```
virtualenv env
```

Activate your virtual environment using:

```
source bin/Scripts/activate
```

Install Flask and SQLAlchemy using:

```
pip install flask flask-sqlalchemy
```

Create the database using:

```
python create_all_dbs.py
```

Finally, run the app using:

```
python app.py
```

This will host the web app on `localhost:5000`.
