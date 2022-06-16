import sqlite3
#database connection
#cnt = sqlite3.connect('sql.db')
#def create_project(conn, project):
 #   sql = '''INSERT INTO users(id, username, password,email, phone,usertype, ststus, createddate)
   #         VALUES('1', 'chandan', 'asdfghhjk', 'cyadav419@gmail.com', '9817213383', 'admin', '1', '2022-06-13' )'''
cnt = sqlite3.connect('sql.db')

#id INTEGER,
#username TEXT,
#password TEST,
#email TEXT,
#phone TEXT,
#usertype TEXT,
#status INTEGER,
#createddate TEXT,
#updateddate TEXT

cnt.execute('''INSERT INTO users (id, username, password, email, phone, usertype, status, createddate) VALUES(
'1', 'chandan', 'asdfghjk', 'cyadav419@gmail.com', '9817213383', 'admin', '1', '2022-06-13'
);''')

cur = cnt.cursor()
#cur.execute(conn, project)
cnt.commit()
#return cur.lastrowid