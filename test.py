import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")
print(DISCORD_TOKEN)
