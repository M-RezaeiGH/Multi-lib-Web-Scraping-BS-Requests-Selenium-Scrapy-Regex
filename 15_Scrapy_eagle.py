print("*** Scrapy Framework:Making a spider - moving between links ***", "\n")

"""
    *The Scrapy framework has some general rules:
    
    1. The class name should include two parts:
       - The first part is the "your python file name".
       - The second part is the word "Spider".
       
    2. All classes must inherit from "scrapy.Spider".

    ** All classes must have two attributes and method:

    1- attribute name: which should be the name of the spider, 
      the framework suggests is "the name of your the python file."

    2- There must be a start_urls attribute in the class:
      This variable is a [list] containing "the addresses of the websites" you want to crawl.

    3- Make a method which name is "parse"

    4- for run code, open vscode terminal:
     1- activate your env in your vscode terminal with : "conda activate MyScrapyEnv"
     2- and write code in terminal: "scrapy crawl PojectName"
    
     5-You can "disable caching" entirely by adding the following line to "settings.py" file, so that old data is not stored:
      "HTTPCACHE_ENABLED = False"
      Then, run the spider again.

    6- you can save your output in (json , csv and JL) files with write below code in terminal:
      - scrapy crawl PojectName -o info.json
      - scrapy crawl PojectName -o info.csv
      - scrapy crawl PojectName -o info.jl   # JSON Lines (or JSONL)
"""
from typing import Any
import scrapy
from scrapy.http import Response

class EagleSpider(scrapy.Spider):
    name = '16_eagle'
    # start_urls = [
    #     "https://quotes.toscrape.com/",
    #     "https://www.python.org/",
    #     "https://www.skysports.com/",
    # ]
    
    start_urls = [
        "https://quotes.toscrape.com/",
    ]
    def parse(self, response):
        """
        for run codes open vscode terminal and write "scrapy crawl 16_eagle"
        Task: find texts & writer and tags in toscrape site.
        """
        # suggest use below print:
        print("#" * 100)
        # print(response)

        """ Introduce some methods:
            1- for first tag: use "get" (similar find in beautifullsoup)
            2- "extract_first" methode is similar to get
            3- for ALL tag use "getall" (similar find_All in beautifullsoup) 
            4- "extract" methode is similar to getall
        """

        # Using CSS selector to get the title text
        # print(f"site title's text is: {response.css('title::text').get()}")

        # Using XPath to get the title text
        # print(f"site title's text using XPath is: {response.xpath('//title/text()').get()}")

        # extract requirement data in text boxes in page1:
        # <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
        for data in response.css('div.quote'):
                # Extracting quote information
                # To get an output, we use Generator (and not a 'return' that returns the body of the function.)
                # In this case, an object is returned to us , which creates a sequence of values
                # yield is a dictionary which key is your optional name.
                yield {
                    'text': data.css('span.text ::text').get(),
                    'author': data.css('small.author ::text').get(),
                    'tags': data.css('div.tags a::text').getall(),
                }
                
        """extract requirement data in text boxes in ALL PAGES:"""
        # NEXT page element: <li class="next"> <a href="/page/2/">Next <span aria-hidden="true">→</span></a> </li>
        # next_page = response.xpath('//li.next a@(href)')

        "Approach-1:urljoin"
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page:
        #      next_page = Response.urljoin(next_page)  # use for:"/page/2/"
        #      yield scrapy.Request(url=next_page, callback=self.parse)

        "Approach-2:use follow for urljoin+request together"
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
             yield Response.follow(next_page,callback=self.parse)