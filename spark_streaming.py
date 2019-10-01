import json, os
import time, sys
from datetime import datetime
from utils import tag_dict
import findspark

findspark.add_packages(["org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0"])
findspark.init()
import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import pymongo_spark
pymongo_spark.activate()
from pymongo import MongoClient
from mypredictor import myStreamPredictor
from pyspark.sql import Row

from nltk import pos_tag
from nltk.tokenize import word_tokenize, RegexpTokenizer

