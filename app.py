from flask import Flask, render_template, jsonify
import subprocess
import scripts.webscrap_book as webscrap_book  # Import the updated webscraping script

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image_to_pdf')
def image_to_pdf():
    subprocess.call(["python", "scripts/image_to_pdf.py"])
    return "Image to PDF conversion complete!"

@app.route('/slideshare_to_pdf')
def slideshare_to_pdf():
    subprocess.call(["python", "scripts/slideshare_to_pdf.py"])
    return "Slideshare to PDF conversion complete!"

@app.route('/text_to_speech')
def text_to_speech():
    subprocess.call(["python", "scripts/text_to_speech.py"])
    return "Text to Speech conversion complete!"

@app.route('/web_scraping')
def web_scraping():
    data = webscrap_book.scrape_books()
    return render_template('books.html', books=data)

if __name__ == '__main__':
    app.run(debug=True)
