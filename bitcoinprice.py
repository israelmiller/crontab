#import packages
import requests
import pandas as pd


#set up the url for the api call
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
#make the request
price = requests.get(url)

#convert the response to a dictionary
price_dict = price.json()
price_dict.keys()

#extract the prices and time from the dictionary
price_extracted = price_dict['bpi'] #extract the prices
time_extracted = price_dict['time'] #extract the time
time_extracted['updated'] #extract the time

#convert the list of posts to a dataframe and  set the filename.
price_df = pd.DataFrame(price_extracted)
time_extracted_string = str(time_extracted['updated'])

filename = str('bitcoin_price(' + (time_extracted_string) + ').csv')


#save the dataframe to a csv file
price_df.to_csv(filename, index=False)

