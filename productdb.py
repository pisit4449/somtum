import sqlite3
from turtle import title

conn = sqlite3.connect('productdb.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                productcode TEXT,
                title TEXT,
                price REAL,
                image TEXT) """)


c.execute("""CREATE TABLE IF NOT EXISTS productorder (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tran TEXT,
                time TEXT,
                tablenum TEXT,
                productcode TEXT,
                title TEXT,
                price REAL,
                quan INTEGER,
                total REAL) """)


def Insert_Product(productcode,title,price,image):
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)' # จำนวนเเท่ากับ ตัวแปร บวก ID
        c.execute(command,(None,productcode,title,price,image))
    conn.commit()  # save database
    print('======Saved Product Success=======')
    # add status after insert product
    # find = Show_product_single(productid)
    # print('fine = Show_product_single=====>',find)
    # insert_product_status(find[0],'show')

def View_Product():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        result = c.fetchall()
    return result


def Product_Icon_List():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        product = c.fetchall()

    result = []

    for p in product:
        result.append(p)

    result_dict = {}
    # print('RESULT=======>',result)
    # result = [(1, 'ST-1001', 'ตำไทย', 50.0, 'c:\\Images\\espresso.png')]
    for r in result:
        result_dict[r[0]] = {'id':r[0],'productcode':r[1],'title':r[2],'price':r[3],'image':r[4]}

    # print('RESULT DICT >>>>>>>>',result_dict)
    # {1: {'id': 1, 'productcode': 'ST-1001', 'title': 'ตำไทย', 'price': 50.0, 'image': 'c:\\Imag}
    return result_dict


# ================ Table Order ===========================================================
def Insert_Product_Order(tran,time,tablenum,productcode,name,price,quan,total):
    with conn:
        command = 'INSERT INTO productorder VALUES (?,?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tran,time,tablenum,productcode,name,price,quan,total))
    conn.commit()
    print('======Saved Order Success=======')


def Show_Order_Single(ID):
    with conn:
        command = 'SELECT * FROM productorder WHERE tablenum=(?)'
        c.execute(command,([ID]))
        result = c.fetchall()
    # print(result) [(12, 'PEA-221102214443', '02/11/2022 21:44:54', '11', 'ST-1001', 'ตำไทย', 50.0, 2, 100.0)]
    return result 


def Show_Order_Dict(Table):
    with conn:
        command = 'SELECT * FROM productorder WHERE tablenum=(?)'
        c.execute(command,([Table]))
        order = c.fetchall()
    # print("ORDER ===>",order)
    
    result = []

    for o in order:
        result.append(o)
        # print('RESULT=======>',result)
        # RESULT=======> [(19, 'PEA-221103190832', '03/11/2022 19:08:42', '44', 'ST-1004', 'ตำปูนา', 100.0, 1, 100.0)]
    result_dict = {}

    for r in result:
        result_dict[r[0]] = {'id':r[0],'transaction':r[1],'time':r[2],'table':r[3],'productcode':r[4],'title':r[5],'price':r[6],'quan':r[7],'total':r[8]}

    # print('RESULT DICT ========>',result_dict)
    return order

    
    #RESULT DICT ========> {19: {'id': 19, 'transaction': 'PEA-221103190832', 'time': '03/11/2022 19:08:42', 'table': '44', 'productcode': 'ST-1004', 'title': 'ตำปูนา', 'price': 100.0, 'quan': 1, 'total': 100.0},

def Show_Order_Table_Title(Table):
    with conn:
        command = 'SELECT * FROM productorder WHERE tablenum=(?)'
        c.execute(command,([Table]))
        order = c.fetchall()
    print("ORDER ===>",order)
    return order


if __name__=='__main__':
    # pass
    # Insert_Product('ST-1004','ตำปูนา',100,r'c:\Images\espresso.png')
    # Product_Icon_List()
    # Show_Order_Single(11)
    Show_Order_Dict(44)
    # Show_Order_Table_Title(1,'ตำไทย')