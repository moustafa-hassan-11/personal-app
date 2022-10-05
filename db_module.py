import mysql.connector
import mysql.connector.pooling
import os 


def get_cm():
    url = os.environ['url']
    database = os.environ['db']
    return url,database
    #pass
    # config = os.environ['MY_CONFIG']


def get_sec():
    username = os.environ['username']
    password = os.environ['password']
    return username,password



###########################################################################
############ Openning a pool of connections ###############################
url,db = get_cm()
user,pass_ = get_sec()
dbconfig = { 'host': url,
             'user': user,
             'password': pass_,
             'database': db,
           }
pool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 32,
                                                      **dbconfig)
###########################################################################



def database_con():


  conn = pool.get_connection()
  cursor = conn.cursor()
  _SQL = """select rest_name from rest"""
  cursor.execute(_SQL)
  restaurants = cursor.fetchall()
  return restaurants
  #for row in res:
  #    print(row)
def get_rest():
  
    conn = pool.get_connection()
    cursor = conn.cursor()
    _SQL = """select rest_name from rest"""
    cursor.execute(_SQL)
    restaurants = cursor.fetchall()
    cursor.close()
    conn.close()

    return restaurants

def get_category():

    conn = pool.get_connection()
    cursor = conn.cursor()
    _SQL = """select * from rest"""
    cursor.execute(_SQL)
    types = cursor.fetchall()
    cursor.close()
    conn.close()
    return types

##################################################
################ get orders ######################

def get_order():

    conn = pool.get_connection()
    cursor = conn.cursor()
    _SQL = """select * from order_view"""
    cursor.execute(_SQL)
    orders = cursor.fetchall()
    cursor.close()
    conn.close()

    return orders
####################################################
def add_order(rest_name,username,order: str) -> None:

    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute(
    "select restID from rest where rest_name = %s", [rest_name])
    rest_id = cursor.fetchone()[0]
    cursor.execute(
    "select userID from users where username = %s", [username])
    user_id = cursor.fetchone()[0]
    print (rest_id,user_id)
    query = "insert into orders (items, userID, restID) values (%s, %s, %s)"
    values = (order, user_id, rest_id)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()






#####################################################
def get_order_user_history(username):


    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute(
    "select * from order_view where username = %s", [username])

    orders = cursor.fetchall()
    cursor.close()
    conn.close()

    return orders
####################################################


def auth_(username: str , password: str) -> bool:


    conn = pool.get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    user_records = cursor.fetchall()
    cursor.close()
    conn.close()
    
    #users_in_db = users_records[0][1]
    #print (user_records[0])
    for user in user_records:
        #print (user)
        if username == user[1] and password == user[6]:
            #print ("authentication is done")
            return True
    return False    

################################################################
def verify_username(username: str ) -> bool:


    conn = pool.get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    user_records = cursor.fetchall()
    cursor.close()
    conn.close()

    for user in user_records:
        #print (user)
        if username == user[1]:
            return True
    return False

################################################################

def register_(username:str,fn:str,ln:str,age:int,gender:str,password:str) -> None:


    #print (username + fn + ln + str(age) + gender + password)
    conn = pool.get_connection()
    cursor = conn.cursor()
    query = "insert into users (username, fn, ln ,age ,gender ,password) values (%s, %s, %s, %s, %s, %s)"
    values = (username, fn, ln, age, gender, password)
    cursor.execute(query,values)
    #age_ = str(age)
    #cursor.execute("insert into users values (%s, %s, %s, %s, %s, $s)", (username, fn, ln, age_, gender, password))
    conn.commit()
    cursor.close()
    conn.close()


def create_(name:str,food_type:str,review:str) -> None:


    conn = pool.get_connection()
    cursor = conn.cursor()
    query = "insert into rest (rest_name,food_type,review) values (%s, %s, %s)"
    values = (name,food_type,review)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_(name:str) -> None:


    conn = pool.get_connection()
    cursor = conn.cursor()
    #query = "delete from rest where rest_name = %s"
    #values = (name)
    cursor.execute(
    "select restID from rest where rest_name = %s", [name])
    rest_id = cursor.fetchone()[0]
    print (rest_id)

    cursor.execute(
    "delete from orders where restID = %s", [rest_id])
    cursor.execute(
    "delete from rest where rest_name = %s", [name])
    #cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()

def update_(restname:str=None,food_type:str=None,review:str=None) -> None:

    if food_type == None and review == None:
        mesg = "nothing to be updated!"
        return (mesg) 
    elif food_type == '' and review == '':
        mesg = "Nothing to be updated!"
        food_type=None
        review=None
        return (mesg)
    else:
        #this block of code is not used but not deleted to not break the fun.....this happened because of adding connection pool after almost finishing coding
        url,db = get_cm()
        user,pass_ = get_sec()
        dbconfig = { 'host': url,
                     'user': user,
                     'password': pass_,
                     'database': db,
                   }

        if  food_type  and review:
            conn = pool.get_connection()
            cursor = conn.cursor()
            query = """Update rest set food_type = %s, review = %s where rest_name = %s"""
            values = (food_type, review, restname)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
        elif food_type and not review:
            conn = pool.get_connection()
            cursor = conn.cursor()
            query = """Update rest set  food_type = %s where rest_name = %s"""
            values = (food_type, restname)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
        elif not food_type and review :    
            conn = pool.get_connection()
            cursor = conn.cursor()
            query = """Update rest set  review = %s where rest_name = %s"""
            values = (review, restname)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
        else:
            mesg = "No Update for Any Restaurant!"
            return mesg

##################################
def get_echo():

  conn = pool.get_connection()   
  cursor = conn.cursor()
  _SQL = """select message from management"""
  cursor.execute(_SQL)
  message = cursor.fetchall()
  return message[0]



###################################################
########## Testing Connection Pooling #############
###################################################
def test_pool():

      conn = pool.get_connection()
      cursor = conn.cursor()
      _SQL = """select message from management"""
      cursor.execute(_SQL)
      message = cursor.fetchall()
      return message[0]



