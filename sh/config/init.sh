#!/bin/bash
"Initializing the Spark Worker Container"
trap '' HUP
cat /etc/simple_grid/config/spark_env.conf >> ~/.bashrc
# Add the PySpark classes to the PYTHONPATH:
if [ -z "${PYSPARK_PYTHONPATH_SET}" ]; then
  export PYTHONPATH="${SPARK_HOME}/python:${PYTHONPATH}" >> ~/.bashrc
  export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.7-src.zip:${PYTHONPATH}" >> ~/.bashrc
  export PYSPARK_PYTHONPATH_SET=1 >> ~/.bashrc
fi
source ~/.bashrc
mkdir -p $SPARK_WORKER_LOG
echo "Copying spark-defaults.conf to /spark/conf"
cp /etc/simple_grid/conf/spark-defaults.conf /spark/conf/
echo "Starting spark worker"
/spark/bin/spark-class org.apache.spark.deploy.worker.Worker \
    --webui-port $SPARK_WORKER_WEBUI_PORT $SPARK_MASTER >> $SPARK_WORKER_LOG/spark-worker.out 2>&1 </dev/null &
echo "All Set!"
exit 0