# IOTLondon
The files used in the Basho London IOT roadshow demonstration.  In the demonstration, the environment is Linux Mint 17.1 with 8GB of RAM and 50GB of hard disk.  In this document I will assume that people will use the same environment.  For RHEL/CentOS you will have to change some of the pre-requisite package names slightly.

## Pre-requistites
* Linux Mint 17.1 updates as necessary (sudo apt update, sudo apt upgrade)
* Riak TS 1.4 (Full instructions and download from [here](http://docs.basho.com/riak/ts/1.4.0/#get-started))
* python-pip
* libfreetype6-dev
* libpng-dev
* libffi-dev
* libssl-dev
* THE BIGGIE- if you want to use the Spak demo, you will need a working installation of at least Spark 1.6.  I will not include instructions for that here as it is complicated and I have never been able to install it the same way twice!
* If you are using Spark, you will need the riak-spark connector from [here](http://d3kbcqa49mib13.cloudfront.net/spark-1.6.2-bin-hadoop2.6.tgz).  This should be placed in a convenient sub-directory. You will also need the 'findspark' python package ($ pip install findspark).


## Installation
Once the pre-requisites are installed you need to create a new python virtual environment (recommended).  I called my 'aarhus' not unnaturally.  To do that:

$ sudo pip install virtualenv

Change directories as necessary

$ virtualenv aarhus

will create a new python virtualenv in a subdirectory called 'aarhus' in the directory you are in.

Cd into 'aarhus', activate your virtualenv ('source ./bin/activate') and use pip to load the necessary python packages by 

$ pip install -r all-packages.txt --upgrade

Once the load has completed, the non-spark demo can be started from your python virtualenv as follows:

$ jupyter notebook

Once running you should create the table using the clearly named(!) relevant notebook, come out of jupyter and upload the sample data using the load-data.py script.  Once successful, you can restart Jupyter and run the querying aarhus data notebook.  If you also want to run the spark notebook you will need to restart Jupyter as follows:

$ SPARK_CLASSPATH=<path to the riak-spark connector jar file **INCLUDING THE JAR FILE NAME**> jupyter notebook

