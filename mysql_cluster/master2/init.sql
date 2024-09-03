-- 账号使用master1上同步过来的账号

-- master2从库连接master1主库，开始同步所有master1主库的数据
change replication source to source_host='language-mysql-master1',source_user='copydata-master1',source_password='admin@123K#',GET_MASTER_PUBLIC_KEY=1;
start replica;
show replica status\G;
