from sensor.configuration.mongo_db_connection import MongoDBClient
import os,sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils.main_utils import read_yaml_file

env_file_path=os.path.join(os.getcwd(),"env.yaml")

def set_env_variable(env_file_path):

    if os.getenv('MONGO_DB_URL',None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']

