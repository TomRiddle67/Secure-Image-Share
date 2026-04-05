# 🔐 Secure Image Share

A secure image sharing app built with Python — available as both a **CLI tool** and a **REST API** with API key authentication.

Upload images, get a unique secret ID, and retrieve them securely. Built from scratch with real engineering practices.

---

## 🚀 What It Does

- 📤 **Upload** any image via CLI or HTTP request
- 🔑 **Get a unique ID** automatically generated for your image
- 📥 **Retrieve** your image anytime using that ID
- 🛡️ **Stores images locally** with UUID-based naming so no two files ever clash
- ⚡ **REST API** powered by FastAPI with auto-generated documentation
- 🔐 **API Key Authentication** — only authorised users can upload or retrieve images

---

## 🗂️ Project Structure

```
secure_image_share/
│
├── main.py            # CLI entry point
├── api.py             # FastAPI REST API
├── storage.py         # Handles saving and retrieving images (shared by CLI & API)
├── id_generator.py    # Generates unique UUIDs for each image
├── config.py          # App settings, storage path, and API keys
│
└── images/            # Where uploaded images are stored
```

---

## ⚙️ Setup

**Requirements:**
- Python 3.x

**Clone the repo:**
```bash
git clone https://github.com/TomRiddle67/Secure-Image-Share.git
cd Secure-Image-Share
```

**Install API dependencies:**
```bash
pip3 install fastapi uvicorn python-multipart
```

**Configure your API keys in `config.py`:**
```python
API_KEYS = [
    "your-secret-key-1",
    "your-secret-key-2"
]
```

---

## 💻 CLI Usage

### Upload an image
```bash
python3 main.py upload <path_to_image>
```
**Example:**
```bash
python3 main.py upload photo.jpg
```
**Output:**
```
✅ Image Saved Successfully!
🔑 Your Secret ID is: 018a79f1-0268-410d-bac3-0f7adb3789c9
💡 Keep this ID safe — it's the only way to retrieve your image!
```

### Retrieve an image
```bash
python3 main.py get <your_secret_id>
```
**Output:**
```
🎉 Found it! Your image is at: images/018a79f1-0268-410d-bac3-0f7adb3789c9.jpg
```

---

## 🌐 API Usage

### Start the server
```bash
uvicorn api:app --reload
```
Server runs at: `http://127.0.0.1:8000`

Interactive API docs at: `http://127.0.0.1:8000/docs` 🪄

---

## 🔐 Authentication

All API endpoints require a valid API key sent in the request header:

```
X-API-Key: your-secret-key
```

| Scenario | Response |
|----------|----------|
| No key provided | `401 Unauthorized` |
| Wrong key | `401 Unauthorized` |
| Valid key | `200 Success` |

### How to authenticate in Swagger UI:
1. Go to `http://127.0.0.1:8000/docs`
2. Click the 🔒 **Authorize** button
3. Enter your API key
4. All requests will include your key automatically!

---

## 📡 Endpoints

### `GET /`
Welcome message — no authentication required.

**Response:**
```json
{
  "Message": "🛠 Welcome to Secure Image Share API!"
}
```

---

### `POST /upload` 🔒
Upload an image file. **Requires API key.**

**Request:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/upload' \
  -H 'X-API-Key: your-secret-key' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@photo.jpg;type=image/jpeg'
```

**Success Response:**
```json
{
  "image_id": "001a45ec-7ff0-473c-abeb-ca616729bb7c"
}
```

**Error Response:**
```json
{
  "detail": "Invalid or missing API key"
}
```

---

### `GET /get/{image_id}` 🔒
Retrieve an image by its unique ID. **Requires API key.**

**Request:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/get/001a45ec-7ff0-473c-abeb-ca616729bb7c' \
  -H 'X-API-Key: your-secret-key'
```

**Responses:**
- ✅ Returns the actual image file
- ❌ `401` — Invalid or missing API key
- ❌ `404` — Image not found:
```json
{
  "detail": "Image not found"
}
```

---

## 🧠 How It Works

```
CLI                          API
─────────────────────────────────────────────
user types command     →     HTTP request
app prints output      →     JSON response
main.py handles input  →     endpoints handle requests
runs locally           →     runs as a server for everyone
```

1. User sends request with valid **API key** in header
2. Server verifies key — rejects if invalid
3. User provides image (path via CLI or file via HTTP)
4. App generates a **UUID** — a random ID that will never repeat
5. App copies image into `images/` folder renamed to that UUID
6. User receives UUID as their **secret retrieval key**
7. Later, user provides UUID + API key and app returns the image

---

## 🛠️ Built With

| Module | Purpose |
|--------|---------|
| `uuid` | Generates unique image IDs |
| `shutil` | Copies image files |
| `os` | Handles file paths and folders |
| `sys` | Reads CLI arguments |
| `fastapi` | REST API framework |
| `uvicorn` | ASGI server to run FastAPI |
| `python-multipart` | Handles file uploads via HTTP |

---

## 🌱 Roadmap

- [x] CLI image upload and retrieval
- [x] REST API with FastAPI
- [x] API Key authentication
- [ ] Expiring image links
- [ ] Image encryption
- [ ] Rate limiting
- [ ] Deploy to cloud (Railway / Render)

---

Author
TomRiddle67
