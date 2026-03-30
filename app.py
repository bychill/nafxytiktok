from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ================= LOBBY =================
@app.route("/")
def home():
    return render_template("home.html")

# ================= TIKTOK =================
@app.route("/tiktok", methods=["GET","POST"])
def tiktok():
    video_url = None
    music_url = None
    error = None

    if request.method == "POST":
        tipe = request.form.get("type")
        url = request.form.get("url")

        if not url:
            error = "Link nyaa mana kunyuk? 😑"
        else:
            try:
                res = requests.get(f"https://tikwm.com/api/?url={url}").json()

                if "data" in res:

                    if tipe == "video":
                        video_url = res["data"].get("play")
                        if not video_url:
                            error = "Video ilangg kaya diaa sama yangg lain 😢"

                    elif tipe == "mp3":
                        music_url = res["data"].get("music")
                        if not music_url:
                            error = "Audio nya kaga adaa bjir  😢"

                else:
                    error = "Link nyaa busukk bett 😭"

            except:
                error = "sorryy sorry APII nyaa eror berarti 😵"

    return render_template(
        "tiktok.html",
        video_url=video_url,
        music_url=music_url,
        error=error
    )

# ================= TOOLS =================
@app.route("/tools", methods=["GET","POST"])
def tools():
    text = None
    error = None

    if request.method == "POST":
        file = request.files.get("image")

        if not file or file.filename == "":
            error = "kaga adaa gambar nya jierr"
        else:
            try:
                res = requests.post(
                    "https://api.ocr.space/parse/image",
                    files={"filename": file},
                    data={"apikey": "helloworld"}
                ).json()

                text = res["ParsedResults"][0]["ParsedText"]

            except:
                error = "Gambar lu buriqq gw maless baca 😒"

    return render_template(
        "tools.html",
        text=text,
        error=error
    )

# ================= YOUTUBE =================
@app.route("/youtube")
def youtube():
    return """
    <body style='
        background:#0f0f0f;
        color:white;
        text-align:center;
        font-family:Arial;
    '>

    <h1 style='
        margin-top:80px;
        font-size:50px;
        color:white;
        background:red;
        display:inline-block;
        padding:10px 30px;
        border-radius:15px;
        box-shadow:0 0 25px red;
    '>
    𝐍𝐀𝐅𝐗𝐘 𝐖𝐄𝐁
    </h1>

    <div style='
        margin-top:60px;
        font-size:30px;
        color:red;
    '>
    ∅
    </div>

    <div style='
        margin-top:20px;
        font-size:20px;
        font-weight:bold;
    '>
    ni fitur besok aja lah gw publik malas update nya
    </div>

    <div style='
        margin-top:50px;
        font-weight:bold;
    '>
    powered by: aby suka mie ayam 🤤
    </div>

    </body>
    """

# ================= RUN =================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
