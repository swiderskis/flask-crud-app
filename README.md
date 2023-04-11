# flask-taskmaster-webapp
A task master CRUD web app, allowing users to add items to a to-do list, update their descriptions, mark them as complete, and delete entries 📝

Built using [Flask](https://flask.palletsprojects.com/), based upon on [this](https://www.youtube.com/watch?v=Z1RJmh_OqeA) YouTube tutorial.

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
source env/Scripts/activate
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
