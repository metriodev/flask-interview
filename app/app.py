import os
from flask import Flask, render_template, request
from google.cloud import storage

app = Flask(__name__)

storage_client = storage.Client()
bucket_name = os.environ["BUCKET_NAME"]

@app.route("/")
def show_uploader():
    return render_template("index.html")


@app.route("/uploader", methods=["POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        blob = storage_client.bucket(bucket_name).blob(f.filename)
        blob.upload_from_string(f.read(), content_type=f.content_type)
        return "file uploaded successfully"

if __name__ == "__main__":
    print(f"Environment: {os.environ['ENVIRONMENT']}")
    print(f"Log Level: {os.environ['LOG_LEVEL']}")
    app.run(host="0.0.0.0", port=8080)
