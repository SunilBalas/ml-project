# fetching data from various sources like, CSV, Excel, Databases, APIs, etc... code here !

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config: DataIngestionConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion method started")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the data as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=20)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion finished")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as ex:
            raise CustomException(ex, sys)

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()