import discord,os,sys
from discord.ext import commands

write = True  
file_path = "test.txt"

bot = commands.Bot(command_prefix='$')

@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx):
    count = 0
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        count += 1
    await ctx.channel.send(f"unbanned {count} members by wwz'#4877")
    
    if(write):
        with open(file_path, 'a') as f:
            for user in banned_users:
                f.write('\n')
                f.write(str(user.user))

TOKEN = "YOUR TOKEN"  
bot.run(TOKEN)
