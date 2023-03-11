from dao.JobDao import JobDao

class JobService():

    def getJobPageList(self, searchs, currentPage, pageSize):
        jobDao = JobDao()
        try:
            rs = jobDao.getJobPageList(searchs, currentPage, pageSize)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getAllJobList(self):
        jobDao = JobDao()
        try:
            rs = jobDao.getAllJobList()
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobPageList2(self, searchs, currentPage, pageSize):
        jobDao = JobDao()
        try:
            rs = jobDao.getJobPageList2(searchs, currentPage, pageSize)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobPageList3(self, searchs, currentPage, pageSize):
        jobDao = JobDao()
        try:
            rs = jobDao.getJobPageList3(searchs, currentPage, pageSize)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobPageList4(self, searchs, currentPage, pageSize):
        jobDao = JobDao()
        try:
            rs = jobDao.getJobPageList4(searchs, currentPage, pageSize)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobPageList5(self, searchs, currentPage, pageSize):
        jobDao = JobDao()
        try:
            rs = jobDao.getJobPageList5(searchs, currentPage, pageSize)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobPageList6(self, searchs, currentPage, pageSize):
        jobDao = JobDao()
        try:
            rs = jobDao.getJobPageList6(searchs, currentPage, pageSize)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    '''def getAllJobList2(self):
        jobDao = JobDao()
        try:
            rs = jobDao.getAllJobList2()
            return rs
        finally:
            jobDao.close()
            pass
        pass'''

    def createJobSimilarJob(self, params):
        jobDao = JobDao()
        try:
            rs = jobDao.createJobSimilarJob(params)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobByJobName(self, book_name):  # 分页参数，为了进行分页查询
        jobDao = JobDao()
        try:
            rs = jobDao.getJobByJobName(book_name)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobByJobId(self, book_id):  # 分页参数，为了进行分页查询
        jobDao = JobDao()
        try:
            rs = jobDao.getJobByJobId(book_id)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getJobSimilarList(self, book_id):  # 分页参数，为了进行分页查询
        jobDao = JobDao()
        print(book_id)
        try:
            print("============getJobSimilarList===========")
            rs = jobDao.getJobSimilarList(book_id)
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getSalaryStatisticByJobType(self):
        jobDao = JobDao()
        try:
            rs = jobDao.getSalaryStatisticByJobType()
            return rs
        finally:
            jobDao.close()
            pass
        pass

    def getBookGrade(self):
        jobDao = JobDao()
        try:
            rs = jobDao.getBookGrade()
            return rs
        finally:
            jobDao.close()
            pass
        pass

    # 获取图书类型
    def getBookType(self):
        jobDao = JobDao()
        try:
            rs = jobDao.getBookType()
            return rs
        finally:
            jobDao.close()
            pass
        pass

    pass

    pass