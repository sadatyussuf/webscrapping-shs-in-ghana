from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Providing the url where the data is to be retrieved
url = 'https://yellgh.com/full-list-of-shs-in-ghana-all-secondary-schools-2021/'

# fetching th data from the given url
get_url = requests.get(url)

# using Beautifulsoup to parse the contents(html) of the page
soup = bs(get_url.content, 'html.parser')

# Find all the h2 tag with text('List of the Regions in Ghana') in them
regions =[region.text[15:-7] for region in soup.find_all('h2') if 'List' in region.text]

# creating an empty list where the row will be inserted
table_list = []

# find all the table tags
tables = soup.find_all('table')

for i,table in enumerate(tables):

    # Find and list all the text in the th(table head) tag
    table_head = [x.text for x in table.find_all('th')]

    # Find all tablebody(tbody) tag
    table_body = table.find('tbody')

    # Loop through all the rows in the tbody tag
    for tr in table_body:

        # Find all the td(table data) tag in the tr(table row)
        t_data = tr.find_all('td')

        # Find and list all the text in the td tag except empty cells
        table_row = [cell.text for cell in t_data if cell.text != '']

        # Add the appropriate regions to the row of data
        table_row.append(regions[i])

        # check for empty rows
        if table_row:
            table_list.append(table_row)

# Added Region to the list of headers
table_head.append('Region')

# make a data_frame/table with the items in the table_list as the rows and table_head as the column headers
df = pd.DataFrame(table_list,columns=table_head)

# create a csv file with the dataframe/table
df.to_csv('shs_in_ghana.csv', encoding='utf-8',index=False)
