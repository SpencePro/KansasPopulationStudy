from selenium import webdriver
import sqlite3
import re

'''def make_database():
	conn = sqlite3.connect('KansasPopulationStats.db')
	c = conn.cursor()
	
	c.execute("""CREATE TABLE kansas_population_stats (
		rank TEXT,
		town_name TEXT,
		population INTEGER
	)""")

	conn.commit()
	conn.close()

make_database()'''

driver = webdriver.Chrome()

driver.get('https://www.kansas-demographics.com/cities_by_population')

table = driver.find_elements_by_xpath('//table')  # table becomes a list of all info in the table

def write_to_db(rank, town_name, population):
	conn = sqlite3.connect('KansasPopulationStats.db')
	c = conn.cursor()
	c.execute("INSERT INTO kansas_population_stats VALUES (?,?,?)", (rank, town_name, population))
	conn.commit()
	conn.close()

def parse(table): 
	num = 2
	while num < 501:
		for town in table:
			rank = town.find_element_by_xpath(f'//tr[{num}]/td[1]').text
			
			if 'TIE' in rank:  # if there are multiple items in the name column, separate them
				name = town.find_element_by_xpath(f'//tr[{num}]/td[2]').text
				name = re.split(', and |, | and ', name)
				name_length = len(name)
				name_num = 0  # set variable that will increase with each iteration

				population = town.find_element_by_xpath(f'//tr[{num}]/td[3]').text
				if ',' in population:
					population = str(population).replace(',', '')  # remove comma from the population number
				
				while name_num < name_length:  # the index increases with each iteration up to the number of elements; this allows the function to handle any number of elements
					write_to_db(str(rank), str(name[name_num]), int(population))  # write each TIEd town to DB as own entry
					print('Rank:', rank)
					print('Name:', name[name_num])
					print('Population:', population, '\n')
					name_num += 1

			else:	
				name = town.find_element_by_xpath(f'//tr[{num}]/td[2]').text
				population = town.find_element_by_xpath(f'//tr[{num}]/td[3]').text
				if ',' in population:
					population = str(population).replace(',', '')
				write_to_db(str(rank), str(name), int(population))
				print('Rank:', rank)
				print('Name:', name)
				print('Population:', population, '\n')
			
			num += 1

print("Scraping...")
parse(table)
print("Done")
