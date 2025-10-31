from gradio_client import Client, handle_file  # OutfitAnyone Parameters:
import os

# Define file paths
model_image_path = 'C:\\Avinash\\VTON\\model.jpg'
top_garment_path = 'C:\\Avinash\\VTON\\top_garment.png'
bottom_garment_path = 'C:\\Avinash\\VTON\\bottom_garment.png'

# Check if files exist
if not os.path.exists(model_image_path):
    print(f"File {model_image_path} does not exist.")
    exit(1)
if not os.path.exists(top_garment_path):
    print(f"File {top_garment_path} does not exist.")
    print("Please check the file path and ensure the file exists.")
    exit(1)
if not os.path.exists(bottom_garment_path):
    print(f"File {bottom_garment_path} does not exist.")
    exit(1)

# Handle files
model_name = handle_file(model_image_path)
top_garment = handle_file(top_garment_path)
bottom_garment = handle_file(bottom_garment_path)

# Initialize the client
client = Client("HumanAIGC/OutfitAnyone")

# Make the prediction
result = client.predict(
    model_name=model_name,
    garment1=top_garment,
    garment2=bottom_garment,
    api_name="/get_tryon_result"
)

# from gradio_client import Client, handle_file

# client = Client("HumanAIGC/OutfitAnyone")
# result = client.predict(
#     model_name=handle_file('path_to_model2_image.png'),
#     garment1=handle_file('path_to_top_garment.png'),
#     garment2=handle_file('path_to_bottom_garment.png'),
#     api_name="/get_tryon_result"
# )
