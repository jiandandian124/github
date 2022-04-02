# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from twisted.internet.error import TCPTimedOutError, TimeoutError
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random

class MsdsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MsdsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    # def __init__(self):
    #     # self.retry_http_codes = [ 503]
    #     self.PROXIES = [
    #     '114.67.236.208:9999',
    #     '223.244.179.60:3256',
    #     '60.191.11.249:3128',
    #     '223.241.77.244:3256',
    #     '218.7.171.91:3128',
    #     '112.195.240.126:3256'
    # ]
    # def process_response(self, request, response, exception, spider):
    #     """当下载器完成http请求，返回响应给引擎的时候调用process_response"""

    #     if response.status == '503':
    #         self.process_request_back(request, spider)  # 连接超时才启用代理ip机制
    #         return request
    #     elif isinstance(exception, TimeoutError):
    #         self.process_request_back(request, spider)  # 连接超时才启用代理ip机制
    #         return request
        
    #     elif isinstance(exception, TCPTimedOutError):
    #         self.process_request_back(request, spider)
    #         return request
    #     else:
    #         return response
    
    # def process_exception(self, request, exception, spider):       
    #     if isinstance(exception, TimeoutError):
    #         self.process_request_back(request, spider)  # 连接超时才启用代理ip机制
    #         return request
        
    #     elif isinstance(exception, TCPTimedOutError):
    #         self.process_request_back(request, spider)
    #         return request

    # def process_request_back(self, request, spider):
    #     proxy = random.choice(self.PROXIES)
    #     request.meta['proxy'] = proxy
        # request.headers["Proxy-Authorization"] = xun.headers

    


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
