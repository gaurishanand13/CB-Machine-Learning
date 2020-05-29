import scrapy
class json_parsing_quotes_spider(scrapy.Spider):

    name = "json_parsing_quotes_spider"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #Note -  Best way to learn, how you will be fetching the data , just run this 
        #' scrapy shell "http://quotes.toscrape.com/page/1/" ' on terminal. To learn how you can perform actions on the response coming from the net
        # (for more reference see the screesnshots of how the response was handled)

        for q in response.css('div.quote'): 
            text = q.css('span.text::text').get() 
            author = q.css('small.author::text').get() 
            tags = q.css('a.tag::text').getall()

            #It will make a json array in the json file where we are yielding the data and yield writes the function 
            yield{
                'text' : text,
                'author' : author,
                'tags' : tags
            }

        
# To run the above spider, run the below command in terminal -> this will make a new quotes.json file and save the ouput json in quotes.json file.
# scrapy crawl json_parsing_quotes_spider -o quotes.json
#  Don't need to make quotes.json file before only, it will make it automatically
