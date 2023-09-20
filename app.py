from flask import Flask,render_template,request,redirect
import mysql.connector

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlog',methods=['POST','GET'])
def adminlog():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        print(username,password)
        try: 
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="event"
            )
            cursor=connection.cursor()
            cursor.execute("select * from admin where username='"+username+"' and password='"+password+"'")
            result = cursor.fetchall()
            print(result)
            print('database connected')
            if result:
                return render_template('admin1.html',m='login successfully')
            else:
                return render_template('admin.html',m='login not successfully')

        except Exception as e:
            print('error in server connecting',+str(e))

    return render_template('new.html',m='not')
   


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/Signin',methods=['POST','GET'])
def Signin():
    if request.method=='POST':
        try:
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="event"
            )
            username=request.form['username']
            password=request.form['password']
            print(username,password)
            cursor=connection.cursor()
            cursor.execute("select * from userlog where username='"+username+"' and password='"+password+"'")
            res = cursor.fetchall()
            print(res)
            if res:
                return render_template('events.html',m='user login  successfully')
            else:
                return render_template('login.html',m='user login successfully')
        except Exception as e:
            print(e)
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/Signup',methods=['POST','GET'])
def Signup():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        phone=request.form['phone']
        password=request.form['password']
        print(username,email,phone,password)
        try:
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="event"
            )
            cursor=connection.cursor()
            cursor.execute("insert into userlog values ('"+username+"','"+email+"','"+phone+"','"+password+"')")
            connection.commit()
            return render_template('index.html',mes='register successfully')
        except Exception as e:
            print(e)
            return render_template('index.html',mes='register not successfully')

    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route('/wedding',  methods=['GET', 'POST'])
def wedding():
    if request.method == 'POST':
        # Get form data
        hname = request.form['hname']
        wname = request.form['wname']
        email = request.form['email']
        phone = request.form['phone']
        event_date = request.form['event_date']
        message = request.form['message']
        additional_events = request.form.getlist('additional_events')

        # Do something with the form data, e.g., store it in a database
        # Here, we'll just print the data to the console
        print(f"Name: {hname}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Event Date: {event_date}")
        print(f"Message: {message}")
        print(f"Additional Events: {', '.join(additional_events)}")

        # You can also redirect the user to a thank-you page
        # return render_template('thank_you.html')
        k = ', '.join(additional_events)
        # For now, let's redirect back to the wedding page
        # cursor=connection.cursor()
        try: 
            connection=mysql.connector.connect(#to connect an mysql
            host="localhost",
            user="root",#database user name
            password="",#database password
            database="event"#database name 
            )
            cursor=connection.cursor()

            print("database connected")
        
        except Exception as e:
            print("error in connecting to the server "+str(e))
        cursor.execute("insert into wedding (hname,wname,email,phone,event_date,message,k) values('"+hname+"', '"+wname+"','"+email+"', '"+phone+"', '"+event_date+"', '"+message+"', '"+k+"')")
        connection.commit()#to save in database
        cursor.close()#to close an cursor 
        connection.close()#close database connection 
        print("database connected")
        return redirect(f'/userweddingdetail/{email}')
    return render_template('wedding.html')
    
@app.route('/userweddingdetail/<email>')
def userweddingdetail(email):
    
    try: 
        connection=mysql.connector.connect(#to connect an mysql
        host="localhost",
        user="root",#database user name
        password="",#database password
        database="event"#database name 
        )
        cursor=connection.cursor()
        cursor.execute("SELECT *FROM wedding where email ='"+ email +"'")
        m=cursor.fetchall()

        print(m)
        c= m[0: ]
        print(c)
        d=list(c[0])
        print(d)

        cursor.close()#to close an cursor 
        connection.close()#close database connection 

        print("database connected")
        return render_template("weddingdetails.html", wed = m, d= d)
        
    except Exception as e:
        print("error in connecting to the server "+str(e))
    

    return render_template("weddingdetails.html")

@app.route('/bdy', methods=['GET','POST'])
def bdy():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        place = request.form['place']
        event_date = request.form['event_date']
        message = request.form['message']

        # Do something with the form data, e.g., store it in a database
        # Here, we'll just print the data to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Place: {place}")
        print(f"Event Date: {event_date}")
        print(f"Message: {message}")

        # You can also redirect the user to a thank-you page
        # return render_template('thank_you.html')
        # cursor=connection.cursor()
        try: 
            connection=mysql.connector.connect(#to connect an mysql
            host="localhost",
            user="root",#database user name
            password="",#database password
            database="event"#database name 
            )
            cursor=connection.cursor()

            print("database connected")
        
        except Exception as e:
            print("error in connecting to the server "+str(e))
        cursor.execute("insert into birthday (name,email,phone,place,event_date,message) values('"+name+"', '"+email+"', '"+phone+"', '"+place+"', '"+event_date+"', '"+message+"')")
        connection.commit()#to save in database
        cursor.close()#to close an cursor 
        connection.close()#close database connection 
        print("database connected")
        
            # For now, let's redirect back to the home page
        return redirect(f"/userbirthdaydetail/{email}")

    return render_template('name.html')

@app.route('/userbirthdaydetail/<email>')
def userbirthdaydetail(email):
    
    try: 
        connection=mysql.connector.connect(#to connect an mysql
        host="localhost",
        user="root",#database user name
        password="",#database password
        database="event"#database name 
        )
        cursor=connection.cursor()
        cursor.execute("SELECT *FROM birthday where email ='"+ email +"'")
        m=cursor.fetchall()

        print(m)
        c= m[0: ]
        print(c)
        d=list(c[0])
        print(d)

        cursor.close()#to close an cursor 
        connection.close()#close database connection 

        print("database connected")
        return render_template("birthdaydetails.html", data = m, b= d)
        
    except Exception as e:
        print("error in connecting to the server "+str(e))
    

    return render_template("birthdaydetails.html")

@app.route('/corporate', methods=['GET','POST'])
def corporate():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        place = request.form['place']
        event_date = request.form['event_date']
        message = request.form['message']

        # Do something with the form data, e.g., store it in a database
        # Here, we'll just print the data to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Place: {place}")
        print(f"Event Date: {event_date}")
        print(f"Message: {message}")

        # You can also redirect the user to a thank-you page
        # return render_template('thank_you.html')
        # cursor=connection.cursor()
        try: 
            connection=mysql.connector.connect(#to connect an mysql
            host="localhost",
            user="root",#database user name
            password="",#database password
            database="event"#database name 
            )
            cursor=connection.cursor()

            print("database connected")
        
        except Exception as e:
            print("error in connecting to the server "+str(e))
        cursor.execute("insert into corporate (name,email,phone,place,event_date,message) values('"+name+"', '"+email+"', '"+phone+"', '"+place+"', '"+event_date+"', '"+message+"')")
        connection.commit()#to save in database
        cursor.close()#to close an cursor 
        connection.close()#close database connection 
        print("database connected")
        
         # For now, let's redirect back to the home page
        return redirect(f"/userbirthdaydetail/{email}")

    return render_template('corporate.html')

@app.route('/admin1')
def admin1():
    
    try: 
        connection=mysql.connector.connect(#to connect an mysql
        host="localhost",
        user="root",#database user name
        password="",#database password
        database="event"#database name 
        )
        cursor=connection.cursor()
        cursor.execute("SELECT *FROM birthday")
        k=cursor.fetchall()
        print(k)
        a= k[0: ]
        print(a)
        b=list(a[0])
        print(b)
        cursor.execute("SELECT *FROM wedding")
        m=cursor.fetchall()

        print(m)
        c= m[0: ]
        print(c)
        d=list(c[0])
        print(d)

        cursor.close()#to close an cursor 
        connection.close()#close database connection 

        print("database connected")
        return render_template("admin1.html", data=k, b=b, wed = m, d= d)
        
    except Exception as e:
        print("error in connecting to the server "+str(e))
    

    return render_template("admin1.html")

@app.route('/remove/<ni>', methods=['POST'])
def remove(ni):
    if request.method == 'POST':
            # Do something with the form data, e.g., store it in a database
            # Here, we'll just print the data to the console
        print(ni)
        
            # You can also redirect the user to a thank-you page
            # return render_template('thank_you.html')
        
            # For now, let's redirect back to the wedding page
            # cursor=connection.cursor()
    
        connection=mysql.connector.connect(#to connect an mysql
        host="localhost",
        user="root",#database user name
        password="",#database password
        database="event"#database name 
        )
        cursor=connection.cursor()

        print("database connected viki")
        print(ni)
        cursor.execute("delete from birthday where email='"+ ni +"'")
        connection.commit()#to save in database
        cursor.close()#to close an cursor 
        
        print("database connected vikas ")
        return redirect('/admin1')

@app.route('/removew/<ni>', methods=['POST'])
def removew(ni):
    if request.method == 'POST':
            # Do something with the form data, e.g., store it in a database
            # Here, we'll just print the data to the console
        print(ni)
        
            # You can also redirect the user to a thank-you page
            # return render_template('thank_you.html')
        
            # For now, let's redirect back to the wedding page
            # cursor=connection.cursor()
    
        connection=mysql.connector.connect(#to connect an mysql
        host="localhost",
        user="root",#database user name
        password="",#database password
        database="event"#database name 
        )
        cursor=connection.cursor()

        print("database connected viki")
        print(ni)
        cursor.execute("delete from wedding where email='"+ ni +"'")
        connection.commit()#to save in database
        cursor.close()#to close an cursor 
        
        print("database connected vikas ")
        return redirect('/admin1')   
if __name__:
    app.run(debug=True)