import sys
from storage import save_image, get_image

def main ():
    if len(sys.argv) < 2:
        print("🛠 Welcome to Secure Image Share!")
        print("─────────────────────────────────")
        print("python  main.py upload <image_path>")
        print("python  main.py get <image_id>")
        return
    command = sys.argv [1]
    if command =="upload":
        image_path = sys.argv [2]
        image_id = save_image(image_path)
        print(f"Image Saved Successfully!")
        print(f"🔑 Your Secret ID is: {image_id}")
        print(f"Keep this ID safe🔐 it's the only way to retrieve your image!")

    elif command == "get":
        image_id = sys.argv [2]
        path = get_image(image_id)
        if path:
            print(f"found it!: {path}")
        else:
            print("Image not found")
    else:
         print(f"unknown command: {command}")

if __name__ =="__main__":
        main()