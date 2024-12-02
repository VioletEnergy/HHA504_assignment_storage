from google.cloud import storage
from PIL import Image
import io
import os

# Step 1: Set up your Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_secret_2.json'

# Step 2: Create a Google Cloud Storage client
client = storage.Client()

# Step 3: Create a bucket or use an existing one
bucket_name = 'laura-ahi-dummy-demo'  # Change this to your bucket name
bucket = client.bucket(bucket_name)


## create a list of files in /images with path 
files_upload = []
for root, dirs, files in os.walk("images"):
    for file in files:
        files_upload.append(os.path.join(root, file))

for file in files_upload:
    ## print working on
    print("fWorking on {file}") 
    ## load file using io into memory
    with open(file, 'rb') as f:
        file_byte_array = f.read()
    print(file)
    ## just keep file name 
    file = file.split("/")[-1]
    print('new file name: ', file)
    ## upload file to GCS
    try:
        blob = bucket.blob(file)
        blob.upload_from_string(file_byte_array, content_type='image/png')
        print(f"Image uploaded successfully to Google Cloud Storage!")
    except Exception as e:
        print(f"Error: {e}")



# Step 4: Create a fake image using Pillow
image = Image.new('RGB', (100, 100), color = (73, 109, 137))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')

# Step 5: Upload the fake image to Google Cloud Storage
blob = bucket.blob('fake_image.png')
blob.upload_from_string(image_byte_array.getvalue(), content_type='image/png')

print("Image uploaded successfully to Google Cloud Storage!")