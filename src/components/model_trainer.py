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
from src.utils import save_object , evaluate_models

@dataclass
class ModelTrainerConfig:
    model_trainer_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer():
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("train test split")

            x_train , y_train , x_test , y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models = {
                "Linear Regression", LinearRegression(),
                "Random Forest", RandomForestRegressor(),
                "DecisionTree Regressor", DecisionTreeRegressor(),
                "CatBoost Regressor", CatBoostRegressor(),
                "XgBoost Regressor", XgBoostRegressor(),
                "GradientBoosting Regressor", GradientBoostingRegressor(),
                "Ada Boost Regressor", AdaBoostRegressor(),
                "Extra Trees Regressor", ExtraTreesRegressor()
                
            }

            model_report:dict = evaluate_models(x_train=x_train , y_train=y_train ,
                                    x_test = x_test ,y_test=y_test , models=models )
            


        except Exception as e:
            raise CustomException(e,sys)
        