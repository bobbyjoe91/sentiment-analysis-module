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