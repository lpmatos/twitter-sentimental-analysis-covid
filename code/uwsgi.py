# -*- coding: utf-8 -*-

import os, sys
from flask import Flask
from flask_cors import CORS
from restplus import configure as config_api
from endpoints.tweets.routes import ns_tweets
from endpoints.mongo.routes import ns_mongo

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def create_app(config_filename=None):
  app = Flask(__name__, instance_relative_config=True)
  _ = CORS(app, resources={r"*": {"origins": "*"}})
  config_api(app)
  app.api.add_namespace(ns_tweets)
  app.api.add_namespace(ns_mongo)
  register_blueprints(app)
  return app

def register_blueprints(app):
  from endpoints import api_blueprint
  app.register_blueprint(api_blueprint)

# ==============================================================================
# GLOBAL
# ==============================================================================

application = create_app()

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
  application.run(debug=True, host='0.0.0.0', port=5000)
