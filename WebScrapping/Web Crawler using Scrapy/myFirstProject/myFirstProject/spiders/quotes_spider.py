#I have seen the basics from of scrapy from this webSite - https://docs.scrapy.org/en/latest/intro/tutorial.html
import scrapy

#Spiders are classes that you define and Scrapy uses it to scrape information from a website. These all classes should
#inherit the base Spider Class which is in scrapy module for it to srap information from the website.
#We will run this class's object from terminal , which by default first runs the parse function.
class QuotesSpider(scrapy.Spider):

    name = "quotes" #It is the name of the spider. Therefore it must be unique within a project.

    #From this , we return an iterable of Request urls
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #Here we need to define , how the data should be parsed .  When a response from the requests on  url's mentioned in start_request
    #is made. This function will be called for each url in the above lists of urls
    def parse(self, response):
        self.log('type(response) is ' + str(type(response)))

        pageNumber = response.url.split("/")[-2] #Getting the page number from the url
        filename = 'quotes-%s.html' % pageNumber
        self.log('Saved file %s' % filename)

        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('type(response.body) is' +  str(type(response.body)))

#For running the above spider, run the command scrapy crawly spider_name i. in this case 'scrapy crawl quotes'
#This scrawler will write the file with names quotes-1.html and quotes-2.html with the html data of the above 2 sites