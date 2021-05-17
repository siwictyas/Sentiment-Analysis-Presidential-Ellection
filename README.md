# Sentiment-Analysis-Presidential-Ellection

Pada penelitian ini dilakukan dengan memanfaatkan data tweet saat pemilu dengan menggunakan keyword berupa nama paslon 1 dan 2, topik debat yang sedang dibicarakan, dlsb. Untuk mendapatkan data di setiap pulau, penelitian ini melakukan scrapping data berdasarkan geocode (longitude, latitude) dari setiap provinsi. Dari data tersebut kemudian dilakukan pengelompokkan provinsi yang masuk ke dalam 1 pulau yang sama. Untuk selanjutnya data tersebut diolah untuk melakukan analisis sentimen yang kemudian dilakukan proses pemodelan topik di setiap sentimennya. Langkah proses pengerjaan pada penelitian ini adalah :
- Data Collection setiap provinsi
- Data Preprocessing
- Sentiment Analysis (perbandingan ML dan DL)
- Topic Modeling (LDA)
- Visualisasi (Django)
