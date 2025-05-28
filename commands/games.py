import discord
from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="blackjack", aliases=["bj"])
    async def blackjack(self, ctx, bet: str = None, mode: str = None):
        await ctx.send("Blackjack command executed.")

    @commands.command(name="coinflip", aliases=["cf"])
    async def coinflip(self, ctx, prediction: str = None, bet: int = None):
        await ctx.send("Coinflip command executed.")

    @commands.command(name="connectfour", aliases=["c4", "connect4"])
    async def connectfour(self, ctx):
        await ctx.send("Connect Four command executed.")

    @commands.command(name="crash", aliases=["cr"])
    async def crash(self, ctx, bet: int = None, mode: str = None):
        await ctx.send("Crash command executed.")

    @commands.command(name="findthelady", aliases=["ftl"])
    async def findthelady(self, ctx, bet: int = None, mode: str = None):
        await ctx.send("Find the Lady command executed.")

    @commands.command(name="gamble", aliases=["g", "play"])
    async def gamble(self, ctx, bet: int = None, mode: str = None):
        await ctx.send("Gamble command executed.")

    @commands.command(name="higherorlower", aliases=["hol"])
    async def higherorlower(self, ctx):
        await ctx.send("Higher or Lower command executed.")

    @commands.command(name="poker", aliases=["pkr"])
    async def poker(self, ctx, ante: int = None, bonus: str = None):
        await ctx.send("Poker command executed.")

    @commands.command(name="race", aliases=["r"])
    async def race(self, ctx, racer_type: str = None, prediction: str = None, bet: int = None):
        await ctx.send("Race command executed.")

    @commands.command(name="roll", aliases=["ro", "rd", "dr", "diceRoll", "dice"])
    async def roll(self, ctx, dice_type: str = None, prediction: str = None, bet: int = None):
        await ctx.send("Roll command executed.")

    @commands.command(name="roulette", aliases=["rou"])
    async def roulette(self, ctx, prediction: str = None, bet: int = None):
        await ctx.send("Roulette command executed.")

    @commands.command(name="rockpaperscissors", aliases=["rps"])
    async def rockpaperscissors(self, ctx, selection: str = None, bet: int = None):
        await ctx.send("Rock Paper Scissors command executed.")

    @commands.command(name="sevens", aliases=["sv"])
    async def sevens(self, ctx, prediction: str = None, bet: int = None):
        await ctx.send("Sevens command executed.")

    @commands.command(name="slots", aliases=["sl", "slot"])
    async def slots(self, ctx, bet: int = None):
        """Simulates a slot machine."""
        if bet is None or bet <= 0:
            await ctx.send("Please provide a valid bet amount.")
            return

        # Define the slot machine symbols
        symbols = [
            "<:sseven:1375930768823423087>",
            "<:sdiamond:1375930786728906843>",
            "<:sbar:1375930807851421727>",
            "<:sbell:1375930824498610216>",
            "<:sshoe:1375930849836531794>",
            "<:slemon:1375930868354383922>",
            "<:smelon:1375930883701346304>",
            "<:sheart:1375930928001581157>",
            "<:scherry:1375930944300781629>"
        ]

        # Spin the slots
        slot1 = random.choice(symbols)
        slot2 = random.choice(symbols)
        slot3 = random.choice(symbols)

        # Determine the payout
        payout = 0
        if slot1 == slot2 == slot3:
            # Three of a kind
            if slot1 == "<:sseven:1375930768823423087>":
                payout = bet * 500
            elif slot1 == "<:sdiamond:1375930786728906843>":
                payout = bet * 25
            elif slot1 == "<:sbar:1375930807851421727>":
                payout = bet * 5
            elif slot1 == "<:sbell:1375930824498610216>":
                payout = bet * 3
            elif slot1 == "<:sshoe:1375930849836531794>":
                payout = bet * 2
            elif slot1 == "<:slemon:1375930868354383922>":
                payout = bet * 1
            elif slot1 == "<:smelon:1375930883701346304>":
                payout = bet * 0.75  # 3:4
            elif slot1 == "<:sheart:1375930928001581157>":
                payout = bet * 0.5  # 1:2
            elif slot1 == "<:scherry:1375930944300781629>":
                payout = bet * 0.5  # 1:2
        elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
            # Two of a kind
            if slot1 == slot2 or slot1 == slot3:
                symbol = slot1
            else:
                symbol = slot2
            if symbol == "<:sseven:1375930768823423087>":
                payout = bet * 25
            elif symbol == "<:sdiamond:1375930786728906843>":
                payout = bet * 10
            elif symbol == "<:sbar:1375930807851421727>":
                payout = bet * 3
            elif symbol == "<:sbell:1375930824498610216>":
                payout = bet * 2
            elif symbol == "<:sshoe:1375930849836531794>":
                payout = bet * 1
            elif symbol == "<:slemon:1375930868354383922>":
                payout = bet * 1
            elif symbol == "<:smelon:1375930883701346304>":
                payout = bet * 0.75  # 3:4
            elif symbol == "<:sheart:1375930928001581157>":
                payout = bet * 0.75  # 3:4
            elif symbol == "<:scherry:1375930944300781629>":
                payout = bet * 0.25  # 1:4

        # Display the results
        result_message = (
            f"{slot1} | {slot2} | {slot3}\n"
            f"You bet: {bet}\n"
        )

        if payout > 0:
            result_message += f"You won: {payout}!"
        else:
            result_message += "You lost."

        await ctx.send(result_message)

    @commands.command(name="tictactoe", aliases=["ttt"])
    async def tictactoe(self, ctx):
        await ctx.send("Tic Tac Toe command executed.")

async def setup(bot):
    await bot.add_cog(Games(bot))
