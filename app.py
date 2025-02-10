from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_video(url, format_type):
    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "format": "mp4" if format_type == "video" else "bestaudio",
        "ffmpeg_location": r"C:\ffmpeg-master-latest-win64-gpl-shared\bin",
    }

    if format_type == "audio":
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if format_type == "audio":
            filename = filename.rsplit(".", 1)[0] + ".mp3"
        return filename

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        format_type = request.form["format"]
        filepath = download_video(url, format_type)
        return send_file(filepath, as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
