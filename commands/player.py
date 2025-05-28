import discord
from discord.ext import commands

class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="boosts", aliases=["bs"])
    async def boosts(self, ctx, action: str = "show", boost: str = None, amount: int = None):
        await ctx.send("Boosts command executed.")

    @commands.command(name="buy", aliases=["b"])
    async def buy(self, ctx, item_type: str = None, item_id: str = None, amount: int = None):
        await ctx.send("Buy command executed.")

    @commands.command(name="cooldowns", aliases=["cd"])
    async def cooldowns(self, ctx, detailed: str = None):
        await ctx.send("Cooldowns command executed.")

    @commands.command(name="daily")
    async def daily(self, ctx):
        await ctx.send("Daily command executed.")

    @commands.command(name="gift", aliases=["gifts"])
    async def gift(self, ctx, recipient: str = None):
        await ctx.send("Gift command executed.")

    @commands.command(name="goals", aliases=["tasks", "t"])
    async def goals(self, ctx):
        await ctx.send("Goals command executed.")

    @commands.command(name="leaderboard", aliases=["lb"])
    async def leaderboard(self, ctx, leaderboard: str = None, category: str = None, scope: str = None):
        # leaderboard: player/game/item/mining
        # category: leaderboard name or id
        # scope: "global" or None
        await ctx.send("Leaderboard command executed.")

    @commands.command(name="lookup", aliases=["find"])
    async def lookup(self, ctx, user: str = None, page: str = None):
        await ctx.send("Lookup command executed.")

    @commands.command(name="lotto", aliases=["lottery", "ticket", "tickets"])
    async def lotto(self, ctx, tickets_to_buy: int = None):
        await ctx.send("Lotto command executed.")

    @commands.command(name="monthly")
    async def monthly(self, ctx):
        await ctx.send("Monthly command executed.")

    @commands.command(name="overtime", aliases=["ot"])
    async def overtime(self, ctx):
        await ctx.send("Overtime command executed.")

    @commands.command(name="prestige")
    async def prestige(self, ctx, prestige_type: str = None):
        await ctx.send("Prestige command executed.")

    @commands.command(name="profile", aliases=["me", "bal", "balance", "my"])
    async def profile(self, ctx, page: str = None):
        await ctx.send("Profile command executed.")

    @commands.command(name="sell", aliases=["s"])
    async def sell(self, ctx, item_id: str = None, amount: int = None):
        await ctx.send("Sell command executed.")

    @commands.command(name="send", aliases=["transfer", "give"])
    async def send(self, ctx, recipient: str = None, amount: int = None):
        await ctx.send("Send command executed.")

    @commands.command(name="shop", aliases=[])
    async def shop(self, ctx, shop_type: str = None, page: str = None):
        await ctx.send("Shop command executed.")

    @commands.command(name="spin", aliases=["randomItem"])
    async def spin(self, ctx):
        await ctx.send("Spin command executed.")

    @commands.command(name="vote", aliases=["v"])
    async def vote(self, ctx, detailed: str = None):
        await ctx.send("Vote command executed.")

    @commands.command(name="weekly")
    async def weekly(self, ctx):
        await ctx.send("Weekly command executed.")

    @commands.command(name="work", aliases=["wk", "w"])
    async def work(self, ctx):
        await ctx.send("Work command executed.")

    @commands.command(name="yearly")
    async def yearly(self, ctx):
        await ctx.send("Yearly command executed.")

async def setup(bot):
    await bot.add_cog(Player(bot))
