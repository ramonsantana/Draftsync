import requests

# Your Device Magic API token
api_token = 'YOUR_API_TOKEN'

# The ID of the form and draft you're working with
form_id = 'FORM_ID'
draft_id = 'DRAFT_ID'

# The URL of your cloud server where the draft will be stored
cloud_server_url = 'CLOUD_SERVER_URL'

# Headers for Device Magic API
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

# Function to upload or update the draft copy on the cloud server
def upload_draft_copy():
    # Get the draft data from Device Magic
    response = requests.get(f'https://api.devicemagic.com/organizations/YOUR_ORG_ID/forms/{form_id}/drafts/{draft_id}', headers=headers)
    draft_data = response.json()

    # Upload the draft data to the cloud server
    cloud_response = requests.post(cloud_server_url, json=draft_data, headers=headers)
    if cloud_response.status_code == 200:
        print('Draft copy uploaded/updated successfully.')
    else:
        print('Failed to upload/update draft copy.')

# Function to remove the draft copy from the cloud server
def remove_draft_copy():
    # Send a delete request to the cloud server
    cloud_response = requests.delete(f'{cloud_server_url}/{draft_id}', headers=headers)
    if cloud_response.status_code == 200:
        print('Draft copy removed successfully.')
    else:
        print('Failed to remove draft copy.')

# Example usage
upload_draft_copy()
# Call remove_draft_copy() when the draft is submitted
