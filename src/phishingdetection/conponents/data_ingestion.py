from phishingdetection.logging import logger
from statsmodels.stats.outliers_influence import variance_inflation_factor
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
import logging
from src.phishingdetection.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def feature_selection(self):
        data=pd.read_csv('dataset_full.csv')
        col_list = [col for col in data.columns if col != 'phishing']
        X = data[col_list]
        vif_data = pd.DataFrame()
        vif_data['feature'] = X.columns
        vif_data['VIF'] = [variance_inflation_factor(X.values, i)
                           for i in range(len(X.columns))]
        # Filter features based on VIF < 10
        selected_features = vif_data[vif_data['VIF'] < 10]['feature'].tolist()
        return selected_features

    def read_csv(self, selected_features):
        data = pd.read_csv('dataset_full.csv')
        logging.info("Dataset is read successfully")

        x = data[selected_features]
        y = data['phishing']

        df = pd.concat([x, y], axis=1)

        df.to_csv(self.config.train_path, index=False, header=True)
       

