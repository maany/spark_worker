#!/bin/bash
docker build -t spark_worker_sh_pre_config ./sh/pre_config/
docker run -it -e "EXECUTION_ID=1" -v $(pwd)/:/component_repository spark_worker_sh_pre_config bash