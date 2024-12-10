#!/bin/bash
# 定义 CA 证书和用户名密码
CA_CERT="config/certs/http_ca.crt"
ELASTIC_URL="https://localhost:9200/_security/_authenticate"

# 检查 Elastic 用户
if ! curl -fsSL --cacert "$CA_CERT" -u "elastic:${ELASTIC_PASSWORD}"  "$ELASTIC_URL" > /dev/null; then
  echo "test: Elastic 用户认证失败"
  exit 1
fi

# 检查 Kibana 用户
if ! curl -fsSL --cacert "$CA_CERT" -u "kibana_system:${KIBANA_PASSWORD}" "$ELASTIC_URL" > /dev/null; then
  echo "test: Kibana 用户认证失败"
  exit 1
fi

# 检查证书文件被成功备份
if [ ! -f "certs_backup/http_ca.crt" ]; then
  echo "test: 证书文件备份失败"
  exit 1
fi
 
# 健康检查通过
echo "Health check passed"
exit 0
