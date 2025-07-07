import requests

def konversi_mata_uang(api_key, jumlah, mata_uang_asal, mata_uang_tujuan):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{mata_uang_asal}"
    try:
        respon = requests.get(url)
        respon.raise_for_status()
        data = respon.json()

        if data['result'] == 'success':
            rates = data['conversion_rates']
            
            if mata_uang_tujuan in rates:
                kurs_tujuan = rates[mata_uang_tujuan]
                hasil_konversi = jumlah * kurs_tujuan

                print(f'''
---- HASIL KONVERSI ----
{jumlah} {mata_uang_asal} = {hasil_konversi:.2f} {mata_uang_tujuan}
(kurs 1 {mata_uang_asal} = {kurs_tujuan} {mata_uang_tujuan})
------------------------''')
            else:
                print("Error: Mata uang yang di tuju tidak terdaftar.")
        else:
            print("Error: Gagal mengambil data dari API, cek kembali API.")
    
    except requests.exceptions.HTTPError as eror_http:
        if respon.status_code == 404:
            print(f"Eror: Kode mata uang asal {mata_uang_asal} tidak didukung / tidak ada.")
        else:
            print(f"Eror HTTP terjadi: {eror_http}.")
    except requests.exceptions.RequestException as req_eror:
        print(f"Error koneksi: {req_eror}.")
    except Exception as e:
        print(f"Terjadi sebuah eror: {e}")

while True:
    if __name__ == "__main__":
        API_KEY = "API KEY"
        try:
            jumlah_mata_uang = float(input("masukkan jumlah mata uang: "))
            asal = input("Dari mata uang (kode): ").upper()
            tujuan = input("Ke mata uang (kode): ").upper()
            konversi_mata_uang(API_KEY,jumlah_mata_uang,asal,tujuan)

        except ValueError:
            print("\nError: Jumlah uang harus angka saja.")