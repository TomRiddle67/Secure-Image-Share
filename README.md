# 🔐 Secure Image Share

A secure image sharing app built with Python — available as both a **CLI tool** and a **REST API**.

Upload images, get a unique secret ID, and retrieve them anytime. Built from scratch with real engineering practices.

---

## 🚀 What It Does

- 📤 **Upload** any image via CLI or HTTP request
- 🔑 **Get a unique ID** automatically generated for your image
- 📥 **Retrieve** your image anytime using that ID
- 🛡️ **Stores images locally** with UUID-based naming so no two files ever clash
- ⚡ **REST API** powered by FastAPI with auto-generated documentation

---

## 🗂️ Project Structure

```
secure_image_share/
│
├── main.py            # CLI entry point
├── api.py             # FastAPI REST API
├── storage.py         # Handles saving and retrieving images (shared by CLI & API)
├── id_generator.py    # Generates unique UUIDs for each image
├── config.py          # App settings (storage folder path)
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
**Example:**
```bash
python3 main.py get 018a79f1-0268-410d-bac3-0f7adb3789c9
```
**Output:**
```
🎉 Found it! Your image is at: images/018a79f1-0268-410d-bac3-0f7adb3789c9.jpg
```

### No arguments
```bash
python3 main.py
```
**Output:**
```
🔐 Welcome to Secure Image Share!
─────────────────────────────────
Commands:
  📤 python main.py upload <image_path>
  📥 python main.py get <image_id>
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

### Endpoints

#### `GET /`
Welcome message confirming API is running.

**Response:**
```json
{
  "Message": "🛠 Welcome to Secure Image Share API!"
}
```

---

#### `POST /upload`
Upload an image file.

**Request:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@photo.jpg;type=image/jpeg'
```

**Response:**
```json
{
  "image_id": "001a45ec-7ff0-473c-abeb-ca616729bb7c"
}
```

---

#### `GET /get/{image_id}`
Retrieve an image by its unique ID.

**Request:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/get/001a45ec-7ff0-473c-abeb-ca616729bb7c'
```

**Response:**
- ✅ Returns the actual image file
- ❌ Returns `404` if ID not found:
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
runs locally           →     runs as a server
```

1. User provides an image (path via CLI or file via HTTP)
2. App generates a **UUID** — a random ID that will never repeat
3. App copies the image into `images/` folder renamed to that UUID
4. User receives the UUID as their **secret retrieval key**
5. Later, user provides the UUID and app returns the image

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
- [ ] API Key authentication
- [ ] Expiring image links
- [ ] Image encryption
- [ ] Rate limiting
- [ ] Deploy to cloud (Railway / Render)

---

Author
TomRiddle67

