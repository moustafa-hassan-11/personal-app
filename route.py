from flask import Flask,render_template, redirect, url_for, request, session
import  db_module

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'
##
## for logging out session.pop('logged_in')
##
def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False

@app.route("/")
def entry():
    return render_template('entry.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    print (request.method)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exist = db_module.auth_(username,password)
        if not exist  :
            error = "Invalid Credentials. Please try again.\n <div class=\"text\"> <a href=\"/login\">Login.</a> <h3>Create a new account <a href=\"/registration\">Register.</a></h3>"
            return str(error)
            #error = data
        elif exist and username =='admin' :

            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('admin_console'))
        else:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('restaurant'))
    return render_template('login.html', error=error)


@app.route('/logout', methods=['GET'])
def logout():
    error = None
    session.pop('logged_in')
    return redirect(url_for('login'))

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    error = None
    print (request.method)
    if request.method == 'POST':
        u_ = request.form['username']
        fn_ = request.form['fn']
        ln_ = request.form['ln']
        age_ = request.form['age']
        pass_ = request.form['password']
        gender_ = request.form['gender']
        exist = db_module.verify_username(u_)
        print (u_+ pass_ + ln_ + age_ + gender_ + pass_)
        if  u_ !=  'admin' and not exist:
          result= db_module.register_(u_,fn_,ln_,age_,gender_,pass_)
          #return redirect(url_for('reg_result', error=error))
          return render_template('reg_result.html')
        elif exist: 
            error = "The user is already registered\n. Please try again.\n <div class=\"text\"> <a href=\"/login\">Login.</a>"
            return str(error)
        else:
            error = 'Please Fill all the inputs'
    return render_template('registration.html', error=error)
#####
###INSERT INTO users (username,fn,ln,age,gender,password)
##    -> values ("admin","admin","admin",28,"male","admin@123");

#
@app.route('/restaurants', methods=['GET','POST'])
def restaurant():
    error = None
    
    if request.method == 'GET' and check_logged_in() and session['username'] != 'admin':
        user = session['username']
        data_ = db_module.get_order_user_history(user)
        rest_ = db_module.get_category()
        rest_name_ = db_module.get_rest()
        print (rest_)
        print (session['username'])
        return render_template('restaurants.html', orders=data_,restaurants=rest_,rest=rest_name_)
    elif request.method == 'GET' and check_logged_in() and session['username'] == 'admin':
        return str("Sorry, This page is not for admins!!\n Try to login as a normal user <h3>Try to login again: <a href=\"/login\">Login</a></h3>")
    elif request.method == 'POST' and check_logged_in() and session['username'] != 'admin':
        item = request.form['order']
        rest = request.form.get('actions')
        user = session['username']
        print (rest,user,item)
        result = db_module.add_order(rest,user,item)
        if result == None:
           mesg = "Your order has been submitted <h3>check you order <a href=\"/restaurants\">home</a></h3>"
           return str(mesg)
        else:
            return str("something went wrong") 
    else:
        return redirect(url_for('login'))



@app.route('/admin_console', methods=['GET','POST'])
def admin_console():
    error = None
    if request.method == 'GET' and check_logged_in() and session['username'] == 'admin':
        #select = request.form.get('actions')
        #print (select)
        rest_ = db_module.get_rest()
        #category_ = db_module.get_category()
        orders_ = db_module.get_order()
        data_ = db_module.get_category()
        print (data_)
        return render_template('console.html', rest=rest_,data=data_,order_view=orders_)
    elif request.method == 'POST' and check_logged_in() and session['username'] == 'admin':
        #error = "Wrong url"
        select = request.form.get('actions')
        if select == 'read':
            return redirect(url_for('restaurant'))
        elif select == 'add':
            return redirect(url_for('create_rest'))
        elif select == 'delete':
            return redirect(url_for('delete_rest'))
        elif select == 'update':
            return redirect(url_for('update_rest'))
        #print (select)
        return str(select)
    elif check_logged_in() and session['username'] != 'admin':
        return str("You don't have privileges to open this page!")
    else:
        return str("You are Not logged in")

@app.route('/rest/create', methods=['GET', 'POST'])
def create_rest():
    error = None
    print (request.method + "#########")
    if request.method == 'POST' and check_logged_in() and session['username'] == 'admin':
        print ("yessssookkkkk")
        rest_name = request.form['rest_name']
        print (rest_name)
        type_ = request.form['type']
        review = request.form['review']
        result = db_module.create_(rest_name,type_,review)
        print (rest_name,type_,review)
        print ("Okay this is pooooooooooost")
        if result == None:
            mesg = "the Restaurant: "+rest_name+" has been added.\n <div class=\"text\"> <h3>Doing another Management Action<a href=\"/admin_console\">!Click here</a></h3> </div> "
            return str(mesg)
        else:
           error = "Something went wrong"
           return str(error)
    elif request.method == 'GET' and check_logged_in() and session['username'] == 'admin':
        return render_template('create.html')
    else:
        error = "Please login First"
        return str(error)
@app.route('/rest/delete', methods=['GET', 'POST'])
def delete_rest():
    error = None
    if request.method == 'POST' and check_logged_in() and session['username'] == 'admin':
          rest_name = request.form['rest_name'] 
          result = db_module.delete_(rest_name)
          if result == None:
              mesg = "the Restaurant: "+rest_name+" has been deleted.\n <div class=\"text\"> <h3>Doing another Management Action<a href=\"/admin_console\">!Click here</a></h3> </div>"
              return str(mesg)
          else:
              error = "Something went wrong"
              return str(error)
    elif request.method == 'GET' and check_logged_in() and session['username'] == 'admin': 
          return render_template('delete.html')
    else:
         return str("Please login first")

@app.route('/rest/update', methods=['GET','POST'])
def update_rest():        
    error = None
    if request.method == 'POST' and check_logged_in() and session['username'] == 'admin':
          rest_name_ = request.form['rest_name']
          category_ = request.form['food_type']
          review_ = request.form['review']

          result = db_module.update_(restname=rest_name_,food_type=category_,review=review_)
          if result == None:
              mesg = "the Restaurant: "+rest_name_+" has been Updated.\n <div class=\"text\"> <h3>Doing another Management Action<a href=\"/admin_console\">!Click here</a></h3> </div>"
              return str(mesg)
          else:
              error = "Something went wrong"
              return str(result)
    elif request.method == 'GET' and check_logged_in() and session['username'] == 'admin':
          return render_template('update.html')
    else:
          return str("Please Login First")

##################################################
################# Home & Order Pages #############
##################################################

@app.route('/order', methods=['GET','POST'])
def order():
    error = None
    if request.method == 'GET':
       render_template('order.html')


@app.route('/healthz', methods=['GET'])
def app_ready():
    error = None
    if request.method == 'GET':
       return str('The application is up')
    

@app.route('/health_db', methods=['GET'])
def app_live():
    error = None
    if request.method == 'GET':
       message = db_module.get_echo()
       return str(message[0])



#app.run(debug=True)
if __name__ == '__main__':
   app.run(debug=True)


