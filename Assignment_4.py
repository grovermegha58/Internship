#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install requests beautifulsoup4')
get_ipython().system('pip install selenium beautifulsoup4')



# In[8]:


#ANS:1)
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table that contains the data
table = soup.find('table', {'class': 'wikitable'})

# Initialize lists to store data
rank_list = []
name_list = []
artist_list = []
upload_date_list = []
views_list = []

# Iterate through each row in the table
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    rank = columns[0].text.strip()
    name = columns[1].text.strip()
    artist = columns[2].text.strip()
    upload_date = columns[3].text.strip()
    views = columns[4].text.strip()

    # Append data to the lists
    rank_list.append(rank)
    name_list.append(name)
    artist_list.append(artist)
    upload_date_list.append(upload_date)
    views_list.append(views)

# Print the scraped data
for i in range(len(rank_list)):
    print(f"A) Rank: {rank_list[i]}")
    print(f"B) Name: {name_list[i]}")
    print(f"C) Artist: {artist_list[i]}")
    print(f"D) Upload date: {upload_date_list[i]}")
    print(f"E) Views: {views_list[i]}")
    print("------------------------")


# In[9]:


#ANS:2)
import requests
from bs4 import BeautifulSoup

url = "https://www.bcci.tv/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the international fixtures page
fixtures_link = soup.find('a', {'href': '/international/fixtures'})
fixtures_url = f"https://www.bcci.tv{fixtures_link['href']}"

# Send a GET request to the international fixtures URL
fixtures_response = requests.get(fixtures_url)

# Parse the HTML content of the fixtures page
fixtures_soup = BeautifulSoup(fixtures_response.text, 'html.parser')

# Initialize lists to store data
series_list = []
place_list = []
date_list = []
time_list = []

# Find the relevant elements in the fixtures page
fixture_elements = fixtures_soup.find_all('li', {'class': 'event-list-item'})

# Iterate through each fixture element
for fixture in fixture_elements:
    series = fixture.find('h2').text.strip()
    place = fixture.find('p', {'class': 'fixture__additional-info'}).text.strip()
    date = fixture.find('div', {'class': 'fixture__date'}).text.strip()
    time = fixture.find('span', {'class': 'fixture__time'}).text.strip()

    # Append data to the lists
    series_list.append(series)
    place_list.append(place)
    date_list.append(date)
    time_list.append(time)

# Print the scraped data
for i in range(len(series_list)):
    print(f"A) Series: {series_list[i]}")
    print(f"B) Place: {place_list[i]}")
    print(f"C) Date: {date_list[i]}")
    print(f"D) Time: {time_list[i]}")
    print("------------------------")


# In[10]:


#ANS:3)
import requests
from bs4 import BeautifulSoup

url = "http://statisticstimes.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the economy page
economy_link = soup.find('a', {'href': '/economy'})
economy_url = f"http://statisticstimes.com{economy_link['href']}"

# Send a GET request to the economy URL
economy_response = requests.get(economy_url)

# Parse the HTML content of the economy page
economy_soup = BeautifulSoup(economy_response.text, 'html.parser')

# Find the link to the State-wise GDP page
state_gdp_link = economy_soup.find('a', {'href': '/economy/gdp-of-indian-states'})
state_gdp_url = f"http://statisticstimes.com{state_gdp_link['href']}"

# Send a GET request to the State-wise GDP URL
state_gdp_response = requests.get(state_gdp_url)

# Parse the HTML content of the State-wise GDP page
state_gdp_soup = BeautifulSoup(state_gdp_response.text, 'html.parser')

# Initialize lists to store data
rank_list = []
state_list = []
gsdp_1819_list = []
gsdp_1920_list = []
share_1819_list = []
gdp_billion_list = []

# Find the relevant elements in the State-wise GDP page
table_rows = state_gdp_soup.find('table', {'id': 'table_id'}).find('tbody').find_all('tr')

# Iterate through each table row
for row in table_rows:
    columns = row.find_all('td')
    rank = columns[0].text.strip()
    state = columns[1].text.strip()
    gsdp_1819 = columns[2].text.strip()
    gsdp_1920 = columns[3].text.strip()
    share_1819 = columns[4].text.strip()
    gdp_billion = columns[5].text.strip()

    # Append data to the lists
    rank_list.append(rank)
    state_list.append(state)
    gsdp_1819_list.append(gsdp_1819)
    gsdp_1920_list.append(gsdp_1920)
    share_1819_list.append(share_1819)
    gdp_billion_list.append(gdp_billion)

# Print the scraped data
for i in range(len(rank_list)):
    print(f"A) Rank: {rank_list[i]}")
    print(f"B) State: {state_list[i]}")
    print(f"C) GSDP(18-19): {gsdp_1819_list[i]}")
    print(f"D) GSDP(19-20): {gsdp_1920_list[i]}")
    print(f"E) Share(18-19): {share_1819_list[i]}")
    print(f"F) GDP($ billion): {gdp_billion_list[i]}")
    print("------------------------")


# In[12]:


#ANS:5)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up the Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

# Provide the path to your ChromeDriver executable
chrome_path = '/path/to/chromedriver'

# Set up the Chrome service
chrome_service = ChromeService(chrome_path)

# Start the Chrome browser
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the Billboard homepage
driver.get("https://www.billboard.com/")

# Click on the "Charts" option
charts_option = driver.find_element(By.XPATH, '//li[contains(text(), "Charts")]')
charts_option.click()

# Click on the "Hot 100" page link
hot_100_link = driver.find_element(By.XPATH, '//a[contains(text(), "Hot 100")]')
hot_100_link.click()

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chart-list-item')))

# Get the HTML content of the page
html_content = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize lists to store data
song_names = []
artist_names = []
last_week_ranks = []
peak_ranks = []
weeks_on_board = []

# Find the relevant elements on the Hot 100 page
chart_items = soup.find_all('div', class_='chart-list-item')

# Iterate through each chart item
for item in chart_items:
    song_name = item.find('span', class_='chart-list-item__title-text').text.strip()
    artist_name = item.find('div', class_='chart-list-item__artist').text.strip()
    last_week_rank = item.find('div', class_='chart-list-item__last-week').text.strip()
    peak_rank = item.find('div', class_='chart-list-item__weeks-at-one').text.strip()
    weeks_on_board = item.find('div', class_='chart-list-item__weeks-on-chart').text.strip()

    # Append data to the lists
    song_names.append(song_name)
    artist_names.append(artist_name)
    last_week_ranks.append(last_week_rank)
    peak_ranks.append(peak_rank)
    weeks_on_board.append(weeks_on_board)

# Print the scraped data
for i in range(len(song_names)):
    print(f"A) Song name: {song_names[i]}")
    print(f"B) Artist name: {artist_names[i]}")
    print(f"C) Last week rank: {last_week_ranks[i]}")
    print(f"D) Peak rank: {peak_ranks[i]}")
    print(f"E) Weeks on board: {weeks_on_board[i]}")
    print("------------------------")

# Close the browser
driver.quit()



# In[13]:


#ANS:6)
import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize lists to store data
book_names = []
author_names = []
volumes_sold = []
publishers = []
genres = []

# Find the table that contains the data
table = soup.find('table', {'class': 'in-article sortable'})

# Iterate through each row in the table
for row in table.find('tbody').find_all('tr'):
    columns = row.find_all('td')
    book_name = columns[1].text.strip()
    author_name = columns[2].text.strip()
    volumes = columns[3].text.strip()
    publisher = columns[4].text.strip()
    genre = columns[5].text.strip()

    # Append data to the lists
    book_names.append(book_name)
    author_names.append(author_name)
    volumes_sold.append(volumes)
    publishers.append(publisher)
    genres.append(genre)

# Print the scraped data
for i in range(len(book_names)):
    print(f"A) Book name: {book_names[i]}")
    print(f"B) Author name: {author_names[i]}")
    print(f"C) Volumes sold: {volumes_sold[i]}")
    print(f"D) Publisher: {publishers[i]}")
    print(f"E) Genre: {genres[i]}")
    print("------------------------")


# In[14]:


#ANS:7)
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls095964455/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize lists to store data
names = []
year_spans = []
genres = []
runtimes = []
ratings = []
votes = []

# Find the relevant elements on the IMDb page
series_items = soup.find_all('div', class_='lister-item-content')

# Iterate through each TV series item
for series_item in series_items:
    name = series_item.find('h3', class_='lister-item-header').find('a').text.strip()
    year_span = series_item.find('span', class_='lister-item-year').text.strip()
    genre = series_item.find('span', class_='genre').text.strip()
    runtime = series_item.find('span', class_='runtime').text.strip()
    rating = series_item.find('span', class_='ipl-rating-star__rating').text.strip()
    votes_count = series_item.find('span', attrs={'name': 'nv'}).text.strip()

    # Append data to the lists
    names.append(name)
    year_spans.append(year_span)
    genres.append(genre)
    runtimes.append(runtime)
    ratings.append(rating)
    votes.append(votes_count)

# Print the scraped data
for i in range(len(names)):
    print(f"A) Name: {names[i]}")
    print(f"B) Year span: {year_spans[i]}")
    print(f"C) Genre: {genres[i]}")
    print(f"D) Run time: {runtimes[i]}")
    print(f"E) Ratings: {ratings[i]}")
    print(f"F) Votes: {votes[i]}")
    print("------------------------")


# In[16]:


#ANS:8)
import requests
from bs4 import BeautifulSoup

# URL for the UCI Machine Learning Repository home page
url = "https://archive.ics.uci.edu/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the "Show All Dataset" page
show_all_link = soup.find('a', {'href': '/ml/datasets.php'})
show_all_url = f"https://archive.ics.uci.edu{show_all_link['href']}"

# Send a GET request to the "Show All Dataset" page
show_all_response = requests.get(show_all_url)

# Parse the HTML content of the "Show All Dataset" page
show_all_soup = BeautifulSoup(show_all_response.text, 'html.parser')

# Initialize lists to store data
dataset_names = []
data_types = []
tasks = []
attribute_types = []
no_of_instances = []
no_of_attributes = []
years = []

# Find the relevant elements on the "Show All Dataset" page
dataset_rows = show_all_soup.find_all('tr', {'valign': 'top'})

# Iterate through each dataset row
for dataset_row in dataset_rows:
    columns = dataset_row.find_all('td', {'valign': 'top'})
    
    # Extract data from columns
    dataset_name = columns[0].text.strip()
    data_type = columns[1].text.strip()
    task = columns[2].text.strip()
    attribute_type = columns[3].text.strip()
    no_of_instances_val = columns[4].text.strip()
    no_of_attributes_val = columns[5].text.strip()
    year = columns[6].text.strip()

    # Append data to the lists
    dataset_names.append(dataset_name)
    data_types.append(data_type)
    tasks.append(task)
    attribute_types.append(attribute_type)
    no_of_instances.append(no_of_instances_val)
    no_of_attributes.append(no_of_attributes_val)
    years.append(year)

# Print the scraped data
for i in range(len(dataset_names)):
    print(f"A) Dataset name: {dataset_names[i]}")
    print(f"B) Data type: {data_types[i]}")
    print(f"C) Task: {tasks[i]}")
    print(f"D) Attribute type: {attribute_types[i]}")
    print(f"E) No of instances: {no_of_instances[i]}")
    print(f"F) No of attributes: {no_of_attributes[i]}")
    print(f"G) Year: {years[i]}")
    print("------------------------")


# In[ ]:




