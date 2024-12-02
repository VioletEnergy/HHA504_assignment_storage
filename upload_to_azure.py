from azure.storage.blob import BlobServiceClient

# Azure Storage connection string and container details
connection_string = "DefaultEndpointsProtocol=https;AccountName=azurecloudstoragehw;AccountKey=Muhd3/N6ObkunJA+/8WfIxa2xWaBSI3JqDY8nqUw9ffDeJTrgwazE54ciVkpMfpxqsjJ2XqZ1IMt+ASt80iTTQ==;EndpointSuffix=core.windows.net"
container_name = "use-this-container"  
blob_name = "person101_bacteria_485.jpeg" 
file_path = "images1/person101_bacteria_485.jpeg"  

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

try:
    # Get a BlobClient for the specific container and blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Upload the file
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"File '{blob_name}' successfully uploaded to container '{container_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")

