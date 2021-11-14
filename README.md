# Sky Bet League Competition
This project is to fetch data from an API, clean/re-structure that data, and use it to feed analytics.

Environment: Google Colab.
Original file is located at https://colab.research.google.com/drive/1rl-uw9S-JfW1z9fUedy19AyTn7V0XwtB

## Connecting Drive to Colab and Mounting Google Drive

```
from google.colab import drive
drive.mount('/content/drive')
```

## Setting up PySpark in Colab

```
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
```

## Installing Apache Spark 3.1.2 with Hadoop 3.2 from the link

```
!wget -q https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
```

## To unzip that folder

```
!tar xf spark-3.1.2-bin-hadoop3.2.tgz
```

## Install findspark library
```
!pip install -q findspark
```

## To set the environment path
```import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.1.2-bin-hadoop3.2"
```

## To locate Spark in the system
```
import findspark
findspark.init()
```

## To know the location where Spark is installed
```
findspark.find()
```

## To view the Spark UI
```
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip ngrok-stable-linux-amd64.zip
get_ipython().system_raw('./ngrok http 4050 &')
!curl -s http://localhost:4040/api/tunnels
```

## Author 
Name: Aminu Habib
InCrowd Sports