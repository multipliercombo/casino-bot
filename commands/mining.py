import discord
from discord.ext import commands

class Mining(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="craft", aliases=["cft"])
    async def craft(self, ctx, craft_type: str = None, amount: int = None):
        await ctx.send("Craft command executed.")

    @commands.command(name="dig", aliases=["d"])
    async def dig(self, ctx):
        await ctx.send("Dig command executed.")

    @commands.command(name="inventory", aliases=["inv", "i"])
    async def inventory(self, ctx):
        await ctx.send("Inventory command executed.")

    @commands.command(name="mine", aliases=["m"])
    async def mine(self, ctx):
        await ctx.send("Mine command executed.")

    @commands.command(name="process", aliases=["p", "pr"])
    async def process(self, ctx):
        await ctx.send("Process command executed.")

    @commands.command(name="start_mine", aliases=["start"])
    async def start_mine(self, ctx):
        await ctx.send("Start Mine command executed.")

    @commands.command(name="upgrade")
    async def upgrade(self, ctx, miner: str = None, upgrade_id: str = None, amount: int = None):
        await ctx.send("Upgrade command executed.")

async def setup(bot):
    await bot.add_cog(Mining(bot))
