import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN", default="/Users/kshitij/Documents/Projects/Discord-Bot-LLMs/Assets")
print(DISCORD_TOKEN)
