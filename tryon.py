from gradio_client import Client, handle_file
from PIL import Image
import io
import os
import time
import httpx
import base64
import json

# Use environment variable for the token (do NOT hardcode)
HF_TOKEN = os.getenv("HF_API_TOKEN")
if not HF_TOKEN:
    raise RuntimeError(
        "HF_API_TOKEN not set. Set it in your environment before running the script.")

# Initialize the client
client = Client("levihsu/OOTDiffusion")


def make_prediction_with_retries(client, retries=3, delay=5):
    for attempt in range(retries):
        try:
            result = client.predict(
                # Model Image (ensure file exists)
                vton_img=handle_file('model.jpg'),
                # Shirt Image (ensure file exists)
                garm_img=handle_file('hafe.jpg'),
                n_samples=1,
                n_steps=20,
                image_scale=2,
                seed=-1,
                api_name="/process_hd"
            )
            return result
        except httpx.ConnectTimeout:
            if attempt < retries - 1:
                print(
                    f"Attempt {attempt + 1} failed. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise


def save_image_from_result(result, out_path="output_hafe34.jpg"):
    # Common result structures:
    # - list with dicts: [{'image': <...>}]
    # - direct PIL.Image
    # - bytes or base64 string
    # - URL to image
    img_obj = None

    # Drill into common wrappers
    if isinstance(result, list) and len(result) > 0:
        candidate = result[0]
        if isinstance(candidate, dict) and 'image' in candidate:
            img_obj = candidate['image']
        else:
            img_obj = candidate
    else:
        img_obj = result

    # If it's already a PIL Image
    if isinstance(img_obj, Image.Image):
        img_obj.save(out_path)
        return out_path

    # If bytes-like
    if isinstance(img_obj, (bytes, bytearray)):
        img = Image.open(io.BytesIO(img_obj)).convert("RGB")
        img.save(out_path)
        return out_path

    # If it's a string: could be path, base64, or URL
    if isinstance(img_obj, str):
        s = img_obj
        # data URL (base64)
        if s.startswith("data:"):
            header, b64 = s.split(",", 1)
            data = base64.b64decode(b64)
            img = Image.open(io.BytesIO(data)).convert("RGB")
            img.save(out_path)
            return out_path
        # pure base64
        try:
            decoded = base64.b64decode(s)
            # Heuristic: if decoded starts with PNG/JPEG magic bytes, treat as image
            if decoded[:4] in (b'\x89PNG', b'\xff\xd8\xff\xe0', b'\xff\xd8\xff\xe1'):
                img = Image.open(io.BytesIO(decoded)).convert("RGB")
                img.save(out_path)
                return out_path
        except Exception:
            pass
        # URL case
        if s.startswith("http://") or s.startswith("https://"):
            resp = httpx.get(s)
            resp.raise_for_status()
            img = Image.open(io.BytesIO(resp.content)).convert("RGB")
            img.save(out_path)
            return out_path
        # local file path
        if os.path.exists(s):
            img = Image.open(s).convert("RGB")
            img.save(out_path)
            return out_path

    # Unknown format: write a JSON dump for inspection
    with open("last_result_debug.json", "w", encoding="utf-8") as f:
        json.dump({"result": str(result)}, f, ensure_ascii=False, indent=2)
    raise RuntimeError(
        "Could not interpret model output. See last_result_debug.json for details.")


# Run
if __name__ == "__main__":
    result = make_prediction_with_retries(client)
    saved = save_image_from_result(result, out_path="output_hafe34.jpg")
    print(f"Image saved to {saved}")
