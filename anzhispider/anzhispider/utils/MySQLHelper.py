import os
import pymysql
import pymysql.cursors
import logging

thread_logger = logging.getLogger()


class MySQLHelper:
    def __init__(self):
        pass

    def query(self, sql):
        # 打开数据库连接
        db = self.conn()

        # 使用cursor()方法获取操作游标
        cur = db.cursor()

        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        # sql = "select * from user"
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录
            return results
        except Exception as e:
            thread_logger.debug('[mysql]：{} \n\tError SQL： {}'.format(e, sql))
            raise e
        finally:
            self.close(db)  # 关闭连接

    def update(self, sql):
        # 2.插入操作
        db = self.conn()

        # 使用cursor()方法获取操作游标
        cur = db.cursor()

        try:
            data = cur.execute(sql)
            # 提交
            data1 = db.commit()
            return True
        except Exception as e:
            thread_logger.debug('[mysql]：{} \n\tError SQL： {}'.format(e, sql))
            # 错误回滚
            db.rollback()
            return False
        finally:
            self.close(db)

    # 建立链接
    def conn(self):
        db = pymysql.connect(host="***数据库地址***", user="***数据库用户名**",
                             password="****数据库密码***", db="app_anzhigame", port=3306, use_unicode=True,
                             charset="utf8mb4")
        return db

    # 关闭
    def close(self, db):
        db.close()
