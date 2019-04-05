#!/bin/bash
docker stop simple_spark_worker && docker rm simple_spark_worker
### BOOT EVENT ###
sudo docker build -t simple_spark_worker sh/
sudo docker run -itd \
    --name simple_spark_worker \
    --privileged \
    -p 8081:8081 \
    -v $(pwd)/sh/config:/etc/simple_grid/config \
    -v $(pwd)/augmented_site_level_config_file.yaml:/etc/simple_grid/augmented_site_level_config_file.yaml \
    simple_spark_worker \
#### PRE INIT HOOKS #####


### INIT EVENT ######
sudo docker exec -st simple_spark_worker /etc/simple_grid/config/init.sh

#### POST INIT HOOKS ######