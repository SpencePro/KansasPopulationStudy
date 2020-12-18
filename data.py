import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


'''def drop_tables():
    conn = sqlite3.connect('KansasPopulationStats.db')
    c = conn.cursor()

    c.execute('DROP TABLE kansas_population_stats')

    c.execute("""CREATE TABLE kansas_population_stats (
		rank TEXT,
		town_name TEXT,
		population INTEGER
	)""")

    conn.commit()
    conn.close()

drop_tables()'''

conn = sqlite3.connect('KansasPopulationStats.db')

towns_info = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    """, conn)

towns_ties = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    WHERE rank LIKE '%TIE%'
    """, conn)

towns_top_ten = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    WHERE rank IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    """, conn)

towns_above_100_000 = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    WHERE population > 100000
    """, conn)

towns_above_10_000 = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    WHERE population > 10000
    """, conn)

towns_above_1000 = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    WHERE population > 1000
    """, conn)

towns_below_1000 = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    WHERE population < 1000
    """, conn)

towns_below_100 = pd.read_sql_query("""
    SELECT rank, town_name, population
    FROM kansas_population_stats
    WHERE population < 100
    """, conn)


towns_info_df = pd.DataFrame(towns_info, columns=['population'])
towns_ties_df = pd.DataFrame(towns_ties, columns=['population'])
towns_top_10_df = pd.DataFrame(towns_top_ten, columns=['rank', 'town_name', 'population'])
towns_above_100_000_df = pd.DataFrame(towns_above_100_000, columns=['population'])
towns_above_10_000_df = pd.DataFrame(towns_above_10_000, columns=['population'])
towns_above_1000_df = pd.DataFrame(towns_above_1000, columns=['population'])
towns_below_1000_df = pd.DataFrame(towns_below_1000, columns=['population'])
towns_below_100_df = pd.DataFrame(towns_below_100, columns=['population'])


# All towns compared to tied towns
# Bar Chart
'''
plt.figure(figsize=(8, 4))

titles = ['All Towns', 'Tied Towns']
values = [len(towns_info_df), len(towns_ties_df)]
colors = ['#00bf83', '#ee00ff']
for title, value, color in zip(titles, values, colors):
    plt.bar(title, value, color=color, label=value, zorder=2)

plt.grid(axis='y', color='black', linestyle='--', linewidth=0.5, zorder=1)
plt.xlabel('Towns in Kansas', fontdict={'fontname': 'Arial', 'fontsize': 12})
plt.ylabel('Number of Towns', fontdict={'fontname': 'Arial', 'fontsize': 12})

plt.title('Comparison of Population Among Towns in Kansas', pad=15, fontdict={
    'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 12})

plt.legend()
plt.show()'''

# Pie Chart
'''values = [len(towns_info_df) - len(towns_ties_df), len(towns_ties_df)]
titles = [f'Towns with Unique\nPopulations\n({values[0]})', f'Towns with Tied\nPopulations\n({values[1]})']

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=titles, shadow=False, autopct='%1.01f%%', startangle=90)
ax1.axis('equal')

plt.title('Towns in Kansas by Population', fontdict={'fontname':'Arial', 'fontweight':'bold', 'fontsize':12})
plt.show()'''

# All towns compared to towns with fewer than 1000, 100 people
# Bar chart
'''
plt.figure(figsize=(8, 4))

titles = ['All Towns', 'Below 1000 People', 'Below 100 People']
values = [len(towns_info_df), len(towns_below_1000_df), len(towns_below_100_df)]
colors = ['#00bf83', '#ee00ff', '#10009e']
for title, value, color in zip(titles, values, colors):
    plt.bar(title, value, color=color, label=value, zorder=2)

plt.grid(axis='y', color='black', linestyle='--', linewidth=0.5, zorder=1)
plt.xlabel('Size of Towns', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.ylabel('Number of Towns', fontdict={'fontname': 'Arial', 'fontsize': 14})

plt.title('Towns in Kansas by Population', fontdict={'fontname':'Arial', 'fontweight':'bold', 'fontsize':14})
plt.legend()
plt.show()'''

# Pie Chart
'''values = [len(towns_info_df) - len(towns_below_1000_df), len(towns_below_1000_df) - len(towns_below_100_df), len(towns_below_100_df)]
titles = [f'Towns with Greater\nThan 1000 People ({values[0]})', f'Between 1000 and 100 People ({values[1]})', f'Fewer Than 100 People ({values[2]})']

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=titles, shadow=False, autopct='%1.01f%%', startangle=90)
ax1.axis('equal')

plt.title('Towns in Kansas by Population', fontdict={'fontname':'Arial', 'fontweight':'bold', 'fontsize':14}, pad=15)
plt.show()'''

# Name and population of top 10 towns in Kansas
# Bar Chart
'''
plt.figure(figsize=(8, 4))

for ind in towns_top_10_df.index:
    labels = [towns_top_10_df['town_name'][ind]]
    values = [towns_top_10_df['population'][ind]]
    colors = ['#fc0303', '#00bf83', '#bd0000', '#8900c4', '#00cf41', '#10009e', '#ee00ff', '#4d0752', '#00328f', '#05ecfc']
    plt.bar(labels, values, color=colors[ind], label=towns_top_10_df['population'][ind], zorder=2)

plt.grid(axis='y', color='black', linestyle='--', linewidth=0.5, zorder=1)
plt.xlabel('Towns', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.ylabel('Population', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.xticks(rotation=35, fontsize=8)

plt.title('Top 10 Towns in Kansas by Population', fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})
plt.legend()
plt.show()'''

# Compare Population of Kansas to Population of top 10 towns, towns over 100,000
# Bar Chart
'''
plt.figure(figsize=(8, 4))

titles = ['All Towns', 'Top 10', 'Over 100,000']
values = [towns_info_df['population'].sum(), towns_top_10_df['population'].sum(), towns_above_100_000_df['population'].sum()]
colors = ['#00bf83', '#00cf41', '#4d0752']
for title, value, color in zip(titles, values, colors):
    plt.bar(title, value, color=color, label=value, zorder=2)

plt.grid(axis='y', color='black', linestyle='--', linewidth=0.5, zorder=1)
plt.xlabel('Size of Towns (By Population)', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.ylabel('Population', fontdict={'fontname': 'Arial', 'fontsize': 14})

plt.title('Kansas Towns by Population', fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})
plt.legend()
plt.show()'''

# Pie Chart for Population of Top 10
'''values = [towns_top_10_df['population'].sum(), towns_info_df['population'].sum() - towns_top_10_df['population'].sum()]
titles = [f'Towns in the\nTop 10 by\nPopulation\n({values[0]})', f'Other Towns\n({values[1]})']

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=titles, shadow=False, autopct='%1.01f%%', startangle=90)
ax1.axis('equal')

plt.title('Distribution of Population Among Towns in Kansas', fontdict={'fontname':'Arial', 'fontweight':'bold', 'fontsize':14})
plt.show()'''

# Pie Chart for Population of Towns Above 100,000
'''values = [towns_above_100_000_df['population'].sum(), towns_info_df['population'].sum() - towns_above_100_000_df['population'].sum()]
titles = [f'Towns with more\nthan 100,000 people\n({values[0]})', f'Other Towns\n({values[1]})',]

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=titles, shadow=False, autopct='%1.01f%%', startangle=90)
ax1.axis('equal')

plt.title('Distribution of Population Among Towns in Kansas', fontdict={'fontname':'Arial', 'fontweight':'bold', 'fontsize':14})
plt.show()'''

# Compare Population of Kansas to Population of towns below 1000, below 100
# Bar Chart
'''
plt.figure(figsize=(8, 4))

titles = ['All Towns', 'Below 1,000', 'Below 100']
values = [towns_info_df['population'].sum(), towns_below_1000_df['population'].sum(),
        towns_below_100_df['population'].sum()]
colors = ['#00bf83', '#00cf41', '#4d0752']
for title, value, color in zip(titles, values, colors):
    plt.bar(title, value, color=color, label=value, zorder=2)

plt.grid(axis='y', color='black', linestyle='--', linewidth=0.5, zorder=1)
plt.xlabel('Size of Towns (By Population)', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.ylabel('Population (Millions)', fontdict={'fontname': 'Arial', 'fontsize': 14})

plt.title('Kansas Towns by Population', fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})
plt.legend()
plt.show()'''

# Pie Chart
'''values = [towns_below_1000_df['population'].sum(), towns_below_100_df['population'].sum(), towns_info_df['population'].sum() - towns_below_1000_df['population'].sum() - towns_below_100_df['population'].sum()]
titles = [f'Towns with populations\nbelow 1000 ({values[0]})', f'Towns with populations\nbelow 100 ({values[1]})', f'Other towns\n({values[2]})']

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=None, shadow=False, autopct='%1.01f%%', pctdistance=1.1, labeldistance=0, startangle=90)
ax1.axis('equal')

plt.title('Distribution of Population Among Towns in Kansas', pad=15, fontdict={
        'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 12})

plt.legend(loc=3, labels=titles)
plt.show()'''


print('Total number of towns in Kansas:', len(towns_info_df))
print('Number of towns in Kansas with a tied population:', len(towns_ties_df))
print('Number of towns in Kansas with over 100,000 people:', len(towns_above_100_000_df))
print('Number of towns in Kansas with over 10,000 people:', len(towns_above_10_000_df))
print('Number of towns in Kansas with over 1,000 people:', len(towns_above_1000_df))
print('Number of towns in Kansas with under 1,000 people:', len(towns_below_1000_df))
print('Number of towns in Kansas with under 100 people:', len(towns_below_100_df))

print('Top ten towns:')
print('Rank|Name|Population')
for ind in towns_top_10_df.index:
    print(towns_top_10_df['rank'][ind], towns_top_10_df['town_name'][ind], towns_top_10_df['population'][ind])

print('Number of people who live in Kansas:', towns_info_df['population'].sum())
print('Number of people who live in the top 10 towns in Kansas:', towns_top_10_df['population'].sum())
print('Number of people who live in towns with greater than 100,000 people in Kansas:', towns_above_100_000_df['population'].sum())
print('Number of people who live in towns with greater than 10,000 people in Kansas:', towns_above_10_000_df['population'].sum())
print('Number of people who live in towns with greater than 1,000 people in Kansas:', towns_above_1000_df['population'].sum())
print('Number of people who live in towns with fewer than 1,000 people in Kansas:', towns_below_1000_df['population'].sum())
print('Number of people who live in towns with fewer than 100 people in Kansas:', towns_below_100_df['population'].sum())


