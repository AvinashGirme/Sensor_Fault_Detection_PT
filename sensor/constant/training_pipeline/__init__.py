import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

SAVED_MODEL_DIR = os.path.join("saved_models")
#defining common constant variable for training pipeline
TARGET_COLUMN ="class"
PIPELINE_NAME: str ="sensor"
ARTIFACT_DIR: str ="artifact"
FILE_NAME: str ="sensor.csv"

TRAIN_FILE_NAME: str ="train.csv"
TEST_FILE_NAME: str ="test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")
SCHMA_DROP_COLS = "drop_columns"