import discord
import storage
import swear

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  count = swear.bad_word_count(message.content)  

  if count > 0:
    # Get the current history
    previous = storage.fetch_value(message.author.id)

    if previous is None:
      previous = 0

    latest = previous + count
    
    # Update the databse
    storage.set_value(message.author.id, latest)

    # Print a message
    await message.channel.send(f"You said {count} bad words, for a total of {latest} bad words.")


client.run('Discord_Token_Here')


# https://discord.com/api/oauth2/authorize?client_id=1113849670570102814&permissions=2419190832&scope=bot

