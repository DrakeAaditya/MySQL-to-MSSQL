import mysql.connector          # MySQL Connector Library
import pyodbc                   # MSSQL Connector Library
import getpostdb


# MySQL Connection Starts here #
def connect_mysql():
    cdx = getpostdb.cds_mysql
    mysql_conn = mysql.connector.connect(
        host=cdx[0],
        user=cdx[1],
        passwd=cdx[2],
        db=cdx[3]
    )

    return mysql_conn.cursor()
# MySQL Connection Ends here #


# MSSQL Connection Starts here #
def connect_mssql():
    cdx = getpostdb.cds_mssql
    mssql_conn = pyodbc.connect(Driver="{SQL Server}",
                            Server={cdx[0]},
                            Database={cdx[1]},
                            uid={cdx[2]},
                            pwd={cdx[3]})

    return mssql_conn.cursor()
# MSSQL Connection Ends here #


def get_MSSQL_Query(table_name):
    mssql_cursor = connect_mssql()
    mssql_cursor.execute("SELECT * FROM %s" % (table_name))
    string = []

    for row in mssql_cursor:
        string.append(row)
    
    return string

def get_MySQL_Query(table_name):
    mysql_cursor = connect_mysql()
    mysql_cursor.execute("Select * from %s" % (table_name))
    
    string = []
    
    for row in mysql_cursor:
        string.append(row)
    
    print(string)




print(get_MSSQL_Query('prac'))