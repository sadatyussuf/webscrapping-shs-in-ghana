from wsgiref import headers

from bs4 import BeautifulSoup as bs
import requests

# Providing the url where the data is to be retrieved
url = 'https://yellgh.com/full-list-of-shs-in-ghana-all-secondary-schools-2021/'

# fetching th data from the given url
get_url = requests.get(url)
# print(get_url.status_code)

soup = bs(get_url.content,'html.parser')


dict = {}

table = soup.find('table')

table_head = [x.text for x in table.find_all('th')]

table_body = table.find('tbody')

# table_head = table.find_all('th')
table_list = []
for tr in table_body:
    # print('--------------------------------')
    t_data = tr.find_all('td')

    table_row = [cell.text for cell in t_data]
    # print(row_text)
    # print('--------------------------------')
    if table_row:
        table_list.append(table_row)
# dict['key']='value'
print(table_head)
print(table_list)

# tables = soup.find_all('table')
# print(len(tables))
# dict = {}
# for table in tables:
#     for content in table.children:
#         for td in content:
#             print(td)
