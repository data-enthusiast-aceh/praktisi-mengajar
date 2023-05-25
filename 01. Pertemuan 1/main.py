#print("Hello World")

# Percabangan

nama_mahasiswa = "Rizki"
uas = 80
uts = 80
tugas = 70
kuis = 60

total = (uas * 0.4) + (uts * 0.3) + (tugas * 0.2) + (kuis * 0.1)

print(f"Nilai Anda adalah     : {total}")

if total >= 60:
    print("Keterangan Anda         : Lulus")
elif total < 60:
    print("Keterangan Anda         : Gagal")

if total >= 85:
    huruf = 'A'
elif total >= 70:
    huruf = 'B'
elif total >= 60:
    huruf = 'C'
elif total >= 50:
    huruf = 'D'
else:
    huruf = 'E'

print(f"Nilai Huruf Anda adalah  : {huruf}")
print("==================================================\n\n")





# d 	for integers
# f 	for floating point numbers
# b 	for binary numbers
# o 	for octal numbers
# x 	for octal hexadecimal numbers
# s 	for string
# e 	for floating point in exponent format

# def calculate_final_grade(uas, uts, tugas, kuis):
#     uas_weight = 0.4
#     uts_weight = 0.3
#     tugas_weight = 0.2
#     kuis_weight = 0.1
#
#     final_grade = (uas * uas_weight) + (uts * uts_weight) + (tugas * tugas_weight) + (kuis * kuis_weight)
#     return final_grade
#
#
# nama_mahasiswa = input("Masukkan Nama Mahasiswa: ")
# mata_kuliah = input("Masukkan Mata Kuliah: ")
# nim_mahasiswa = input("Masukkan NIM Mahasiswa: ")
# nilai_uas = float(input("Masukkan Nilai UAS: "))
# nilai_uts = float(input("Masukkan Nilai UTS: "))
# nilai_tugas = float(input("Masukkan Nilai Tugas: "))
# nilai_kuis = float(input("Masukkan Nilai Kuis: "))
#
# nilai_akhir = calculate_final_grade(nilai_uas, nilai_uts, nilai_tugas, nilai_kuis)
#
# if nilai_akhir >= 80:
#     grade = "A"
# elif nilai_akhir >= 70:
#     grade = "B"
# elif nilai_akhir >= 60:
#     grade = "C"
# elif nilai_akhir >= 50:
#     grade = "D"
# else:
#     grade = "E"
#
# print("\n===== Detail Mahasiswa =====")
# print("Nama Mahasiswa:", nama_mahasiswa)
# print("Mata Kuliah:", mata_kuliah)
# print("NIM Mahasiswa:", nim_mahasiswa)
# print("Nilai Akhir:", nilai_akhir)
# print("Grade:", grade)


