import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game=discord.Game("테스트봇")
    await client.change_presence(status=discord.Status.offline, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("우주에 있는거 같아. 반가워.")

access_token=os.environ["BOT_TOKEN"]
client.run(access_token);
