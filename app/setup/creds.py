import os
import dotenv

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./app/setup/service_account.json"


