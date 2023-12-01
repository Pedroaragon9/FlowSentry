#Script for BioMS3
import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime  

shared_drive_path = r"O:\Public\Proteomics-Core-Lab-Data\ChromCheck\log"  
slack_token = "abcdefg"  # Update with your Slack token
channel_id = "hijklmn"  #  update with your Slack channel ID

client = WebClient(token=slack_token)

def send_slack_message(message):
    try:
        response = client.chat_postMessage(channel=channel_id, text=message)
        assert response["message"]["text"] == message
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

def main():
    files_already_seen = set()
    while True:
        current_files = set(os.listdir(shared_drive_path))
        new_files = current_files - files_already_seen
        if new_files:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current time of the error
            for file in new_files:
                send_slack_message(f"Beeeep-Booop, error detected at {current_time}")
            files_already_seen = current_files
        time.sleep(60)  # 60 seconds interval between checks

if __name__ == "__main__":
    main()
