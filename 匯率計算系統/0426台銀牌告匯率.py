from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
import requests
from bs4 import BeautifulSoup
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 取得匯率資訊
url = 'https://rate.bot.com.tw/xrt'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'html.parser')

# 存放幣名
coins_name = []
# 現金買賣匯率
cash_exchange_rate = []
# 即期買賣匯率
spot_exchange_rate = []
# 存放匯率資料
dict_buy_cash = {}
dict_sell_cash = {}
dict_buy_spot = {}
dict_sell_spot = {}

# 匯率更新時間
data_time = sp.find('span', class_='time').text.strip()

# 幣種資訊
country = sp.find_all('div', class_='visible-phone print_hide')
for countries in country:
    country_name = countries.text.strip()
    coins_name.append(country_name)

work = sp.find('span', class_='color-red').text.strip()  # 是否為營業時間

# 現金匯率
cash = sp.find_all('td', class_='rate-content-cash')
for exchange_rate in cash:
    cash_exchange_rate.append(exchange_rate.text.strip())

# 即期匯率
spot = sp.find_all('td', class_='rate-content-sight')
for exchange_rate_spot in spot:
    spot_exchange_rate.append(exchange_rate_spot.text.strip())

j = 0
for i in range(0, 19):
    dict_buy_cash[coins_name[i]] = cash_exchange_rate[j]
    dict_sell_cash[coins_name[i]] = cash_exchange_rate[j + 1]
    j += 2

k = 0
for i in range(0, 19):
    dict_buy_spot[coins_name[i]] = spot_exchange_rate[k]
    dict_sell_spot[coins_name[i]] = spot_exchange_rate[k + 1]
    k += 2
'''
# 顯示匯率資訊
print('現鈔買:', dict_buy_cash, '\n')
print('現鈔賣:', dict_sell_cash, '\n')
print('即期買:', dict_buy_spot, '\n')
print('即期賣:', dict_sell_spot)
'''




# 創建GUI介面元件
def create_label(parent, text, x, y, width=None, height=None, font_size=10, anchor=None):
    """創建標籤元件並放置在指定位置"""
    custom_font = font.Font(family="Helvetica", size=font_size)
    label = tk.Label(parent, text=text,font=custom_font,anchor="w")
    label.place(x=x, y=y, width=width, height=height)
    return label

def create_entry(parent, x, y, width=None, height=None):
    """創建輸入框元件並放置在指定位置"""
    entry = tk.Entry(parent)
    entry.place(x=x, y=y, width=width, height=height)
    return entry

def create_combobox(parent, values, x, y, width=None, height=None):
    """創建下拉框元件並放置在指定位置"""
    combo = ttk.Combobox(parent, values=values)
    combo.place(x=x, y=y, width=width, height=height)
    return combo

def create_button(parent, text, command, x, y, width=None, height=None):
    """創建按鈕元件並放置在指定位置"""
    button = tk.Button(parent, text=text, command=command)
    button.place(x=x, y=y, width=width, height=height)
    return button

def show_help():
    """顯示使用說明視窗"""
    help_text = """
    歡迎使用台灣銀行牌告匯率試算程式！

    使用說明：
    1. 點選現金或即期
    2. 在台幣輸入框中輸入您想要試算的金額。
    3. 從下拉框中選擇欲兌換貨幣。
    4. 點擊“兌換”按鈕以計算匯率換算結果。
    5. 如果您想顯示即時匯率資訊，請點擊“顯示匯率”按鈕。
    6. 您也可以查看歷史匯率圖表，請先在下拉式選單選擇貨幣並點擊“歷史匯率”按鈕。

    謝謝您的使用！
    """
    
    help_window = tk.Toplevel(root)
    help_window.title("使用說明")
    
    help_label = tk.Label(help_window, text=help_text, justify="left")
    help_label.pack(padx=20, pady=20)

def quit_app():
    """退出應用程式"""
    root.destroy()
'''
def show_history_rates():
    s=[]
    for i in my_date:
        a = i.split('/')[1:3]
        s.append('/'.join(a))
    s.reverse()
    q=s[1::4]
    date=s#反轉後的s字串
    listy1=history_sell_cash
    listy2=history_buy_cash
    #plt.style.use("seaborn")
    fig, axes = plt.subplots(2, 1, figsize=(15, 15))  

    #畫現鈔匯率
    axes[0].plot(date, listy1, 'r.-', label='sell')
    axes[0].plot(date, listy2, 'y.-', label='buy')
    axes[0].set_title(url_history_tail + ' Banknote exchange rate')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Price')
    axes[0].legend()
    axes[0].set_xticks(q)
    axes[0].tick_params(axis='x', rotation=45)

    #畫即期匯率
    axes[1].plot(date, history_sell_spot, label='Sell')
    axes[1].plot(date, history_buy_spot, label='Buy')
    axes[1].set_title(url_history_tail + ' Spot exchange rate')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Price')
    axes[1].legend()
    axes[1].set_xticks(q)
    axes[1].tick_params(axis='x', rotation=45)

    plot_window = tk.Toplevel(root)
    plot_window.title("Matplotlib Plot")
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
'''


def validate_numeric_input(text):
    """驗證輸入是否為數字"""
    if text.isdigit() or text == "":
        return True
    else:
        return False


#按下兌換按鈕後顯示
def get_entry_value():
    entry_value = entry1.get()
    entry2_value = combo.get()
    option_value = option.get()
    if option_value=="1":#現金
            entry2.delete(0, tk.END)  # Clear existing text in entry2
            entry2.insert(0, "%.3f"%(float(entry_value)/float(dict_buy_cash[entry2_value])))
            entry3.delete(0, tk.END)  # Clear existing text in entry2
            entry3.insert(0, "%.3f"%(float(entry_value)/float(dict_sell_cash[entry2_value])))
    elif option_value=="0":#即期
            entry2.delete(0, tk.END)
            entry2.insert(0, "%.3f"%(float(entry_value)/float(dict_buy_spot[entry2_value])))
            entry3.delete(0, tk.END)
            entry3.insert(0, "%.3f"%(float(entry_value)/float(dict_sell_spot[entry2_value])))       

#即時匯率顯示
def show_exchange_rates():
    """顯示各貨幣匯率"""
    text.config(state=tk.NORMAL)
    text.delete(1.0, tk.END)
    buy1="現金買入: \n"
    text.insert(tk.END, buy1)
    for key,value in dict_buy_cash.items():
       exchange_rates = f"{key}:{value}\n"
       text.insert(tk.END, exchange_rates)
    text.insert(tk.END, "\n")
    sell1="現金賣出: \n"
    text.insert(tk.END, sell1)
    for key,value in dict_sell_cash.items():
       exchange_rates = f"{key}:{value}\n"
       text.insert(tk.END, exchange_rates)  
    text.insert(tk.END, "\n")       
    buy2="即期買入: \n"
    text.insert(tk.END, buy2)
    for key,value in dict_buy_spot.items():
       exchange_rates = f"{key}:{value}\n"
       text.insert(tk.END, exchange_rates)
    text.insert(tk.END, "\n")
    sell2="即期賣出: \n"
    text.insert(tk.END, sell2)
    for key,value in dict_sell_spot.items():
       exchange_rates = f"{key}:{value}\n"
       text.insert(tk.END, exchange_rates)         
    text.config(state=tk.DISABLED)


# 建立主視窗
root = tk.Tk()
root.geometry("800x800")
root.resizable(False, False)
root.title("台灣銀行-牌告匯率&試算")

# 背景圖片
img = PhotoImage(file="background.png")
btn = Label(root, image=img)
btn.pack()

# 建立菜單
menubar = tk.Menu(root)
root.config(menu=menubar)

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_command(label="使用說明", command=show_help)
menubar.add_cascade(label="Help", menu=help_menu)

# 建立標籤
label1 = create_label(root, work, 170, 20, width=150, height=30,font_size=20)
label2 = create_label(root, "更新時間:"+str(data_time), 400, 20, width=295, height=30,font_size=18)
label3 = create_label(root, "台幣 :", 135, 100, width=50, height=30,font_size=12)
label4 = create_label(root, "元=>", 290, 100, width=50, height=30,font_size=12)
label5 = create_label(root, "買入:                       元", 590, 80, width=150, height=30,font_size=12, anchor="w")
label6 = create_label(root, "賣出:                       元", 590, 120, width=150, height=30,font_size=12, anchor="w")

# 建立輸入框
entry1 = create_entry(root, 195, 100, width=80, height=30)
entry1.config(validate="key", validatecommand=(root.register(validate_numeric_input), "%P"))
#validate_numeric_input 是一個函式，它會檢查輸入是否為數字

#買入輸出框
entry2=create_entry(root, 635, 80, width=80, height=30)

#賣出輸出框
entry3=create_entry(root, 635, 120, width=80, height=30)

# 建立下拉選單

def get_selected_item():
    ii=''
    selected_item = combo.get()
    for i in selected_item[-4:-1]:
        ii+=i
    
    url_history_head='https://rate.bot.com.tw/xrt/quote/l6m/'
    url_history_tail=ii
    url_history=url_history_head+url_history_tail

    #html2=requests.get(url_history)
    #html2.encoding='utf-8'

    #偽裝成伺服器
    def get_url(url,my_headers):
        response=requests.get(url,headers=my_headers)
        response.encoding='utf-8'
        return response
    my_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    data=get_url(url_history,my_headers)
    sp2=BeautifulSoup(data.text,'html.parser')



    #獲取日期
    my_date=[]#存放歷史匯率的日期
    count=0
    date_=sp2.find_all('td', class_='text-center')
    for h in date_:
        coin_history = h.text.strip()
        my_date.append(coin_history)
    del my_date[1::2]
    #print(my_date)

    #獲取歷史匯率
    history_buy_cash=[] #現金買入
    history_sell_cash=[] #現金賣出
    chart_element = sp2.find('div', {'class': 'chart'})#取得網站歷史匯率
    data_history =  chart_element.get('data-local')
    data_ = json.loads(data_history)
    series=data_['series']


    total=len(series[0]['data'])#歷史匯率總筆數
    for ii in range(total):
        history_sell_cash.append(series[0]['data'][ii][1])
    #print('賣出:',history_sell_cash)
    for jj in range(total):
        history_buy_cash.append(series[1]['data'][jj][1])
    #print('買入:',history_buy_cash)
    #print(history_buy_cash)

    #即期歷史匯率
    history_spot=[]
    history_buy_spot=[]
    history_sell_spot=[]
    items=sp2.find_all("td",class_='rate-content-sight text-right print_table-cell')
    for item in items:
        x=item.text.strip()
        history_spot.append(x)
    for i in range(246):
        if i%2==0:
            history_buy_spot.append(float(history_spot[i]))
        else:
            history_sell_spot.append(float(history_spot[i]))
    
    s=[]
    for i in my_date:
        a = i.split('/')[1:3]
        s.append('/'.join(a))
    s.reverse()
    q=s[1::4]
    date=s#反轉後的s字串
    listy1=history_sell_cash
    listy2=history_buy_cash
    #plt.style.use("seaborn")
    fig, axes = plt.subplots(2, 1, figsize=(15, 15))  

    #畫現鈔匯率
    axes[0].plot(date, listy1, 'r.-', label='sell')
    axes[0].plot(date, listy2, 'y.-', label='buy')
    axes[0].set_title(url_history_tail + ' Banknote exchange rate')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Price')
    axes[0].legend()
    axes[0].set_xticks(q)
    axes[0].tick_params(axis='x', rotation=45)


    #畫即期匯率
    axes[1].plot(date, history_sell_spot, label='Sell')
    axes[1].plot(date, history_buy_spot, label='Buy')
    axes[1].set_title(url_history_tail + ' Spot exchange rate')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Price')
    axes[1].legend()
    axes[1].set_xticks(q)
    axes[1].tick_params(axis='x', rotation=45)

    plot_window = tk.Toplevel(root)
    plot_window.title("Matplotlib Plot")
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()        
    
    #print(selected_item)
combo = create_combobox(root, coins_name, 355, 100, width=120, height=30)
default_value = coins_name[0]#在下拉選單設置預設值以免發生Error
combo.set(default_value)


# 建立按鈕
button1 = create_button(root, "兌換", get_entry_value, 490, 100, width=80, height=30)
button2 = create_button(root, "退出", quit_app, 700, 750, width=80, height=30)
button3 = create_button(root, "顯示即時匯率", show_exchange_rates, 700, 700, width=80, height=30)
button4 = create_button(root, "歷史匯率", get_selected_item, 700, 650, width=80, height=30)


# 建立文字框和卷軸
text = tk.Text(root, width=70, height=45)
text.place(x=150, y=175)
text.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.place(x=650, y=175, height=575)
text.config(yscrollcommand=scrollbar.set)

# 創建radio選項變數
option = tk.StringVar()

# radio預設值
option.set(1)

# 創建兩個radio選擇框
radio_button1 = tk.Radiobutton(root, text="現金", variable=option, value=1,font=12)
radio_button2 = tk.Radiobutton(root, text="即期", variable=option, value=0,font=12)

# 放置選擇框在指定位置
radio_button1.place(x=55, y=80)
radio_button2.place(x=55, y=125)


# 主程式執行
root.mainloop()
'''
#歷史
url_history_head='https://rate.bot.com.tw/xrt/quote/l6m/'
url_history_tail=input('輸入要查詢的幣別(英文):')
url_history=url_history_head+url_history_tail

#html2=requests.get(url_history)
#html2.encoding='utf-8'

#偽裝成伺服器
def get_url(url,my_headers):
    response=requests.get(url,headers=my_headers)
    response.encoding='utf-8'
    return response
my_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
data=get_url(url_history,my_headers)
sp2=BeautifulSoup(data.text,'html.parser')



#獲取日期
my_date=[]#存放歷史匯率的日期
count=0
date_=sp2.find_all('td', class_='text-center')
for h in date_:
    coin_history = h.text.strip()
    my_date.append(coin_history)
del my_date[1::2]
#print(my_date)

#獲取歷史匯率
history_buy_cash=[] #現金買入
history_sell_cash=[] #現金賣出
chart_element = sp2.find('div', {'class': 'chart'})#取得網站歷史匯率
data_history =  chart_element.get('data-local')
data_ = json.loads(data_history)
series=data_['series']


total=len(series[0]['data'])#歷史匯率總筆數
for ii in range(total):
    history_sell_cash.append(series[0]['data'][ii][1])
#print('賣出:',history_sell_cash)
for jj in range(total):
    history_buy_cash.append(series[1]['data'][jj][1])
#print('買入:',history_buy_cash)
#print(history_buy_cash)

#即期歷史匯率
history_spot=[]
history_buy_spot=[]
history_sell_spot=[]
items=sp2.find_all("td",class_='rate-content-sight text-right print_table-cell')
for item in items:
    x=item.text.strip()
    history_spot.append(x)
for i in range(246):
    if i%2==0:
        history_buy_spot.append(float(history_spot[i]))
    else:
        history_sell_spot.append(float(history_spot[i]))
    #print(i)
#print('買入:',history_buy_spot)
#print('賣出:',history_sell_spot)




#畫折線圖
s=[]
for i in my_date:
    a = i.split('/')[1:3]
    s.append('/'.join(a))
s.reverse()
q=s[1::4]
date=s#反轉後的s字串
listy1=history_sell_cash
listy2=history_buy_cash
#plt.style.use("seaborn")
fig, axes = plt.subplots(2, 1, figsize=(15, 15))  

#畫現鈔匯率
axes[0].plot(date, listy1, 'r.-', label='sell')
axes[0].plot(date, listy2, 'y.-', label='buy')
axes[0].set_title(url_history_tail + ' Banknote exchange rate')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Price')
axes[0].legend()
axes[0].set_xticks(q)
axes[0].tick_params(axis='x', rotation=45)

#畫即期匯率
axes[1].plot(date, history_sell_spot, label='Sell')
axes[1].plot(date, history_buy_spot, label='Buy')
axes[1].set_title(url_history_tail + ' Spot exchange rate')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Price')
axes[1].legend()
axes[1].set_xticks(q)
axes[1].tick_params(axis='x', rotation=45)

#plt.tight_layout()
plt.show()


'''