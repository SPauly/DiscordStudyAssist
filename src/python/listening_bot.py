import discord

class ListeningBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.guilds = True  # Enable guild events (optional)
    intents.message_content = True
    client = ListeningBot(intents=intents)
    client.run('')
