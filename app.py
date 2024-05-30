from flask import Flask, request, render_template

import sys
sys.path.append(r'C:\Users\HP\OneDrive\Desktop\SPC\templates\pdf_page_counter.py')

from pdf_page_counter import count_pdf_pages

app = Flask(__name__)

# Simulated database of uploaded files
uploaded_files = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Check if a file was uploaded
        if "file" in request.files:
            uploaded_file = request.files["file"]
            if uploaded_file.filename != "":
                # Save the uploaded file
                uploaded_file.save(uploaded_file.filename)
                
                # Count the number of pages in the PDF file
                num_pages = count_pdf_pages(uploaded_file)
                
                # Add the file and its page count to the database
                uploaded_files.append({"filename": uploaded_file.filename, "num_pages": num_pages})
                
                # Display success message
                return render_template("success.html", filename=uploaded_file.filename, num_pages=num_pages)
        # If no file was uploaded or an error occurred
        return render_template("error.html")
    # If accessing the page via GET request
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
