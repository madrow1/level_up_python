import scrapy

# All of this is created with Scrapy commands in the terminal
# scrapy startproject $project_name <- generates project files
# scrapy genspider $name $url <- creates a spider pointing to the start domain 
class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    # Function that defines how to data collected from the start_url will be parsed by the spider
    def parse(self, response):
        # two potential strategies here, either using CSS or Xpath, 
        #title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        return {"title" : title}

