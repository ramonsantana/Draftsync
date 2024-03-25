from flask import Flask, request
import requests

app = Flask(__name__)

# Your Device Magic API token, organization ID, and form ID
api_token = 'YOUR_API_TOKEN'
org_id = 'YOUR_ORG_ID'
form_id = 'YOUR_FORM_ID'

# The URL of your cloud server where the draft will be synced and removed
cloud_server_url = 'YOUR_CLOUD_SERVER_URL'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Check if a draft was saved and sync it
    if data['event'] == 'draft_saved':
        draft_id = data['data']['draft_id']
        sync_draft(draft_id)
    # Check if a draft was submitted and remove it
    elif data['event'] == 'draft_submitted':
        draft_id = data['data']['draft_id']
        remove_draft(draft_id)
    return '', 200

def sync_draft(draft_id):
    # Get the draft data from Device Magic
    response = requests.get(f'https://api.devicemagic.com/organizations/{org_id}/forms/{form_id}/drafts/{draft_id}', headers={'Authorization': f'Bearer {api_token}'})
    draft_data = response.json()

    # Sync the draft data to the cloud server
    cloud_response = requests.post(cloud_server_url, json=draft_data)
    if cloud_response.status_code == 200:
        print('Draft synced successfully.')
    else:
        print('Failed to sync draft.')

def remove_draft(draft_id):
    # Send a DELETE request to the cloud server to remove the draft
    cloud_response = requests.delete(f'{cloud_server_url}/{draft_id}')
    if cloud_response.status_code == 200:
        print('Draft removed successfully.')
    else:
        print('Failed to remove draft.')

if __name__ == '__main__':
    app.run(debug=True)
