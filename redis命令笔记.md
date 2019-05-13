设置键值对：`SET key value`  
查询单个值：`GET key`  
检查是否存在一个值(存在返回1，否则为0)：`EXISTS key`  
设置过期时间：`EXPIRE key seconds`  
查找符合条件的keys(模糊查询用*):`KEYS key`  
从一个数据库迁移到另外一个数据库:`MOVE key db_destination`  
移除过期时间：`PERSIST key`  
随即返回一个key_name：`RANDOMKEY`  
修改key的名称：`RENAME key newname`  
查看key的类型:`TYPE key`  
查询value切片之后的值(可使用负数)：`GETRANGE key start end`  
查询多个值:`MGET key1 key2...`  
查询value的长度:`STRLEN key`  
新增多个键值对:`MSET key1 value1 key2 value2...`  
新增多个键值对(给定的key都不存在):`MSETNX key1 value1...`  
将key中存储的数字值增1(减少为`DECR`)：`INCR key`  
将key中存储的数字值增n：`INCRBY key n`   
将key中存储的数字值增浮点型：`INCRBYFLOAT key n_f`  
