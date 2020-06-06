from discord.ext import commands
import discord


class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="vote")
    async def _vote(self, ctx, title, *kouho):
        count = len(kouho)
        
        if count == 1:
            react_list = [u"\u2B55", u"\u274C"]
        
        elif 2 <= count <= 9:
            react_list = [
                "\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT SEVEN}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT EIGHT}\N{COMBINING ENCLOSING KEYCAP}",
                "\N{DIGIT NINE}\N{COMBINING ENCLOSING KEYCAP}"]
        else:
            await ctx.send("候補の数が少なすぎるか多すぎます\n1個以上9個以下にしてください")
            return

        content = ""
        if not count == 1:
            for i in range(count):
                content += f"{react_list[i]}:{kouho[i]}\n"
            embed = discord.Embed(title=f"**{title}**", description=content)
            react_list = react_list[:count]
        else:
            embed = discord.Embed(title=f"**{title}**", description=kouho[0])

        msg = await ctx.send(embed=embed)
        for react in react_list:
            await msg.add_reaction(react)


def setup(bot):
    bot.add_cog(Vote(bot))
