from TextSummariser.src.textSummariser.components.data_ingestion import DataIngestion
from TextSummariser.src.textSummariser.logging import logger
from TextSummariser.src.textSummariser.config.configuration import ConfigurationManager

class DataIngestionPipelineStage1:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager ()
            data_ingestion_config = config.get_data_ingestion_config ()
            data_ingestion = DataIngestion (config = data_ingestion_config)
            data_ingestion.download_file ()
            data_ingestion.extract_zip_file ()
        except Exception as e:
            raise e
