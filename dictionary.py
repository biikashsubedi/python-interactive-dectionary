import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user='root',
    password='bikash',
    host='127.0.0.1',
    database='pythonDictionary'
)
cursor = con.cursor()

word = input('please choose word for definition: ')

query = cursor.execute(f"SELECT * FROM Dictionary where title = '{word}' ")
results = cursor.fetchall()

print('========================================================================')
if results:
    for item in results:
        print(item[2])
else:
    print('word does not found ☹️, Please try another')
