# Youtuber Subscriber Count Desktop Background

This program gets the current subscriber count of a youtuber of your choice and displays it as your desktop background.

## Setup

Fill out notes.txt with your channel id and PATH where the program is being run from.
You will also need to get an API key from https://console.cloud.google.com/apis/dashboard for the youtube data API.

### Example
    Channel_Id=12345ABCDE
    API_Key=ExampleAPIKey12345
    PATH=C:\Users\Example\Documents\Folder
    
### Mistakes with notes.txt format

- Dont put a space after equal sign
- Make sure file location doesn't end in a forward slash

## Build
    git clone https://github.com/fvek01/Desktop-Subscribers
    pip install -r requirements.txt
