# sentiment-analysis-module

Modul analisis sentimen yang dikembangkan dengan Python 3

Package yang dibutuhkan:

- tweepy
- nltk
- jupyter notebook/ anaconda

Database dikembangkan dengan SQLite 3



### Konfigurasi _file_ config.py

Untuk dapat menjalankan modul ini, silahkan buat _file_ config.py pada direktori proyek ini, lalu buatlah kode Python sebagai berikut

```python
api_public = '...' # API Key
api_private = '...' # API Key Secret
access_public = '...' # Access Token
access_private = '...' # Access Token Secret
```

Silahkan ganti tanda ... dengan kode API dan _Access Token_ akun _Twitter Developer_ Anda. Tetap gunakan tanda petik karena kode _Access Token_ dan API harus bertipe _string_.



### Pengaturan _Database_

Untuk memasukkan _database_, silahkan masukkan direktori database SQLite3 Anda pada variabel DATABASE_DIR main.py. 

_Database_ yang dapat digunakan pada proyek/ modul ini adalah yang memiliki struktur sebagai berikut:

![ERD](assets/erd.png)

Tersedia juga _file_ databaseInit.sql untuk membuat _database_ SQLite 3 kosong dengan struktur seperti gambar di atas. Silahkan eksekusi _file_ .sql tersebut dengan _DB browser_ (DBeaver, dll) atau dengan menggunakan terminal dengan perintah sebagai berikut (misal nama _database_ baru adalah "NewDatabase.db"):

Linux/ MacOS

```sqlite
sqlite3 NewDatabase.db ".read databaseInit.sql"
```

Windows

```sqlite
sqlite3.exe NewDatabase.db ".read databaseInit.sql"
```



