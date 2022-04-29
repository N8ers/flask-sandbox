## Running the app

1. If running for the first time, you'll need to export the flask app with `export FLASK_APP=<project, flaskr in this case>` and the flask env with `export FLASK_ENV=development`.
1. From the parent dir `flask_doc_tutorial`, run `flask`

## Create venv

1. Navigate to project directory and run `python3 -m venv venv`
1. Activate the env with: `. venv/bin/activate`
1. Deactivate env with `deactivate`

## Python Notes

`__name__`: This value will change base on how the code is ran. If you run the file it is in, `__name__` will equal `__main__`. If you import a file with `__name__`, then it will equal the name of the file you import.

## Flask Blueprint

A blueprint is a way to organize related view and other code.

## 'g'

a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request. The connection is stored and reused instead of creating a new connection if `get_db` is called a second time in the same request.

## args/kwargs

`*args` and `**kwargs` allow you to pass multiple arguments or keyword arguments into a function.

```py
def my_sum(a,b):
  return a + b

# what if we expand the function to take unlimited args!
def my_sum(*args):
  result = 0
  for x in args:
    result += x
  return result

my_sum([2,4,6,8])

# args works for lists, kwargs works for named arguments
def concatenate(**kwargs):
  result = ""
  for arg in kwargs.values():
    result += arg
  return result

concatenate(a="python", b="is", c="cool")
```

- args -

## TODO
