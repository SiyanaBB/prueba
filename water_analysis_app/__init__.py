import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

print("Loading __init__.py")

# Initialize SQLAlchemy and Marshmallow here
db = SQLAlchemy()
ma = Marshmallow()

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='ITGZzw-AlirMGsoPhes1vw',  # Replace 'dev' with a random value when deploying
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, 'water_quality_analysis.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.update(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions with the app
    db.init_app(app)
    ma.init_app(app)

    # Import and register your blueprints or routes here
    # This is also where you should import your models
    # Make sure to import routes after db and ma to avoid circular imports
    with app.app_context():
        from .models import User, Feedback, Data, Prediction, Visualization, Location, Feature, XTest, XTrain, YTest, YTrain  
        from .routes import api_bp  # Import routes after models have been defined
        app.register_blueprint(api_bp)

    return app


