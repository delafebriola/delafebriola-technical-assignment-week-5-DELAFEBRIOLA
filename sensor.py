import time #library waktu
import board #library board untuk menentukan pin GPIO yang akan digunakan.
import adafruit_dht #pustaka khusus untuk DHT11
import psutil #library yang digunakan untuk  mengambul informasi tentang proses yang sedang berjalan.

for proc in psutil.process_iter(): #untuk mengembalikan iterator yang menghasilkan instance kelas proses untuk semua proses yang berjalan di mesin lokal.
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei': 
        proc.kill() #perintah untuk mmenghentikan proses.
sensor = adafruit_dht.DHT11(board.D23) #mendefinisikan nama sensor dan nomor pin yang digunakan.
while True: #mengulang perintah ranpa kondisi apa pun sampai pernyataan break dieksekusi di dalam loop.
    try:
        temp = sensor.temperature #membaca nilai temperatur atau suhu.
        humidity = sensor.humidity #membaca nilai kelembaban.
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity)) 
    except RuntimeError as error: #menangani error apabila terdapat kesalahan dalam proses runtime error.
        print(error.args[0]) #menampilkan output error
        time.sleep(2.0) #delay waktu selama 2 detik
        continue #sensor akan terus membaca dan menampilkan hasil.
    except Exception as error: #mendeteksi kesalahan selama dieksekusi.
        sensor.exit() #fungsi untuk keluar dari perintah.
        raise error #digunakan untuk membagkitkan ekspesi ketika kondisi error.
    time.sleep(2.0) #delay  waktu selama 2 detik dalam menampilkan hasil dari sensor.
