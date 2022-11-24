# Tugas Besar IF2124 Teori Bahasa Formal dan Otomata: Program Parser Bahasa JavaScript dengan Python

## Daftar Isi
- [Deskripsi Singkat](#deskripsi-singkat)
- [Anggota Kelompok](#anggota-kelompok)
- [Cara Menjalankan Program](#cara-menjalankan-program)

## Deskripsi Singkat
Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat pemeriksaan sintaks bahasa atau parsing yang dibuat oleh programmer untuk memastikan program dapat dieksekusi tanpa menghasilkan error. Parsing ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai dilakukan.
Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan parsing. Sudah sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler dengan performa yang tinggi. Terdapat CFG, CNF-e, CNF+e, 2NF, 2LF, dll untuk grammar yang dapat digunakan, dan terdapat LL(0), LL(1), CYK, Earley’s Algorithm, LALR, GLR, Shift-reduce, SLR, LR(1), dll untuk algoritma yang dapat digunakan untuk melakukan parsing.
Pada tugas besar ini, implementasikan parser untuk JavaScript (Node.js) untuk beberapa statement dan sintaks bawaan JavaScript. Gunakanlah konsep CFG untuk pengerjaan parser yang mengevaluasi syntax program. Untuk nama variabel dan operasi (+, -, >, dll) dalam program, gunakanlah FA.
(Dikutip dari [Spesifikasi Tugas Pemrograman IF2124 Teori Bahasa Formal dan Otomata](https://docs.google.com/document/d/1JodthYhXxtxvxZXdkrC29XP6AzYEQSi7ll9z_fTseA0/edit#))

## Anggota Kelompok
1. Arleen Chrysantha Gunardi (13521059)
2. Margaretha Olivia Haryono (13521071)
3. Austin Gabriel Pardosi (13521089)

## Cara Menjalankan Program
1. Clone repository ini.
2. Pastikan file JavaScript yang ingin dicek berada pada folder yang sama dengan program repository ini.
3. Jalankan program dengan perintah
```
python parserprogram.py <nama-file-javascript>
```
Contoh:
```
python parserprogram.py “inputAcc.js”
```
