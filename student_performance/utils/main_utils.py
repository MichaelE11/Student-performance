import os
import sys
import numpy as np
import dill
import yaml
from pandas import DataFrame

from student_performance.exception import student_performanceException
from student_performance.logger import logging

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path, "rb") as yaml_file
        return yaml.safe_load(yaml_file)
    
    except Exception as e:
        raise student_performanceException(e,sys) from e

def write_yaml_file(file_path:str, content:object, replace:bool=False)-> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content,file)

    except Exception as e:
        raise student_performanceException(e,sys) from e
    
def load_object(file_path:str)->object:
    logging.info("Enter the load_object method of utils")

    try:
        with open(file_path, "rb") as file_obj:
            obj=dill.load(file_obj)

        logging.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise student_performanceException(e,sys) from e
    

def save_numpy_array_data(file_path:str, array:np.array):
    """
    save numpy array dat tofile
    file_path: str location of file to save
    array:np.array data to save
    """
    
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise student_performanceException(e,sys) from e
    

def save_object(file_path:str, obj:object)->None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise student_performanceException(e,sys) from e


def drop_Column(df:DataFrame, cols:list)->DataFrame:
    """
    cols: list of columns to be dropped
    """    

    logging.info("Entered the drop_column method of utils")

    try:
        df=df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_column method in the utils")

        return df

    except Exception as e:
        raise student_performanceException(e,sys) from e
    


    


