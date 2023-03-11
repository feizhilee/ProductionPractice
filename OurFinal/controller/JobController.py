from flask import Blueprint, render_template, session, redirect, request
from service.JobService import JobService
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import jieba
import numpy as np
import math

jobController = Blueprint("jobContorller", __name__)
jobService = JobService()

currentPage = 1


def getPageNumNext():
    return currentPage + 1
    pass


@jobController.route("/joblist", methods=['get', 'post'])
def getJobList():
    jobList = jobService.getJobPageList(searchs={}, currentPage=1, pageSize=20)
    print("===================joblist======================")
    return render_template("joblist.html", jobList=jobList)
    pass


@jobController.route("/joblist2", methods=['get', 'post'])
def getJobList2():
    jobList2 = jobService.getJobPageList2(searchs={}, currentPage=1, pageSize=20)
    print("===================joblist2======================")
    return render_template("joblist2.html", jobList2=jobList2)
    pass


@jobController.route("/joblist3", methods=['get', 'post'])
def getJobList3():
    jobList3 = jobService.getJobPageList3(searchs={}, currentPage=1, pageSize=20)
    print("===================joblist3======================")
    return render_template("joblist3.html", jobList3=jobList3)
    pass

@jobController.route("/joblist4", methods=['get', 'post'])
def getJobList4():
    jobList4 = jobService.getJobPageList4(searchs={}, currentPage=1, pageSize=20)
    print("===================joblist4======================")
    return render_template("joblist4.html", jobList4=jobList4)
    pass

@jobController.route("/joblist5", methods=['get', 'post'])
def getJobList5():
    jobList5 = jobService.getJobPageList5(searchs={}, currentPage=1, pageSize=20)
    print("===================joblist5======================")
    return render_template("joblist5.html", jobList5=jobList5)
    pass

@jobController.route("/joblist6", methods=['get', 'post'])
def getJobList6():
    jobList6 = jobService.getJobPageList6(searchs={}, currentPage=1, pageSize=20)
    print("===================joblist6======================")
    return render_template("joblist6.html", jobList6=jobList6)
    pass

@jobController.route("/pagenumnext", methods=['get', 'post'])
def getPageNumNext():
    book_id = request.args.get('book_id')
    cPage = int(book_id) + 20
    cPage = math.ceil(cPage / 20)
    jobList = jobService.getJobPageList(searchs={}, currentPage=cPage, pageSize=20)
    print("===================joblist======================")
    return render_template("joblist.html", jobList=jobList)
    pass


@jobController.route("/pagenumnext2", methods=['get', 'post'])
def getPageNumNext2():
    book_id = request.args.get('book_id')
    cPage = int(book_id) + 20
    cPage = math.ceil(cPage / 20) - 163
    jobList2 = jobService.getJobPageList2(searchs={}, currentPage=cPage, pageSize=20)
    print("===================joblist======================")
    return render_template("joblist2.html", jobList2=jobList2)

@jobController.route("/pagenumnext3", methods=['get', 'post'])
def getPageNumNext3():
    book_id = request.args.get('book_id')
    cPage = int(book_id) + 20
    cPage = math.ceil(cPage / 20) - 327
    jobList3 = jobService.getJobPageList3(searchs={}, currentPage=cPage, pageSize=20)
    print("===================joblist======================")
    return render_template("joblist3.html", jobList3=jobList3)

@jobController.route("/pagenumnext4", methods=['get', 'post'])
def getPageNumNext4():
    book_id = request.args.get('book_id')
    cPage = int(book_id) + 20
    cPage = math.ceil(cPage / 20) - 499
    jobList4 = jobService.getJobPageList4(searchs={}, currentPage=cPage, pageSize=20)
    print("===================joblist======================")
    return render_template("joblist4.html", jobList4=jobList4)

@jobController.route("/pagenumnext5", methods=['get', 'post'])
def getPageNumNext5():
    book_id = request.args.get('book_id')
    cPage = int(book_id) + 20
    cPage = math.ceil(cPage / 20) - 657
    jobList5 = jobService.getJobPageList5(searchs={}, currentPage=cPage, pageSize=20)
    print("===================joblist======================")
    return render_template("joblist5.html", jobList5=jobList5)

@jobController.route("/pagenumnext6", methods=['get', 'post'])
def getPageNumNext6():
    book_id = request.args.get('book_id')
    cPage = int(book_id) + 20
    cPage = math.ceil(cPage / 20) - 802
    jobList6 = jobService.getJobPageList6(searchs={}, currentPage=cPage, pageSize=20)
    print("===================joblist======================")
    return render_template("joblist6.html", jobList6=jobList6)

@jobController.route("/pagenumpre", methods=['get', 'post'])
def getPageNumPre():
    try:
        book_id = request.args.get('book_id')
        cPage = int(book_id) - 20
        cPage = math.ceil(cPage / 20)
        jobList = jobService.getJobPageList(searchs={}, currentPage=cPage, pageSize=20)
        print("===================joblist======================")
        return render_template("joblist.html", jobList=jobList)
    except:
        jobList = jobService.getJobPageList(searchs={}, currentPage=1, pageSize=20)
        print("===================joblist======================")
        return render_template("joblist.html", jobList=jobList)
        pass

@jobController.route("/pagenumpre2", methods=['get', 'post'])
def getPageNumPre2():
    try:
        book_id = request.args.get('book_id')
        cPage = int(book_id) - 20
        cPage = math.ceil(cPage / 20) - 163
        jobList2 = jobService.getJobPageList2(searchs={}, currentPage=cPage, pageSize=20)
        print("===================joblist======================")
        return render_template("joblist2.html", jobList2=jobList2)
    except:
        jobList2 = jobService.getJobPageList2(searchs={}, currentPage=1, pageSize=20)
        print("===================joblist2======================")
        return render_template("joblist2.html", jobList2=jobList2)
        pass

@jobController.route("/pagenumpre3", methods=['get', 'post'])
def getPageNumPre3():
    try:
        book_id = request.args.get('book_id')
        cPage = int(book_id) - 20
        cPage = math.ceil(cPage / 20) - 327
        jobList3 = jobService.getJobPageList3(searchs={}, currentPage=cPage, pageSize=20)
        print("===================joblist======================")
        return render_template("joblist3.html", jobList3=jobList3)
    except:
        jobList3 = jobService.getJobPageList3(searchs={}, currentPage=1, pageSize=20)
        print("===================joblist3======================")
        return render_template("joblist3.html", jobList3=jobList3)
        pass

@jobController.route("/pagenumpre4", methods=['get', 'post'])
def getPageNumPre4():
    try:
        book_id = request.args.get('book_id')
        cPage = int(book_id) - 20
        cPage = math.ceil(cPage / 20) - 499
        jobList4 = jobService.getJobPageList4(searchs={}, currentPage=cPage, pageSize=20)
        print("===================joblist======================")
        return render_template("joblist4.html", jobList4=jobList4)
    except:
        jobList4 = jobService.getJobPageList4(searchs={}, currentPage=1, pageSize=20)
        print("===================joblist4======================")
        return render_template("joblist4.html", jobList4=jobList4)
        pass

@jobController.route("/pagenumpre5", methods=['get', 'post'])
def getPageNumPre5():
    try:
        book_id = request.args.get('book_id')
        cPage = int(book_id) - 20
        cPage = math.ceil(cPage / 20) - 657
        jobList5 = jobService.getJobPageList5(searchs={}, currentPage=cPage, pageSize=20)
        print("===================joblist======================")
        return render_template("joblist5.html", jobList5=jobList5)
    except:
        jobList5 = jobService.getJobPageList5(searchs={}, currentPage=1, pageSize=20)
        print("===================joblist5======================")
        return render_template("joblist5.html", jobList5=jobList5)
        pass

@jobController.route("/pagenumpre6", methods=['get', 'post'])
def getPageNumPre6():
    try:
        book_id = request.args.get('book_id')
        cPage = int(book_id) - 20
        cPage = math.ceil(cPage / 20) - 802
        jobList6 = jobService.getJobPageList6(searchs={}, currentPage=cPage, pageSize=20)
        print("===================joblist======================")
        return render_template("joblist6.html", jobList6=jobList6)
    except:
        jobList6 = jobService.getJobPageList6(searchs={}, currentPage=1, pageSize=20)
        print("===================joblist5======================")
        return render_template("joblist6.html", jobList6=jobList6)
        pass

@jobController.route("/pagenumend1", methods=['get', 'post'])
def getPageNumEnd1():
    book_id = request.args.get('book_id')
    cPage = int(book_id)
    cPage = math.ceil(cPage / 20)
    jobList = jobService.getJobPageList(searchs={}, currentPage=cPage, pageSize=10)
    print("===================joblist======================")
    return render_template("joblist.html", jobList=jobList)
    pass

@jobController.route("/pagenumend2", methods=['get', 'post'])
def getPageNumEnd2():
    book_id = request.args.get('book_id')
    cPage = int(book_id)
    cPage = math.ceil(cPage / 20) - 163
    jobList2 = jobService.getJobPageList2(searchs={}, currentPage=cPage, pageSize=15)
    print("===================joblist======================")
    return render_template("joblist2.html", jobList2=jobList2)
    pass

@jobController.route("/pagenumend3", methods=['get', 'post'])
def getPageNumEnd3():
    book_id = request.args.get('book_id')
    cPage = int(book_id)
    cPage = math.ceil(cPage / 20) - 327
    jobList3 = jobService.getJobPageList3(searchs={}, currentPage=cPage, pageSize=15)
    print("===================joblist======================")
    return render_template("joblist3.html", jobList3=jobList3)
    pass

@jobController.route("/pagenumend4", methods=['get', 'post'])
def getPageNumEnd4():
    book_id = request.args.get('book_id')
    cPage = int(book_id)
    cPage = math.ceil(cPage / 20) - 499
    jobList4 = jobService.getJobPageList4(searchs={}, currentPage=cPage, pageSize=13)
    print("===================joblist======================")
    return render_template("joblist4.html", jobList4=jobList4)
    pass

@jobController.route("/pagenumend5", methods=['get', 'post'])
def getPageNumEnd5():
    book_id = request.args.get('book_id')
    cPage = int(book_id)
    cPage = math.ceil(cPage / 20) - 657
    jobList5 = jobService.getJobPageList5(searchs={}, currentPage=cPage, pageSize=8)
    print("===================joblist======================")
    return render_template("joblist5.html", jobList5=jobList5)
    pass

@jobController.route("/pagenumend6", methods=['get', 'post'])
def getPageNumEnd6():
    book_id = request.args.get('book_id')
    cPage = int(book_id)
    cPage = math.ceil(cPage / 20) - 802
    jobList6 = jobService.getJobPageList6(searchs={}, currentPage=cPage, pageSize=14)
    print("===================joblist======================")
    return render_template("joblist6.html", jobList6=jobList6)
    pass


@jobController.route("/jobSimilar", methods=['get', 'post'])
def jobSimilar():
    print("===================jobSimilar======================")

    # 第一次合并，仅得到词汇表

    jobList = jobService.getAllJobList()
    texts = []
    for job in jobList:
        jobDes1 = job['book_name']
        jobDes2 = job['book_introduction']
        tmp1 = " ".join(list(jieba.cut(jobDes1)))
        tmp2 = " ".join(list(jieba.cut(jobDes2)))
        tmp = tmp1 + " " + tmp2
        texts.append(tmp)
    vectorizer = CountVectorizer()  # 传入一维数据
    # 传入词库，用于统计词库和词数
    tf = vectorizer.fit_transform(texts)
    print(tf.shape)
    print(len(texts))
    # 得到词库。词汇表
    words = vectorizer.get_feature_names_out()
    print(words)
    print(len(words))

    # 第二次分别合并。这是为了保证 book_name 与 book_introduction 在tf值的第二维上保持一致，需要各自重新再以word为基础进行一次append.  这里注意对原词表进行稀释。即加强后来的频率
    # name部分
    jobList = jobService.getAllJobList()
    text_name = []
    for i in words:
        text_name.append(i)

    for job in jobList:
        jobDes = job['book_name']
        text_add = " ".join(list(jieba.cut(jobDes))) + " "
        text_name.append(text_add * 10)
    vectorizer = CountVectorizer()  # 传入一维数据
    # 传入词库，用于统计词库和词数
    tf = vectorizer.fit_transform(text_name)
    tfidfTransformer = TfidfTransformer()
    # 计算tf-iwf(of name)
    tfiwf_name = tfidfTransformer.fit_transform(tf)
    print(tfiwf_name.shape)

    # introduction部分
    jobList = jobService.getAllJobList()
    text_intro = []
    for i in words:
        text_intro.append(i)

    for job in jobList:
        jobDes = job['book_introduction']
        text_add = " ".join(list(jieba.cut(jobDes))) + " "
        text_intro.append(text_add * 10)
    vectorizer = CountVectorizer()  # 传入一维数据
    # 传入词库，用于统计词库和词数
    tf = vectorizer.fit_transform(text_intro)
    tfidfTransformer = TfidfTransformer()
    # 计算tf-iwf(of introduction)
    tfiwf_intro = tfidfTransformer.fit_transform(tf)
    print(tfiwf_intro.shape)

    # 获取辞典部分的行索引
    start_index = len(words)  # 41827

    # 剔除辞典部分 ，  计算加权 tf值
    tfiwf = tfiwf_name[start_index:, :] * 0.5 + tfiwf_intro[start_index:, :] * 0.5
    print(tfiwf.shape)

    from sklearn.metrics.pairwise import linear_kernel
    # 通过向量的余弦相似度，计算出第一个文本和所有其他文本之间的相似度（!!注意此处包含了自己）
    # 处理相似度高的数据，并进行关联
    rowId = 0
    count = 10
    for row in tfiwf:
        src = jobList[rowId]
        cosine_similarities = linear_kernel(row,
                                            tfiwf).flatten()  # 计算第二行和其他行句子的相似度 结果为1表示和自己的相似度一致，结果为0表示和第三行句子没有任何重复之处
        for i in range(count + 1):  # 两层循环，只推荐十个数据
            index = np.argmax(cosine_similarities)  # 找到相似度最高的数据
            des = jobList[index]
            if src['book_id'] == des['book_id']:  # 排除自己
                cosine_similarities[index] = 0
                continue
                pass
            else:
                # 写数据库
                book_id = src['book_id']
                book_similar_id = des['book_id']
                cos_similar = cosine_similarities[index]
                cosine_similarities[index] = 0  # 每次找到相似度最大的数据后，就将其所对应的相似度置为0，以找到次大的数据
                if cos_similar > 0.1:
                    params = [book_id, book_similar_id, cos_similar]
                    jobService.createJobSimilarJob(params)
                    pass
                pass
        rowId += 1
        # count = 0
        pass

    return redirect("/joblist")
    pass


@jobController.route('/jobdetail', methods=['get', 'post'])
def getJobDetail():
    book_name = request.args.get('book_name')
    print(book_name)
    job = jobService.getJobByJobName(book_name)
    # jobSimilarList = jobService.getJobSimilarList(book_name)
    return render_template("joblist.html", job=job, jobList=job)  # jobSimilarList=jobSimilarList)
    pass


@jobController.route('/jobdetail2', methods=['get', 'post'])
def getJobDetail2():
    print("============= getJobDetail controller==================")
    book_id = request.args.get('book_id')
    print(book_id)
    job = jobService.getJobByJobId(book_id)
    jobSimilarList = jobService.getJobSimilarList(book_id)
    return render_template("jobdetail.html", job=job, jobList=jobSimilarList)
    pass


# 定义flask的json接口
import json


@jobController.route('/jobbar', methods=['get', 'post'])
def jobBarJson():
    jobBardata = jobService.getSalaryStatisticByJobType()
    print(type(jobBardata))
    return json.dumps(jobBardata, ensure_ascii=False)
    pass


@jobController.route("/charts-sparkline", methods=['get', 'post'])
def chartssparkline():
    print("==================bookbar================")
    return render_template("charts-sparkline.html")
    pass


# 定义flask的json接口
@jobController.route('/jobPie',methods=['post','get'])
def jobPiejson():
    jobPiedata = jobService.getBookType()
    # print(type(jobPiedata))
    # print(jobPiedata)
    return json.dumps(jobPiedata, ensure_ascii=False)
    pass