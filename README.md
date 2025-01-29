# Scroll Forge

ScrollForge is a Python application that uses the Telethon library to interact with the Telegram API. It fetches PDF files from a specified Telegram channel and saves them locally.

[Note: This is a temporary readme file. The final version will be updated soon.]

## Prerequisites

- Python 3.6 or higher
- A Telegram account
- Telethon library
- python-dotenv library

Go to the [Telegram API website](https://my.telegram.org/auth) and log in with your Telegram account. Create a new application and note down the `API_ID` and `API_HASH` values.

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/ScrollForge.git
    cd ScrollForge
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `secrets.env` file**:

    Create a `secrets.env` file in the [session](http://_vscodecontentref_/1) directory with the following content:

    ```plaintext
    API_ID=your_api_id
    API_HASH=your_api_hash
    CHANNEL_USERNAME=your_channel_username
    PHONE_NUMBER=your_phone_number
    ```

    Replace `your_api_id`, `your_api_hash`, `your_channel_username`, and `your_phone_number` with your actual Telegram API credentials and channel username.

5. **First Authenticate with your phone number**:

    Run the following command to authenticate with your phone number:

    ```bash
    python telegram_fetch.py
    ```

    This will send an OTP to your phone number. Enter the OTP to authenticate.

6. **Run the application**:

    ```bash
    python app.py
    ```

    This will start the application and download PDF files from the specified Telegram channel to the [pdfs](http://_vscodecontentref_/2) directory.

## Files

- app.py: Main script to fetch PDF files from a Telegram channel.
- telegram_fetch.py: Script to initialize and login to the Telegram client.
- requirements.txt: List of dependencies required for the project.
- README.md: This file, providing setup instructions and information about the project.

## To Do
- [ ] A proper backend to store the PDF files using flask.
- [ ] Basic frontend to display the PDF files.
- [ ] Plan on API integration.
- [ ] Plan more features to the application.
- [ ] Update license.


## License

Will update soon.
