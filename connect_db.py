import mysql.connector

dbconfig = { 'host': '127.0.0.1',
'user': 'rest',
'password': 'root123',
'database': 'restaurant', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """select rest_name from rest"""
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

"""
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""

cursor.execute(_SQL)

"""


"""
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
print(row)

"""


def log_request(req: 'flask_request', res: str) -> None:
  """Log details of the web request and the results."""
  dbconfig = { 'host': '127.0.0.1',
               'user': 'vsearch',
               'password': 'vsearchpasswd',
               'database': 'vsearchlogDB', }
  import mysql.connector
  conn = mysql.connector.connect(**dbconfig)
  cursor = conn.cursor()
  _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
  cursor.execute(_SQL, (req.form['phrase'],
                 req.form['letters'],
                 req.remote_addr,
                 req.user_agent.browser,
                 res, ))
  conn.commit()
  cursor.close()
