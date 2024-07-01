import requests

def call_api(prompt, realtime):
    url = 'https://itzpire.com/ai/gpt-logic'
    params = {
        'q': prompt,
        'logic': 'respon dalam bahasa yang di inputkan. anda adalah sebuah ahli dalam bahasa pemerograman html jadi tulis hanya dalam respon html. hasilkan hanya <h2><h3><p>',
        'realtime': realtime
    }

    try:
        response = requests.get(url, params=params)
        response_data = response.json()  # Jika respons dari API adalah JSON
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Contoh penggunaan:
prompt = input("Masukkan prompt Anda: ")
realtime_option = input("Pilih opsi realtime (1 untuk true, 2 untuk false): ")

realtime = True if realtime_option == '1' else False

result = call_api(prompt, realtime)

if result:
    print("Response dari API:")
    print(result)
else:
    print("Gagal memanggil API.")
