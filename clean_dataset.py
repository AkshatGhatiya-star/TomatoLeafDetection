import os
from PIL import Image

def clean_directory(directory):
    print(f"\n🧹 Cleaning directory: {directory}")
    count_deleted = 0
    count_checked = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            count_checked += 1

            # Skip non-image files
            if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            try:
                # Try to open the image to verify it's valid
                with Image.open(file_path) as img:
                    img.verify()
            except Exception as e:
                try:
                    print(f"⚠️ Removing unreadable/missing file: {file_path}")
                    os.remove(file_path)
                    count_deleted += 1
                except Exception as err:
                    print(f"❌ Could not delete {file_path}: {err}")

    print(f"✅ Done cleaning {directory}")
    print(f"🔹 Checked: {count_checked}")
    print(f"🔹 Deleted: {count_deleted}")
    return count_deleted

# Run cleaner on both train and valid folders
train_path = 'dataset/train'
valid_path = 'dataset/valid'

if os.path.exists(train_path):
    clean_directory(train_path)
if os.path.exists(valid_path):
    clean_directory(valid_path)

print("\n🎉 Dataset cleanup complete! You can now safely train your model.")
dir /x

