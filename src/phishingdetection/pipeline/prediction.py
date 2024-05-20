from phishingdetection.config.configuration import ConfigurationManager
from phishingdetection.utils.common import read_yaml, create_directories, load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model = load_object(file_path='phishing_model.pkl')
            preds = model.predict(features)
            return preds
        
        except Exception as e:
            raise e
