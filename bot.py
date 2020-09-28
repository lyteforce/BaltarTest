import discord


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()


client = discord.Client()


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    id = client.get_guild(704428414693539898)
    channels = ["commands"]

    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")  # If the user says !hello, send back Hi
        elif message.content == "!users":
            await message.channel.send(f"""`# of Members: {id.member_count}`""")


client.run(token)
