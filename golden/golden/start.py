from scrapy import cmdline
cmdline.execute("scrapy crawl data -o item.csv -t csv".split())