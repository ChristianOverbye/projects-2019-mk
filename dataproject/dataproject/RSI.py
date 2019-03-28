## pip install plotly  <-- install inorder to show the plot type
## pip install talib

#%%
import pandas_datareader
import plotly.plotly as py
import plotly.graph_objs as go
import talib 
##import cufflinks as cf
import pandas as pd
from datetime import datetime
#%%


#%%
start = datetime(2018,1,1)
end = datetime(2018,12,31)
ticker = 'TSLA'

#%%
def prices(name, start=start, end=end):
    '''returns a dataframe with stock-information for a given company'''
    return pandas_datareader.iex.daily.IEXDailyReader(name, start, end).read()


tesla = prices(ticker, start,end)
tesla.reset_index(inplace=True)


#%%
close = tesla['close'].values
#%%
rsi = talib.RSI(close, timeperiod = 14)


tesla["RSI"]= rsi
tesla["Overbought"] = 70
tesla["Oversold"] = 30
#%%
tesla.head(n=20)
#%%
help(go.Scatter)
#%%
trace1 = go.Scatter(
    y=tesla['RSI'],
    x=tesla['date'],    
    name = "RSI",
    line = dict(color = '#7F7F7F'),
    )

#%%
trace2 = go.Scatter(
    y=tesla['Overbought'],
    x=tesla['date'],   
    name = "Overbought",
    line = dict(color = '#63c442'),
    hoverinfo='none'
    )
#%%
trace3 = go.Scatter(
    y=tesla['Oversold'],
    x=tesla['date'],   
    name = "Oversold",
    line = dict(color = '#705d65'),
    hoverinfo='none'
    )
#%%
trace4 = go.Scatter(
    y=tesla['close'],
    x=tesla['date'],   
    name = "Price",
    line = dict(color = '#2ed362'),
    )


#%%
data = [trace1,trace2,trace3,trace4]
#%%
layout = dict(
    title='Nvidia with RSI',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=12,
                     label = '1 year',
                     stepmode='backward'),
                dict(step='all')

            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)
#%%
fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "Nvidia1")