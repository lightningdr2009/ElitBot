import discord

#id = 521239617312260096
#id_test = 739147050179887185
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(521239617312260096)
    id_test = client.get_guild(739147050179887185)

    if message.content.find("e/hello") != -1:
        await message.channel.send("`Hi`")
    if message.content.find("e/info") != -1:
        await message.channel.send("`Version: 0.1\n Creator: lightningdr2009\n Purpose in life: To be on the ElitSMP discord server.`")
    if message.content.find("e/smp_members") != -1:
        await message.channel.send("`Members in ElitSMP:\n RayKillerYt\n RahulTGM`")

client.run(token)