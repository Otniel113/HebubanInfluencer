# HebubanInfluencer
Mencari influencer user di Twitter menggunakan metode Centrality Eigenvector dengan topik game Heaven Burns Red yang dilakukan bersama dengan Made Indrayana Putra.

## File
1. 01.CrawlingHebuban.py => Untuk melakukan crawling twitter

```Perlu diperhatikan untuk Bearer Token harap diisi dengan Bearer Token sendiri yang didapatkan jika memiliki akun Twitter Developer.```

2. 02.ModelHebuban.ipynb => Untuk analisis hasil crawling

## Abstrak
Di era sekarang, orang-orang dapat dengan mudah berinteraksi satu dengan yang lain menggunakan media sosial tanpa ada batasan tempat. Salah satu media sosial yang cukup populer adalah Twitter. Ada banyak cuitan <i>tweet</i> di Twitter dari berbagai pengguna khususnya pada suatu topik tertentu. Terdapat pengguna yang memiliki pengaruh <i>influential user</i> terhadap topik-topik tersebut. Pencarian pengguna tersebut penting karena mempengaruhi terkenalnya suatu topik dan juga dapat mempengaruhi orang lain dalam pembahasan topik tersebut. Salah satu topik yang dibahas adalah di bidang game, secara spesifik Heaven Burns Red dengan genre gabungan Visual Novel dan Turn-Based RPG. Game ini cukup terkenal, khususnya di Jepang karena pernah berada di peringkat 1 App Store. Dalam penelitian ini telah dibangun analisis jejaring sosial berbentuk graf dan mencari influential user tersebut dengan menggunakan metode Eigenvector Centrality. Hasil akhir yang didapatkan adalah username dari 11 <i>influence user</i>.

<b>Kata kunci:</b> influential user, heaven burns red, eigenvector centrality

## Tujuan
Tujuan dalam penelitian ini adalah membangun model jejaring sosial pada topik game Heaven Burns Red dan menemukan influential users (pengguna berpengaruh) dalam
topik Heaven Burns Red menggunakan metode Eigenvector Centrality.

## Dataset
Dataset didapatkan dengan melakukan metode crawling pada media sosial Twitter bertopik games Heaven Burns Red dengan menggunakan <i>hashtag</i> #ヘブバン. Tweet yang diambil sebanyak 15000 tweet terbaru dari tanggal 7 April 2022. Banyak data akhir yang berhasil dikumpulkan adalah 14853 karena data yang bernilai error tidak dimasukan ke dalam dataset.

## Hasil
1. Spesifikasi Graf

| Parameter | Nilai |
| -- | -- |
| Banyak node | 4367 |
| Banyak edge | 7112 |
| Berarah | Tidak |
| Berbobot | Tidak |
| Multiedge | Tidak |
| Loop | Tidak |
| Jenis graf | Simple graph |

2. Graf Jejaring Sosial
![Gambar1 (1)](https://user-images.githubusercontent.com/57952404/167336964-cd44ba7f-5dee-456f-a974-976576ec79d9.png)

3. Sebelas Influence User

| Username | Nilai Eigenvector |
| -- | -- |
| [heavenburnsred](https://twitter.com/heavenburnsred) | 0,699312 |
| [Yuugen_99](https://twitter.com/Yuugen_99)	| 0,040409 |
| [ndjiru_n](https://twitter.com/ndjiru_n) | 0,040397 |
| [092596Tk](https://twitter.com/092596Tk) | 0,038065 |
| [Tatika081](https://twitter.com/Tatika081) | 0,029662 |
| [KegurunekuR33](https://twitter.com/KegurunekuR33) | 0,028999 |
| [game_tori10](https://twitter.com/game_tori10) | 0,028088 |
| [ogayan0301](https://twitter.com/ogayan0301) | 0,026894 |
| [kegani_0207](https://twitter.com/ndjiru_n) | 0,026858 |
| [DIVAvivylove1](https://twitter.com/ndjiru_n) | 0,026283 |
| [sera050520](https://twitter.com/ndjiru_n)	| 0.025813 |

## Kesimpulan dan Saran
1. Kesimpulan
Berdasarkan hasil penelitian yang dilakukan, dapat disimpulkan bahwa telah berhasil dibangun model jejaring sosial berdasarkan tweet dengan menggunakan graf berjenis simple graph yang memiliki banyak node 4367 dan banyak edge 7112, serta telah didapatkan 11 influence user dengan menggunakan Eigenvector Centrality dengan user berupa official account, fans, pemain, dan juga seniman.

2. Saran
Penelitian ini masih memiliki keterbatasan seperti jenis media sosial adalah Twitter dengan topik game Heaven Burns Red, dan menggunakan metode Centrality Eigenvector, saran untuk penelitian selanjutnya adalah dengan melakukan penelitian dengan media sosial yang lain seperti Facebook atau Instagram, menggunakan topik yang berbeda baik masih di bidang game ataupun tidak, dan menggunakan metode Centrality yang berbeda seperti Degree dan Betweenness.

## Sitasi
Jika ingin menggunakan program ini lagi, khususnya pada algoritma crawling file 01.CrawlingHebuban.py, dapat diganti 4 parameter yaitu : Bearer Token, Query, Max Result, Limit

![image](https://user-images.githubusercontent.com/57952404/167337728-24a27ae0-e1ac-4117-a5fd-5c35d5bc8a80.png)

Dan dapat melakukan sitasi dengan informasi sebagai berikut:
```
Author : Otniel Abiezer, Made Indrayana Putra
Date : April 2022
Title : HebubanInfluencer
URL : https://github.com/Otniel113/HebubanInfluencer
```

## Laporan
Untuk laporan lengkap dapat dilihat pada https://www.overleaf.com/read/trgsdmqcrqpw
