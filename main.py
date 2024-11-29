from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("ZUMBA_DB", 'postgresql://zumba_user:xwmWnpuzcSuq7KcuoWBS3NfQPCtsCy57@dpg-ct3ims9u0jms73a15260-a/zumba')
Bootstrap5(app)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/pictures')
def show_pictures():
    return render_template('album.html')



if __name__ == '__main__':
    app.run()
