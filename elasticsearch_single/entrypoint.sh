#!/bin/bash

# 检查es是否启动成功
check_health() {
    curl -fsSL --cacert config/certs/http_ca.crt -u "elastic:$ELASTIC_PASSWORD" https://localhost:9200 > /dev/null 2>&1
}

# 等待 Elasticsearch 健康,后台执行任务
(
    sleep 20 # 首次等待20秒后开始检查

    # task 1
    echo -e "----- 1. 检查es运行状态: -----"
    until check_health; do
        echo "$(date +"%Y-%m-%d %H:%M:%S") - es未就绪，等待重试..."
        sleep 1 # 重试间隔1秒
    done
    echo -e "\n\n\n----- es 已就绪 -----\n\n\n"

    # task 2
    echo -e "----- 2. 设置kibana_system用户的密码 -----"
    until curl -fsSL -s -X POST -H "Content-Type: application/json"\
     --cacert config/certs/http_ca.crt -u "elastic:${ELASTIC_PASSWORD}"\
     -d "{\"password\":\"${KIBANA_PASSWORD}\"}" \
     https://localhost:9200/_security/user/kibana_system/_password > /dev/null 2>&1;do
     echo "$(date +"%Y-%m-%d %H:%M:%S") - Kibana 密码设置失败，重试中..."
     sleep 1
    done
    echo -e "\n\n\n----- kibana_system 重置成功 -----\n\n\n" 

    # task 3
    # 将容器生成的config文件 拷贝到备份目录
    echo -e "----- 3. 备份certs目录为certs_backup -----"
    rm -rf /usr/share/elasticsearch/certs_backup/*
    cp -r /usr/share/elasticsearch/config/certs/* /usr/share/elasticsearch/certs_backup
) &


# 启动 Elasticsearch 进程
/bin/tini -- /usr/local/bin/docker-entrypoint.sh eswrapper