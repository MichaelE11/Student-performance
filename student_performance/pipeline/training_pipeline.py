import sys
from student_performance.exception import student_performanceException
from student_performance.logger import logging
from student_performance.components.data_ingestion import DataIngestion
from student_performance.entity.config_entity import DataIngestionConfig
from student_performance.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("Entered the stat_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and test set from mondo db")
            logging.info("exited the start_data_ingestion method of the trainpipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise student_performanceException(e, sys)
        
    def run_pipeline(self, )-> None:
        try: 
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise student_performanceException(e,sys)
