-- 初始化 language db
CREATE DATABASE IF NOT EXISTS `language`;
-- 初始化 language user     [修改为你的密码]
CREATE USER `language`@'%' IDENTIFIED BY 'YourPWD';
GRANT all privileges ON `language`.* to `language`@'%';
GRANT all privileges ON `test_language`.* to 'language'@'%';


-- 初始化 interview db
CREATE DATABASE IF NOT EXISTS `interview`;
-- 初始化 interview user    [修改为你的密码]
CREATE USER `interview`@'%' IDENTIFIED BY 'YourPWD';
GRANT all privileges ON `interview`.* to `interview`@'%';
GRANT all privileges ON `test_interview`.* to 'interview'@'%';