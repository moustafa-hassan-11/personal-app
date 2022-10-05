# Restaurant_demo

Name= Moustafa Youssef


dockerhub Link: https://hub.docker.com/repository/docker/moustafayoussef/restaurant_database
GitHub Link: https://github.com/Moustafa-youssef-linux/Restaurant_demo




The Development environment in which i did the task is:

Red Hat Enterprise Linux 8.4 (Ootpa)


**NOTE**

There are two branches main and test. Please Conider only test branch. Since I have lately a conflict between them.

################################################################################################
########## Applicatoin Info ####################################################################
Applicaton is written in python flask and backed by mysql database with basic html.
You can start logging in admin user using the following credentials
username: admin
password: admin@123



the available APIs:

@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
@app.route('/logout', methods=['GET'])
@app.route('/registration', methods=['GET', 'POST'])
@app.route('/restaurants', methods=['GET','POST'])
@app.route('/admin_console', methods=['GET','POST'])
@app.route('/rest/create', methods=['GET', 'POST'])
@app.route('/rest/delete', methods=['GET', 'POST'])
@app.route('/rest/update', methods=['GET','POST'])
@app.route('/order', methods=['GET','POST'])
@app.route('/healthz', methods=['GET'])
@app.route('/health_db', methods=['GET'])


Note: 
In the database,I created the management table which contains a simple 
message retrieved by /health_db endpoint. In this way i can test the connection between the APP and DB.
it's added as a liveness probe inside K8s for testing connection periodically.
###############################################################################################

############################ K8s ###############################################################################
there is a directory called K8s under which you can find all the required resources for deploying the app on K8s

there's a secret resource which is created for storing db username & password

Note(1):
the ingress resource is deployed and tested with nginx ingress controller

Note(2):
I've used DockerHub to store the images after building them.It's better so that for testing the app the K8s will pull it directly from there.

################################################################################################################


# for anything not clear or not mentioned in ReadMe,I will be grateful to hear back from you

Email: moustafayoussef759@gmail.com
LinkedIn: https://www.linkedin.com/in/moustafa-youssef-63398a116/



