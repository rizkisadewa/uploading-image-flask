import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Make the path for the folder of the image
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/') # make the target for the images
    print(target) # just print the target and checking the correct file

    # checking the directory, if there is no folder then make the folder
    if not os.path.isdir(target):
        os.mkdir(target)

    # due to we specify that can upload multiple files, then we need to looping.
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename

        # tell the server to put the file in specific destination
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

if __name__== "__main__":
    app.run(port=4555, debug=True)