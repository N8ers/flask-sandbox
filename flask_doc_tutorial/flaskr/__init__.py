import os
from flask import Flask

# our application factory function
def create_app(test_config=None):
  # creates a flask instance
  app = Flask(__name__, instance_relative_config=True)
  # sets up some default config for the app
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
  )

  if test_config is None:
    # will override default config, if 'config.py' exists (like for secret keys on deploy)
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  # ensure the instance folder (app.instance_path) exists. Flask doesn't create the instance folder, it must be done manually.
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # Hello World route
  @app.route('/hello')
  def hello():
    return 'Jello world'
  
  return app