import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

sql = """
select * from users;
"""

cur.execute(sql)
results = cur.fetchall()
print('results=',results)
for row in results:
    print('================')
    print('row=',row)
    print('id=', row[0])
    print('username=', row[1])
    print('password=', row[2])
    print('age=', row[3])

sql = """
select * from messages;
"""

cur.execute(sql)
messages = cur.fetchall()
print('messages=',results)
for row in messages:
    print('================')
    print('row=',row)
    print('message_id=', row[0])
    print('sender_id=', row[1])
    print('message=', row[2])
    print('created_at=', row[3])

