import os
import sys
import numpy as np

from dataclass import dataclass

from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import(
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor,
    ExtraTreesRegressor
)
from sklearn.tree import DecisionTreeRegressor
from xgboost import XgBoostRegressor
from catboost import CatBoostRegressor

from src.exception import CustomException
from src.logger import logging

@dataclass
class ModelTrainerConfig:
    model_trainer_file_path = os.path.join("artifacts","")

class ModelTrainer():
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("train test split")

            models = (
                ("Linear Regression", LinearRegression())
            )
        except Exception as e:
            raise CustomException(e,sys)
        