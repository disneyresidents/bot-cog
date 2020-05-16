from discord.ext import commands
import discord
import asyncio


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        guild = self.bot.get_guild(700880842309894175)
        if ctx.author in guild.members:
            user = guild.get_member(ctx.author.id)
            role = discord.utils.get(guild.roles, id=700890355259670599)
            if role in user.roles:
                return True
            return False
        return False

    @commands.command()
    async def announce(self, ctx, content):
        announce_chs = [662666842137034763, 702759218255495240]
        embed = discord.Embed(title="", description=content, color=0x3399FF)
        msg_list = []
        for ch_id in announce_chs:
            ch = self.bot.get_channel(ch_id)
            msg = await ch.send(embed=embed)
            msg_list.append(msg)

        if ctx.channel.id in announce_chs:
            await ctx.message.delete()

    @commands.command(name="reload")
    async def _reload(self, ctx, cog_name):
        try:
            self.bot.reload_extension(f'cogs.{cog_name}')
        except commands.ExtensionNotFound:
            await ctx.send('指定されたcogが見つかりませんでした')
        except commands.ExtensionNotLoaded:
            await ctx.send('指定されたcogが見つかりませんでした')
        else:
            await ctx.message.add_reaction('\U00002705')


def setup(bot):
    bot.add_cog(Admin(bot))