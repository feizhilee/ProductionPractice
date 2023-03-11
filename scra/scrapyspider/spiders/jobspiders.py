import scrapy
from scrapyspider.items import ScrapyspiderItem

class JobspidersSpider(scrapy.Spider):
    name = 'jobspiders'
    print("===========JobspidersSpider entered=============")
    # start_urls = ['http://category.dangdang.com/pg2-cp01.03.56.00.00.00.html']
    start_urls = []
    base_url = ""
    page_no = 1

    def __init__(self, bookType, url, *args, **kw):
        super().__init__(*args, **kw)
        self.booktype = bookType
        JobspidersSpider.base_url = url
        JobspidersSpider.start_urls.append(self.base_url.format(JobspidersSpider.page_no))
        pass

    def parse(self, response):
        pagebookList = response.xpath('//div[@id="search_nature_rg"]/ul')  # 返回一个选择器对象列表  Selector
        for i in range(1, 61, 1):
            for bookinfo in pagebookList:  # 60条
                name_plus_intro = bookinfo.xpath('li[{0}]/p[1]/a/text()'.format(i))
                writer = bookinfo.xpath('li[{0}]/p[5]/span[1]/a[1]/text()'.format(i))
                publisher = bookinfo.xpath('li[{0}]//p[5]/span[3]/a/text()'.format(i))
                price = bookinfo.xpath('li[{0}]//p[3]/span[1]/text()'.format(i))
                str_grade = bookinfo.xpath(
                    'li[{0}]//p[4]/span/span'.format(i))  # <a ****/a> 括号里的内容，无法直接用text()提取，反之其它在括号中间的就可以用
                recommend_reason = bookinfo.xpath('li[{0}]//p[2]/text()'.format(i))

                if name_plus_intro and writer and publisher and price and str_grade:
                    # name and intro
                    wanna_text = name_plus_intro.extract()[0].strip()
                    if wanna_text.find('（') > 20 or wanna_text.find('（') == -1:  # 没有英文括号
                        if wanna_text.find('(') == 1:  # 当当网程序员错把中文括号打成英文括号，背全锅
                            book_name = wanna_text.split('(', 1)[0]
                            book_intro = wanna_text.split('(', 1)[1].replace(')', ' ')
                        else:
                            if wanna_text.find(' ') > 20 or wanna_text.find(' ') == -1:  # 没有intro
                                book_name = wanna_text.strip()
                                book_intro = "无"
                            else:  # 没有中英文括号，用空格分割book_name 和 introduction
                                book_name = wanna_text.split(' ', 1)[0]
                                book_intro = wanna_text.split(' ', 1)[1]
                    else:
                        book_name = wanna_text.split('（', 1)[0]
                        book_intro = wanna_text.split('（', 1)[1].replace('）', ' ')

                    # writer
                    writer = writer.extract()[0].strip()

                    # publisher
                    publisher = publisher.extract()[0].strip()

                    # price
                    price = price.extract()[0].strip()
                    price = price[1:]
                    price = float(price)

                    # grade
                    str_grade = str_grade.extract()[0].strip()
                    str_grade = str_grade.split(":", 1)[1].strip()
                    str_grade = str_grade.split("%", 1)[0]
                    grade = float(str_grade) / 20.0

                    # recommend_reason

                    try:
                        recommend_reason = recommend_reason.extract()[0].strip()
                        pass
                    except:
                        recommend_reason = "无"
                        pass

                    # recommend_reason = recommend_reason.extract()[0].strip()
                    # print("书名: " + book_name)
                    # print("类型: " + self.booktype)
                    # print("作者: " + writer)
                    # print("出版社: " + publisher)
                    # print("简介: " + book_intro)
                    # print("价格: " + str(price) + "元")
                    # print("评分: " + str(grade) + "星")
                    # print("推荐理由: " + recommend_reason)
                    # print('=' * 100)

                    # jobCompany = jobCompany.extract()[0].strip()
                    # jobDetail = "".join(jobDetail1.extract()) + "".join(jobDetail2.extract())

                    pipItem = ScrapyspiderItem()
                    pipItem['book_name'] = book_name
                    pipItem['book_introduction'] = book_intro
                    pipItem['writer'] = writer
                    pipItem['publisher'] = publisher
                    pipItem['price'] = price
                    pipItem['book_grade'] = grade
                    pipItem['recommend_reason'] = recommend_reason
                    pipItem['book_type'] = self.booktype
                    yield pipItem  # 向管道输出数据
                    pass



        print("=======================第{0}页爬完==========================".format(JobspidersSpider.page_no))
        # 分页采集数据
        JobspidersSpider.page_no += 1
        next_url = JobspidersSpider.base_url.format(JobspidersSpider.page_no)
        if JobspidersSpider.page_no < 61:   #控制爬取的页数
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
        pass
