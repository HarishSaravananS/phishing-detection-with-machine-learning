from src.phishingdetection.config.configuration import ConfigurationManager
from src.phishingdetection.conponents.data_ingestion import DataIngestion
from src.phishingdetection.logging import logger



class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        selected_features=data_ingestion.feature_selection()
        data_ingestion.read_csv(selected_features)