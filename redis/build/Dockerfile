FROM redis:7.0-alpine

# 拷贝初始化脚本
WORKDIR /data
COPY ./init_keys /usr/local/etc/redis/init_keys
COPY ./start.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/start.sh

# 启动
CMD ["start.sh"]
