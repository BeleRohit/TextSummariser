from src.textSummariser.logging import logger
from src.textSummariser.config.configuration import ConfigurationManager
from src.textSummariser.components.data_validation import DataValidation



class Stage2DataValidation:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager ()
            data_validation_config = config.get_data_validation_config ()
            data_validation = DataValidation (config = data_validation_config)
            data_validation.validate_all_files_exist ()
        except Exception as e:
            raise e



