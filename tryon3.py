import os
from gradio_client import Client, handle_file

# Define file paths
background_image_path = 'C:\\Avinash\\VTON\\path_to_image.png'
garment_image_path = 'C:\\Avinash\\VTON\\path_to_garment.png'

# Check if files exist
if not os.path.exists(background_image_path):
    print(f"File {background_image_path} does not exist.")
    exit(1)
if not os.path.exists(garment_image_path):
    print(f"File {garment_image_path} does not exist.")
    exit(1)

# Initialize the client
client = Client("jallenjia/Change-Clothes-AI")

# Make the prediction
result = client.predict(
    dict={"background": handle_file(
        background_image_path), "layers": [], "composite": None},
    garm_img=handle_file(garment_image_path),
    garment_des="Description",
    is_checked=True,
    is_checked_crop=False,
    denoise_steps=30,
    seed=-1,
    category="upper_body",
    api_name="/tryon"
)
