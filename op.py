import pymysql
from DBUtils.PooledDB import PooledDB


class OPMysql(object):
    """数据库连接池."""

    __pool = None

    def __init__(self, host, port, user, passwd):
        # 构造函数，创建数据库连接、游标
        self.conn = OPMysql.getmysqlconn(host, port, user, passwd)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn(host, port, user, passwd):
        if OPMysql.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, host=host, user=user, passwd=passwd, port=port, charset='utf8')
        return __pool.connection()

    # 查询
    def op_select(self, sql):
        # print('op_select', sql)
        self.cursor.execute(sql)  # 执行sql
        select_res = self.cursor.fetchall()  # 返回结果为字典
        # print('op_select', select_res)
        return select_res

    # 释放资源
    def dispose(self):
        self.cursor.close()
        self.conn.close()
