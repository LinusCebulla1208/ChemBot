import discord
from discord.ext import commands as cmd
from chempy import balance_stoichiometry as balance

client = cmd.Bot(command_prefix="-")

@client.event
async def on_ready():
  print(f"{client.user.name} ist nun online!")

@client.command
async def balance(ctx, equation):
  edukte = equation.split("=")[0].replace(" ", "").split("+")
  produkte = equation.split("=")[1].replace(" ", "").split("+")
  reac, prod = balance()
  await ctx.send(f"{str(dict(reac))} = {str(dict(prod))}")

client.run("NzYzODM0OTU4NDIyMjEyNjA4.X39evQ.FzxNFwqe5Z4jHYKGB425V5U4xdE")
