import sqlite3
#database connection
cnt = sqlite3.connect('stdnt.db')
#create table
cnt.execute('''CREATE TABLE student(
id INTEGER,
username TEXT,
password TEST,
email TEXT,
phone TEXT,
usertype TEXT,
status INTEGER,
createddate TEXT
);''')

cnt.execute('''INSERT INTO users VALUES(
'1', 'chandan', 'cyadav419@gmail.com', '9817213383', 'admin', '1', '2022-06-13', '2022-06-13' 

);''')