#!/bin/sh

# 当redis启动成功时,执行初始化操作
(
    echo "`date`" >> ./log.txt
    echo "sub thread start.." >> ./log.txt

    num=0;
    # redis-cli ping is PONG
    while true;
    do
        status=`redis-cli ping`;
        echo "${num} ${status}" >> ./log.txt

        # 当在2分钟内启动才会初始化
        if [ ${status} == 'PONG' ] && [ ${num} -lt 120 ]
        then
            # 启动成功执行初始化脚本
            cat /usr/local/etc/redis/init_keys | redis-cli
            echo "初始化成功" >> ./log.txt
            echo "success" > ./status
            break;
        else
            echo "初始化失败" >> ./log.txt
            echo "error" > ./status
        fi

        let "num++";
        sleep 1;
    done

    echo "sub thread end..." >> ./log.txt
) &

# 启动redis
redis-server /usr/local/etc/redis/redis.conf
