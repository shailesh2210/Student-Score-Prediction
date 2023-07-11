import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_file_path:str = os.path.join("artifacts", "train.csv")
    test_file_path:str = os.path.join("artifacts", "test.csv")
    raw_file_path:str = os.path.join("artifacts", "raw.csv")

class Dataingestion:
    def __init___(self):
        pass