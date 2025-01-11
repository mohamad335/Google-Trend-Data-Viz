import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#set the date format and locators
year = mdates.YearLocator()
month = mdates.MonthLocator()
year_format = mdates.DateFormatter('%Y')
df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')
df_btc_price.dropna(inplace=True)
#convert the all data type of date to datetime
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE) 
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
#change the btc price from daily date to monthly date
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
#Plot the Tesla stock price against the Tesla search volume 
plt.figure(figsize=(12,6), dpi=105)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
ax1.set_xlabel('Year')
ax1.set_ylabel('TSLA Stock Price', fontdict=font1)
ax2.set_ylabel('Search Trend', fontdict=font2)
ax1.set_ylim([0, 600]) # set y-axis limit
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()]) # set x-axis limit
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='skyblue')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='red')
#set the x-axis major locator and major formatter
ax1.xaxis.set_major_locator(year)
ax1.xaxis.set_minor_locator(month)
ax1.xaxis.set_major_formatter(year_format)
plt.title('Tesla Web Search vs Price', fontdict=font1)
plt.savefig('images/Tesla Web Search vs Price.png')
plt.show()


