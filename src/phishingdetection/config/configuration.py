from phishingdetection.constants import *
from phishingdetection.utils.common import read_yaml, create_directories
from src.phishingdetection.entity import (DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        # Corrected the syntax for DataIngestionConfig instantiation
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            test_path=config.test_path,  # Swapped train_path and test_path
            train_path=config.train_path   # Swapped train_path and test_path
        )

        return data_ingestion_config


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        # Corrected the syntax for  instantiation
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
            test_path=config.test_path,
            train_y_path=config.train_y_path,
            test_y_path=config.test_y_path  # Swapped train_path and test_path
              # Swapped train_path and test_path
        )

        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            file_path=config.file_path,
            # Add other attributes as needed from your ModelTrainerConfig class
        )

        return model_trainer_config




    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])
        

        model_evaluation_config = ModelEvaluationConfig(
              root_dir=config.root_dir,
              file_path= config.file_path,
              models_path=config.models_path
            
           
        )

        return model_evaluation_config
