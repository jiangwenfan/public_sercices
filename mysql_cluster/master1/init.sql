-- 创建主从同步账号
create user 'copydata-master1'@'%' identified by 'admin@123K#';
grant replication slave on *.* to 'copydata-master1'@'%';
FLUSH PRIVILEGES;

-- master1从库连接master2主库，开始同步所有master2主库的数据
change replication source to source_host='language-mysql-master2',source_user='copydata-master1',source_password='admin@123K#',GET_MASTER_PUBLIC_KEY=1;
start replica;
show replica status\G;
