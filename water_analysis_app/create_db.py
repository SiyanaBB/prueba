from pathlib import Path
from datetime import datetime
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import XTest, XTrain, YTest, YTrain, Feature, Location, User, Data, Prediction, Visualization

app = Flask(__name__, instance_relative_config=True)

# Adjust the path as necessary for your project
db_path = 'sqlite:///' + str(Path(__file__).parent.joinpath('water_quality_analysis.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

def load_x_data(file_path, dataset_type):
    df = pd.read_excel(file_path, header=0)  # Assuming first row is the header
    num_locations = 37  # Number of locations per day

    with app.app_context():
        for i in range(0, len(df), num_locations):  # Process each day's data
            day_data = df.iloc[i:i + num_locations]  # Extract one day's data for all locations
            date = pd.to_datetime(day_data.iloc[0, -1]).date()  # Assuming the date is in the last column
            
            for index, row in day_data.iterrows():
                location_id = index % num_locations + 1
                feature_data = {
                    'date': date,
                    'location_id': location_id,
                    'feature1': row['F1'],
                    'feature2': row['F2'],
                    'feature3': row['F3'],
                    'feature4': row['F4'],
                    'feature5': row['F5'],
                    'feature6': row['F6'],
                    'feature7': row['F7'],
                    'feature8': row['F8'],
                    'feature9': row['F9'],
                    'feature10': row['F10'],
                    'feature11': row['F11'],
                }
                
                if dataset_type == "train":
                    db.session.add(XTrain(**feature_data))
                else:
                    db.session.add(XTest(**feature_data))
        
        db.session.commit()


def load_y_data(file_path, dataset_type):
    df = pd.read_excel(file_path, header=0)

    with app.app_context():
        for index, row in df.iterrows():
            date = pd.to_datetime(row['Date']).date()

            y_data = {'date': date}
            
            # Access columns by their numeric labels directly
            for i in range(1, 38):
                y_data[f'location{i}'] = row[i]  # Direct numeric access

            if dataset_type == "train":
                db.session.add(YTrain(**y_data))
            else:
                db.session.add(YTest(**y_data))
        
        db.session.commit()


def load_data_from_excel():
    with app.app_context():
        excel_file_path = Path(__file__).parent.parent / 'data' / 'water_features_locs.xlsx'
        
        # Load 'Feature' data
        features_df = pd.read_excel(excel_file_path, sheet_name='features', header=None)
        for _, row in features_df.iterrows():
            feature_name = row[0]  # Assuming the first column is the feature name.
            feature_description = row[1]  # Assuming the second column is the feature description.
            # Check if the feature already exists.
            existing_feature = Feature.query.filter_by(name=feature_name).first()
            if existing_feature:
                # Optionally update the existing feature's description.
                existing_feature.description = feature_description
            else:
                # If the feature does not exist, add a new one.
                new_feature = Feature(name=feature_name, description=feature_description)
                db.session.add(new_feature)
        
        # Load 'Location' data
        locations_df = pd.read_excel(excel_file_path, sheet_name='locations')
        for _, row in locations_df.iterrows():
            location = Location(
                id=row['location_id'],
                location_group=row['Location group'],
                site_number=row['Site number'],
                site_name=row['Site Name'],
                decimal_latitude=row['Decimal latitude'],
                decimal_longitude=row['Decimal longitude']
            )
            db.session.add(location)
        
        db.session.commit()



def main():
    create_tables()
    
    # Go up one directory from the current script's directory, then into the 'Data' directory
    data_dir = Path(__file__).parent.parent / 'Data'
    
    load_x_data(data_dir / 'X_tr_prepared.xlsx', "train")
    load_x_data(data_dir / 'X_te_prepared.xlsx', "test")
    load_y_data(data_dir / 'Y_tr_prepared.xlsx', "train")
    load_y_data(data_dir / 'Y_te_prepared.xlsx', "test")

    load_data_from_excel()

    print("Database initialization and data loading complete.")

if __name__ == '__main__':
    main()
