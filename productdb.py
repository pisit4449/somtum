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
    # print(result)
    return result 





if __name__=='__main__':
    # pass
    # Insert_Product('ST-1004','ตำปูนา',100,r'c:\Images\espresso.png')
    # Product_Icon_List()
    Show_Order_Single(11)