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
- Jumlah ISBN Buku: 271,357
- Jumlah Judul Buku: 242,132
- Jumlah Penulis Buku: 102,022
- Jumlah Tahun Terbit Buku: 116
- Jumlah Penerbit Buku: 16,805
- 
Terlihat bahwa jumlah ISBN buku tidak sama dengan jumlah Judul Buku, menunjukkan adanya data yang hilang atau duplikat. Oleh karena itu, langkah cleaning akan dilakukan pada data ini.
   
**Ratings**

ada data Ratings, tidak ditemukan error atau missing values. Berikut adalah jumlah nilai unik pada setiap variabel:
- Jumlah User ID: 105,283
- Jumlah ISBN Buku: 340,556
  
Terdapat 105,283 pengguna yang memberikan penilaian terhadap 340,556 buku. Distribusi rating dapat dianalisis lebih lanjut untuk memahami pola penilaian pengguna.

![Distribusi Rating Buku](https://github.com/user-attachments/assets/e8020183-9a2c-451e-85a2-c19cec43974f)
    
**Users**

Berdasarkan informasi variabel pada data Users, ditemukan adanya missing value pada kolom Age. 
Jumlah total pengguna yang tercatat dalam data ini adalah 105.283. Berikut adalah distribusi usia pengguna yang tercatat:
    
![Distribusi Umur Pengguna](https://github.com/user-attachments/assets/47fdad0c-4eae-4117-96c5-a1d710e83417)

# Data Preparation
Persiapan data merupakan langkah penting dalam pengembangan model machine learning. Pada proyek ini, proses Data Preparation menjadi krusial untuk memastikan hasil analisis dan pemodelan yang akurat. Data yang tidak dipersiapkan dengan baik dapat memengaruhi kualitas model secara signifikan.
Berikut tahapan Data Preparation yang dilakukan pada proyek ini:

## Data Preparation untuk Content-Based Filtering
1. **Membersihkan Data pada Kolom Year-Of-Publication**
   - Menghapus data tidak valid pada kolom `Year-Of-Publication` dan mengonversinya menjadi tipe integer.
   - Code:
     ```python
     books['Year-Of-Publication'] = pd.to_numeric(books['Year-Of-Publication'], errors='coerce')
     books = books.dropna(subset=['Year-Of-Publication'])
     books['Year-Of-Publication'] = books['Year-Of-Publication'].astype(int)
     ```

2. **Menghapus Kolom yang Tidak Relevan**
   - Menghapus kolom `Image-URL-S`, `Image-URL-M`, dan `Image-URL-L` dari dataframe `books` karena tidak diperlukan untuk analisis atau pemodelan.
   - Code:
     ```python
     books = books.drop(columns=['Image-URL-S', 'Image-URL-M', 'Image-URL-L'])
     ```

3. **Membuat Dataframe dengan Kolom Penting**
   - Membuat dataframe baru `books_df` yang hanya berisi kolom `ISBN`, `Book-Rating`, `Title`, `Author`, `Year-Of-Publication`, dan `Publisher`.
   - Code:
     ```python
     books_df = books[['ISBN', 'Book-Rating', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]
     ```

## Data Preparation untuk Collaborative Filtering
1. **Encoding Data**
   - Mengonversi kolom `User-ID` dan `ISBN` menjadi angka terurut (encoding) untuk kompatibilitas dengan model machine learning.
   - Code:
     ```python
     from sklearn.preprocessing import LabelEncoder
     label_encoder = LabelEncoder()
     ratings['User-ID'] = label_encoder.fit_transform(ratings['User-ID'])
     ratings['ISBN'] = label_encoder.fit_transform(ratings['ISBN'])
     ```

2. **Menambah Kolom Hasil Encoding**
   - Menambahkan kolom hasil encoding `User-ID` dan `ISBN` ke dataframe utama.
   - Code:
     ```python
     df['User-ID-Encoded'] = ratings['User-ID']
     df['ISBN-Encoded'] = ratings['ISBN']
     ```

3. **Konversi Tipe Data Book-Rating**
   - Mengonversi kolom `Book-Rating` menjadi tipe `float32` untuk mempercepat proses pemodelan dan mengurangi penggunaan memori.
   - Code:
     ```python
     ratings['Book-Rating'] = ratings['Book-Rating'].astype('float32')
     ```

4. **Mengurutkan Data dan Mengonversi ke List**
   - Mengurutkan dataframe berdasarkan kolom tertentu untuk mempermudah pengolahan data.
   - Code:
     ```python
     fix_books = books.sort_values(by=['Year-Of-Publication']).reset_index(drop=True)
     fix_books_list = fix_books.values.tolist()
     ```

## Sampling Data
Dataset awal memiliki ukuran besar dengan beberapa atribut yang tidak relevan untuk sistem rekomendasi. Sampling dilakukan untuk mempercepat proses analisis dan pelatihan model, tanpa mengurangi kualitas data yang diperlukan, dapat menggunakan code berikut:

```python
sampled_books = books.sample(frac=0.1, random_state=42)
sampled_ratings = ratings[ratings['ISBN'].isin(sampled_books['ISBN'])]
```

## Intergration Data
Pada tahap ini menggabungkan data Books dan Ratings agar dapat digunakan dalam pemodelan nantinya. untuk melakukan penggabungan data, dapat menggunakan code berikut:

    ```python
    books_rating = ratings.merge(books, on='ISBN', how='left')
    ```
## Missing Value
Pada proses penggabung bisa saja terdapat missing value, sehingga perlu melakukan pengecekan agar tidak terjadi error nantinya dalam proses pemodelan. Pada DataFrame terdapat missing value berjumlah 118.648      pada variable Book-Title, Book-Author, Year-Of-Publication dan Publisher. Untuk mengatasi ini akan melakukan penghapusan pada data yang terdapat missing value dengan code berikut :

    ```python
    books_clean = books_rating.dropna()
    ```
Sebelumnya, terdapat rating yang bernilai 0, pada dasarnya rating tidak dimulai dari 0 melainkan dari satu. penyebab rating 0 bisa berbagai hal seperti pengguna tidak mengisi penilaian sehingga sistem akan memasukan nilai 0. untuk itu akan melakukan penghapusan juga pada data yang memiliki rating 0.

## Duplicated
Pada sebuah data bisa terdapat duplikat, karena dalam pemodelan ini hanya akan menggunakan data unik, sehingga akan melakukan pembersihan pada data yang duplikat, dengan code berikut:

    ```python
    preparation = books_clean.drop_duplicates('placeID')
    ```
## Ekstraksi Fitur dengan TF-IDF
Untuk pendekatan Content-Based Filtering, deskripsi buku diubah menjadi representasi numerik menggunakan TF-IDF, dapat menggunakan code berikut: 

    ```python
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(books_clean['Book-Title'])
    ```
## Encode Label
Beberapa atribut yang berbentuk kategori (seperti User-ID dan ISBN) diubah menjadi representasi numerik menggunakan encoding untuk memastikan kompatibilitas dengan algoritma machine learning, dengan code berikut :

    ```python
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    ratings['User-ID'] = label_encoder.fit_transform(ratings['User-ID'])
    ratings['ISBN'] = label_encoder.fit_transform(ratings['ISBN'])
    ```
## Split Data
Dataset dibagi menjadi training dan testing untuk mengevaluasi performa model, dengan code berikut :

    ```python
    from sklearn.model_selection import train_test_split
    train_data, test_data = train_test_split(ratings, test_size=0.2, random_state=42)
    ```
# Modelling and Result
Pada Modelling sistem rekomendasi akan menggunakan 2 pendeketan yaitu Metode Content Based Filtering dan Collaborative Filtering

## Content Based Filtering
### **Penjelasan**
Pendekatan ini menggunakan deskripsi atau atribut buku untuk membuat rekomendasi. Dalam sistem ini, representasi numerik buku dibuat menggunakan **TF-IDF** (Term Frequency-Inverse Document Frequency) untuk menangkap pentingnya kata-kata unik dalam deskripsi buku. Kemudian, digunakan **Cosine Similarity** untuk menghitung kemiripan antar buku.

- **Kelebihan**:
  1. Tidak memerlukan data pengguna lain, hanya data buku.
  2. Dapat merekomendasikan item baru dengan karakteristik serupa.
  3. Menghasilkan rekomendasi yang lebih terpersonalisasi.

- **Kekurangan**:
  1. Cenderung hanya merekomendasikan buku yang mirip dengan preferensi sebelumnya (serupa).
  2. Tidak mampu menangani perubahan selera pengguna.
  3. Tidak bisa memberikan rekomendasi jika data atribut buku tidak mencukupi.

#### **Cara Kerja Model**
1. **Ekstraksi Fitur Buku**:
   - Menggunakan **TF-IDF** untuk mengonversi judul atau deskripsi buku menjadi vektor numerik.
   - Contoh implementasi:
     ```python
     from sklearn.feature_extraction.text import TfidfVectorizer
     vectorizer = TfidfVectorizer(stop_words='english')
     tfidf_matrix = vectorizer.fit_transform(book_titles)
     ```
2. **Penghitungan Kemiripan**:
   - Menggunakan **Cosine Similarity** untuk menghitung derajat kemiripan antar buku.
     ```python
     from sklearn.metrics.pairwise import cosine_similarity
     cosine_sim = cosine_similarity(tfidf_matrix)
     ```

#### **Hasil Top-N Recommendation**
Berikut 5 buku teratas yang direkomendasikan untuk pengguna berdasarkan kemiripan dengan buku yang disukai:
| No | Judul Buku                             | Penulis          |
|----|----------------------------------------|------------------|
| 1  | The Partner                           | John Grisham     |
| 2  | Cliente, El                           | John Grisham     |
| 3  | The Runaway Jury                      | John Grisham     |
| 4  | The Street Lawyer                     | John Grisham     |
| 5  | Java Software Solutions               | John Lewis       |

---

## Cosine Similarity
Cosine similarity adalah metrik yang digunakan untuk mengukur sejauh mana dua vektor arah mendekati sejajar satu sama lain. Dalam sistem rekomendasi, cosine similarity digunakan untuk menentukan seberapa mirip dua item atau dua profil pengguna berdasarkan preferensi mereka terhadap fitur-fitur tertentu. Semakin tinggi nilai cosine similarity antara dua item, semakin mirip kedua item tersebut.
- Metode ini menghitung kemiripan antar buku berdasarkan vektor hasil TF-IDF.
- Implementasi:
      ```python
      from sklearn.metrics.pairwise import cosine_similarity
      cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
      ```
Rumus Cosine Similarity
![image](https://github.com/user-attachments/assets/9c8a0447-6cea-435b-b1db-27c93c0994fb)
Hasil dari perhitungan cosine similarity adalah nilai antara -1 dan 1. Nilai 1 menunjukkan bahwa dua vektor sepenuhnya sejajar (sama persis), nilai 0 menunjukkan bahwa vektor tersebut tegak lurus (tidak ada kesamaan), dan nilai -1 menunjukkan bahwa dua vektor sejajar tetapi berlawanan arah.
Pada penerepan Cosine Similarity dapat diakses dengan menggunakan sklearn dan memanggil fungsi cosine_similarity
Untuk memudahkan pengguna mendapatkan buku yang sesuai atau relavan dapat menggunakan pendekatan Content Based Filtering yang memberikan item (buku) yang sesuai berdasarkan kesukaan pengguna sebelumnya. Content Based Filtering mempelajari minat pengguna berdasarkan dari data objek yang disukai di masa lalu. Semakin banyak informasi yang diberikan pengguna, semakin baik akurasi sistem rekomendasi.

## Collaborative-Based Filtering
### **Penjelasan**
Pendekatan ini memanfaatkan data historis interaksi pengguna seperti rating untuk memberikan rekomendasi berdasarkan pola preferensi pengguna lain.

- **Kelebihan**:
  1. Tidak memerlukan informasi atribut buku.
  2. Dapat menangkap tren kolektif dari data interaksi pengguna.
  3. Mampu memberikan rekomendasi di luar preferensi langsung pengguna.

- **Kekurangan**:
  1. Sulit menangani pengguna atau buku baru (*cold-start problem*).
  2. Bergantung pada ketersediaan data interaksi.
  3. Rentan terhadap data sparsity (jumlah data yang minim).

#### **Cara Kerja Model**
1. **Matrix Factorization**:
   - Menggunakan pendekatan *latent factor* untuk memetakan hubungan antara pengguna dan buku.
   - Model melibatkan faktor tersembunyi yang menjelaskan preferensi pengguna.
   - Contoh:
     ```python
     from surprise import SVD
     from surprise.model_selection import cross_validate

     model = SVD()
     cross_validate(model, data, measures=['RMSE'], cv=5, verbose=True)
     ```
2. **Evaluasi dengan RMSE**:
   - Menghitung *Root Mean Squared Error* untuk mengevaluasi akurasi prediksi.
     ```python
     from sklearn.metrics import mean_squared_error
     rmse = np.sqrt(mean_squared_error(true_ratings, predicted_ratings))
     print(f'RMSE: {rmse}')
     ```

#### **Hasil Top-N Recommendation**
Berikut 5 buku teratas yang direkomendasikan:
| No | Judul Buku                             | Penulis          |
|----|----------------------------------------|------------------|
| 1  | Seabiscuit: An American Legend         | Laura Hillenbrand|
| 2  | The Phantom Tollbooth                  | Norton Juster    |
| 3  | Cold Sassy Tree                        | Olive Ann Burns  |
| 4  | Forbidden Magic                        | Cheyenne McCray  |
| 5  | Attack Of The Deranged Mutant Killer Snow Goons | Bill Watterson |

# Evaluation
Perhitungan akurasi rekomendasi dilakukan untuk mencari nilai error atau kesalahan dari sistem rekomendasi. Perhitungan ini dilakukan dengan membandingkan nilai prediksi dan nilai aktual yang diberikan pengguna untuk setiap pasangan pengguna dan item.

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


## Hasil Training Model 
|   |                                                                                              |                                                        |
|--:|---------------------------------------------------------------------------------------------:|-------------------------------------------------------:|
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step - loss: 0.1945 - root_mean_squared_error: 0.0643 -| val_loss: 0.6826 - val_root_mean_squared_error: 0.4080 |       
|   |                                                                                                                                          Epoch 91/100 |       
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 3s 3ms/step - loss: 0.1940 - root_mean_squared_error: 0.0643 -| val_loss: 0.6841 - val_root_mean_squared_error: 0.4081 |       
|   |                                                                                                                                          Epoch 92/100 |   
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step - loss: 0.1928 - root_mean_squared_error: 0.0625 -| val_loss: 0.6857 - val_root_mean_squared_error: 0.4082 |       
|   |                                                                                                                                          Epoch 93/100 |      
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step - loss: 0.1898 - root_mean_squared_error: 0.0618 -| val_loss: 0.6873 - val_root_mean_squared_error: 0.4084 |      
|   |                                                                                                                                          Epoch 94/100 | 
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 3s 2ms/step - loss: 0.1917 - root_mean_squared_error: 0.0618 -| val_loss: 0.6893 - val_root_mean_squared_error: 0.4086 |    
|   |                                                                                                                                          Epoch 95/100 | 
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step - loss: 0.1890 - root_mean_squared_error: 0.0619 -| val_loss: 0.6909 - val_root_mean_squared_error: 0.4087 |              
|   |                                                                                                                                          Epoch 96/100 |                 
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 3s 2ms/step - loss: 0.1892 - root_mean_squared_error: 0.0609 -| val_loss: 0.6929 - val_root_mean_squared_error: 0.4090 |             
|   |                                                                                                                                         Epoch 97/100  |             
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step - loss: 0.1930 - root_mean_squared_error: 0.0591 -| val_loss: 0.6946 - val_root_mean_squared_error: 0.4091 |               
|   |                                                                                                                                          Epoch 98/100 |                
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step - loss: 0.1864 - root_mean_squared_error: 0.0565 -| val_loss: 0.6968 - val_root_mean_squared_error: 0.4094 |                
|   |                                                                                                                                        Epoch 99/100   |                 
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 3s 2ms/step - loss: 0.1904 - root_mean_squared_error: 0.0574 -| val_loss: 0.6986 - val_root_mean_squared_error: 0.4095 |                 
|   |                                                                                                                                        Epoch 100/100  |                
|   | 1000/1000 ━━━━━━━━━━━━━━━━━━━━ 3s 2ms/step - loss: 0.1912 - root_mean_squared_error: 0.0556 -| val_loss: 0.7003 - val_root_mean_squared_error: 0.4096 |

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
    - 
## Content Based Filtering
Untuk mengukur seberapa bagus akurasi rekomendasi, disini menggunakan 3 evaluasi yaitu Precision, Recall dan F1-Score
- Precision Precision adalah perbandingan antara True Positive (TP) dengan banyaknya data yang diprediksi positif. rumus untuk Precision

![image](https://github.com/user-attachments/assets/a209055a-3345-42bc-ac1e-34e2ab48aa40)

- Recall Recall adalah perbandingan antara True Positive (TP) dengan banyaknya data yang sebenarnya positif. rumus untuk Recall

![image](https://github.com/user-attachments/assets/3fcaef35-4b1c-45eb-8967-b454744b474e)

- F1-Score F1-Score adalah harmonic mean dari precision dan recall. Nilai terbaik F1-Score adalah 1.0 dan nilai terburuknya adalah 0. Secara representasi, jika F1-Score punya skor yang baik mengindikasikan bahwa model klasifikasi k precision dan recall yang baik. rumus untuk F1-Score:

![image](https://github.com/user-attachments/assets/37dd5aca-9f76-4ade-a26e-bc1f4f87ed4e)



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

## Dampak terhadap Business Understanding
1. Menjawab Problem Statement
   - Model berhasil membantu pengguna menemukan buku baru yang belum pernah mereka baca sebelumnya.
   - Dengan rekomendasi berbasis kesamaan deskripsi, model juga mempersonalisasi pengalaman pengguna.
2. Mencapai Goals
   - Tujuan untuk meningkatkan eksplorasi pengguna terhadap kategori buku baru berhasil dicapai melalui pendekatan content-based filtering.
3. Dampak pada Solusi
   - Sistem rekomendasi ini memiliki potensi besar untuk meningkatkan kepuasan pengguna, memperluas eksposur buku, dan mendorong penjualan.
     
## Conclusion
Sistem rekomendasi buku ini berhasil memberikan rekomendasi yang relevan dengan kebutuhan pengguna. Evaluasi menggunakan precision, recall, F1-score, dan RMSE menunjukkan performa model yang sangat baik.


