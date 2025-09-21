import os 
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from prod_assitant.utils.config_loader import load_config
from prod_assitant.utils.model_loader import ModelLoader


class DataIngestion:
    """
    Class to Handle Data Transformation and ingestion into Astra db using Vector Stores
    """
    def __init__(self):
        pass
    def load_env_variables(self):
        pass
    def get_csv_file(self):
        pass
    def load_csv(self):
        pass
    def transform_data(self):
        pass
    def store_in_vectordb(self):
        pass 
    def run_pipeline(self):
        pass