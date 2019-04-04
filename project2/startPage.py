#! C:\Users\Thinkpad\Miniconda3\python.exe
import cgi
import cgitb
import sqlite3
import myDatabase as db
import pymysql
#import MySQLdb

cgitb.enable(format = 'text')
#cgitb.enable(display=0, logdir="/var/log/httpd/cgi_err/")


def write_html():
    form = cgi.FieldStorage()
    print("Content-Type: text/html")

    print("""
        <html><head><title>game start</title><head><body>

    """)
    write_create_game_form()
   
    

def write_create_game_form():
    #<form action="new_game.py" method="post">
    print("""<p><b>Let's start a new Game!</b>
    <form action="new_game.py" method="post">
      Player 1: <input type="text" size=10 name="player1">
      Player 2: <input type="text" size=10 name="player2">
      Range:     <input type="text" size=1  name="range">
      <input type="submit" value="Create">
    </form>
    """, end="")


def connect_db():
    
    conn = pymysql.connect(host=db.host,user=db.user,port=db.port,passwd=db.password,db=db.dbname)


    cursor = conn.cursor()
    cursor.execute("show databases")

    

    for i in my_cursor:
        print(i)
    return cursor

def write_db():
    if os.path.exists('persons.db'):
        result = True
    else:
        result = False

    db = sqlite3.connect('persons.db')
    db.row_factory = sqlite3.Row
        
    if not result:
        db.execute("CREATE TABLE friends (first TEXT, last TEXT, bday TEXT, email TEXT PRIMARY KEY)")
        db.execute("CREATE TABLE colleagues (first TEXT, last TEXT, bday TEXT, email TEXT PRIMARY KEY)")
    else:
        return db
            
    return db

write_html()
