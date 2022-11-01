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

    print('RESULT DICT >>>>>>>>',result_dict)
    return result_dict




if __name__=='__main__':
    # pass
    # Insert_Product('ST-1004','ตำปูนา',100,r'c:\Images\espresso.png')
    Product_Icon_List()