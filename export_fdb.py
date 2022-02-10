import fdb
import pandas as pd

con = fdb.connect(host="localhost", database=r"C:\Program Files\Firebird\Firebird_3_0\SFPB0001.FDB",user='sysdba', password='teste123')


sql_query = pd.read_sql_query('''
                              select * from SFPTB071_EMPRESARE
                              '''
                              ,con) # here, the 'con' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\elton\Desktop\export_data.csv', index = False) # place 'r' before the path name to avoid any errors in the path(editado)
