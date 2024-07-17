from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # أسماء الصور التي ستعرض
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg', 
              'image6.jpg', 'image7.jpg', 'image8.jpg', 'image9.jpg', 'image10.jpg',
              'image11.jpg', 'image12.jpg', 'image13.jpg', 'image14.jpg', 'image15.jpg',
              'image16.jpg', 'image17.jpg']
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
