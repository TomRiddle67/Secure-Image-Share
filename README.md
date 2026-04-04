# 🛠 Secure Image Share CLI

A lightweight command-line app that lets you upload images and retrieve them using a unique secret ID — built with Python.

---

## 🚀 What It Does

- 📤 **Upload** any image from your computer
- 🔑 **Get a unique ID** automatically generated for your image
- 📥 **Retrieve** your image anytime using that ID
- 🛡️ **Stores images locally** with UUID-based naming so no two files ever clash

---

## 🗂️ Project Structure

```
secure_image_share/
│
├── main.py            # CLI entry point — where the app starts
├── storage.py         # Handles saving and retrieving images
├── id_generator.py    # Generates unique UUIDs for each image
├── config.py          # App settings (storage folder path)
│
└── images/            # Where uploaded images are stored
```

---

## ⚙️ Setup

**Requirements:**
- Python 3.x
- No external libraries needed — uses Python's built-in modules only!

**Clone the repo:**
```bash
git clone https://github.com/TomRiddle67/Secure-Image-Share.git
cd Secure-Image-Share
```

---

## 💻 Usage

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

---

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

---

### No arguments
```bash
python3 main.py
```
**Output:**
```
🛠 Welcome to Secure Image Share!
─────────────────────────────────
Commands:
  📤 python main.py upload <image_path>
  📥 python main.py get <image_id>
```

---

## 🧠 How It Works

1. User provides an image path
2. App generates a **UUID** (Universally Unique Identifier) — a random ID that will never repeat
3. App copies the image into the `images/` folder renamed to that UUID
4. User receives the UUID as their **secret retrieval key**
5. Later, user provides the UUID and app locates and returns the image path

---

## 🛠️ Built With

| Module | Purpose |
|--------|---------|
| `uuid` | Generates unique image IDs |
| `shutil` | Copies image files |
| `os` | Handles file paths and folders |
| `sys` | Reads CLI arguments |

---

## 🚀 Next Phase: Secure Image API

This project is evolving from a CLI tool into a backend API using FastAPI.

### Goals
- Upload images via HTTP requests
- Generate unique IDs for access
- Retrieve images using endpoints
- Reuse existing storage and ID logic

### Planned Enhancements
- Password protection per image
- Expiring image links
- File type validation
- Delete image by ID
- Encryption for stored images

 Author
 TomRiddle 
