from dao.UserDao import UserDao

class UserService():

    def getUserByUserName(self, userName):
        userDao = UserDao()

        try:
            rs = userDao.getUserByUserName(userName)
            return rs
        finally:
            userDao.close()
        pass
    pass