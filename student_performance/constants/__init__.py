import os

from datetime import date

DATABASE_NAME="STUDENT_PERFORMANCE"

COLLECTION_NAME="performance_data"

MONGODB_URL_KEY="MONGODB2_URL"# this url is saved in the environment

PIPELINE_NAME:str= "studentperformance"
ARTIFACT_DIR:str="artifact"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

FILE_NAME:str="studentperformance.csv" # take note of this file name it could be new_data.csv
MODEL_FILE_NAME:str="model.pkl"

TARGET_COLUMN= "G3"
CURRENT_YEAR=date.today().year

PROCESSING_OBJECT_FILE_NAME= "preprocessimg.pkl"
SCHEMA_FILE_PATH= os.path.join("config", "schema.yaml")

AWS_ACCESS_KEY_ID_ENV_KEY="AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY="AWS_SECRET_ACCESS_KEY"
REGION_NAME="us-east-1"


"""
data ingestion related constant
"""
DATA_INGESTION_COLLECTION_NAME:str="performance_data"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2


"""
data validation relatedconstant
"""
DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report_yaml"


"""
data transformation related constant
"""
DATA_TRANSFORMATION_DIR_NAME:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str="transformed_object"


"""
model trainer related constant
"""
MODEL_TRAINER_DIR_NAME:str="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str="model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float=0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH:str=os.path.join("config", "model.yaml")


"""
model evaluation
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE:float=0.02
MODEL_BUCKET_NAME="studentperformance-model2025"
MODEL_PUSHER_S3_KEY="model-registry"

APP_HOST ="0.0.0.0"
APP_PORT=8080
