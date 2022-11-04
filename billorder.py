
from tkinter import *
from tkinter import ttk, messagebox
import productdb as pd

class CheckBill:

    def __init__(self):
        pass


    def popup(self, Table):
        rootCB = Toplevel()
        rootCB.geometry('1120x700')
        rootCB.iconbitmap('images/dog.ico')
        rootCB.title('Check Bill')
        rootCB.focus()

        # Listbill = pd.Show_Order_Single(Table)
        # print('ListBill ======>', Listbill)
        # [(16, 'PEA-221102214504', '02/11/2022 21:45:17', '33', 'ST-1004', 'ตำปูนา', 100.0, 1, 100.0)]
        text = f'เช็คบิล โต๊ะที่ {Table}'
        L = Label(rootCB, text=text, font=(None, 20),fg='blue').pack(pady=10)

        Frame_bill_order = Frame(rootCB)
        Frame_bill_order.place(x=30, y=50)

        Frame_total = Frame(rootCB)
        Frame_total.place(x=30, y=400)

        Frame_button = Frame(rootCB)
        Frame_button.place(x=740, y=400)

        Frame_QRcode = Frame(rootCB)
        Frame_QRcode.place(x=550, y=400)

        Frame_Bank = Frame(rootCB)
        Frame_Bank.place(x=80, y=560)        


        allorder = pd.Show_Order_Dict(Table)
        olist = []
        quan = []
        total = []
        global v_pay
        def InsertTableCheckBill():
            table_check_bill.delete(*table_check_bill.get_children())
            for m in allorder:
                olist.append(m[5])
                if olist[0] == m[5]:
                    quan.append(m[7])
                    total.append(m[8])
                    squan = sum(quan)
                    stotal = sum(total)
                    v1,v2,v3,v4,v5,v6 = m[1],m[2],m[3],m[4],m[5],m[6]
                else:
                    table_check_bill.insert('', END, values=[m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8]])
            table_check_bill.insert('', END, values=[v1,v2,v3,v4,v5,v6,squan,stotal])

            count = sum([m[8] for m in allorder])
            discount = 0
            sumtotal = count - discount

            text = f'ยอดรวม  {count}  บาท'
            L = Label(Frame_total,text=text,fg='green', font=(None,20)).grid(row=0, column=0,sticky=W)

            text = f'ส่วนลด  {discount}  บาท'
            L = Label(Frame_total,text=text,fg='green', font=(None,20), justify=LEFT).grid(row=1, column=0,sticky=W)
            
            v_total = StringVar()
            v_total.set(f'จำนวนเงินทั้งสิ้น  {sumtotal:,.2f}  บาท')
            L_total = Label(Frame_total, textvariable=v_total ,font=('Angsana New',35,'bold'),fg='red')
            L_total.grid(row=2, column=0,sticky=W)

            global state
            state = 1

            def Change_money(event=None):
                global state
                global chang
                if state == 1:
                    m = v_pay.get()
                    chang = m - sumtotal
                    v_chang.set(f'เงินทอน  {chang:,.2f}  บาท')
                    state += 1
                    Bchang.configure(text='เช็คบิล')
                elif state == 2:
                    print('Print OUt')

                    rootCB.destroy()
                    state = 1

            rootCB.bind('<Return>', Change_money)

            v_pay = DoubleVar()
            v_pay.set(0.0)
            Emoney = Entry(Frame_button, textvariable=v_pay, width=10, font=(None,25))
            Emoney.grid(row=0,column=0, padx=10)
            Emoney.bind('<Up>', lambda x: v_pay.set(v_pay.get() + 100))
            Emoney.bind('<Down>', lambda x: v_pay.set(v_pay.get() - 20))
            Emoney.focus()

            Bchang = Button(Frame_button, text='คำนวณเงินทอน', font=(None, 15),background='#98fc03', command=Change_money)
            Bchang.grid(row=0, column=1, ipadx=5, ipady=5, pady=5)

            v_chang = DoubleVar()
            v_chang.set(f'เงินทอน  0.0  บาท')
            L = Label(Frame_button, textvariable=v_chang ,font=('Angsana New',35,'bold'),fg='red')
            L.grid(row=1, column=0, columnspan=2)

            
            img = PhotoImage(file='images/QRcodeprompay.png')
            qrcode = Label(Frame_QRcode, image=img)
            qrcode.config(image=img)
            qrcode.image = img
            qrcode.pack()


            global v_banknote
            v_banknote = 0
            def Banknote(bank):
                global v_banknote
                v_banknote += bank
                v_pay.set(v_banknote)

            def clear_banknote(event=None):
                global v_banknote
                v_banknote = 0
                v_pay.set(0)

            rootCB.bind('<F12>',clear_banknote)

            L = Label(Frame_QRcode, text='F12 เคลียร์จำนวนเงิน',font=(None, 12))
            L.pack(pady=10)
            img_bn1000 = PhotoImage(file='images/b1000.png')
            BN1000 = Button(Frame_Bank, command=lambda b=1000 : Banknote(b))
            BN1000.grid(row=0, column=0)
            BN1000.config(image=img_bn1000)
            BN1000.image = img_bn1000

            img_bn500 = PhotoImage(file='images/b500.png')
            BN500 = Button(Frame_Bank, image=img_bn500, command=lambda b=500 : Banknote(b))
            BN500.grid(row=0, column=1)
            # BN1000.config(image=img_bn1000)
            BN500.image = img_bn500

            img_bn100 = PhotoImage(file='images/b100.png')
            BN100 = Button(Frame_Bank, image=img_bn100, command=lambda b=100 : Banknote(b))
            BN100.grid(row=0, column=2)
            # BN1000.config(image=img_bn1000)
            BN100.image = img_bn100

            img_bn50 = PhotoImage(file='images/b50.png')
            BN50 = Button(Frame_Bank, image=img_bn50, command=lambda b=50 : Banknote(b))
            BN50.grid(row=0, column=3)
            # BN1000.config(image=img_bn1000)
            BN50.image = img_bn50

            img_bn20 = PhotoImage(file='images/b20.png')
            BN20 = Button(Frame_Bank, image=img_bn20, command=lambda b=20 : Banknote(b))
            BN20.grid(row=0, column=4)
            # BN20.config(image=img_bn20)
            BN20.image = img_bn20
            

            
        # ========== TABLE CHECKBILL ======================================================
        header = ['เลขที่ใบเสร็จ','เวลา','โต๊ะที่','Code', 'รายการ','ราคา','จำนวน','รวมเงิน']
        h_width = [200,200,80,100,220,80,80,100]

        table_check_bill = ttk.Treeview(Frame_bill_order,columns=header,show='headings',height=10)
        table_check_bill.pack()
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 16) , foreground="red",rowheight = 40,anchor='E')
        style.configure("Treeview", font=('Calibri', 16,'bold'))
        style.configure("Treeview", rowheight=30)

        for hd,hw in zip(header,h_width):
            table_check_bill.heading(hd,text=hd)
            table_check_bill.column(hd,width=hw)

        InsertTableCheckBill()

        rootCB.bind('<Escape>', lambda x: rootCB.destroy())

        rootCB.mainloop()

    def command(self):
        self.popup()


if __name__ == '__main__':
    pass