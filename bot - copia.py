import discord
import youtube_dl
from discord.ext import commands
import asyncio
from itertools import cycle

TOKEN = 'NDM3OTU0MjY4MDA0MzUyMDEw.DfyXSw.d2dXxWrMEP2uk4qv-cWETs-RkKU'
client = commands.Bot(command_prefix = '?')
players = {}

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='xhelp'))
    print(" Join : " + client.user.name)

#---Commands---

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
        await client.say(output)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    #-Bot-joins-voice-channel
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    #-Bot-plays-music
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = players
    player.start()

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.voice_channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        mwssages.append(message)
    await client.delete_messages(messages)

@client.command(pass_context=True)
async def prueba(ctx):
    channel = ctx.message.channel
    emb = discord.Embed(
        title = 'Comandos',
        colour=000000
    )

    emb.set_author(name="Xmass",icon_url="https://media.discordapp.net/attachments/440563361114226709/440599722093183005/logo.jpg?width=473&height=473")

    await client.send_message(channel, embed=emb)

client.run(TOKEN)
