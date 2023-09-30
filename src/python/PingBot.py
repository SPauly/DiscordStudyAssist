import discord

class PingBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

if __name__ == "__main__":
    client = PingBot(intents=intents)
    client.run('my token goes here')
