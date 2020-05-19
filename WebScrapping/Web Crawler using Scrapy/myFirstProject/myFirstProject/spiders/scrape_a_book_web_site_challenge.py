import scrapy
class scrappingBookWebSite(scrapy.Spider):

    name = "scrappingBookWebSite"

    def __init__(self):
        with open("books.csv",'a') as f:
            f.write("image_url,book_title,product_price" + "\n")



    #Don't need to write all the 50 urls. Instead i will make it recursive. At the end of each url , i will get the url for the next website too
    def start_requests(self):
        urls = [
            'http://books.toscrape.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        booksList = response.css('ol.row')[0].css('li') 

        with open("books.csv",'a') as f:
            for book in booksList:
                image_url = book.css('img').attrib['src'] 
                #This is how an attribute can be fetched
                book_title = book.css('h3 a::attr(title)').get()#We can also get the attribute like this -> book.css('h3 a')::attr[title]
                price = book.css('div.product_price p.price_color::text').get() 
                temp = str(image_url) + "," + f'"{book_title}"' + "," + str(price) + "\n"
                f.write(temp)

        temp = response.css('li.next a::attr(href)').get()
        #Now we will recurrsively call on the next url
        if temp is not None:
            next_url = ""
            if "catalogue" not in temp:
                next_url = "http://books.toscrape.com/catalogue/" + temp 
            else:
                next_url = "http://books.toscrape.com/" + temp
            yield scrapy.Request(next_url,callback=self.parse)
