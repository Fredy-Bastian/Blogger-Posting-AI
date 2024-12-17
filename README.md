# **Blogger AI Posting Script**

Script Python ini digunakan untuk **mengotomatisasi posting artikel ke Blogger** dengan bantuan **AI Generative (Gemini)**. Data seperti token, ID Blogger, dan prompt disimpan dalam file `settings.json` agar mudah diubah.

---

## **Fitur Utama**

1. **Posting Artikel Otomatis**  
   Menggunakan AI untuk membuat konten HTML dengan format `<h2>`, `<h3>`, dan `<p>` sesuai SEO.

2. **Manajemen Prompt dan ID Blogger**  
   Anda dapat menyimpan prompt dan ID Blogger langsung di `settings.json` melalui menu program.

3. **Otorisasi Otomatis**  
   Token OAuth Blogger disimpan di `settings.json`, tidak memerlukan file `client_secrets.json`.

4. **Log Proses Dinamis**  
   Menampilkan log proses yang berjalan dalam satu baris untuk pengalaman yang lebih baik.

---

## **Persyaratan**

Pastikan Anda memiliki:
- **Python 3.x** terinstal.
- Library Python berikut:
  ```bash
  pip install google-auth google-auth-oauthlib requests google-generativeai

Struktur Proyek
Berikut adalah struktur direktori proyek
blogger-ai-posting/
│
├── auto_post.py          # Script utama program
├── settings.json         # File untuk menyimpan token, prompt, dan ID Blogger
└── README.md             # Dokumentasi proyek (file ini)


For further explanation, please visit: [Fredy Bastian](https://www.fredybastian.com/)
