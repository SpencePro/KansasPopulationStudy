# KansasPopulationStudy
This is a small project to show the population distribution in the state of Kansas. I was curious to see to what extent the 'small town' characterization of Kansas holds true by looking at what percentage of the population lives in a town of a given size. ‘Town’ in this project refers to a municipality, and the list of towns and their populations comes from https://www.kansas-demographics.com/cities_by_population. 

I have always conceived of Kansas as a rural, ‘small-town’ state, and I was curious to know exactly how true this is. I created a web scraper with Selenium, `main.py`, and gathered the towns and their populations from the website and placed it in an SQLite database, `KansasPopulationStats.db`. I then used Pandas to parse the data and organize it into data frames, which I was then able to visualize as both bar and pie charts with Matplotlib. I decided to use Selenium as it is significantly faster than BeautifulSoup, and Scrapy, while even faster, is not optimized for Windows. I decided to use SQLite as the relatively small amount of data and the low complexity of the database meant that the lightweight built-in Python module `sqlite3` was sufficient for my purposes; no need for a server-based database like MySQL or PostgreSQL. I used Pandas because the data frames it creates are very easy to manipulate and plug directly into a visual presentation module, and I used Matplotlib to display these visuals as it is the simplest tool for this task. I may update this in the future, and use the Seaborn extension to create more intricate, appealing visuals.

The project consists of the following components:

env - The virtual environment containing the modules used in this project; these are: selenium, pandas, matplotlib, and
sqlite3.  

main.py - The main webscraper of the project. Creates the SQLite tables, scrapes the websites, and writes the results
to the database. 

data.py - The file where the database is queried, the results are converted to Pandas dataframes, and Matplotlib
creates the visuals. 

KansasPopulationStats.db - The database which holds the scraped town ranks, town names, and populations. 
SQLite was used as the database due to being lightweight, and to the low number of items to be placed in it. 

Kansas Population Study.ipynb - The Jupyter notebook version of the project's data visualization, which
combines the code and visuals from data.py with a brief explanation of the , presented
cleanly in a Jupyter notebook for those who prefer that. 

chromedriver.exe - The webdriver in this project is Chrome Webdriver version 87. If you wish to use this program for
yourself you will need to use the correct webdriver for your browser and version.  
