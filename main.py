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
df_unemployment_2004_20= pd.read_csv('data/UE Benefits Search vs UE Rate 2004-20.csv')
df_btc_price.dropna(inplace=True)
#convert the all data type of date to datetime
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE) 
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_unemployment_2004_20.MONTH = pd.to_datetime(df_unemployment_2004_20.MONTH)
#change the btc price from daily date to monthly date
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
#Plot the Tesla stock price against the Tesla search volume 
def plot_tesla_price():
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
def plot_bitcoin_price():
    plt.figure(figsize=(12, 6), dpi=105)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    ax1 = plt.gca() # get current axis
    ax2 = ax1.twinx()
    ax1.set_xlabel('Year')
    ax1.set_ylabel('BTC Price', fontdict=font1)
    ax2.set_ylabel('Search Trend', fontdict=font2)
    ax1.set_ylim([0, 15000]) # set y-axis limit
    ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()]) # set x-axis limit
    ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color='skyblue',linestyle='--')
    ax2.plot(df_btc_search.MONTH, df_btc_search.BTC_NEWS_SEARCH, color='red',linestyle='-',marker='o',markersize=5)
    #set the x-axis major locator and major formatter
    ax1.xaxis.set_major_locator(year)
    ax1.xaxis.set_minor_locator(month)
    ax1.xaxis.set_major_formatter(year_format)
    plt.title('Bitcoin News Search vs Price', fontdict=font1)
    plt.savefig('images/Update Bitcoin News Search vs Price.png')
    plt.show()
#Plot the Unemployment Rate against the Search Trend for "Unemployment Benefits"
def plot_unemployment():
    roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
    plt.figure(figsize=(12, 6), dpi=105)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    ax1 = plt.gca() # get current axis
    ax2 = ax1.twinx()
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Unemployment Rate', fontdict=font1)
    ax2.set_ylabel('Search Trend', fontdict=font2)
    ax1.set_ylim([0, 11]) # set y-axis limit
    ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()]) # set x-axis limit
    ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color='skyblue',linestyle='--')
    ax2.plot(df_unemployment.MONTH, df_unemployment['UE_BENEFITS_WEB_SEARCH'], color='red')
    #set the x-axis major locator and major formatter
    ax1.xaxis.set_major_locator(year)
    ax1.xaxis.set_minor_locator(month)
    ax1.xaxis.set_major_formatter(year_format)
    plt.title('Unemployment Benefits Search vs Rate', fontdict=font1)
    plt.savefig('images/Unemployment Benefits Search vs Rate.png')
    plt.show()
def rolling_us_unemployment():
    plt.figure(figsize=(14,8), dpi=105)
    plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)
 
    ax1 = plt.gca()
    ax2 = ax1.twinx()
 
    ax1.xaxis.set_major_locator(year)
    ax1.xaxis.set_major_formatter(year_format)
    ax1.xaxis.set_minor_locator(month)
    
    ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
    ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
    
    ax1.set_ylim(bottom=3, top=10.5)
    ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])
    
    # Calculate the rolling average over a 6 month window
    roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
    
    ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
    ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
    plt.savefig('images/Rolling US.png')
    plt.show()
def plot_unemployment_2004_20():
    plt.figure(figsize=(12, 6), dpi=105)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    ax1 = plt.gca() # get current axis
    ax2 = ax1.twinx()
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Unemployment Rate', fontdict=font1)
    ax2.set_ylabel('Search Trend', fontdict=font2)
    ax1.set_ylim([0, 11]) # set y-axis limit
    ax1.set_xlim([df_unemployment_2004_20.MONTH.min(), df_unemployment_2004_20.MONTH.max()]) # set x-axis limit
    ax1.plot(df_unemployment_2004_20.MONTH, df_unemployment_2004_20.UNRATE, color='skyblue',linestyle='--')
    ax2.plot(df_unemployment_2004_20.MONTH, df_unemployment_2004_20.UE_BENEFITS_WEB_SEARCH, color='red')
    #set the x-axis major locator and major formatter
    ax1.xaxis.set_major_locator(year)
    ax1.xaxis.set_minor_locator(month)
    ax1.xaxis.set_major_formatter(year_format)
    plt.title('Unemployment Benefits Search vs Rate', fontdict=font1)
    plt.savefig('images/Unemployment Benefits Search vs Rate.png')
    plt.show()
plot_tesla_price()
plot_bitcoin_price()
plot_unemployment()
rolling_us_unemployment()
plot_unemployment_2004_20()


