import requests
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 

def get_information(informations):
        """Function for extracting information from html page"""
        info_list = []
        for information in informations:
            info = information.get_text(strip=True) 
            info_list.append(info)

        return info_list

def extract_year_and_name(title):
    """Function to extract year and name from title"""
    parts = title.split(' ', 1)
    year = parts[0]
    name = parts[1]
    return year, name
    
cars_info = []
page_number = 1

car_model = input('Please type the name of the car model that you want to search for: ')
print('The results will be ready in a few seconds. Please wait...')

while page_number < 5:

    url = f"https://www.cars.com/shopping/all/{car_model}/?page={page_number}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title_elements = soup.find_all("h2", class_="title")
    mileage_elements = soup.find_all("div", class_="mileage")
    stock_elements = soup.find_all("p", class_="stock-type")
    price_elements = soup.find_all("span", class_="primary-price")

    title = get_information(title_elements)
    mileage = get_information(mileage_elements)
    stock = get_information(stock_elements)
    price = get_information(price_elements)

    for i in range(len(mileage_elements)-1):
        year, name = extract_year_and_name(title[i])
        car_info = {'Name': name, 'Year': year, 'Mileage': mileage[i+1],
                'Stock': stock[i], 'Price': price[i]}
        cars_info.append(car_info)

    page_number += 1 

    sleep(randint(2,5))

print('\n', cars_info)