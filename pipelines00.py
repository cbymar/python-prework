

#########################################
# https://campus.datacamp.com/courses/building-data-engineering-pipelines-in-python/creating-a-data-transformation-pipeline-with-pyspark?ex=13
# pyspark packaging
"""
Need installation of spark, access to ref'd resources, classpath configured.
"spark-submit", which comes with SPark.
Set up launch environ.
spark-submit \
    --master "local[*]" \
    --py-files PY_FILES \
    MAIN_PYTHON_FILE \
    app_arguments
"""

"""
zip \
    --recurse-paths \
    dependencies.zip \
    pydiaper

spark-submit \
    --py-files dependencies.zip \
    pydiaper/cleaning/clean_prices.py
"""
# Package everything in pydiaper into a zip file.
# ~/workspace/spark_pipelines$ ls -al
"""
total 52
drwxrwxr-x 5 repl repl 4096 May 20 01:19 .
drwxr-xr-x 1 repl repl 4096 May 20 01:14 ..
drwxrwxr-x 2 repl repl 4096 Sep 24  2019 .circleci
-rw-r--r-- 1 repl repl 5010 May 20 01:19 dependencies.zip
-rw-rw-r-- 1 repl repl   59 Sep 24  2019 .gitignore
-rw-rw-r-- 1 repl repl   79 Sep 24  2019 __init__.py
-rw-rw-r-- 1 repl repl  197 Sep 24  2019 Pipfile
-rw-rw-r-- 1 repl repl 5309 Sep 24  2019 Pipfile.lock
drwxrwxr-x 6 repl repl 4096 Sep 24  2019 pydiaper
drwxrwxr-x 2 repl repl 4096 Sep 24  2019 script
"""
# Submitted the whole pipeline as a Spark job.
# spark-submit --py-files spark_pipelines/pydiaper/pydiaper.zip spark_pipelines/pydiaper/pydiaper/cleaning/clean_ratings.py

####################
# Unit tests for Pyspark app.
# Extracting and loading separately for test purposes
# spark.read.csv()'s and then teh join & transform

"""
Create df in memory to test transformations. Clear inputs. 


"""

from datetime import date
from pyspark.sql import Row

Record = Row("country", "utm_campaign", "airtime_in_minutes", "start_date", "end_date")

# Create a tuple of records
data = (
  Record("USA", "DiapersFirst", 28, date(2017, 1, 20), date(2017, 1, 27)),
  Record("Germany", "WindelKind", 31, date(2017, 1, 25), None),
  Record("India", "CloseToCloth", 32, date(2017, 1, 25), date(2017, 2, 2))
)

# Create a DataFrame from these records
frame = spark.createDataFrame(data)
frame.show()
#########################
"""
unittest, doctest [in std lib]
pytest, nose [separate packages]
.circleci/config.yaml
jobs:
    test:
        docker:
            - image: circleci/python:3.8.0
        steps:
            - checkout
            - run: pip install -r requirements.txt
            - run: pytest .
"""
########sequence for CI tool testing
"""
checkout app from vcs; install deps; run test suite; create artifacts once tests pass; save.
go to destination; run 
$ pytest . 
"""


#################################
# chaining together example from datacamp:
spark_args = {"py_files": dependency_path,
              "conn_id": "spark_default"}
# Define ingest, clean and transform job.
with dag:
    ingest = BashOperator(task_id='Ingest_data', bash_command='tap-marketing-api | target-csv --config %s' % config)
    clean = SparkSubmitOperator(application=clean_path, task_id='clean_data', **spark_args)
    insight = SparkSubmitOperator(application=transform_path, task_id='show_report', **spark_args)

    # set triggering sequence
    ingest >> clean >> insight

#######################################################
# Notes airflow deployment:
# from datacamp course
"""
export AIRFLOW_HOME=~/airflow
pip install apache-airflow
airflow initdb (populates 2 config files and the sqlite db, and the logs folder)
Production folder will include, as seen:
Folders for connections, dags, plugins (hooks etc), tests, variables/pools
Good first test: dagbag import.
we upload dags by either 
- cloning repo onto airflow server,
- or use rsync/scp to copy project files to the server
- or package dags into zip folder and copy zip folder over
- or regularly sync dags folder in particular to the airflow server



"""




