from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_ingestion import DataIngestionConfig
from src.MLProject.components.data_transformation import DataTransformationConfig, DataTranformation
from src.MLProject.components.model_trainer import ModelTrainerConfig, ModelTrainer

import sys

if __name__ == "__main__":
    logging.info("the execition has started")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTranformation()
        train_arr, test_arr,_= data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        # model Training
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
    