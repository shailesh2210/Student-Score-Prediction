import os
import sys
import numpy as np
sys.path.append(r'D:\live end to end machine learning projects')

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
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object , evaluate_models

@dataclass
class ModelTrainerConfig:
    model_trainer_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer():
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initaite_model_trainer(self, train_array, test_array):
        try:
            logging.info("train test split")

            x_train , y_train , x_test , y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
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
            
            # to Get best model score from dict 
            best_model_score  = max(sorted(model_report.values()))

            # to get the best model name
            best_model_name = list(best_model_score.keys())[
                    list(model_report.values().index(best_model_score))
            ]

            best_model = models[best_model_name]

            if best_model_score>0.6:
                raise CustomException("No best model found")

            logging.info(f"Best found model in both train and test dataset")

            save_object(
                file_path=self.model_trainer_config.model_trainer_file_path,
                obj = best_model
            )

            prediction = models.predict(x_test)
            score = r2_score(y_test , prediction)
            return score

        except Exception as e:
            raise CustomException(e,sys)
        