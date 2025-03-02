from student_performance.configuration.mongo_db_connection import MongoDBClient
from student_performance.constants import DATABASE_NAME
from student_performance.exception import student_performanceException
import pandas as pd
import sys
import numpy as np
from typing import Optional

class StudentPreformanceData:
    """
    this class helps to enter mongo db copy data and convert to data frame
    """
    def __init__(self):
        try:
            self.mongo_client=MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise student_performanceException(e, sys)
        
    def export_collection_as_dataframe(self, collection_name:str, database_name:Optional[str]=None)->pd.DataFrame:
        try:
            """
            export entire collection as dataframe
            return pd.Dataframe of collection
            """
            if database_name is None:
                collection=self.mongo_client.database[collection_name]
            else:
                collection=self.mongo_client[database_name][collection_name]

            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise student_performanceException(e, sys)