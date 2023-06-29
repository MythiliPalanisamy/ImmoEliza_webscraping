from bs4 import BeautifulSoup
import requests


def home_details(url):
    html_text=requests.get(url).text

    soup = BeautifulSoup(html_text, 'html.parser')
    #Body_overview= soup.find_all('tbody',class_='classified-table__body')


    '''create an empty list and assign the above html content to the list.
            the second index of the html content conveys the interior section
            '''
    house = []
    house = soup.find_all('tbody',class_='classified-table__body')
    interior_house = house[1].find_all('tr')
    facilities_house = house[3].find_all('tr')


    ''' Dictionary created in order to store the table headers (th) and their values (td)
    A list is then creatted for each key and value to store the corresponding th and td
    a for loop is then created to iterate over the multiple keys and values corresponding to the interior, whilst removing the trailing white spaces (strip)
    '''

    interior={}
    interior_key=[]
    interior_value=[]

    for elem in interior_house:
        for th in elem.find_all('th'):
            interior_key.append(th.contents[0].strip())
            
        for td in elem.find_all('td'):
            interior_value.append(td.contents[0].strip())


    facilities={}
    facilities_key=[]
    facilities_value=[]

    for elem in facilities_house:
        for th in elem.find_all('th'):
            facilities_key.append(th.contents[0].strip())
            
        for td in elem.find_all('td'): 
            facilities_value.append(td.contents[0].strip())


        ''' Looking at the 'td' tag, we see that there are 2 span tags within the list, conveying the same info. Hence, we only want the first value of the list.
    We look for all the spans and command that we print the first value'''

    '''financials={}
    financials_key=[]
    financials_value=[]

    for elem in financial_house:
        for th in elem.find_all('th'):
            financials_key.append(th.contents[0].strip())
            
        for td in elem.find_all('td'):
            if len(td.find_all('span'))>0:
                financials_value.append(td.find_all('span')[0].contents[0].strip())

        We only want to convey the price of the property. Therefore, once we have elements for the first key/value, add them to the dictionary  

        if financials_key and financials_value:
                    financials[financials_key[0]] = financials_value[0]    
        break'''
    return interior, facilities