from cgitb import text
from itertools import count
from msilib.schema import tables
from os import stat
from secrets import choice
from select import select
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import productdb as pd
# import billorder as bill
from billorder import *

checkbill = CheckBill()



root = Tk()
root.title("Pupea Shop")
root.iconbitmap('images/dog.ico')
root.geometry("1350x700+0+0")
# root.state('zoomed') 

#================== Menu Bar ============================================================
menubar = Menu(root)
root.config(menu=menubar)

#================== Menu File ============================================================
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)

def ExportDatabase():
    print("ExportDatabase")

filemenu.add_command(label='Export', command=ExportDatabase, font=('Angsana New', 15))
filemenu.add_command(label='Exit', command=root.destroy, font=('Angsana New', 15))

#================== Menu File ============================================================
Frame_name_shop = Frame(root, bg='#03d3fc', padx=550)
Frame_name_shop.pack(pady=10)

Lnameshop = Label(Frame_name_shop, text="ร้านขายส้มตำ", font=('Angsana New', 40) )
Lnameshop.pack()
Lnameshop.config(background='#03d3fc',fg='red')


#================== Button Table =========================================================
Frame_search = Frame(root)
Frame_search.place(x=25,y=95)

v_search = StringVar()
ESearch = Entry(Frame_search, textvariable=v_search, width=20, font=(None, 20))
ESearch.grid(row=0,column=0)

def SearchTable(event=None):
    tables = v_search.get()
    # [(12, 'PEA-221102214443', '02/11/2022 21:44:54', '11', 'ST-1001', 'ตำไทย', 50.0, 2, 100.0)
    try:
        res = pd.Show_Order_Single(tables)
        print('RES ====>',res)
        print('RES ======>',res[0][3])
        productid = res[0][3]
        checkbill.command()
        
    except:
        messagebox.showwarning('Not Found','ไม่สินค้าในโต๊ะที่คุณค้นหา')
        v_search.set('')
        ESearch.focus()
    
    
ESearch.bind('<Return>', SearchTable)
ESearch.bind('<F3>', lambda x :v_search.set(''))
Bsearch = Button(Frame_search,text='Search',font=(None, 11), background='#031cfc',fg='white',command=SearchTable)  #,command=SearchBarcode
Bsearch.grid(row=0, column=1, padx=10,ipadx=30,ipady=5)


Frame_table_number = Frame(root)
Frame_table_number.place(x=20, y=150)

allorder = {}
allproduct = pd.Product_Icon_List()
# print('allproduct ============>',allproduct)
#allproduct = {1: {'id': 1, 'productcode': 'ST-1001', 'title': 'ตำไทย', 'price': 50.0, 'image': 'c:\\Images\}
def InsertTableOrder():
    table_order.delete(*table_order.get_children())
    for i ,m in enumerate(allorder.values(),start=1):
        # print('M =======>',m)  # M =======> [1, 'ST-1001', 'ตำไทย', 50.0, 1, 50.0]
        table_order.insert('', END, values=[i ,m[0],m[1],m[2],m[3],m[4],m[5]])






def AddMenuOrder(id = 1):
    if id not in allorder:
        allorder[id] = [allproduct[id]['id'],allproduct[id]['productcode'],allproduct[id]['title'],allproduct[id]['price'], 1, allproduct[id]['price']]
    else:
        quan = allorder[id][4] + 1
        total = allproduct[id]['price'] * quan
        allorder[id] = [allproduct[id]['id'],allproduct[id]['productcode'],allproduct[id]['title'],allproduct[id]['price'], quan, total]
    
    count = []
    for i in allorder.values():
        count.append(i[5])
        # print('Count ====>',count)   Count ====> [100.0, 120.0]
        s_total = sum(count)

    v_total.set(f'{s_total:,.2f}')   
    
    InsertTableOrder()

row = 0
column = 0
column_quan = 4
for k,p in allproduct.items():   
    if column == column_quan:
        column = 0
        row += 1

    B = Button(Frame_table_number,text=p['title'],font=('Angsana New', 20),fg='blue',background='#98fc03')
    B.grid(row=row,column=column,ipadx=20)
    B.config(command=lambda m = k : AddMenuOrder(m))
    column += 1
    
Frame_table = Frame(root)
Frame_table.place(x=600, y=95)

L = Label(Frame_table, text='โต๊ะที่ : ', font=('Angsana New', 30),fg='blue').grid(row=0, column=0)
v_table = StringVar()
v_table.set('')
E = Entry(Frame_table, textvariable=v_table, width=5, font=('None', 20),fg='blue',justify=CENTER).grid(row=0, column=1)

Frame_transaction = Frame(root)
Frame_transaction.place(x=1050, y=110)

v_transaction = StringVar()
stramp = datetime.now().strftime('PEA-'+'%y%m%d%H%M%S')
v_transaction.set(stramp)
lbl_tran = Label(Frame_transaction,textvariable=v_transaction,font=(None,16))
lbl_tran.configure(fg='blue')
lbl_tran.pack(padx=10)

def SaveOrder():
    stramp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    transaction =  v_transaction.get()
    tablenum = v_table.get()
    for m in allorder.values():
        # print('M ======>',m, transaction)  M ======> [1, 'ST-1001', 'ตำไทย', 50.0, 1, 50.0]
        m.insert(0, transaction)
        m.insert(1, stramp)
        m.insert(2, tablenum)
    # ALLORDER ====> {1: ['PEA-221102212140', '02/11/2022 21:21:46', '222', 1, 'ST-1001', 'ตำไทย', 50.0, 1, 50.0]
    for a in allorder.values():
        pd.Insert_Product_Order(a[0],a[1],a[2],a[4],a[5],a[6],a[7],a[8])
    
    ResetOrder()
    




# =========== Table Order ======================================
Frame_table_order = Frame(root)
Frame_table_order.place(x=600, y=150)

header = ['No.','Id','Code','Title','Price','Quantity','Total']
h_width = [50,50,100,220,100,100,100]

table_order = ttk.Treeview(Frame_table_order,columns=header,show='headings',height=12)
table_order.pack()
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 16) , foreground="purple")
style.configure("Treeview", font=('Calibri', 16,'bold'))
style.configure("Treeview", rowheight=30)

for hd,hw in zip(header,h_width):
    table_order.heading(hd,text=hd)
    table_order.column(hd,width=hw)

Frame_total = Frame(root)
Frame_total.place(x=600, y=540)

v_total = StringVar()
v_total.set(0.0)

L_price = Label(Frame_total, text='รวมราคา:  ' ,font=('Angsana New',40,'bold'),fg='red').grid(row=0, column=0)
L_total = Label(Frame_total, textvariable=v_total ,font=('Angsana New',40,'bold'),fg='red').grid(row=0, column=1)
L_bath = Label(Frame_total, text='    บาท' ,font=('Angsana New',40,'bold'),fg='red').grid(row=0, column=2)


def DeleteOrder(event=None):
    select = table_order.selection()
    if len(select) != 0:
        choice = messagebox.askyesno('ลบรายการ order','คุณต้องการลบรายการสินค้าหรือไม่')
        if choice == True:
            data = table_order.item(select)['values']
            del allorder[data[1]]
            count = sum([m[5] for m in allorder.values()])
            v_total.set(f'{count:,.2f}')
            InsertTableOrder()
            print('Delete Success')
        else:
            pass
    else:
        messagebox.showwarning('ไม่ได้เลือกรายการ','กรูราเลือกรายการก่อนลบ')

table_order.bind('<Delete>', DeleteOrder)

def ResetOrder():
    global allorder
    allorder = {}
    table_order.delete(*table_order.get_children())
    v_total.set(0.0)
    stramp = datetime.now().strftime('PEA-'+'%y%m%d%H%M%S')
    v_transaction.set(stramp)
    v_table.set('')



Frame_function = Frame(root)
Frame_function.place(x=470,y=142)

B = Button(Frame_function,text='SAVE',font=(None, 15), background='#031cfc',fg='white',command=SaveOrder)  #,command=SearchBarcode
B.grid(row=0, column=0,pady=10,ipadx=25,ipady=10)

B = Button(Frame_function,text='CLE',font=(None, 15), background='#031cfc',fg='white',command=ResetOrder)  
B.grid(row=1, column=0,ipadx=30,ipady=10)




root.mainloop()