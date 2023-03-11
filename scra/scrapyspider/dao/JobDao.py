from scrapyspider.dao.BaseDao import BaseDao


'''
用来实现对职位数据的数据库操作
'''
class JobDao(BaseDao):

    def createJobs(self, params=[]):
        sql = "insert into book_info (book_name, book_introduction, writer, publisher, price, book_grade, recommend_reason, book_type) " \
              "values (%s, %s, %s, %s, %s, %s, %s, %s)"
        result = self.execute(sql, params)
        self.commit()
        return result
        pass

    # # SQL分析  聚合函数  count  sum  avg  group by
    # def getSalaryStaticsByJobType(self):
    #     sql = "select avg(meanSalary) as meanSalary, jobType from t_jobinfo group by jobType"
    #     self.execute(sql, ret="")
    #     rs = self.fetchall()
    #     return rs
    #     pass
    #
    #     # SQL分析  聚合函数  count  sum  avg  group by
    #
    # def getSalaryStaticsByJobCity(self):
    #     sql = "select avg(meanSalary) as meanSalary, jobCity from t_jobinfo group by jobCity"
    #     self.execute(sql, ret="")
    #     rs = self.fetchall()
    #     return rs
    #     pass

    pass