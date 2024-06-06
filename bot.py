from twitchio.channel import Channel
from twitchio.ext import commands # Twitchio module to connect script to twitch
from typing import List, Optional, Tuple # Typing module for optinal arguments
from functions import * # Importing functions from functions.py
from sqlite import *

class Bot(commands.Bot): # Using the class Bot for all commands
    async def name_from_id():
        channelList = channels()
        b = await bot.fetch_channels(channelList)
        print(b)

    def __init__(self): # Initialise our Bot with our access token, prefix and a list of channels to join on boot
        super().__init__(token='wgp2vs69qgarqssnqok0r812uhso3g', prefix='!', initial_channels=channelList) # Reading the channels to connect to from test list

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_command_error(self, context: commands.Context, error: Exception): # Handling errors
        if isinstance(error, commands.CommandNotFound): # Non existent command. As many other bots use the same prefix, we are just going to ignore unknown commands
            return
        # Invalid argument. The commands currently only have optional string arguments, therefore this cannot appear.
        # It's still good to keep it in here, incase more commands are added
        elif isinstance(error, commands.ArgumentParsingFailed): 
            await context.send("Invalid argument")
        elif isinstance(error, OSError): # Failing to open a file
            print("File opening failed")
            print(error)
            await context.send("There was an error opening a file, contact bot host")
        else: # If the error isn't any of the above, it is sent to the terminal
            print(error)

    async def join_channels(self, channels: List[str] | Tuple[str]):
        return await super().join_channels(channels)

    @commands.command(name="today") # Command to see how many entries
    async def today(self, ctx: commands.Context, argument: Optional[str] | None):
        channel = ctx.channel.name
        username = name_from_user(argument)
        if argument is None or len(argument) <= 2:
            name = name_from_user(channel)
            await ctx.send(today(name))
        elif username != 0:        
            await ctx.send(today(username))
        else:
            await ctx.send(today(argument.lower()))

    @commands.command(name="nethers") # Command to see how many entries
    async def nethers(self, ctx: commands.Context, argument: Optional[str] | None):
        channel = ctx.channel.name
        username = name_from_user(argument)
        if argument is None or len(argument) <= 2: 
            name = name_from_user(channel)
            await ctx.send(enters(name))
        elif username != 0:
            await ctx.send(enters(username))
        else:
            await ctx.send(enters(argument.lower()))


    @commands.command(name="enters") # Command to see how many entries
    async def enters(self, ctx: commands.Context, argument: Optional[str] | None):
        channel = ctx.channel.name
        username = name_from_user(argument)
        if argument is None or len(argument) <= 2:
            name = name_from_user(channel)
            await ctx.send(enters(name))
        elif username != 0:
            await ctx.send(enters(username))
        else:
            await ctx.send(enters(argument.lower()))


    @commands.command(name="botadd") # Command to add the bot to your own channel
    async def botadd(self, ctx: commands.Context):
        user = ctx.author.name
        id = ctx.author.id
        if add_channel(user, id) == 0:
            await ctx.send(f'Already added')
        else:
            channelList.append(user) # Adding the username into the list
            await bot.join_channels([user]) # Adding the bot to all channels in the list
            await ctx.send(f'Bot added')

    
    @commands.command(name="test") # Command to add bot to the callers channel
    async def test(self, ctx: commands.Context):    
        print("test")
        await ctx.send("test")

    @commands.command(name="group") # Command to see how many entries
    async def group(self, ctx: commands.Context, argument: Optional[str] | None):
        user = ctx.author.name
        if argument is None or len(argument) <= 2:
            await ctx.send(get_group(user))
        else:
            add_group(argument, user)
            await ctx.send(f"group set to {argument}")

    @commands.command(name="enterlb") # Command to see how many entries
    async def enterlb(self, ctx: commands.Context, argument: Optional[str] | None):
        if argument is None or len(argument) <= 2:
            await ctx.send(leaders(None))
        else:
            await ctx.send(leaders(argument))

    @commands.command(name="enterlbat") # Command to see how many entries
    async def enterlbat(self, ctx: commands.Context, argument: Optional[str] | None):
        if argument is None or len(argument) <= 2:
            await ctx.send(leaders_alltime(None))
        else:
            await ctx.send(leaders_alltime(argument))

    @commands.command(name="guide") # Gives a guide to the user
    async def guide(self, ctx: commands.Context):
        await ctx.send(f'https://pastebin.com/98pQa1vK')


channelList = channels()
bot = Bot()

bot.run() # Starting bot