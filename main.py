import discord
import dotenv
import os
import processing
import conversational

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("DiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	type = processing.what_type_of_message(message.content)
	if message.author.bot:
		return
	elif message.content == "Help" or message.content == "help":
		await message.channel.send("Hey! This Bot is easy to use! For masking sentences use <mask>!")
	elif type == "Conversation":
		await message.channel.send(processing.message_conversation(message=message.content))
	elif type == "Masking":
		await message.channel.send(processing.message_masking(message=message.content))
	elif type == "Translate":
		await message.channel.send(processing.message_translate(message=message.content))


dotenv.load_dotenv()
bot.run(os.getenv("TOKEN"))