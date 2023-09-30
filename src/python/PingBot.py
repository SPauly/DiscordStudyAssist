import discord
from discord.ext import commands

class PingBot(commands.Bot):
    def __init__(self, intents: discord.Intents = discord.Intents.all()):
        super().__init__(command_prefix="b!", intents=intents)

    async def setup_hook():
        """ load your cogs here, also push the app commands"""
        await self.load_extension("Commands", package=__package__)
        self.tree.copy_global_to(guild=self.get_guild(int(os.getenv("MY_GUILD"))))
        await self.tree.sync(guild=guild)
        print(f"Bot is ready to go")

if __name__ == "__main__":
    bot = PingBot()
    bot.run(os.getenv("TOKEN"))
