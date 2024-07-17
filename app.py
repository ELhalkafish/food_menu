from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    # قراءة محتوى ملف HTML من نفس الدليل
    with open('index.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content, images=['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg', 
              'image6.jpg', 'image7.jpg', 'image8.jpg', 'image9.jpg', 'image10.jpg',
              'image11.jpg', 'image12.jpg', 'image13.jpg', 'image14.jpg', 'image15.jpg',
              'image16.jpg', 'image17.jpg'])

@app.route('/static/images/<path:filename>')
def static_files(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)
