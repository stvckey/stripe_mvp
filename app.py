from stripe import StripeClient
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("STRIPE_SECRET_KEY")

print(key)