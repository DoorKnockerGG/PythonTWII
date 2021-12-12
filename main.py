import pandas as pd
import requests

datestr = '20211026'
r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

tickers = [] #宣告List
for i in r.text.split('\r\n'):
    if (len(i.split('",')) == 17 and i[0] != '='):
        _ticker = i.split('",') #使用",區隔每一個價格
        _ticker = [t.replace('"','') for t in _ticker] #將左邊的" 取代成空字元
        _ticker = [t.replace(',','') for t in _ticker] #將數字千分為 取代為空字元
        tickers.append(_ticker)

df = pd.DataFrame(tickers)

#將第一列的資料換成標題，並且刪除第一列
df.columns = df.loc[0,:]
df.drop(0, axis = 0 , inplace = True)

#找出前面幾筆資料進行檢查
df.head()
