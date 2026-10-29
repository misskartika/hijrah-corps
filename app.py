
from flask import Flask, render_template

app = Flask(__name__)

BUSINESS = {
    "name": "Hijrah Corps",
    "tagline": "Digital Solutions for Business Growth",
    "description": (
        "Kami membantu bisnis membangun kehadiran digital melalui "
        "website profesional, desain yang terarah, dan solusi digital "
        "yang disesuaikan dengan kebutuhan usaha."
    ),
    "whatsapp": "6282171841634",
    "email": "halo@hijrahcorps.com",
    "services": [
        {
            "number": "01",
            "title": "Website Development",
            "description": (
                "Website profil perusahaan, landing page, dan website "
                "bisnis yang responsif serta mudah diakses."
            ),
        },
        {
            "number": "02",
            "title": "UI/UX & Web Design",
            "description": (
                "Desain website yang modern, terstruktur, dan membantu "
                "pengunjung memahami bisnis Anda."
            ),
        },
        {
            "number": "03",
            "title": "Digital Business Solutions",
            "description": (
                "Solusi digital untuk mendukung proses bisnis, "
                "meningkatkan efisiensi, dan membuka peluang baru."
            ),
        },
    ],
}


@app.route("/")
def home():
    return render_template("index.html", business=BUSINESS)


if __name__ == "__main__":
    app.run(debug=True)
