import sqlite3

connection = sqlite3.connect("test_01.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE band_name ='Lions'")
result = cursor.fetchall()
print(result)
#%%% Dummy Code Block
print("YOU CAN'T SEE ME")