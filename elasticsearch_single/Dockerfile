# ccr.ccs.tencentyun.com/docker-hub-cache/elasticsearch:8.16.1
FROM docker.elastic.co/elasticsearch/elasticsearch:8.16.1

# 添加自定义脚本
COPY entrypoint.sh /usr/share/elasticsearch/entrypoint.sh
COPY health_check.sh /usr/share/elasticsearch/health_check.sh

USER root
RUN chmod +x /usr/share/elasticsearch/health_check.sh
USER 1000:0

# 替换默认的启动命令
ENTRYPOINT ["/bin/bash","/usr/share/elasticsearch/entrypoint.sh"]
