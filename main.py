import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    text_msg = message.content

    if message.author == client.user:
        return 
    
    if text_msg.startswith("add:"):
        perguntas = text_msg.split(",")
        perguntas[0] = perguntas[0][5:]
        file = open("perguntas.txt", "a")
        file.write(message.author.name + "\n")

        for pergunta in perguntas:
            file.write(pergunta.lstrip() + "\n") 
        
        file.write("\n")

        await message.channel.send(f"Pergunta recebida com sucesso, {message.author}!")
        await message.delete()
        
            

client.run('')