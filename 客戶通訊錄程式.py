import os, ast

def ReadData():
    with open('PhoneNum.txt','r', encoding = 'UTF-8-sig') as f:
        filedata=f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else: return dict()

def menu():
    os.system("cls")
    print("客戶通訊錄程式")
    print("-------------------------")
    print("1.輸入姓名、電話")
    print("2.顯示姓名、電話")
    print("3.修改電話")
    print("4.刪除姓名、電話")
    print("0.結束程式")
    print("-------------------------")

def input_data():
    while True:
        name = input("請輸入姓名(Enter==>停止輸入)")
        if name=="": break
        if name in data:
            print("{}姓名已存在!".format(name))
            continue
        PhoneNum=input("請輸入電話:")
        data[name]=PhoneNum
        with open('PhoneNum.txt', 'w', encoding = 'UTF-8-sig') as f:
            f.write(str(data))
        print("()已被儲存完畢".format(name))
        
def disp_data():
    print("姓名\t電話")
    print("===============")
    for key in data:
        print("{}\t{}".format(key, data [key]))
    input("按任意鍵返回主選單")
    
    
def edit_data():
    while True:
        name = input("請輸入要改的姓名(Enter==>停止輸入)")
        if name=="": break
        if not name in data:
            print("{}姓名不存在!".format(name))
            continue
        print("原來電話為:{}".format(data[name]))
        PhoneNum=input("請輸入新電話:")
        data[name]=PhoneNum
        with open('PhoneNum.txt', 'w', encoding='UTF-8-sig') as f:
            f.write(str(data))
            input("更改完畢,請按任意鍵回上選舉")
            break

def delete_data():
    while True:
        name = input("請輸入要刪除的姓名(Enter==>停止輸入)")
        if name=="": break
        if not name in data:
            print("{}姓名不存在!".format(name))
            continue
        print("確定删除{}的資料!!".format(name))
        yn=input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            del data[name]
            with open('PhoneNum.txt','w',encoding = 'UTF-8-sig') as f:
                f.write(str(data))
                input("已刪除完畢,請按任意鍵返回主選單")
                break

data=dict()

data = ReadData() #讀取文字檔後轉換為 dict
while True:
    menu()
    choice=int(input("請輸入您的選擇:"))
    print()
    if choice==1:
        input_data()
    elif choice==2:
        disp_data()
    elif choice==3:
        edit_data()
    elif choice==4:
        delete_data()
    else:
        break
print("程式執行完畢!")