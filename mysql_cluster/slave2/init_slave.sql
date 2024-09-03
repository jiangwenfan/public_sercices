-- slave2从库连接master2主库，开始同步所有主库的数据
change replication source to source_host='language-mysql-master2',source_user='copydata-master1',source_password='admin@123K#',GET_MASTER_PUBLIC_KEY=1;
start replica;
show replica status\G;
