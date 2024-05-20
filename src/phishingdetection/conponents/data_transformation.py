import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import logging
import pickle
from src.phishingdetection.entity import (DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig)

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def transform(self):
        data = pd.read_csv(r"artifacts\data_ingestion\train.csv")
        train_df, test_df = train_test_split(data, test_size=0.2)

        logging.info("Read train and test data completed")

        target_column_name = "phishing"

        input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
        target_feature_train_df = train_df[target_column_name]

        input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
        target_feature_test_df = test_df[target_column_name]

        scaler = MinMaxScaler()  
        scaler.fit(input_feature_train_df.values)  
        scaled_input_feature_train_df = scaler.transform(input_feature_train_df.values)
        scaled_input_feature_test_df = scaler.transform(input_feature_test_df.values)

        logging.info("Applying preprocessing object on training dataframe and testing dataframe.")

        # Save the scaler object using pickle
        with open('scalers.pkl', 'wb') as f:
            pickle.dump(scaler, f)

        # Further processing if required
        
        # Save transformed dataframes if needed
        scaled_train_df = pd.DataFrame(scaled_input_feature_train_df, columns=input_feature_train_df.columns)
        scaled_test_df = pd.DataFrame(scaled_input_feature_test_df, columns=input_feature_test_df.columns)
        logging.info("Transformation completed and saved scaler object.")
        scaled_train_df.to_csv(self.config.train_path, index=False)
        scaled_test_df.to_csv(self.config.test_path, index=False)
        target_feature_train_df.to_csv(self.config.train_y_path, index=False)
        target_feature_test_df.to_csv(self.config.test_y_path, index=False)

        logging.info("Transformation completed and saved scaler object.")