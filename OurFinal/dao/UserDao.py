from dao.BaseDao import BaseDao

class UserDao(BaseDao):


    def getUserByUserName(self, userName):
        sql = "select * from t_user where userName=%s"
        result = self.execute(sql, [userName])
        rs = self.fetchone()
        return rs
        pass
    pass