from src.phishingdetection.config.configuration import ConfigurationManager
from src.phishingdetection.conponents.model_training import ModelTrainer
from src.phishingdetection.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
         config = ConfigurationManager()
         model_trainer_config = config.get_model_trainer_config()
         model_trainer_config = ModelTrainer(config=model_trainer_config)
         X_train, y_train, X_test, y_test,models = model_trainer_config.input_data()
         models_dict= model_trainer_config.model_selection(X_train, y_train, X_test, y_test, models)
         model_trainer_config.save_models(models_dict)