# image-Dressing-
This project allows users to upload their image and virtually try on different clothes. After uploading a photo, users can select or add clothing items, which are then automatically applied to the uploaded image using AI-based image processing. The system generates a realistic output showing how the selected clothes look on the user’s image.
# 🧥 Image Dressing Project (Virtual Try‑On)

## 🚀 What’s included

* `tryon.py` — OOTDiffusion example with retry + robust result-saving logic.
* `tryon1.py` — Change-Clothes-AI (lower-body example).
* `tryon2.py` — OutfitAnyone example (top + bottom garments).
* `tryon3.py` — Change-Clothes-AI (upper-body example).
* `tryon.js` — Node.js/JavaScript example using the `@gradio/client` (OOTDiffusion).

---

## 🔧 Prerequisites

* Python 3.8+ (recommended 3.9 or 3.10)
* Node.js 16+ (if using `tryon.js`)
* A Hugging Face API token with model access (set as `HF_API_TOKEN` environment variable)
* Basic Git and GitHub account for pushing the repo

---

## ✅ Step-by-step setup (Python)

1. **Clone / create the repo**

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install Python dependencies**

   ```bash
   pip install --upgrade pip
   pip install gradio_client pillow httpx
   ```

4. **Set your Hugging Face token (do NOT hardcode)**

   macOS / Linux:

   ```bash
   export HF_API_TOKEN="hf_xxx..."
   ```

   Windows (PowerShell):

   ```powershell
   $env:HF_API_TOKEN = "hf_xxx..."
   ```

   Verify in Python (optional):

   ```python
   import os
   print(os.getenv('HF_API_TOKEN') is not None)
   ```

5. **Place your input images**

   * For `tryon.py`: `model.jpg`, `hafe.jpg` (or change the filenames inside the script)
   * For `tryon1.py`: `model2.jpg`, `pant.jpg`
   * For `tryon2.py` and `tryon3.py`: update `model_image_path`, `top_garment_path`, `bottom_garment_path` or `background_image_path` as needed in the script

---

## ▶️ How to run each script

### Python: OOTDiffusion (`tryon.py`)

```bash
python tryon.py
```

* Output example: `output_hafe34.jpg`
* This script includes retry logic (`make_prediction_with_retries`) and robust result parsing/saving.

### Python: Change-Clothes-AI lower-body (`tryon1.py`)

```bash
python tryon1.py
```

* Output example: `output_image_pant.jpg`
* `tryon1.py` in the current state uses a hardcoded HF token inside the file — **remove** it and use environment variable instead.

### Python: OutfitAnyone (`tryon2.py`)

```bash
python tryon2.py
```

* Make sure to update absolute paths in the script or change them to relative paths inside the repo.

### Python: Change-Clothes-AI upper-body (`tryon3.py`)

```bash
python tryon3.py
```

---

## ▶️ How to run `tryon.js` (Node.js)

1. Install dependencies:

```bash
npm init -y
npm install @gradio/client
node tryon.js
```

2. Ensure `tryon.js` has access to the image variables it references (in the provided snippet `modelImage` and `garmentImage` should point to actual files or file blobs). For Node usage you may need to adapt the example to read files from disk and pass them to the client.


## 🧪 Example: Make the scripts easier to run (recommended)

You can add a small CLI wrapper to pass input/output paths and model choices. Example (pseudo):

```bash
python run_tryon.py --model model.jpg --garment pant.jpg --out out.jpg --backend jallenjia/Change-Clothes-AI
```

---

## 📁 Suggested `.gitignore`

```
.venv/
__pycache__/
*.pyc
*.pyo
.env
output_*.jpg
last_result_debug.json
*.sqlite3
```

---

## 📤 Push to GitHub (step-by-step)

1. Initialize repo (if not already):

```bash
git init
git add .
git commit -m "Initial commit: Image Dressing Project"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

2. If you already have the repo remote, just commit & push:

```bash
git add .
git commit -m "Add tryon scripts and README"
git push
```

---

## 🤝 Contributing

Contributions are welcome. Recommended workflow:

1. Fork the repo
2. Create a feature branch `feature/your-change`
3. Open a PR describing changes

Please remove hardcoded tokens and do not commit private API keys.

---

## 📝 License

Choose a license (MIT suggested). Example `LICENSE` content (MIT) can be added.

---

## 🔖 Acknowledgements

* Hugging Face models used: `levihsu/OOTDiffusion`, `jallenjia/Change-Clothes-AI`, `HumanAIGC/OutfitAnyone`.
* `gradio_client` for model interaction.

---

## ❓ Need customization?

If you want, I can also:

* Create a `run_tryon.py` CLI wrapper
* Convert this repo into a Flask or React app with an upload UI
* Produce a GitHub Actions workflow to test the scripts

---

**Author:** Avinash Rai

*README generated and added to the project.*
