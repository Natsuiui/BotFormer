import discord
import dotenv
import os

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("hey dirtbag")

dotenv.load_dotenv()
bot.run(os.getenv("TOKEN", default="/Users/kshitij/Documents/Projects/Discord-Bot-LLMs/Assets/.env"))