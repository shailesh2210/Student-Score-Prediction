import sys
import os
import pandas as pd
import numpy as np
from dataclass import dataclass
sys.path.append(r'D:\live end to end machine learning projects')

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object


class DataTransformationConfig:
    preprocessor_file_obj = os.path.join("artifcats", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transfromation_config = DataTransformationConfig

    def get_transformation_obj(self):

        """
        This function is responsible for data transformation
        """
        try:
            numerical_col = ["writing_score", "reading_score"]
            categorical_col = [
                "gender",
                "race_enthnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median"))
                    ("scaler", StandardScaler())
                ]
            )
            logging.info(f"Numerical Columns ", {numerical_col})

            cat_pipeline = Pipeline(
                steps = [
                   ("imputer", SimpleImputer(strategy = "most_frequent"))
                   ("one_hot_encoder", OneHotEncoder()) 
                   ("scaler", StandardScaler())
                ]
            )

            logging.info(f"Categorical Columns Encoding", {categorical_col})

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline , numerical_col)
                    ("cat_pipeline", cat_pipeline , categorical_col)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self ,train_path , test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading train and test data")

            logging.info("Obtaining preprocesing object")

            preprocessing_obj = self.get_transformation_obj()

            target_column = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_features_train_df = train_df.drop([target_column], axis=1)
            target_features_train_df = train_df[target_column]

            input_features_test_df = test_df.drop([target_column], axis=1)
            target_feature_test_df = test_df[target_column]

            logging.info(
                f"Applying preprocessing objevt on training data and test data"
            )

            input_feature_train_arr = preprocessing_obj.fit_transformation(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transformation(input_features_test_df)

            train_arr = np.c_(
                input_feature_train_arr , np.array(target_features_train_df)
            )

            test_arr = np.c_(
                input_feature_test_arr , np.array(target_feature_test_df)
            )

            logging.info("Saving Preprocessing object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
    