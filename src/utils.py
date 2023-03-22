# common functions, methods, configurations, etc... code here !

import os
import sys

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer

from src.logger import logging
from src.exception import CustomException

import dill

def save_object(file_path:str, obj:ColumnTransformer) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(file_path, exist_ok=True)

        with open(file_path, 'wb') as file:
            dill.dump(obj, file)

        logging.info("Saved pickle file")
    except Exception as ex:
        raise CustomException(ex, sys)