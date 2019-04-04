#! C:\Users\Thinkpad\Miniconda3\python.exe
import cgi
import cgitb
import sqlite3
import random
import myDatabase as db
import pymysql


#cgitb.enable(format = 'text')
#cgitb.enable(display=0, logdir="/var/log/httpd/cgi_err/")


def write_html():
    print("Content-Type: text/html")

    print("""
        <html><head><title>game start</title><head><body>

    """)

    print("""<h1>Welcome to our guessing game!</h1>""")
    

    form = cgi.FieldStorage()
    ranges = 0
    target = 0
    player1 = ""
    player2 = ""
    guess1 = ""
    guess2= ""
    lst = []
    count = 0
    #print(form)

    if("player1" not in form or "player2" not in form or "range" not in form):
        print("<p>Invalid input, please go back and resubmit your input again.</p>")

    else:
        
        count +=1
        player1 = form["player1"].value
        player2 = form["player2"].value
        ranges = form["range"].value
        lst.append(player1)
        lst.append(player2)
        lst.append(ranges)

        conn = pymysql.connect(host=db.host,user=db.user,port=db.port,passwd=db.password,db=db.dbname)
        cursor = conn.cursor()

        cursor.execute("show tables")
        cursor.execute("use myUsers")
       
        cursor = conn.cursor()
        cursor.execute("show tables")
        #cursor.execute("INSERT INTO Information (id, player1, player2, ranges) VALUES (%d,%s,%s)",(int(count),player1,player2,int(ranges)))
        #cursor.execute("INSERT INTO Information (player1) VALUES %s",player1)
        rows = cursor.fetchall()
        cursor.execute("select * from Information")
        #cursor.execute("""INSERT INTO Information(player1,player2,ranges) VALUES(%s,%s,%s);""", (player1,player2,ranges))

       
        target = random.randint(1,int(ranges))
        print('<p>hello '+player1 +'!Thanks for playing our game!</p>')  
        print('<p>hello '+player2 +'!Thanks for playing our game!</p>')
        print('<p>hello Your target is '+str(target)+'</p>')
        
       

       
    cursor.execute("show tables")
    cursor.execute("use myUsers")
    
    #print(player1, player2, ranges)


    #print('************************')
    cursor = conn.cursor()
    cursor.execute("show tables")
    #cursor.execute("INSERT INTO Information (id, player1, player2, ranges) VALUES (%d,%s,%s)",(int(count),player1,player2,int(ranges)))
    #cursor.execute("INSERT INTO Information (player1) VALUES %s",player1)
    rows = cursor.fetchall()
    cursor.execute("select * from Information")
        
    write_create_guess_form(form,player1,player2,target,ranges)
    print(form)

       
       
                  
    


def write_create_guess_form(form,player1,player2,target,ranges):
    #<form action="new_game.py" method="post">
    print("""<p><b>Let's start a new Guess! Please enter your guess below: </b>
    <form action="new_game.py" method="get">"""+
      player1+""": <input type="text" size=5 name="guess1">"""+
      player2+""": <input type="text" size=5 name="guess2">
      <input type="submit" value="Guess">
    </form>
    """, end="")
    print(form,player1,player2,target,ranges)

    

def connect_db():
    
    conn = pymysql.connect(host=db.host,user=db.user,port=db.port,passwd=db.password,db=db.dbname)


    cursor = conn.cursor()
    cursor.execute("show databases")

    for i in my_cursor:
        print(i)
    return cursor


def define_result(guess,target):
    if(guess<target):
        print('<p> the target number is greater than your guess. </p>')
    if(guess>target):
        print('<p> the target number is less than your guess. </p>')
    if(guess<target):
        print('<p> Congratulation! You got the right number! </p>')



write_html()
