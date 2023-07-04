from discord.ext import commands
import discord


class addhost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    @commands.has_role("Helper") 
    async def addhost(self, ctx, user: discord.User):
        if user.id in self.client.host_logs:
            old = self.client.host_logs[user.id]
            self.client.host_logs[user.id] = old + 1
            await ctx.send(f'Successfully added **1** host to {user.mention}.')
        else:
            self.client.host_logs[user.id] = 1
            await ctx.send(f'Successfully added **1** host to {user.mention}.')


async def setup(client):
    await client.add_cog(addhost(client))