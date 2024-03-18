from flask import Blueprint, jsonify
from water_analysis_app.schemas import UserSchema, DataSchema, PredictionSchema, VisualizationSchema, LocationSchema, FeatureSchema, XTrainSchema, XTestSchema, YTrainSchema, YTestSchema
from water_analysis_app.models import User, Data, Prediction, Visualization, Location, Feature
from water_analysis_app.models import db

print("Loading routes.py")

# Create a Blueprint named 'api_bp'
#api_bp = Blueprint('api', __name__)

# Define a route associated with this Blueprint
#@api_bp.route('/')
#def hello():
    #return "Hello from the Blueprint!"


# Create schema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)

data_schema = DataSchema()
datas_schema = DataSchema(many=True)

prediction_schema = PredictionSchema()
predictions_schema = PredictionSchema(many=True)

visualization_schema = VisualizationSchema()
visualizations_schema = VisualizationSchema(many=True)

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)

xtrain_schema = XTrainSchema()
xtrains_schema = XTrainSchema(many=True)

xtest_schema = XTestSchema()
xtests_schema = XTestSchema(many=True)

ytrain_schema = YTrainSchema()
ytrains_schema = YTrainSchema(many=True)

ytest_schema = YTestSchema()
ytests_schema = YTestSchema(many=True)


from flask import Blueprint, jsonify
from .models import Data
from . import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    return "Welcome to the Water Quality Analysis App!"

# User Routes
@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

@api_bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user_schema.dump(user))

# Data Routes
@api_bp.route('/data', methods=['GET'])
def get_data():
    data_entries = Data.query.all()
    return jsonify(datas_schema.dump(data_entries))

@api_bp.route('/data/<int:id>', methods=['GET'])
def get_data_entry(id):
    data_entry = Data.query.get_or_404(id)
    return jsonify(data_schema.dump(data_entry))

# Prediction Routes
@api_bp.route('/predictions', methods=['GET'])
def get_predictions():
    predictions = Prediction.query.all()
    return jsonify(predictions_schema.dump(predictions))

@api_bp.route('/prediction/<int:id>', methods=['GET'])
def get_prediction(id):
    prediction = Prediction.query.get_or_404(id)
    return jsonify(prediction_schema.dump(prediction))

# Visualization Routes
@api_bp.route('/visualizations', methods=['GET'])
def get_visualizations():
    visualizations = Visualization.query.all()
    return jsonify(visualizations_schema.dump(visualizations))

@api_bp.route('/visualization/<int:id>', methods=['GET'])
def get_visualization(id):
    visualization = Visualization.query.get_or_404(id)
    return jsonify(visualization_schema.dump(visualization))

# Location Routes
@api_bp.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify(locations_schema.dump(locations))

@api_bp.route('/location/<int:id>', methods=['GET'])
def get_location(id):
    location = Location.query.get_or_404(id)
    return jsonify(location_schema.dump(location))

# Feature Routes
@api_bp.route('/features', methods=['GET'])
def get_features():
    features = Feature.query.all()
    return jsonify(features_schema.dump(features))

@api_bp.route('/feature/<int:id>', methods=['GET'])
def get_feature(id):
    feature = Feature.query.get_or_404(id)
    return jsonify(feature_schema.dump(feature))

