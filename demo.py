from student_performance.logger import logging
import sys
from student_performance.exception import student_performanceException
 

logging.info("welcome to custom logging")

try:
    2/0

except Exception as e:
    raise student_performanceException(e,sys)