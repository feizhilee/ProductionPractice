# 爬虫启动脚本

from scrapy.cmdline import execute  # 引入爬虫命令行库


execute(['scarpy', 'crawl', 'jobspiders', '-a', 'bookType=法律', '-a',  'url=http://category.dangdang.com/pg{0}-cp01.26.00.00.00.00.html'])
