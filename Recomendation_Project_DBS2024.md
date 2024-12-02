
# Recommendation Project DBS2024

# Overview
Buku adalah media penting untuk menyampaikan informasi, pengetahuan, hingga cerita. Di era digital saat ini, tersedia begitu banyak buku dan informasi dengan berbagai topik, sehingga membuat pembaca sering kesulitan memilih buku yang sesuai dengan minat mereka. Untuk mengatasi masalah ini, sistem rekomendasi hadir sebagai solusi, membantu memprediksi dan menyarankan item yang mungkin menarik bagi pengguna.

Sistem rekomendasi buku dirancang untuk mempermudah pengguna dalam menemukan buku yang sesuai dengan preferensi mereka. Selain itu, sistem ini juga dapat meningkatkan pengalaman pelanggan, memperluas eksposur buku, dan mendorong peningkatan penjualan. Sistem serupa telah diterapkan pada berbagai jenis produk, seperti film, musik, berita, dan lainnya.

Oleh karena itu, penerapan sistem rekomendasi buku memberikan banyak manfaat, baik bagi pembaca, industri buku, maupun masyarakat secara umum. Sistem ini membantu pembaca menemukan buku yang relevan, mendukung pertumbuhan bisnis buku, serta meningkatkan minat baca dan keingintahuan di masyarakat.

Model yang digunakan mencakup pendekatan Collaborative Filtering dan Content-Based Filtering.

## Business Understanding
Penerapan sistem rekomendasi buku dapat memberikan pengalaman yang lebih personal bagi pengguna, meningkatkan kepuasan pelanggan, dan mendorong eksplorasi buku di luar kategori populer. Sistem ini juga berpotensi memperluas penjualan melalui strategi cross-selling, membangun komunitas pembaca yang solid, serta meningkatkan akurasi rekomendasi melalui analisis data dan sentimen pengguna. Contohnya, Netflix menggunakan algoritma canggih untuk merekomendasikan film dan serial berdasarkan riwayat tontonan dan preferensi pengguna. Pendekatan ini berhasil meningkatkan keterlibatan pengguna sekaligus memperpanjang durasi pelanggan tetap menggunakan platform tersebut.

### Problem Statement
1. Bagaimana cara meningkatkan pengalaman pengguna dalam menemukan buku baru yang belum pernah dibaca sebelumnya?
2. Bagaimana cara mempersonalisasi rekomendasi buku untuk setiap pengguna berdasarkan preferensi dan riwayat bacaan mereka?
3. Bagaimana cara mengidentifikasi buku yang berpotensi diminati pengguna di luar kategori populer?

### Goals
1. Mengembangkan sistem rekomendasi yang dapat menyarankan buku baru secara akurat, bahkan jika pengguna belum pernah membaca buku terkait.
2. Meningkatkan personalisasi rekomendasi berdasarkan preferensi individu dan pola bacaan pengguna.
3. Memperluas eksplorasi pengguna dengan merekomendasikan buku di luar kategori atau genre populer.

### Solutions
1. Menggunakan Content-Based Filtering dengan metode TF-IDF untuk mengubah deskripsi buku menjadi representasi numerik, yang kemudian dihitung menggunakan Cosine Similarity untuk mencari buku yang mirip.
2. Memanfaatkan Collaborative Filtering dengan menggunakan user-item interactions dan matrix factorization untuk memberikan rekomendasi berdasarkan preferensi pengguna lainnya yang memiliki pola serupa.
3. Menggunakan Cosine Similarity untuk mencari buku-buku yang belum pernah dibaca oleh pengguna namun memiliki kesamaan dengan buku yang mereka minati, dan memberikan rekomendasi yang beragam dari berbagai kategori.

# Data Understanding
Dataset yang digunakan dalam proyek ini adalah [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data) yang dapat diakses melalui situs Kaggle. Dataset ini tidak mencakup genre buku, sehingga dalam proyek ini, rekomendasi akan didasarkan pada preferensi pengguna terhadap penulis buku.

Dataset ini terdiri dari tiga file utama:

- **Books**:
    Format: CSV (Comma Separated Value).
    Jumlah sampel: 271,360 data.
    Kolom: 8 variabel.
    Terdapat missing values pada beberapa kolom seperti Book-Title, Book-Author, dan Year-Of-Publication.
  
- **Ratings**:
    Format: CSV (Comma Separated Value).
    Jumlah sampel: 1,149,780 data.
    Kolom: 3 variabel.
    Tidak terdapat missing values pada file ini.
  
- **Users**:
    Format: CSV (Comma Separated Value).
    Jumlah sampel: 278,858 data.
    Kolom: 3 variabel.
    Tidak terdapat missing values pada file ini.

  **Informasi Variable**
  **Books**
  - ISBN : Kode Buku
  - Book-Title : Judul Buku
  - Book-Author: Penulis Buku
  - Year-Of-Publication  : Tahun Terbit Buku
  - Publisher : Penerbit Buku
  - Image-URL-S: Ukuran Kecil Gambar Buku
  - Image-URL-M : Ukuran Menengah Gambar Buku
  - Image-URL-L : Ukuran Besar Gambar Buku
  - 
  **Ratings**
  - Users-ID: Id pengguna
  - ISBN: Kode Buku
  - Book-Rating: Penilaian Buku
  - 
  **Users**
  - Users-ID: Id Pengguna
  - Location: Lokasi Pengguna
  - Age: Umur Pengguna
    
# Exploratory Data Analysis
 **Univariate Analysis**
 
**Books**
     Pada data Books, ditemukan tipe data yang tidak sesuai pada kolom Year-Of-Publication, sehingga perlu dilakukan konversi tipe data. Selain itu, kolom Image-URL-S, Image-URL-M, dan Image-URL-L akan dihapus        karena tidak relevan untuk pemodelan sistem rekomendasi. Berikut adalah jumlah nilai unik pada setiap variabel:
    - Jumlah ISBN Buku: 271,357
    - Jumlah Judul Buku: 242,132
    - Jumlah Penulis Buku: 102,022
    - Jumlah Tahun Terbit Buku: 116
    - Jumlah Penerbit Buku: 16,805
    Terlihat bahwa jumlah ISBN buku tidak sama dengan jumlah Judul Buku, menunjukkan adanya data yang hilang atau duplikat. Oleh karena itu, langkah cleaning akan dilakukan pada data ini.
    
**Ratings**
    ada data Ratings, tidak ditemukan error atau missing values. Berikut adalah jumlah nilai unik pada setiap variabel:
    - Jumlah User ID: 105,283
    - Jumlah ISBN Buku: 340,556
    Terdapat 105,283 pengguna yang memberikan penilaian terhadap 340,556 buku. Distribusi rating dapat dianalisis lebih lanjut untuk memahami pola penilaian pengguna.
    ![Distribusi Rating Buku](https://github.com/user-attachments/assets/e8020183-9a2c-451e-85a2-c19cec43974f)
    
**Users**
    Berdasarkan informasi variabel pada data Users, ditemukan adanya missing value pada kolom Age. Jumlah total pengguna yang tercatat dalam data ini adalah 105.283. Berikut adalah distribusi usia pengguna yang 
    tercatat:
    ![Distribusi Umur Pengguna](https://github.com/user-attachments/assets/47fdad0c-4eae-4117-96c5-a1d710e83417)

# Data Preparation
Persiapan data merupakan langkah penting dalam pengembangan model machine learning. Pada proyek ini, proses Data Preparation menjadi krusial untuk memastikan hasil analisis dan pemodelan yang akurat. Data yang tidak dipersiapkan dengan baik dapat memengaruhi kualitas model secara signifikan.
Berikut tahapan Data Preparation yang dilakukan pada proyek ini:
## Intergration Data
Pada tahap ini menggabungkan data Books dan Ratings agar dapat digunakan dalam pemodelan nantinya. untuk melakukan penggabungan data, dapat menggunakan code berikut:

    books_rating = ratings.merge(books, on='ISBN', how='left')

## Missing Value
Pada proses penggabung bisa saja terdapat missing value, sehingga perlu melakukan pengecekan agar tidak terjadi error nantinya dalam proses pemodelan. Pada DataFrame terdapat missing value berjumlah 118.648      pada variable Book-Title, Book-Author, Year-Of-Publication dan Publisher. Untuk mengatasi ini akan melakukan penghapusan pada data yang terdapat missing value dengan code berikut :

    books_clean = books_rating.dropna()
    
Sebelumnya, terdapat rating yang bernilai 0, pada dasarnya rating tidak dimulai dari 0 melainkan dari satu. penyebab rating 0 bisa berbagai hal seperti pengguna tidak mengisi penilaian sehingga sistem akan memasukan nilai 0. untuk itu akan melakukan penghapusan juga pada data yang memiliki rating 0.

## Duplicated
Pada sebuah data bisa terdapat duplikat, karena dalam pemodelan ini hanya akan menggunakan data unik, sehingga akan melakukan pembersihan pada data yang duplikat dengan code berikut:

    preparation = books_clean.drop_duplicates('placeID')

# Modelling and Result
Pada Modelling sistem rekomendasi akan menggunakan 2 pendeketan yaitu Metode Content Based Filtering dan Collaborative Filtering

## Content Based Filtering
Untuk memudahkan pengguna mendapatkan buku yang sesuai atau relavan dapat menggunakan pendekatan Content Based Filtering yang memberikan item (buku) yang sesuai berdasarkan kesukaan pengguna sebelumnya. Content Based Filtering mempelajari minat pengguna berdasarkan dari data objek yang disukai di masa lalu. Semakin banyak informasi yang diberikan pengguna, semakin baik akurasi sistem rekomendasi.
Berikut Kelebihan dan Kekurangan Content Based Filtering:

Kelebihan :
- Memberikan rekomendasi berdasarkan preferensi pengguna
- Tidak bergantung pada Data Eksternal, seperti item populer atau pengguna lain
- Dapat memberikan rekomendasi terhadap item baru

Kekurangan:
- Merekomendasikan item yang serupa
- Tidak Mampu Menangani Perubahan Selera Pengguna

## TF-IDF
Sebelum data digunakan untuk pemodelan, data perlu diubah terlebih dahulu kedalam bentuk numerik agar dapat digunakan sebagai masukan pada Model Machine Learning nantinya. Salah satu teknik yang akan digunakan pada proyek ini adalah TF-IDF (Term Frequency-Inverse Document Frequency).
TF-IDF bertujuan untuk mengukur seberapa penting suatu kata terhadap kata-kata lain dalam dokumen. TF-IDF adalah skema representasi yang umum digunakan untuk sistem pengambilan informasi dan ekstraksi dokumen yang relevan dengan kueri tertentu.
pada proyek ini TF-IDF dapat digunakan dengan cara memanggil fungsi TfidfVectorizer() pada sklearn.

## Cosine Similarity
Cosine similarity adalah metrik yang digunakan untuk mengukur sejauh mana dua vektor arah mendekati sejajar satu sama lain. Dalam sistem rekomendasi, cosine similarity digunakan untuk menentukan seberapa mirip dua item atau dua profil pengguna berdasarkan preferensi mereka terhadap fitur-fitur tertentu. Semakin tinggi nilai cosine similarity antara dua item, semakin mirip kedua item tersebut.

Rumus Cosine Similarity
![image](https://github.com/user-attachments/assets/9c8a0447-6cea-435b-b1db-27c93c0994fb)
Hasil dari perhitungan cosine similarity adalah nilai antara -1 dan 1. Nilai 1 menunjukkan bahwa dua vektor sepenuhnya sejajar (sama persis), nilai 0 menunjukkan bahwa vektor tersebut tegak lurus (tidak ada kesamaan), dan nilai -1 menunjukkan bahwa dua vektor sejajar tetapi berlawanan arah.

Pada penerepan Cosine Similarity dapat diakses dengan menggunakan sklearn dan memanggil fungsi cosine_similarity

Untuk memudahkan pengguna mendapatkan buku yang sesuai atau relavan dapat menggunakan pendekatan Content Based Filtering yang memberikan item (buku) yang sesuai berdasarkan kesukaan pengguna sebelumnya. Content Based Filtering mempelajari minat pengguna berdasarkan dari data objek yang disukai di masa lalu. Semakin banyak informasi yang diberikan pengguna, semakin baik akurasi sistem rekomendasi.

## Result
Berikut hasil 10 Top rekomendasi buku yang telah direkomendasikan berdasarkan sistem rekomendasi:

|   |                                             Title |          Author |   
|--:|--------------------------------------------------:|----------------:|
| 0 |                                       The Partner |    John Grisham |   
| 1 |                                       Cliente, El |    John Grisham |   
| 2 |                                  The Runaway Jury |    JOHN GRISHAM |   
| 3 |                                 The Street Lawyer |    John Grisham |  
| 4 |                                 The Unicorn Peace |        John Lee |  
| 5 | \15-1\": the Master Challenge (A Channel Four ... |      John Lewis |  
| 6 | Java Software Solutions : Foundations of Progr... |      John Lewis |   
| 7 | Crime Classification Manual : A Standard Syste... | John E. Douglas |   
| 8 |                           The Cases That Haunt Us |    John Douglas |   
| 9 | JOURNEY INTO DARKNESS (Lisa Drew Books (Paperb... | John E. Douglas |   

## Metrics
![Training & Validation RMSE over Epochs](https://github.com/user-attachments/assets/e7e9a4a5-5fa9-43f6-9a83-bcc01c8b35bb)
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


# Evaluation
Perhitungan akurasi rekomendasi dilakukan untuk mencari nilai error atau kesalahan dari sistem rekomendasi. Perhitungan ini dilakukan dengan membandingkan nilai prediksi dan nilai aktual yang diberikan pengguna untuk setiap pasangan pengguna dan item.
## Content Based Filtering
Pada Evaluasi hasil model, mendapatkan hasil sebagai berikut:
|   |                                            Metric |           Value | 
|--:|--------------------------------------------------:|----------------:|
| 0 |                                         Precision |        1.000000 |   
| 1 |                                            Recall |        1.000000 |   
| 2 |                                          F1-Score |        1.000000 |

## Collaborative Filtering
Perhitungan nilai akurasi rekomendasi dengan pendekatan Collaborative Filtering dilakukan dengan pendekatan Root Mean Square Error (RMSE). RMSE adalah ukuran perbedaan antara angka (nilai populasi dan sampel) yang sering diterapkan yang diprediksi oleh estimator atau mode. RMSE menggambarkan deviasi standar sampel dari perbedaan antara nilai prediksi dan nilai observasi.
![image](https://github.com/user-attachments/assets/1ac954c2-2579-4e0d-8dd6-e643cd8f756d)

Berikut hasil RMSE pada sistem rekomendasi:

    RMSE: 0.35289653979879504  

## Conclusion
Sistem rekomendasi buku ini berhasil memberikan rekomendasi yang relevan dengan kebutuhan pengguna. Evaluasi menggunakan precision, recall, F1-score, dan RMSE menunjukkan performa model yang sangat baik.
