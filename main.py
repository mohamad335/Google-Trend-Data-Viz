import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
#first we start with tesla
print(df_tesla.head())#the shape of the content in data
print(df_tesla.shape)
#pick the name of columns
print(df_tesla.columns)
#the larget and smallest value of the data
print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')
print(df_tesla.describe())#the discription of the data
#now we start with unploymemnt
print(df_unemployment.head())#the shape of the content in data
print(df_unemployment.shape)
#pick the name of columns
print(df_unemployment.columns)
#the largest value of df_unemployment
print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search:{df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')
#bitcoin search
print(df_btc_search.head())#the shape of the content in data
print(df_btc_search.shape)
#pick the name of columns
print(df_btc_search.columns)
#the largest value of df_btc_search
print('Largest value for "Bitcoin" '
      f'in Web Search:{df_btc_search.BTC_NEWS_SEARCH.max()}')
# we to check if there is any missing value in the data
print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
#it look like there is missing value on btc price
print(f'Missing values for BTC Price?: {df_btc_price.isna().values.any()}')
#so i need to check how many missing value in the data
print(f'Number of missing values: {df_btc_price.isna().values.sum()}')
#now we need to remove the missing value
df_btc_price.dropna(inplace=True)
#convert the all data type of date to datetime
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE) 
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
#change the btc price from daily date to monthly date
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
print(df_btc_monthly.head())



