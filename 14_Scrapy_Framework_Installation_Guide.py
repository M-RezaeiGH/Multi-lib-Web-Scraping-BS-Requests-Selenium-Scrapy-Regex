print("*** Scrapy Framework: ***", "\n")
"NEXT CODES IN MyScrapyProject FOLDER"

print("***1-Installation Guide:****", "\n")
""" in Windows we have error unless you use the Anaconda tool for installation+VIRTUAL ENV, because other libraries must be installed along with Scrapy Lib."""
"conda install -c conda-forge scrapy"

"""in Linux we dont have any problem and you can run (pip install scrapy)"""

print("***2-Create & Activate conda env Guide:****", "\n")
"""
  "for create conda env" : "conda create -n MyProject'sName" --> in this notebook,nmae is : MyScrapyEnv
& "for create conda env+install libraries" : "conda create -n MyScrapyEnv python=3.8 pandas"
& "for activatation env" : "conda activate MyProject'sName" 
& "for de-activatation env" : "conda deactivate"
  "for deleting env": "conda remove --name "MyProject'sName" --all"
 """


print("***3-Which libraries has been installed during installing scrapy Lib.:****", "\n")
scrapy_dependencies = {
    "Twisted": "An asynchronous networking library essential for handling network requests in Scrapy.",
    "lxml": "A library for processing HTML and XML documents, known for its speed and accuracy in parsing web pages.",
    "cssselect": "Enables selection of HTML elements using CSS selectors, useful for locating elements on a web page.",
    "parsel": "Used for parsing and extracting data from HTML and XML documents, integrated directly into Scrapy.",
    "PyOpenSSL": "Helps handle HTTPS requests by providing SSL support.",
    "w3lib": "Contains various tools and functions for processing and analyzing URLs and data.",
    "service_identity": "Used for SSL certificate validation, ensuring secure HTTPS connections.",
    "cryptography": "Provides support for SSL and secure protocols for managing encrypted connections.",
    "queuelib": "A queuing library for managing requests in Scrapy's scheduling system.",
    "itemadapter": "Adapts and standardizes data formats for easier handling within Scrapy."
}

print("***4-Start Guide for scrapy project:****", "\n")
"""
1- Making virtual env. and activate it,
2- Install scrapy,
3- Go to your folder of your project with "cd your address" in anaconda prompt,
4- Make scrapy special folder with run code: "scrapy startproject crawl" in anaconda prompt,
5- Use your ide such as Vscode or etc. and choose your scrapy env.
6- in your ide, click File>Open and find your project with dedicated name.
7- Make spyder in your project with click and go to in your scrapy folder(which has scrapy.cfg file)
8- in that folder and right-click and make new YourProjectName.py
"""
