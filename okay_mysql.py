import mysql.connector

def connect_mysql():
    mysql_conn = mysql.connector.connect(
        host='den1.mysql6.gear.host',
        user='arctecindia',
        passwd='Arctec@345',
        db='arctecindia'
    )

    mysql_cursor = mysql_conn.cursor()
    mysql_cursor.execute("Select * from %s" % ('contact_form'))
    
    string = []
    
    for row in mysql_cursor:
        string.append(row)
    
    print(string)
    

    

print(connect_mysql())