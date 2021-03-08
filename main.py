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

    if message.content.startswith("알고리즘"):
        await message.channel.send("https://us02web.zoom.us/j/86707641669?pwd=K1RCbE9GckREMFFwcGQ4TU9CVjQ5dz09")

    if message.content.startswith("객지"):
        await message.channel.send("https://zoom.us/j/4653627989?pwd=VTJKSEJBWDRYZ1B4OVJqbVRzK1lkUT09")

    if message.content.startswith("겜기"):
        await message.channel.send("(화)https://us02web.zoom.us/j/83602675889?pwd=RXJqTWNXR09sbTJ1OHdrVHM1Q0hrdz09\n(목)https://us02web.zoom.us/j/86816738493?pwd=Z1NiRmd6M1NzZXUrZGUxQ0VVa1lnZz09")

    if message.content.startswith("API"):
        await message.channel.send("https://us02web.zoom.us/j/4507754358?pwd=bXg0cXlWSkNyOHFhNnRuT2dadk1mUT09")

    if message.content.startswith("c#"):
        await message.channel.send("(화)https://zoom.us/j/4653627989?pwd=VTJKSEJBWDRYZ1B4OVJqbVRzK1lkUT09\n(수)https://us02web.zoom.us/j/87533912414?pwd=TzY5ZlViWXh1RFVxZ1JNL3cvbDlCZz09")
  
access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
