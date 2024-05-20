from src.phishingdetection.config.configuration import ConfigurationManager
from src.phishingdetection.conponents.model_evalution import ModelEvaluation
from src.phishingdetection.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        best_model=model_evaluation_config.select_best_model()
        model_evaluation_config.save_models(best_model)
         
    