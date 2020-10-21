from flask import Flask
import os
import socket
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    table_description = '''CREATE TABLE increment (Date_app DATE)'''
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')
    cursor = conn.cursor()
    try: 
    	cursor.execute(table_description)
    except Exception as e:
        print('DB already created')
    conn.commit()
    cursor.close()
    conn.close()
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


@app.route("/plus")
def plus():
    
    date = "21/10/2020"
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')
    cursor = conn.cursor()
    add_date = "INSERT INTO increment(Date_app) VALUES ('2020-10-21')"
    cursor.execute(add_date)
    conn.commit()
    cursor.close()
    conn.close()
    html = f"<h3>{date}</h3>"
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

