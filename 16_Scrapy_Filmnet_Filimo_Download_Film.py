print("*** Scrape Multi-web Websites With One Spider ***", "\n")

"""
    *The Scrapy framework has some general rules:
    
    1. The class name should include two parts:
       - The first part is the "your Python file name".
       - The second part is the word "Spider".
       
    2. All classes must inherit from "scrapy.Spider".

    ** All classes must have two attributes and one method:

    1- Attribute `name`: This should be the name of the spider. 
      The framework suggests using "the name of your Python file."

    2- There must be a `start_urls` attribute in the class:
      This variable is a [list] containing "the addresses of the websites" you want to crawl.

    3- Create a method named `parse`.

    4- To run the code, open the VS Code terminal:
     1- Activate your environment in the VS Code terminal with: "conda activate MyScrapyEnv"
     2- Run the following in the terminal: "scrapy crawl ProjectName"
    
    5- You can "disable caching" entirely by adding the following line to the "settings.py" file so that old data is not stored:
      "HTTPCACHE_ENABLED = False"
      Then, run the spider again.

    6- You can save your output in (JSON, CSV, or JL) files by using the following terminal commands:
      - scrapy crawl ProjectName -o info.json
      - scrapy crawl ProjectName -o info.csv
      - scrapy crawl ProjectName -o info.jl   # JSON Lines (or JSONL)

    7- Filimo's website restricts access to certain pages due to the `robots.txt` file, which defines rules and limitations for crawlers. In this case, it prevents the Scrapy crawler from accessing specific pages, such as `/asparagus/movies/war`.
        In the project settings file, change the value of `ROBOTSTXT_OBEY` to `False`:
        ROBOTSTXT_OBEY = False
        Task:
        Extract the links of the first 50 movies from the page and navigate to the details page of each movie.
"""
           
import scrapy
from scrapy.http import Response

class FilmnetSpider(scrapy.Spider):
    name = 'Filmnet'
    start_urls = [
        "https://filmnet.ir/contents?types=single_video&order=latest&categories=850b9cc8-2e0b-4d92-bafc-5640d3bb0cb0",
        # "https://www.filimo.com/asparagus/movies/war",
    ]

    def parse(self, response: Response):
        """
        Extracts the first 50 movie links and navigates to each movie's detail page.
        """
        print("#" * 100)  # For debugging or marking output

        # Find the first 50 film elements of Filmnet: ul class="css-1xm8omy e1eum8tf0" --> li class="css-1y9sbsv e1e5zztb0"
        film_elements = response.css("ul.css-1xm8omy.e1eum8tf0 li.css-1y9sbsv.e1e5zztb0")[:50]

        for film in film_elements:
            # Get the detail link for each film
            film_link = film.css("a::attr(href)").get()
            if film_link:
                # Make the link absolute and follow it to scrape film details
                yield response.follow(film_link, callback=self.parse_film_details)

    def parse_film_details(self, response: Response):
        """
        Extracts Filmnet details like title, director, actors, and summary from each film's detail page.
        """
        # Extract film title
        title = response.css("div.css-jz7yzp.erovl7p0 h1.css-1iv1u7k.e1eum8tf0::text").get()

        # Extract director
        director = response.css("table.css-orfati.e1eum8tf0 td.css-mf3wsb.e1eum8tf0::text").re_first(r'Director: (.+)')

        # Extract list of actors
        actors = response.css("table.css-orfati.e1eum8tf0 td.css-mf3wsb.e1eum8tf0::text").re(r'Actors: (.+)')

        # Extract summary of the story
        summary = response.css("p.eh50r6x0.css-1bes4v.e1eum8tf0::text").get()

        yield {
            'title': title,
            'director': director,
            'actors': actors,
            'summary': summary,
        }
