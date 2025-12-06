# Tomato Leaf Disease Detection

This project detects diseases in tomato leaves using deep learning.
It has a backend (API), frontend (web UI), and training scripts.

## Project Structure

- `backend/` – FastAPI/Django/Flask API (whatever you use)
- `frontend/` – React/HTML frontend
- `train_model.py` – training script
- `clean_dataset.py` – dataset preprocessing
- `test_api.py` – API testing script

## Dataset

The dataset is large (about 5 GB), so it is stored externally.

👉 **Download dataset from here:**  
https://drive.google.com/drive/folders/10SFVJslhJApa-VsNiEXoSn9Z-u8qXlkO?usp=sharing

After downloading, put the dataset inside a folder named `dataset/`
in the project root:

```text
TomatoLeafDetection/
    dataset/
    backend/
    frontend/
    ...

