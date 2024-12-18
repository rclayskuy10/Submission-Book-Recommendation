# -*- coding: utf-8 -*-
"""Recommendation_Project_DBS2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z6B0f9XwxSS_hL6wRWRV0vtaSp361gxO

**Nama: Riski Pratama**

**DBS 2024 Machine Learning Advance**

#**1. Import Libraries**

### Penjelasan Cell

- **Tujuan**: [!pip install kaggle digunakan untuk menginstal library Kaggle di lingkungan Python].
"""

!pip install kaggle

"""### Penjelasan Cell

- **Tujuan**: [ini adalah langkah awal untuk memuat dan menggunakan berbagai pustaka (libraries) eksternal yang menyediakan fungsi dan kelas untuk mempermudah pengolahan data dan pengembangan model].
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path

"""#**2. Load and Prepare Dataset**

### Penjelasan Cell

- **Tujuan**: [Perintah ini digunakan untuk mengunggah file dari komputer lokal ke Google Colab].
"""

from google.colab import files
files.upload()

"""### Penjelasan Cell

- **Tujuan**: [Perintah-perintah ini digunakan untuk mengonfigurasi API Kaggle di lingkungan Google Colab].
"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

"""### Penjelasan Cell

- **Tujuan**: [Perintah ini digunakan untuk mengunduh dataset book-recommendation-dataset dari Kaggle].
"""

!kaggle datasets download -d arashnic/book-recommendation-dataset

"""### Penjelasan Cell

- **Tujuan**: [Perintah ini digunakan untuk mengekstrak file ZIP yang bernama book-recommendation-dataset.zip].
"""

!unzip book-recommendation-dataset.zip

"""### Penjelasan Cell

- **Tujuan**: [Perintah-perintah ini digunakan untuk membaca file CSV yang diekstrak sebelumnya dan memuatnya ke dalam DataFrame pandas].
"""

books = pd.read_csv('Books.csv')
ratings = pd.read_csv('Ratings.csv')
users = pd.read_csv('Users.csv')

"""### Penjelasan Cell

- **Tujuan**: [Perintah books.head() akan menampilkan lima baris pertama dari DataFrame books].
"""

books.head()

"""### Penjelasan Cell

- **Tujuan**: [Perintah ratings.head() akan menampilkan lima baris pertama dari DataFrame ratings].
"""

ratings.head()

"""### Penjelasan Cell

- **Tujuan**: [Perintah users.head() akan menampilkan lima baris pertama dari DataFrame users].
"""

users.head()

"""##**Exploratory Data Analysis**

###**Univariate**

### Penjelasan Cell

- **Tujuan**: [Perintah books.info() akan memberikan informasi ringkas tentang DataFrame books].
"""

books.info()

"""### Penjelasan Cell

- **Tujuan**: [Perintah ini adalah untuk membersihkan data dengan menghapus nilai yang tidak valid pada kolom Year-Of-Publication dan mengonversi kolom tersebut menjadi tipe data integer].
"""

books = books[~books['Year-Of-Publication'].isin(['DK Publishing Inc', 'Gallimard'])]
books['Year-Of-Publication'] = books['Year-Of-Publication'].astype(int)
books.info()

"""### Penjelasan Cell

- **Tujuan**: [Menghapus kolom Image-URL-S, Image-URL-M, dan Image-URL-L dari DataFrame books, karena dianggap tidak diperlukan untuk analisis].
"""

books.drop(columns=['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], inplace=True)

"""### Penjelasan Cell

- **Tujuan**: [Menghitung dan menampilkan jumlah unik untuk setiap atribut buku, seperti ISBN, judul, penulis, tahun terbit, dan penerbit, untuk memahami distribusi data].
"""

print(f"Jumlah ISBN Buku: {books['ISBN'].nunique()}")
print(f"Jumlah Judul Buku: {books['Book-Title'].nunique()}")
print(f"Jumlah Penulis Buku: {books['Book-Author'].nunique()}")
print(f"Jumlah Tahun Terbit Buku: {books['Year-Of-Publication'].nunique()}")
print(f"Jumlah Penerbit Buku: {books['Publisher'].nunique()}")

"""### Penjelasan Cell

- **Tujuan**: [Perintah ratings.info() adalah untuk menampilkan informasi struktur DataFrame ratings].
"""

ratings.info()

"""### Penjelasan Cell

- **Tujuan**: [Menghitung dan menampilkan jumlah unik User ID dan ISBN buku dalam dataset ratings untuk memahami cakupan data pengguna dan buku yang dinilai].
"""

print(f"Jumlah User ID: {ratings['User-ID'].nunique()}")
print(f"Jumlah ISBN Buku: {ratings['ISBN'].nunique()}")

"""### Penjelasan Cell

- **Tujuan**: [Membuat visualisasi distribusi rating buku menggunakan histogram dengan Seaborn, sehingga memudahkan analisis pola dan frekuensi rating yang diberikan].
"""

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(ratings['Book-Rating'], bins=10, kde=True, color='skyblue')
plt.title("Distribusi Rating Buku", fontsize=14)
plt.xlabel("Rating", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.show()

"""### Penjelasan Cell

- **Tujuan**: [Menampilkan informasi struktur DataFrame users].
"""

users.info()

"""### Penjelasan Cell

- **Tujuan**: [Menghitung jumlah unik User ID dan memvisualisasikan distribusi umur pengguna untuk memahami pola data pengguna].
"""

# Menampilkan jumlah User ID dengan format rapi
print(f"Jumlah User ID: {ratings['User-ID'].nunique():,}\n")

# Visualisasi distribusi umur
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(users['Age'], bins=20, kde=True, color='coral')
plt.title("Distribusi Umur Pengguna", fontsize=14)
plt.xlabel("Umur", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

"""#**3.Data Preparation**

### Penjelasan Cell

- **Tujuan**: [Menghitung jumlah unik User ID dan memvisualisasikan distribusi umur pengguna untuk memahami pola data pengguna].
"""

books_rating = ratings.merge(books, on='ISBN', how='left')
books_rating.head()

"""### Penjelasan Cell

- **Tujuan**: [Menghitung jumlah nilai yang hilang (missing values) di setiap kolom DataFrame books_rating untuk memeriksa kelengkapan data setelah penggabungan].
"""

books_rating.isna().sum()

"""### Penjelasan Cell

- **Tujuan**: [ menghapus baris dengan nilai hilang dari books_rating, memeriksa nilai hilang setelah pembersihan, dan menampilkan dimensi dataset yang bersih].
"""

books_clean = books_rating.dropna()
books_clean.isna().sum()
books_clean.shape

"""### Penjelasan Cell

- **Tujuan**: [Menghapus baris dengan rating 0 dari DataFrame books_clean dan kemudian menampilkan dimensi (jumlah baris dan kolom) dataset yang sudah difilter].
"""

books_clean = books_clean[(books_clean['Book-Rating'] != 0)]
books_clean.shape

"""### Penjelasan Cell

- **Tujuan**: [Menghapus baris duplikat berdasarkan kolom ISBN di DataFrame books_clean, menghasilkan DataFrame baru fix_books yang hanya berisi satu entri per buku].
"""

fix_books = books_clean.drop_duplicates('ISBN')

"""### Penjelasan Cell

- **Tujuan**: [Mengonversi kolom Year-Of-Publication menjadi tipe data integer di DataFrame fix_books, dan kemudian menampilkan informasi tentang struktur dataset setelah konversi menggunakan info()].
"""

fix_books['Year-Of-Publication'] = fix_books['Year-Of-Publication'].astype(int)
fix_books.info()

"""### Penjelasan Cell

- **Tujuan**: [Mengurutkan fix_books berdasarkan ISBN, mengonversi kolom-kolom menjadi list, dan memverifikasi jumlah elemen dalam setiap list].
"""

preparation = fix_books
preparation.sort_values('ISBN')

isbn = preparation['ISBN'].tolist()
title = preparation['Book-Title'].tolist()
rating = preparation['Book-Rating'].tolist()
author = preparation['Book-Author'].tolist()
publication = preparation['Year-Of-Publication'].tolist()
publisher = preparation['Publisher'].tolist()

print(len(isbn))
print(len(title))
print(len(rating))
print(len(author))
print(len(publication))
print(len(publisher))

"""Jumlah datanya sama karena setiap kolom berasal dari DataFrame yang sama (fix_books) dan memiliki jumlah baris yang konsisten. Saat diubah menjadi list menggunakan tolist(), setiap kolom tetap mempertahankan jumlah elemen sesuai dengan jumlah baris dalam DataFrame.

### Penjelasan Cell

- **Tujuan**: [Membuat DataFrame baru books_df dari list yang telah disiapkan, dengan kolom-kolom yang berisi informasi buku seperti ISBN, Rating, Title, Author, Publication, dan Publisher].
"""

books_df = pd.DataFrame({
    'ISBN': isbn,
    'Rating': rating,
    'Title': title,
    'Author': author,
    'Publication': publication,
    'Publisher': publisher
})

"""### Penjelasan Cell

- **Tujuan**: [Menampilkan lima baris pertama dari DataFrame books_df, memberikan gambaran umum tentang struktur dan isi data yang telah disusun].
"""

books_df.head()

"""### Penjelasan Cell

- **Tujuan**: [Mengambil 10000 sampel acak dari DataFrame books_df dan menyimpannya dalam books_sample, dengan menggunakan random_state=123 untuk memastikan hasil yang konsisten setiap kali kode dijalankan].
"""

books_sample = books_df.sample(n=10000, random_state=123)

"""#**4. Model Development**

### Penjelasan Cell

- **Tujuan**: [menampilkan 5 sampel acak dari DataFrame data (yang berisi books_sample)].
"""

data = books_sample
data.sample(5)

"""### Penjelasan Cell

- **Tujuan**: [Membuat dan melatih model TF-IDF (Term Frequency-Inverse Document Frequency) pada kolom Author dari DataFrame data, yang digunakan untuk mengubah teks nama penulis menjadi representasi numerik berbasis frekuensi kata yang penting dalam teks tersebut].
"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfid = TfidfVectorizer()
tfid.fit(data['Author'])

"""### Penjelasan Cell

- **Tujuan**: [Mengonversi kolom Author menjadi matriks TF-IDF menggunakan fit_transform(), dan kemudian memeriksa ukuran matriks TF-IDF dengan shape untuk mengetahui dimensi hasil transformasi, yaitu jumlah baris dan kolom dalam matriks tersebut].
"""

tfidf_matrix = tfid.fit_transform(data['Author'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""### Penjelasan Cell

- **Tujuan**: [mengonversi matriks TF-IDF yang berbentuk sparse menjadi DataFrame yang padat (dense), dengan kolom yang mewakili fitur (kata-kata unik) dan indeks yang mewakili judul buku. Kemudian, kode ini menampilkan 22 kolom acak dan 10 baris acak dari DataFrame tersebut untuk melihat representasi TF-IDF dari buku-buku yang dipilih].
"""

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tfid.get_feature_names_out(),
    index=data.Title
).sample(22, axis=1).sample(10, axis=0)

"""### Penjelasan Cell

- **Tujuan**: [Menghitung kemiripan kosinus antara setiap pasangan buku berdasarkan representasi TF-IDF dari kolom Author. Hasilnya adalah matriks kemiripan kosinus yang menunjukkan seberapa mirip satu buku dengan buku lainnya berdasarkan penulisnya].
"""

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""### Penjelasan Cell

- **Tujuan**: [Membuat matriks kemiripan kosinus antara buku, memeriksa dimensinya, dan menampilkan sebagian acak dari matriks tersebut].
"""

cosine_sim_df = pd.DataFrame(cosine_sim, index=data['Title'], columns=data['Title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""### Penjelasan Cell

- **Tujuan**: [Mendefinisikan fungsi book_recommendations yang memberikan rekomendasi buku berdasarkan kemiripan dengan buku yang diberikan (title), menggunakan matriks kemiripan (similarity_data). Fungsi ini mengembalikan daftar buku terdekat dengan buku yang dipilih, dengan jumlah rekomendasi sebanyak k].
"""

def book_recommendations(title, similarity_data=cosine_sim_df, items=data[['Title', 'Author']], k=10):
    index = similarity_data.loc[:,title].to_numpy().argpartition(
        range(-1, -k, -1))
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(title, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)

"""### Penjelasan Cell

- **Tujuan**: [Menampilkan 10 sampel acak dari kolom Title pada DataFrame data].
"""

data.Title.sample(10)

"""### Penjelasan Cell

- **Tujuan**: [Mencari dan menampilkan baris dalam DataFrame data yang memiliki judul buku "The Chamber". Fungsi eq() digunakan untuk mencocokkan nilai yang tepat di kolom Title].
"""

data[data.Title.eq("The Chamber")]

"""### Penjelasan Cell

- **Tujuan**: [Mendapatkan rekomendasi buku yang mirip dengan "Harry Potter" menggunakan fungsi book_recommendations].
"""

book_recommendations('The Chamber')

"""### Penjelasan Cell

- **Tujuan**: [mengambil 10000 sampel acak dari DataFrame ratings, mengacak data, dan kemudian mereset indeksnya dengan reset_index()].
"""

ratings_sample = ratings.sample(n=10000, random_state=123).reset_index()

"""### Penjelasan Cell

- **Tujuan**: [menampilkan 5 baris pertama dari DataFrame df (yang berisi sampel acak dari ratings_sample)].
"""

df = ratings_sample
df.head()

"""### Penjelasan Cell

- **Tujuan**: [Mengonversi User-ID menjadi angka terurut (encoding) dan sebaliknya, agar bisa digunakan dalam analisis atau model].
"""

user_ids = df['User-ID'].unique().tolist()
print('list userID: ', user_ids)

user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded User-ID : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke user-ID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke UserID: ', user_encoded_to_user)

"""### Penjelasan Cell

- **Tujuan**: [Mengonversi ISBN menjadi angka terurut (encoding) dan sebaliknya, agar bisa digunakan dalam analisis atau model].
"""

# Mengubah ISBN menjadi list tanpa nilai yang sama
books_ids = df['ISBN'].unique().tolist()

# Melakukan proses encoding ISBN
book_to_book_encoded = {x: i for i, x in enumerate(books_ids)}

# Melakukan proses encoding angka ke ISBN
book_encoded_to_book = {i: x for i, x in enumerate(books_ids)}

"""### Penjelasan Cell

- **Tujuan**: [Menambahkan kolom hasil encoding User-ID dan ISBN ke DataFrame df].
"""

# Mapping kedalam variable baru
df['user'] = df['User-ID'].map(user_to_user_encoded)
df['ISBN-Book'] = df['ISBN'].map(book_to_book_encoded)

"""### Penjelasan Cell

- **Tujuan**: [menghitung jumlah pengguna, buku, rentang rating, dan mengonversi Book-Rating ke tipe float32].
"""

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah resto
num_books = len(book_encoded_to_book)
print(num_books)

df['Book-Rating'] = df['Book-Rating'].values.astype(np.float32)

# Nilai minimum Book-Rating
min_rating = min(df['Book-Rating'])

# Nilai maksimal Book-Rating
max_rating = max(df['Book-Rating'])

print('Number of User: {}, Number of Resto: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_books, min_rating, max_rating
))

"""### Penjelasan Cell

- **Tujuan**: [Mengacak urutan data dalam DataFrame df untuk menghilangkan bias urutan dengan menggunakan sample(frac=1)].
"""

# Mengacak dataset
df = df.sample(frac=1, random_state=42)
df

"""### Penjelasan Cell

- **Tujuan**: [Membuat fitur (x), label (y), lalu membagi data menjadi 80% pelatihan dan 20% validasi].
"""

# Membuat variabel x untuk mencocokkan data user dan resto menjadi satu value
x = df[['user', 'ISBN-Book']].values

# Membuat variabel y untuk membuat rating dari hasil
y = df['Book-Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""### Penjelasan Cell

- **Tujuan**: [membuat model rekomendasi buku berbasis embedding untuk memprediksi interaksi pengguna-buku menggunakan dot product dan sigmoid].
"""

class BookRecommender(tf.keras.Model):

  # Inisialisasi fungsi
  def __init__(self, num_users, num_books, embedding_dim, **kwargs):
    super(BookRecommender, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_books = num_books
    self.embedding_dim = embedding_dim
    self.user_embedding_layer = layers.Embedding(  # embedding untuk pengguna
        num_users,
        embedding_dim,
        embeddings_initializer='he_normal',
        embeddings_regularizer=keras.regularizers.l2(1e-6)
    )
    self.user_bias_layer = layers.Embedding(num_users, 1)  # embedding bias pengguna
    self.book_embedding_layer = layers.Embedding(  # embedding untuk buku
        num_books,
        embedding_dim,
        embeddings_initializer='he_normal',
        embeddings_regularizer=keras.regularizers.l2(1e-6)
    )
    self.book_bias_layer = layers.Embedding(num_books, 1)  # embedding bias buku

  def call(self, inputs):
    user_embedded = self.user_embedding_layer(inputs[:, 0])  # mengambil embedding pengguna
    user_bias = self.user_bias_layer(inputs[:, 0])  # mengambil bias pengguna
    book_embedded = self.book_embedding_layer(inputs[:, 1])  # mengambil embedding buku
    book_bias = self.book_bias_layer(inputs[:, 1])  # mengambil bias buku

    # Menghitung hasil perkalian dot produk antara vektor pengguna dan buku
    interaction = tf.tensordot(user_embedded, book_embedded, axes=2)

    # Menambahkan bias dan hasil interaksi
    result = interaction + user_bias + book_bias

    return tf.nn.sigmoid(result)  # fungsi aktivasi sigmoid

"""### Penjelasan Cell

- **Tujuan**: [Meng-compile model BookRecommender dengan loss Binary Crossentropy, optimizer Adam, dan metric RMSE].
"""

model = BookRecommender(num_users, num_books, 50)

model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""### Penjelasan Cell

- **Tujuan**: [Melatih model BookRecommender dengan data pelatihan (x_train, y_train) selama 100 epoch, menggunakan batch size 8, dan memvalidasi model pada data validasi (x_val, y_val)].
"""

history = model.fit(
    x=x_train,
    y=y_train,
    batch_size=8,
    epochs=100,
    validation_data=(x_val, y_val),
    verbose=1
)

"""### Penjelasan Cell

- **Tujuan**: [Memvisualisasikan perubahan RMSE (Root Mean Squared Error) selama proses pelatihan dan validasi model, dengan menampilkan grafik untuk Train RMSE dan Validation RMSE sepanjang epoch].
"""

plt.figure(figsize=(10, 6))
plt.plot(history.history['root_mean_squared_error'], label='Train RMSE', color='b', linewidth=2)
plt.plot(history.history['val_root_mean_squared_error'], label='Validation RMSE', color='r', linewidth=2, linestyle='--')
plt.title('Training and Validation RMSE over Epochs', fontsize=16)
plt.xlabel('Epoch', fontsize=14)
plt.ylabel('Root Mean Squared Error (RMSE)', fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

"""### Penjelasan Cell

- **Tujuan**: [mengidentifikasi buku yang belum dibaca oleh pengguna dan membuat array pasangan pengguna dengan buku tersebut untuk rekomendasi].
"""

books_df = books
df_ratings = ratings_sample

# mengambil sample user
user_id = df_ratings['User-ID'].sample(1).iloc[0]
book_read_by_user = df_ratings[df_ratings['User-ID'] == user_id]


book_no_read = books_df[~books_df['ISBN'].isin(book_read_by_user['User-ID'].values)]['ISBN']
book_no_read = list(
    set(book_no_read)
    .intersection(set(book_to_book_encoded.keys()))
)

book_no_read = [[book_to_book_encoded.get(x)] for x in book_no_read]
user_encoder = user_to_user_encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(book_no_read), book_no_read)
)

"""### Penjelasan Cell

- **Tujuan**: [Menampilkan 5 buku teratas dan terbawah yang direkomendasikan model, serta menampilkan 5 buku yang sudah dibaca pengguna].
"""

user_ratings = model.predict(user_book_array).flatten()

# Menyortir rating dan mendapatkan 5 teratas dan 5 terbawah
top_rated_indices = user_ratings.argsort()[-5:][::-1]  # 5 teratas
bottom_rated_indices = user_ratings.argsort()[:5]  # 5 terbawah

recommended_books_ids_top = [
    book_encoded_to_book.get(book_no_read[i][0]) for i in top_rated_indices
]

recommended_books_ids_bottom = [
    book_encoded_to_book.get(book_no_read[i][0]) for i in bottom_rated_indices
]

# Menampilkan rekomendasi untuk pengguna
print(f"Showing recommendations for user: {user_id}")
print("=" * 30)
print("Books rated highly by user:")
print("-" * 32)

# Mendapatkan 5 buku teratas yang sudah dibaca oleh pengguna
top_rated_books_by_user = (
    book_read_by_user.sort_values(by='Book-Rating', ascending=False)
    .head(5)
    .ISBN.values
)

# Menampilkan informasi buku yang sudah dibaca
user_books_df = books_df[books_df['ISBN'].isin(top_rated_books_by_user)]
for row in user_books_df.itertuples():
    print(f"{row._2}: {row._3}")

print("-" * 32)
print("Top 5 Book Recommendations:")
print("-" * 32)

# Menampilkan rekomendasi buku yang diprediksi (5 teratas)
recommended_books_df_top = books_df[books_df['ISBN'].isin(recommended_books_ids_top)]
for row in recommended_books_df_top.itertuples():
    print(f"{row._2}: {row._3}")

print("-" * 32)
print("Bottom 5 Book Recommendations:")
print("-" * 32)

# Menampilkan rekomendasi buku yang diprediksi (5 terbawah)
recommended_books_df_bottom = books_df[books_df['ISBN'].isin(recommended_books_ids_bottom)]
for row in recommended_books_df_bottom.itertuples():
    print(f"{row._2}: {row._3}")

"""#**5.Model Evaluation**

### Penjelasan Cell

- **Tujuan**: [Membuat rekomendasi buku dan menghitung metrik evaluasi (precision, recall, F1-score) berdasarkan cosine similarity antara buku-buku].
"""

from sklearn.metrics import precision_score, recall_score, f1_score


# menentukan batasan similarity 1 atau 0
threshold = 0.5

# rekomendasi berdasarkan judul
true_title = 'The Chamber'
predicted_books = book_recommendations(true_title, similarity_data=cosine_sim_df, items=data[['Title', 'Author']], k=10)

#  Menyusun data label_truth dengan asumsi threshold
label_truth = np.where(cosine_sim_df >= threshold, 1, 0)

# Mengambil subset dari matriks similarity dan label_truth
sample_size = 10000
cosine_sim_sample = cosine_sim_df.iloc[:sample_size, :sample_size]
label_truth_sample = label_truth[:sample_size, :sample_size]

# Mengonversi matriks similarity menjadi array satu dimensi untuk perbandingan
cosine_sim_flat = cosine_sim_sample.values.flatten()

# Mengonversi matriks label_truth menjadi array satu dimensi
label_truth_flat = label_truth_sample.flatten()

# Menghitung metrik evaluasi
precision = precision_score(label_truth_flat, (cosine_sim_flat >= threshold).astype(int), zero_division=1)
recall = recall_score(label_truth_flat, (cosine_sim_flat >= threshold).astype(int), zero_division=1)
f1 = f1_score(label_truth_flat, (cosine_sim_flat >= threshold).astype(int), zero_division=1)

evaluation_result = pd.DataFrame({
    'Metric': ['Precision', 'Recall', 'F1-Score'],
    'Value': [precision, recall, f1]
})

"""### Penjelasan Cell

- **Tujuan**: [Evaluation_result adalah sebuah DataFrame yang berisi hasil evaluasi dari sistem rekomendasi buku, dengan metrik Precision, Recall, dan F1-Score. ].
"""

evaluation_result.style \
    .background_gradient(cmap='Blues') \
    .set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#4CAF50'), ('color', 'white')]
    }, {
        'selector': 'td',
        'props': [('font-size', '14px'), ('padding', '10px')]
    }]) \
    .hide(axis="index")

"""### Penjelasan Cell

- **Tujuan**: [Menghitung RMSE untuk mengevaluasi prediksi rating buku oleh model, dengan membandingkan rating yang diprediksi dan yang sebenarnya. Semakin rendah RMSE, semakin akurat model].
"""

from sklearn.metrics import mean_squared_error

# Prediksi rating untuk buku yang tidak dibaca oleh user
predicted_ratings = model.predict(user_book_array).flatten()

# Gabungkan recommended_books_ids_top dan recommended_books_ids_bottom
# untuk mendapatkan semua buku yang direkomendasikan
recommended_book_ids = recommended_books_ids_top + recommended_books_ids_bottom

# Ambil rating sebenarnya untuk buku yang tidak dibaca oleh user
true_ratings = np.array([
    df_ratings[
        (df_ratings['User-ID'] == user_id) &
        (df_ratings['ISBN'] == book_encoded_to_book.get(book_id))
    ]['Book-Rating'].values[0]
    if not df_ratings[
        (df_ratings['User-ID'] == user_id) &
        (df_ratings['ISBN'] == book_encoded_to_book.get(book_id))
    ].empty
    else 0  # Atau nilai default sesuai kebutuhan Anda
    for book_id in recommended_book_ids
])

# Pastikan panjang true_ratings dan predicted_ratings sama
min_len = min(len(true_ratings), len(predicted_ratings))
true_ratings = true_ratings[:min_len]
predicted_ratings = predicted_ratings[:min_len]

# Hitung RMSE
rmse = np.sqrt(mean_squared_error(true_ratings, predicted_ratings))

print(f'RMSE: {rmse}')