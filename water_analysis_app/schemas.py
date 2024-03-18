from flask_marshmallow import Marshmallow
from water_analysis_app.models import User, Data, Prediction, Visualization, Feedback, Location, Feature, XTrain, XTest, YTrain, YTest
from water_analysis_app.models import db

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('feedbacks',)  # Exclude feedbacks relationship temporarily
        sqla_session = db.session


class DataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Data
        sqla_session = db.session
        load_instance = True
        include_fk = True

class PredictionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Prediction
        sqla_session = db.session
        load_instance = True

class VisualizationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Visualization
        sqla_session = db.session
        load_instance = True

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback
        sqla_session = db.session
        load_instance = True
        include_fk = True

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        sqla_session = db.session
        load_instance = True

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        sqla_session = db.session
        load_instance = True

class XTrainSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = XTrain
        sqla_session = db.session
        load_instance = True
        include_fk = True

class XTestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = XTest
        sqla_session = db.session
        load_instance = True
        include_fk = True

class YTrainSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = YTrain
        sqla_session = db.session
        load_instance = True
        include_fk = True

class YTestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = YTest
        sqla_session = db.session
        load_instance = True
        include_fk = True
