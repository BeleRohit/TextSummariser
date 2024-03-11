from src.textSummariser.pipeline.stage_1_data_ingestion import Stage1DataIngestion
from src.textSummariser.pipeline.stage_2_Data_Validation import Stage2DataValidation
from src.textSummariser.logging import logger

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>> {STAGE_NAME} started !<<<<<<<<<<<<<<<<<<<<<")
    ingestion_pipeline = Stage1DataIngestion()
    ingestion_pipeline.main()
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>>>>>>>>> {STAGE_NAME} started !<<<<<<<<<<<<<<<<<<<<<")
    validation_pipeline = Stage2DataValidation()
    validation_pipeline.main()
except Exception as e:
    logger.error(e)
    raise e




