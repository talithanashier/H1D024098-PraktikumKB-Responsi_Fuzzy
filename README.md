# 🌑 BodyBalance AI — Sistem Fuzzy Mamdani

* **Nama**: Talitha Nashier
* **NIM**: H1D024098
* **Shift KRS**: C

---

## 🎯 Deskripsi Sistem

**BodyBalance AI** merupakan sistem berbasis **Fuzzy Mamdani** yang digunakan untuk menganalisis keseimbangan tubuh berdasarkan:

* Berat badan (BB)
* Tinggi badan (TB)
* Umur
* Aktivitas harian

Sistem ini tidak hanya menggunakan perhitungan BMI, tetapi juga menerapkan **derajat keanggotaan fuzzy** untuk menghasilkan keputusan yang lebih fleksibel dan realistis.

---

## 🧠 Metode yang Digunakan

Metode yang digunakan adalah **Fuzzy Inference System (FIS) Mamdani**, yang terdiri dari:

1. **Fuzzifikasi**
   Mengubah nilai numerik (BMI) menjadi nilai keanggotaan:

   * Belum Ideal
   * Kurang Ideal
   * Ideal
   * Tidak Ideal

2. **Rule Base (Aturan IF-THEN)**
   Contoh:

   * IF BMI rendah AND aktivitas rendah → Belum Ideal
   * IF BMI normal AND aktivitas tinggi → Ideal
   * IF BMI tinggi AND aktivitas rendah → Tidak Ideal

3. **Inferensi**
   Menghitung skor dari setiap kategori berdasarkan derajat keanggotaan.

4. **Defuzzifikasi (Sederhana)**
   Mengambil nilai tertinggi dari hasil perhitungan untuk menentukan status akhir.

---

## ⚙️ Cara Kerja Sistem

1. User memasukkan data:

   * Berat badan
   * Tinggi badan
   * Umur
   * Aktivitas

2. Sistem menghitung **BMI**:

   ```
   BMI = BB / (TB dalam meter)^2
   ```

3. Nilai BMI diproses dengan fungsi keanggotaan fuzzy:

   * Turun
   * Segitiga
   * Naik

4. Sistem menerapkan aturan fuzzy dan menghasilkan:

   * Status tubuh
   * Saran kesehatan
   * Visualisasi BMI (gauge)
   * Derajat keanggotaan

---

## 🖥️ Fitur Sistem

* 🎯 Analisis keseimbangan tubuh berbasis fuzzy
* 📊 Visualisasi BMI (gauge + pointer)
* 🧠 Derajat keanggotaan fuzzy (bar)
* 💡 Rekomendasi kesehatan
* 📱 Tampilan responsif (desktop & mobile)
* ✨ UI modern (dark mode + animasi)

---

## 🗂️ Struktur Folder

```
FUZZY_RESPONSIKB/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── input.html
│   ├── result.html
│   └── learn.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

---

## ▶️ Cara Menjalankan

1. Pastikan Python sudah terinstall

2. Install Flask (jika belum):

   ```
   pip install flask
   ```

3. Jalankan aplikasi:

   ```
   python app.py
   ```

4. Buka browser:

   ```
   http://127.0.0.1:8000
   ```

