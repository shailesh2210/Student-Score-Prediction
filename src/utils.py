import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException
from src.logger import logging

def save_object(file_path , obj):
    try:
        dir_path = os.path.join(file_path)

        os.mkdirs(dir_path , exist_ok = True)

        with open(file_path , "wb") as file_obj:
            dill.dump(obj , file_obj)

    except Exception as e:
        raise CustomException(e, sys)