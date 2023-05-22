# The purpose of this code is to scrape data from different websites
# and create a dataset for our machine learning model

import os
import json
from bs4 import BeautifulSoup

# List of HTML files to read
# This list contains separate html files of different product pages
html_files = ['amazon_men1.html', 'amazon_men2.html', 'amazon_men3.html', 'amazon_men4.html',
             'amazon_women1.html', 'amazon_women2.html', 'amazon_women3.html', 'amazon_women4.html']

data = []

# Loop through each HTML file
for html_file in html_files:
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all divs with the specified class
    divs = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

    # Extract the desired information from each div
    for div in divs:
        # extract titles
        title_span = div.find('span', class_='a-size-base-plus a-color-base a-text-normal')
        title = title_span.text.strip() if title_span else ''

        # extract links
        link_span = div.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        link = link_span.get('href') if link_span else ''

        # extract ratings
        rating_span = div.find('span', class_='a-icon-alt')
        rating = rating_span.text.strip() if rating_span else ''

        # extract price
        price_span = div.find('span', class_='a-price-whole')
        price = price_span.text.strip() if price_span else ''

        data.append({
            'title': title,
            'link': link,
            'rating': rating,
            'price': price
        })

# Write the extracted data to data.json
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

