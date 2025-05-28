from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="delete_my_data")
    async def delete_my_data(self, ctx):
        await ctx.send("Delete my data command executed.")

    @commands.command(name="donate")
    async def donate(self, ctx):
        await ctx.send("Donate command executed.")

    @commands.command(name="help")
    async def help_command(self, ctx, command_name: str = None):
        await ctx.send("Help command executed.")

    @commands.command(name="invite")
    async def invite(self, ctx):
        await ctx.send("Invite command executed.")

    @commands.command(name="stats")
    async def stats(self, ctx):
        await ctx.send("Stats command executed.")

    @commands.command(name="support")
    async def support(self, ctx):
        await ctx.send("Support command executed.")

async def setup(bot):
    await bot.add_cog(Help(bot))
