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
        SECRET_KEY='ITGZzw-AlirMGsoPhes1vw',  # This is a placeholder. In production, replace with a strong, random value.
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, 'water_quality_analysis.sqlite'),  # Path to the SQLite database
        SQLALCHEMY_TRACK_MODIFICATIONS=False,  # Disables signal handling, which can improve performance and is unnecessary here
    )

    if test_config is None:
        # Load the default configuration file from the instance folder if not in testing mode
        app.config.from_pyfile('config.py', silent=True)
    else:
        # If a test configuration is provided, load it instead
        app.config.update(test_config)

    # Ensure the instance folder exists. Flask uses it for instance-specific files.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        # The folder already exists, no action needed
        pass

    # Initialize extensions with the app context
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints and routes. Import models here to avoid circular imports.
    with app.app_context():
        from water_analysis_app.routes import api_bp  # Import routes as a blueprint
        app.register_blueprint(api_bp, url_prefix='/api')  # Register the blueprint with a URL prefix

    for rule in app.url_map.iter_rules():
        # Debugging: Print all the URL rules for the application
        print(rule)

    return app  # Return the configured Flask application
