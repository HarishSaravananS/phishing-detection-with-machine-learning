from phishingdetection.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        

    def predict(self,features):
        try:
            
            model=load_object(file_path='artifacts.model_evalution.pkl')
            preprocessor=load_object(file_path='scaler.pkl')
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise e    