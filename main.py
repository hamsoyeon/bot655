import discord

client = discord.Client()

token="ODE3MzM1ODU2NTEwNzk1ODE2.YEIBVQ.m5U79lPpFlC5gHwMmMgabEhcmTk" #Token Here from Bot Admin Page

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


client.run("ODE3MzM1ODU2NTEwNzk1ODE2.YEIBVQ.m5U79lPpFlC5gHwMmMgabEhcmTk");
