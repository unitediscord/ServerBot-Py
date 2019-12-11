import discord

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='ServerBot Made by United Discord! (unitediscord.xyz)')

@bot.event
async def on_message(message):
    if 'suicide' in message.content:
        await ctx.send("Suicide is never the answer! Please talk to someone about it!")
    if message.content == "hello":
        await ctx.send("Hello! :smile:")
    if message.content == "hi":
        await ctx.send("Hello! :smile:")

@bot.event
async def on_ready():
    print("{}({}) | https://discordapp.com/api/oauth2/authorize?client_id={}&permissions=8&scope=bot".format(bot.user, bot.user.id, bot.user.id))


bot.run('token')
