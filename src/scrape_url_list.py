"""This file contains all functions related to the gathering of urls for sitescraping"""

from bs4 import BeautifulSoup
from lxml import etree
import requests
from random import randint
import time
from time import sleep

base_url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&orderBy=newest&page=" #starting point for all housing properties of Belgium, sorted starting from newest
page_url = base_url #will get a page NUMBER attached later, but this way page_url can be called already, immoweb does not mind the missing page number


def get_model(page_url): 
    """Turn the url into a nice soup and use etree to get a model which xpath understands"""
    print(page_url)
    html_text= requests.get(page_url).text 
    #print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser') 
    site_model = etree.HTML(str(soup))
    return site_model


def get_property_list(site_model):
    """extract the urls of all search results from the page"""
    properties_per_page = site_model.xpath('//main/div//a[@class="card__title-link"]/@href') #creates a list of all search results (and excludes "similar properties" and "sponsored properties" )
    return properties_per_page

def page_list_to_full_list(full_list, properties_per_page):
    """adds urls to the full list of urls"""
    #print(full_list)
    #print(type(unique_properties_per_page))
    full_list.extend(properties_per_page)
    #print(full_list)
    print("list length: ",len(full_list))
    return full_list

def add_to_file(properties_per_page):
    with open('10k_belgium_url_list.txt', 'a') as output_file:
        for line in properties_per_page:
            output_file.write(f"{line}\n")

def run_through_pages():
    """Scrapes property urls from search results page after page"""
    full_list = []
    for i in range (113,335):
        sleep(randint(1,3))
        page_url = base_url + str(i)
        site_model = get_model(page_url)
        properties_per_page = get_property_list(site_model)
        #print(full_list)
        full_list = page_list_to_full_list(full_list, properties_per_page)
        add_to_file(properties_per_page)
        print(i)
    return full_list


start = time.time()
final_list = run_through_pages()
end = time.time()
print("Time Taken: {:.6f}s".format(end-start))
