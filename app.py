from flask import Flask, render_template, request

app = Flask(__name__)


# =========================
# FUNGSI MEMBERSHIP FUZZY
# =========================
def turun(x, a, b):
    if x <= a:
        return 1
    elif x >= b:
        return 0
    return (b - x) / (b - a)


def naik(x, a, b):
    if x <= a:
        return 0
    elif x >= b:
        return 1
    return (x - a) / (b - a)


def segitiga(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif x == b:
        return 1
    elif x < b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)


# =========================
# ROUTE HALAMAN
# =========================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/input")
def input_page():
    return render_template("input.html")


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/result", methods=["POST"])
def result():
    bb = float(request.form["bb"])
    tb_cm = float(request.form["tb"])
    umur = int(request.form["umur"])
    aktivitas = request.form["aktivitas"]

    tb_m = tb_cm / 100
    bmi = bb / (tb_m * tb_m)

    # =========================
    # MEMBERSHIP BMI
    # =========================
    belum_ideal = turun(bmi, 17, 18.5)
    kurang_ideal = segitiga(bmi, 18, 20, 22)
    ideal = segitiga(bmi, 21, 23, 25)
    tidak_ideal = naik(bmi, 24.5, 30)

    # =========================
    # RULE FUZZY SEDERHANA
    # =========================
    score_belum = belum_ideal * 25
    score_kurang = kurang_ideal * 50
    score_ideal = ideal * 80
    score_tidak = tidak_ideal * 35

    # Pengaruh aktivitas
    if aktivitas == "tinggi" and bmi < 25:
        score_ideal += 8
    elif aktivitas == "rendah" and bmi >= 25:
        score_tidak += 15
    elif aktivitas == "rendah" and bmi < 18.5:
        score_belum += 8

    scores = {
        "Belum Ideal": score_belum,
        "Kurang Ideal": score_kurang,
        "Ideal": score_ideal,
        "Tidak Ideal": score_tidak
    }

    status = max(scores, key=scores.get)

    # =========================
    # HASIL STATUS
    # =========================
    if status == "Belum Ideal":
        icon = "🔵"
        color_class = "blue"
        desc = "Berat badan kamu masih kurang dibandingkan tinggi badan."
        advice = "Tingkatkan asupan nutrisi, protein, dan kalori sehat secara bertahap."

    elif status == "Kurang Ideal":
        icon = "🟡"
        color_class = "yellow"
        desc = "Kondisi tubuh kamu mulai mendekati ideal, tetapi belum berada pada rentang paling seimbang."
        advice = "Jaga pola makan, tidur cukup, dan mulai rutin aktivitas fisik ringan."

    elif status == "Ideal":
        icon = "🟢"
        color_class = "green"
        desc = "Tinggi dan berat badan kamu berada dalam kondisi yang seimbang."
        advice = "Pertahankan pola makan seimbang, olahraga rutin, dan cukup minum air putih."

    else:
        icon = "🔴"
        color_class = "red"
        desc = "Berat badan kamu berada di atas batas ideal berdasarkan tinggi badan."
        advice = "Kurangi makanan tinggi gula/lemak dan tingkatkan aktivitas fisik secara bertahap."

    # =========================
    # INTERPRETASI UMUR
    # =========================
    if umur < 18:
        desc += " Karena usia kamu masih dalam masa pertumbuhan, hasil ini sebaiknya dipahami sebagai gambaran awal."
    elif umur >= 35:
        desc += " Pada usia ini, metabolisme tubuh cenderung mulai menurun sehingga pola hidup perlu lebih dijaga."

    # =========================
    # POINTER GAUGE
    # BMI 0-40 dipetakan ke 0-100%
    # =========================
    pointer = min(max((bmi / 40) * 100, 3), 97)

    return render_template(
        "result.html",
        bb=bb,
        tb=tb_cm,
        umur=umur,
        aktivitas=aktivitas,
        bmi=round(bmi, 1),
        status=status,
        icon=icon,
        desc=desc,
        advice=advice,
        pointer=round(pointer, 1),
        color_class=color_class,
        belum=round(belum_ideal, 2),
        kurang=round(kurang_ideal, 2),
        ideal=round(ideal, 2),
        tidak=round(tidak_ideal, 2)
    )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)