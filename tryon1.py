from gradio_client import Client, handle_file
from PIL import Image
import io
import os
os.environ['HF_API_TOKEN'] = ------enter the api------------

client = Client("jallenjia/Change-Clothes-AI")
result = client.predict(
    dict={"background": handle_file(
        'model2.jpg'), "layers": [], "composite": None},
    garm_img=handle_file('pant.jpg'),
    garment_des="Description",
    is_checked=True,
    is_checked_crop=False,
    denoise_steps=30,
    seed=-1,
    category="lower_body",
    api_name="/tryon"
)

# Adjust indexing if the structure is different
image_path = result[0]['image']

# Open the image using PIL
image = Image.open(image_path)

# Save the image to a file
image.save('output_image_pant.jpg')
print("Image saved to output_image.jpg")

