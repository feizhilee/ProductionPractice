from dao.BaseDao import BaseDao
'''
该类用来实现对职位数据的数据库操作
'''
class JobDao(BaseDao):

    def createJobs(self, params=[]):
        sql = "insert into book_info(book_Name, book_introduction, writer, publisher, price, book_grade, recommend_reason, book_type) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        result = self.execute(sql, params)
        self.commit()
        return result
        pass

    #SQL分析 聚合函数 count sum avg group by
    #运行jobstatistic查看结果
    def getSalaryStatisticByJobType(self):
        sql = "select avg(book_grade) as book_grade, book_type from book_info group by book_type"
        self.execute(sql)
        rs = self.fetchall()
        #print(rs)
        return rs
        pass

    #实现职位数据的查询和推荐
    def getJobPageList(self, searchs, currentPage, pageSize): #分页参数，为了进行分页查询
        sql = "select * from book_info where 1=1"   #‘where 1=1’为了方便后面加查询条件
        params = []
        if searchs.get("book_name"):
            sql += " and book_name=%s "
            params.append(searchs.get("book_name"))
            pass
        startRow = (currentPage - 1)*20
        sql += " limit %s, %s "  # limit 10, 10 表示从第十行取十条
        params.append(startRow)
        params.append(pageSize)
        self.execute(sql, params)
        rs = self.fetchall()
        return rs
        pass

    def getAllJobList(self): #分页参数，为了进行分页查询
        sql = "select * from book_info"   #‘where 1=1’为了方便后面加查询条件

        self.execute(sql)
        rs = self.fetchall()
        return rs
        pass

    #不同类别小说显示
    def getJobPageList2(self, searchs, currentPage, pageSize):  # 分页参数，为了进行分页查询
        sql = "select * from book_info where book_type = '小说'"  # ‘where 1=1’为了方便后面加查询条件
        params = []
        if searchs.get("book_name"):
            sql += " and book_name=%s "
            params.append(searchs.get("book_name"))
            pass
        startRow = (currentPage - 1) * 20
        sql += " limit %s, %s "  # limit 10, 10 表示从第十行取十条
        params.append(startRow)
        params.append(pageSize)
        self.execute(sql, params)
        rs = self.fetchall()
        return rs
        pass

    def getJobPageList3(self, searchs, currentPage, pageSize):  # 分页参数，为了进行分页查询
        sql = "select * from book_info where book_type = '艺术'"  # ‘where 1=1’为了方便后面加查询条件
        params = []
        if searchs.get("book_name"):
            sql += " and book_name=%s "
            params.append(searchs.get("book_name"))
            pass
        startRow = (currentPage - 1) * 20
        sql += " limit %s, %s "  # limit 10, 10 表示从第十行取十条
        params.append(startRow)
        params.append(pageSize)
        self.execute(sql, params)
        rs = self.fetchall()
        return rs
        pass
    def getJobPageList4(self, searchs, currentPage, pageSize):  # 分页参数，为了进行分页查询
        sql = "select * from book_info where book_type = '历史'"  # ‘where 1=1’为了方便后面加查询条件
        params = []
        if searchs.get("book_name"):
            sql += " and book_name=%s "
            params.append(searchs.get("book_name"))
            pass
        startRow = (currentPage - 1) * 20
        sql += " limit %s, %s "  # limit 10, 10 表示从第十行取十条
        params.append(startRow)
        params.append(pageSize)
        self.execute(sql, params)
        rs = self.fetchall()
        return rs
        pass
    def getJobPageList5(self, searchs, currentPage, pageSize):  # 分页参数，为了进行分页查询
        sql = "select * from book_info where book_type = '心理学'"  # ‘where 1=1’为了方便后面加查询条件
        params = []
        if searchs.get("book_name"):
            sql += " and book_name=%s "
            params.append(searchs.get("book_name"))
            pass
        startRow = (currentPage - 1) * 20
        sql += " limit %s, %s "  # limit 10, 10 表示从第十行取十条
        params.append(startRow)
        params.append(pageSize)
        self.execute(sql, params)
        rs = self.fetchall()
        return rs
        pass
    def getJobPageList6(self, searchs, currentPage, pageSize):  # 分页参数，为了进行分页查询
        sql = "select * from book_info where book_type = '法律'"  # ‘where 1=1’为了方便后面加查询条件
        params = []
        if searchs.get("book_name"):
            sql += " and book_name=%s "
            params.append(searchs.get("book_name"))
            pass
        startRow = (currentPage - 1) * 20
        sql += " limit %s, %s "  # limit 10, 10 表示从第十行取十条
        params.append(startRow)
        params.append(pageSize)
        self.execute(sql, params)
        rs = self.fetchall()
        return rs
        pass

    '''def getAllJobList2(self):  # 分页参数，为了进行分页查询
        sql = "select * from book_info where book_type = '科幻小说'"  # ‘where 1=1’为了方便后面加查询条件

        self.execute(sql)
        rs = self.fetchall()
        return rs
        pass'''

    def getJobByJobName(self, book_name):  # 分页参数，为了进行分页查询
        print(book_name)
        sql = "select * from book_info where book_name like %s"
        self.execute(sql, ["%{0}%".format(book_name)])
        rs = self.fetchall()
        print(rs)
        return rs
        pass

    def getJobByJobId(self, book_id):  # 分页参数，为了进行分页查询
        print(book_id)
        sql = "select * from book_info where book_id=%s"
        self.execute(sql, [book_id])
        rs = self.fetchone()
        print(rs)
        return rs
        pass

    def getJobSimilarList(self, book_id):  # 分页参数，为了进行分页查询
        sql = "select * from book_info where book_id in (select bookSimilarId from t_booksimilar where bookId=%s)"  # 多表联查
        self.execute(sql, [book_id])
        rs = self.fetchall()
        print(rs)
        return rs
        pass

    def createJobSimilarJob(self, params):   # params表示传参
        sql = "insert into t_similar values (%s, %s, %s)"
        result = self.execute(sql, params)
        self.commit()
        return result
        pass

    def getBookGrade(self, params):
        sql = "select book_name from book_info where (book_grade = 5.0 && price > 100)"
        result = self.execute(sql, params)
        self.commit()
        return result
        pass

    def getBookType(self):
        # sql1 = "select sum(book_type = '文学理论') as count1,sum(book_type = '纪实文学') as count2,sum(book_type = '名家作品') as count3 from book_info"
        sql1 = "select * from book_num"
        self.execute(sql1, ret="")
        rs1 = self.fetchall()
        return rs1
        pass
    pass
    pass