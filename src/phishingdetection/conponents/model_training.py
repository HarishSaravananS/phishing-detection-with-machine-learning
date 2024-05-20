from src.phishingdetection.entity import (DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig)

from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import pandas as pd
import logging
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, precision_score






class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def input_data(self):
        logging.info("Splitting training and test input data")
        train_data_scaled = pd.read_csv(r"artifacts\data_transformation\train_scaled.csv")
        test_data_scaled = pd.read_csv(r"artifacts\data_transformation\test_scaled.csv")
        train_data=pd.read_csv(r"artifacts\data_transformation\train_y_scaled.csv")
        test_data=pd.read_csv(r"artifacts\data_transformation\test_y_scaled.csv")
        logging.info("Split training and test input data")
        X_train, y_train, X_test, y_test = (
            train_data_scaled.iloc[:, :],
            train_data.iloc[:,:],
            test_data_scaled.iloc[:, :],
            test_data.iloc[:, :]
        )
        
        models = [
            LogisticRegression(max_iter=1000),
            RidgeClassifier(alpha=0.005),
            LinearSVC(dual=False),
            SVC(),
            KNeighborsClassifier(n_neighbors=5),
            DecisionTreeClassifier(),
            RandomForestClassifier(),
            AdaBoostClassifier(),
            MLPClassifier()
        ]

        return X_train, y_train, X_test, y_test, models

    def model_selection(self, X_train, y_train, X_test, y_test, models):
        accuracy_result = []
        precision_result = []
        models_dict = {}

        for model in models:
            model.fit(X_train, y_train.values.ravel())
            y_pred = model.predict(X_test)
            precision = precision_score(y_test, y_pred, average='micro')
            accuracy = accuracy_score(y_test, y_pred)
            accuracy_result.append(accuracy)
            precision_result.append(precision)
            models_dict[str(model)] = {'model': model, 'accuracy': accuracy, 'precision': precision}

        return pd.DataFrame({'models': list(models_dict.keys()), 'accuracy': accuracy_result, 'precision': precision_result}), models_dict

    def save_models(self, models_dict):
        logging.info("Saving models to file")
        with open(self.config.file_path, 'wb') as f:
            pickle.dump(models_dict, f)
        logging.info("Models saved successfully.")