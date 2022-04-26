## Setting up virtual environment with pipenv

### Install pipenv

1. `mkdir test-project`
1. `cd test-project`
1. `pipenv install` (to initialize)

- any further pacakges you wish to install should be done with `pipenv install <packagename>`.

### Activating/Deactivating pipenv

1. `pipenv shell` (activated)
1. `deactivate` (deactivate)

### Activate db

1. After setting up your db in app.py, open a python shell in the terminal `python3`.
1. In the shell run `from app import db`.
1. Then `db.create_all()`.
1. You will then see a db created in the project directory.
