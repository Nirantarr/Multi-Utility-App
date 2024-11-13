from flask import Flask, render_template, jsonify
import subprocess
import scripts.webscrap_book as webscrap_book  # Import the updated webscraping script

app = Flask(__name__)

# decorator used which URL should trigger a specific function.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image_to_pdf')
def image_to_pdf():
    subprocess.call(["python", "scripts/image_to_pdf.py"])  #This runs any type of scripts in background
    return "IMAGE TO PDF CONVERSION COMPLETED..!"

@app.route('/image_compressor')
def image_compressor():
    subprocess.call(["python", "scripts/Image_compressor.py"])
    return "IMAGE COMPRESSION COMPLETED..!"

@app.route('/text_to_speech')
def text_to_speech():
    subprocess.call(["python", "scripts/text_to_speech.py"])
    return "TEXT TO SPEECH CONVERSION COMPLETED..!"

@app.route('/web_scraping')
def web_scraping():
    data = webscrap_book.scrape_books()
    return render_template('books.html', books=data)

if __name__ == '__main__':
    app.run(debug=True)
