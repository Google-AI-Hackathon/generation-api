import os
import dotenv

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

def set_google_application_credentials():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './app/setup/service_account.json'