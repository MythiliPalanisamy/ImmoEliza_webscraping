# ImmoEliza Webscraping
## Table of contents
1. [Introduction](#introduction) 📌
2. [Installation](#installation) 🔧  
3. [Pipeline](#pipeline) 🚀
4. [Completion](#completion) 🏁

<a name="introduction"></a>
## 📌 Introduction

A fictional real estate company "ImmoEliza" wants to create a Machine Learning model to make price predictions on real estate sales in Belgium. Herein, a dataset would need to be created to gather information about at least 10.000 properties all over Belgium. This dataset will later be used as a training set for the prediction model.

<a name="installation"></a>
## 🔧 Installation

[![python](https://img.shields.io/badge/python-3.12.0-green)](https://www.python.org/downloads/)
[![pandas](https://img.shields.io/badge/pandas-1.3.5-yellow)](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/install.html)
[![beautifulsoup](https://img.shields.io/badge/Beautifulsoup-4.12.2-orange)](https://pypi.org/project/beautifulsoup4/)
[![requests](https://img.shields.io/badge/requests-2.31.0-red)](https://pypi.org/project/requests/)
[![lxml](https://img.shields.io/badge/lxml-4.3.9-blue)](https://pypi.org/project/lxml/)
[![regex](https://img.shields.io/badge/regex-indigo)](https://pypi.org/project/regex/)
[![threadpool_executor](https://img.shields.io/badge/threadpool_executor-0.2.2-purple)](https://pypi.org/project/ThreadPoolExecutorPlus/)

* Clone the repository
* Install the requirements with `pip install <module>`
* Run `scrape_url` from `src` to get the list of url
* Run `data_scrape`from `src` to get the data from url list 

<a name="pipeline"></a>
## 🚀 Pipeline

We focused on scraping the data from "Immoweb", a highly utilised real estate platform in Belgium to list new available property.

### Requirements:  

-> Contains a minimum of 10,000 inputs

-> Contains data for all of Belgium

-> Used threading to speed up the collection

### step 1 :  
Scraped the urls of all the properties using `scrape_url_list.py`

### step 2 :  
Using `data_scrape.py` we gathered and stored the following data in a csv file:

* Price
* Address
* Building Condition
* Construction Year
* Bedrooms
* Terrace (surface)
* Shower rooms
* Office
* Toilets
* Energy Class
* Type of Kitchen
* Furnished
* Parking Space
* Garden Area

<a name="completion"></a>
## 🏁 Completion

- Project type  :  Group
- Duration  :  5 days
- Team Members :   
                - Fré Van Oers [LinkedIn](https://www.linkedin.com/in/frevanoers/) [Github](https://github.com/DeFre),  
                - Jonathan_Rab [LinkedIn](https://www.linkedin.com/in/jonathan-rabbi/) [Github](https://github.com/JonathanRabbi),  
                - Mythili [LinkedIn](https://www.linkedin.com/in/mythili-aug/) [Github](https://github.com/MythiliPalanisamy)
              
                            
