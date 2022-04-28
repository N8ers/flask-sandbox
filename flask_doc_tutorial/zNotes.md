## Running the app

1. If running for the first time, you'll need to export the flask app with `export FLASK_APP=<project, flaskr in this case>` and the flask env with `export FLASK_ENV=development`.
1. From the parent dir `flask_doc_tutorial`, run `flask`

## Create venv

1. Navigate to project directory and run `python3 -m venv venv`
1. Activate the env with: `. venv/bin/activate`
1. Deactivate env with `deactivate`

## Python Notes

`__name__`: This value will change base on how the code is ran. If you run the file it is in, `__name__` will equal `__main__`. If you import a file with `__name__`, then it will equal the name of the file you import.
