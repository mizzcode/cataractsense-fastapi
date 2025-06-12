# CataractSense Backend API
Back-end API ini berperan sebagai jembatan antara frontend aplikasi CataractSense dan API Machine Learning yang melakukan deteksi katarak berdasarkan citra mata. API ini dibangun menggunakan FastAPI.

# Project Structure

cataractsense-fastapi/
├── app/
│   ├── main.py               # Entry point aplikasi backend
│   └── routes/
│       └── predict.py        # Endpoint untuk mengirim gambar ke API ML
├── static/
│   └── uploads/              # Tempat file jika perlu menyimpan gambar lokal
├── requirements.txt          # Dependensi Python
├── README.md                 # Dokumentasi proyek ini


# Setup Instructions

1. **Clone this repository:**
    ```
    git clone <repo-url>
    cd cataractsense-fastapi
    ```

2. **Install dependencies:**
Disarankan menggunakan virtual environment:
    ```    
    python -m venv venv
    source venv/bin/activate     # MacOS/Linux
    venv\Scripts\activate        # Windows
    ```
    pip install -r requirements.txt
    ```

3. **Run the FastAPI app:**
    ```
    uvicorn app.main:app --reload --port 8001
    ```

4. **Access API Docs:**
    - Swagger UI: http://localhost:8001/docs
    - Redoc: http://localhost:8001/redoc

# API Usage

**Endpoint:** POST /predict
Mengirim gambar mata ke API ML untuk diproses.

**Request:**
    Method: POST
    Content-Type: multipart/form-data
    Body:
    - key : file
    - Value : file gambar (JPG/PNG)

**Contoh pakai curl:**
```
    curl -X POST "http://localhost:8001/predict" -F "file=@path_to_your_image.jpg"
```

*Response (Contoh):*
```
    {
    "status": "success",
    "result": {
        "prediction": "Katarak",
        "confidence": 0.93
    }
    }
```

# Koneksi ke API Machine Learning
Pastikan API ML sudah berjalan di http://127.0.0.1:8000/predict.

Jika alamat berbeda, ubah URL di file routes/predict.py:
```
    response = requests.post("http://127.0.0.1:8000/predict", files=files)
```

# Deployment Suggestions
Untuk deployment backend:
- uvicorn main:app --reload --port 8001
- Gunakan platform seperti:
    Railway
    Render
    Fly.io

# Catatan Integrasi Frontend
Frontend kamu bisa memanggil endpoint ini (/api/predict) dengan fetch() atau axios menggunakan FormData. 
Contoh fetch di JavaScript:
```
    const formData = new FormData();
    formData.append("file", imageFile);

    const response = await fetch("http://localhost:8001/predict", {
    method: "POST",
    body: formData
    });

    const result = await response.json();
    console.log(result);
```