import pickle
import logging
from src.phishingdetection.entity import ModelEvaluationConfig




class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def select_best_model(self):
        # Load the model selection data from the file
        model_selection_file_path = 'artifacts/model_trainer/model_selection.pkl'
        with open(model_selection_file_path, 'rb') as f:
            loaded_data = pickle.load(f)

        # Check if the loaded data contains the necessary information
        if isinstance(loaded_data, tuple) and len(loaded_data) == 2:
            model_dataframe, model_info_dict = loaded_data
            
            # Process DataFrame
            best_model = None
            best_accuracy = 0
            best_precision = None
            
            for index, row in model_dataframe.iterrows():
                accuracy = row['accuracy']
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_model_name = row['models']
                    best_precision = row.get('precision', None)  # Precision may not always be present

            if best_model_name in model_info_dict:
                best_model_info = model_info_dict[best_model_name]
                best_model = best_model_info['model']
                
                logging.info(f"Best model with accuracy {best_accuracy} and precision {best_precision} loaded successfully.")
                
                # Save the best model to another file
                best_model_path = 'best_models.pkl'  # Choose a file path for the best model
                with open(best_model_path, 'wb') as f:
                    pickle.dump(best_model, f)
                logging.info(f"Best model saved to {best_model_path}")
            else:
                logging.error("No model found with valid accuracy.")
        else:
            logging.error("Loaded data does not contain the necessary information.")


    def save_models(self, best_model):
        logging.info("Saving models to file")
        with open(self.config.file_path, 'wb') as f:
            pickle.dump(best_model, f)
        logging.info("Models saved successfully.")