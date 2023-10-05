# DiscordBot-control-remote-CMD
Execute commands in another computer's Windows Command Prompt using a Discord bot [discord.py], capable of running seamlessly in the background [pythonw]. 

Windows only.

Run the script as administrator to have CMD administrator mode (optional).
## Commands
`;cmd <command>` - Run command in CMD

`;limit <number>` - Limits the maximum number of characters per message. If the OUTPUT TOO LONG error occurs, lower the limit (by default, the limit is 1950)

`;exit` - Shutdown bot

## Run in the background
If you want the script to run in the background, download pythonw using `pip install pythonw`. After that, change the file extension to .pyw. First, test the script, as running in the background may make error messages invisible.
## Dependencies
discord.py - `pip install discord.py`

# Attention
The commands you execute will directly interact with the Windows Command Prompt; it's not simulated, it's real. I do not take responsibility for the commands you choose to run, nor for your intentions.
