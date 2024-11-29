from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("ZUMBA_DB", 'postgresql://zumba_user:xwmWnpuzcSuq7KcuoWBS3NfQPCtsCy57@dpg-ct3ims9u0jms73a15260-a/zumba')
Bootstrap5(app)

@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/pictures')
def show_pictures():
    return render_template('album.html')


@app.route('/gallery/photos')
def show_photos():
    return render_template('photos.html')

@app.route('/gallery/videos')
def show_videos():
    return render_template('videos.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')


@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


if __name__ == '__main__':
    app.run()
