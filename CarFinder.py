﻿import requests
from sys import exit
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 
from statistics import fmean

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

def average_car_price(price_string_list):
    """Function for calculating the average car price"""
    price_float_list = []
    for price in price_string_list:
        if price != 'Not Priced':
            price_only_numbers = float(price.replace('$', '').replace(',', ''))
            price_float_list.append(price_only_numbers)

    if price_float_list:
        return fmean(price_float_list)
    else:
        return None
    
cars_info = []
filtered_price = []
page_number = 1
min_year = 0
max_year = 9999
min_mileage = 0
max_mileage = 999999

car_model = input('Please type the name of the car model that you want to search for: ')

specify_data = input('Do you want to specify year of production and mileage? ("yes" or "no"): ')

try:
    if specify_data.lower() == "yes":
        min_year = int(input('Please enter the minimum year: '))
        max_year = int(input('Please enter the maximum year: '))
        min_mileage = int(input('Please enter the minimum mileage: '))
        max_mileage = int(input('Please enter the maximum mileage: '))
except ValueError:
    print('The provided value was incorrect')
    exit()

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
        mileage_value = int(mileage[i+1].replace(' mi.', '').replace(',', ''))

        if mileage_value >= min_mileage and mileage_value <= max_mileage \
        and int(year) >= min_year and int(year) <= max_year:
            car_info = {'Name': name, 'Year': year, 'Mileage': mileage[i+1],
                    'Stock': stock[i], 'Price': price[i]}
            cars_info.append(car_info)
            filtered_price.append(price[i])

    page_number += 1 

    sleep(randint(2,5))

print('\n', cars_info)

average_price = average_car_price(filtered_price)
if average_price is not None:
    print(f'The average car price is: {average_price}$')
else:
    print('No cars met the specified criteria. Make sure that the data you provided is correct')
