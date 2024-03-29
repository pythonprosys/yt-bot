# Work with Python 3.6
import discord
import time
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    global users
    global count
    if message.author == client.user:
        return
    if message.content.startswith('!yt move'):
        tchannel = discord.utils.get(message.server.channels,name='privat')
        if message.channel == tchannel:
            channel = discord.utils.get(message.server.channels,name='Aufnahme')
            role = discord.utils.get(message.server.roles,name='Verfügbar')
            for member in message.server.members:
                    if role in member.roles:
                        msg = "Du bist dran!"
                        await client.send_message(member, msg)
                        msg = "Wir moven " + str(member) + " rein"
                        await client.send_message(message.channel, msg)
                        await client.move_member(member, channel)
                        await client.remove_roles(member, role)
                        msg = "Du wurdest gemoved"
                        await client.send_message(member, msg)
                        msg = "Nutzer wurde gemoved"
                        await client.send_message(message.channel, msg)
        else:
            msg = "Du hast nicht die Berechtigung"
            await client.send_message(message.channel, msg)
    if message.content.startswith('!yt verfügbar'):
        author = message.author
        role = discord.utils.get(message.server.roles,name='Youtuber')
        for member in message.server.members:
                if role in member.roles:
                    msg = 'YTber, ' + str(author) + ' ist für die Aufnahme verfügbar'
                    await client.send_message(member, msg)
        await client.send_message(message.channel, msg)
        msg = 'Die YTber wissen nun, dass du Bereit für die Aufnahme bist.'
        await client.send_message(message.author, msg)
        msg = 'Bitte warte in der warteschlange'
        await client.send_message(message.author, msg)
        role = discord.utils.get(message.server.roles,name='Verfügbar')
        await client.add_roles(message.author, role)
    if message.content.startswith('!yt support'):
        role = discord.utils.get(message.server.roles,name='Supporter')
        author = message.author
        channel = message.channel
        for member in message.server.members:
            if role in member.roles:
                msg = 'Supporter, ' + str(author) + ' hat ein Problem'
                await client.send_message(member, msg)
        #await client.send_message(message.channel, msg)
        msg = 'Wir werden dich in kürze kontaktieren'
        await client.send_message(message.author, msg)
    if message.content.startswith('!sb pin'):
        msg = 'Schreibe jetzt deine Nachricht'
        await client.send_message(message.channel, msg)
        author = message.author
        channel = message.channel
        def check(message):
            return message.channel == channel and message.author == author
        msg = await client.wait_for_message(check=check)
        await client.pin_message(msg)
        msg = 'Angetackert!'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="YT vs Zuschauer"))
client.run(TOKEN)
