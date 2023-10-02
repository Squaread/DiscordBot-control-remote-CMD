import subprocess
import os
import tempfile
import time


import discord
from discord.ext import commands

TOKEN = 'TOKEN' # Your bot token
PREFIX = ';' # Bot prefix
max_characters = 1950 # Maximum characters per message, 1950 is the default, it can be changed by the ;limit command (between 100 to 2000)

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'\n [SUCCESS] Connected as {bot.user.name}')

# Commands to limit characters per message
@bot.command()
async def limit(ctx, number: int):
    if number > 2000 or number < 100:
        await ctx.send("**[INVALID]** Set a limit between 100 to 2000")
        return
    global max_characters
    max_characters = number
    await ctx.send(f"Character limit per message changed to ``{number}``")
@limit.error
async def limit_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("**[INVALID]** Set a limit between 100 to 2000")
    else:
        await ctx.send(f"``max_characters = {max_characters}``")

# Command to execute cmd
@bot.command()
async def cmd(ctx, *, command):
    try: 
        # Create a temporary file with the .cmd extension and write the command to it
        with tempfile.NamedTemporaryFile(suffix=".cmd", mode="w", delete=False) as script_file:
            script_file.write(command)
            script_file_path = script_file.name
        # Build the cmd command to be executed
        cmd_command = f"cmd /c {script_file_path}"
        # Execute the command 
        output = subprocess.check_output(cmd_command, shell=True, stderr=subprocess.STDOUT)
        output = output.decode('utf-8', errors='ignore')

    # If error
    except subprocess.CalledProcessError as e:
        output = e.output

    # Remove the temporary file
    finally:
        os.remove(script_file_path) 

    # Split the output into smaller parts to avoid very long messages
    output_parts = [output[i:i+max_characters] for i in range(0, len(output), max_characters)]
    # Send the output parts as messages
    for part in output_parts:
        await ctx.send(f'```\n{part}```')
@limit.error
async def cmd_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, commands.BadArgument):
        pass
    else:
        await ctx.send(f"**[OUTPUT TOO LONG]** Reduce characters per message using ``{PREFIX}limit <number>`` (between 100 to 2000)")

# Command to exit (turn off bot)
@bot.command()
async def exit(ctx):
    await ctx.message.add_reaction('✅')
    await bot.close()
    
bot.run(TOKEN)
