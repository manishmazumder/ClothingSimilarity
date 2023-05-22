# ClothingSimilarity
The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites.

We have created two separate files:
- ScrapeData.py: This code is to create dataset for our machine learning model. It scrapes product details from different websites and store it as a JSON object.
- ClothingSImilarity.py: This code is to find similarity between input text and all the product details from different websites. It will display list of 10 most similar items along with title, links to buy, prices and ratings.

To run this code locally:
1. Just run ClothingSimilarity.py. For convenience I have also uploaded the data.json file which served as the main dataset for our model.

Additionally we have created a Dockerfile which contains instructions to create a docker image.
