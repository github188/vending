drop database if exists test;
create database if not exists omd;

create user 'omd'@'%' identified by 'pjsong';
grant all on omd.* to 'omd@%' identified by 'pjsong' with grant option;
flush  privileges;
