
# Recommendation Project DBS2024

## Overview
Proyek ini bertujuan untuk membuat sistem rekomendasi buku berdasarkan dataset rekomendasi buku. 
Dataset mencakup informasi buku, rating, dan data pengguna.

Model yang digunakan mencakup pendekatan Collaborative Filtering dan Content-Based Filtering.

## Business Understanding

### Problem Statement
1. Bagaimana cara merekomendasikan buku berdasarkan minat pembaca?
2. Bagaimana cara meningkatkan kepuasan pengguna dan eksplorasi buku?

### Goals
- Membuat model yang memberikan rekomendasi buku dengan akurasi tinggi.
- Mempermudah pembaca menemukan buku berdasarkan riwayat bacaan mereka.

### Solutions
1. Menggunakan model collaborative filtering untuk rekomendasi.
2. Memanfaatkan metode cosine similarity dalam content-based filtering.

## Data Understanding
Dataset meliputi tiga file utama: 
- **Books**: Informasi tentang judul, penulis, ISBN, dll.
- **Ratings**: Penilaian dari pengguna terhadap buku.
- **Users**: Detail tentang pengguna seperti usia dan lokasi.

## Data Preparation
1. **Preprocessing**:
    - Menangani missing value.
    - Menghapus duplikat.
    - Encoding fitur (user dan buku) untuk digunakan dalam model.

2. **Integrasi Data**:
    - Menggabungkan data buku dan rating.

## Modeling
### Collaborative Filtering
- Membuat pasangan pengguna dengan buku yang belum dibaca.
- Melatih model untuk memprediksi rating berdasarkan pasangan tersebut.

### Content-Based Filtering
- Menggunakan TF-IDF untuk representasi fitur.
- Menghitung cosine similarity untuk menentukan kesamaan antar buku.

## Evaluation

### Metrics
1. **Precision, Recall, F1-Score**: Digunakan untuk mengukur kinerja content-based filtering.
2. **RMSE**: Untuk collaborative filtering, nilai RMSE diperoleh sekitar **0.3528**, menunjukkan prediksi cukup akurat.

### Rekomendasi
- **Top 5 Buku yang Direkomendasikan**:
    - Seabiscuit: An American Legend
    - The Phantom Tollbooth
    - Cold Sassy Tree
    - Forbidden Magic
    - Attack Of The Deranged Mutant Killer Snow Goons

- **Bottom 5 Buku yang Direkomendasikan**:
    - Deception Point
    - The Plains of Passage
    - The Summons
    - Cold Mountain
    - Scarlet Feather

## Conclusion
Sistem rekomendasi buku ini berhasil memberikan rekomendasi yang relevan dengan kebutuhan pengguna. Evaluasi menggunakan precision, recall, F1-score, dan RMSE menunjukkan performa model yang sangat baik.
