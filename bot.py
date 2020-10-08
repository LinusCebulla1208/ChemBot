import discord
from discord.ext import commands as cmd
from chempy import balance_stoichiometry as balance

client = cmd.Bot(command_prefix="-")

@client.event
async def on_ready():
  print(f"{client.user.name} ist nun online!")

@client.command(name="balance")
async def balance_(ctx, equation):
  edukte = equation.split("=")[0].replace(" ", "").split("+")
  produkte = equation.split("=")[1].replace(" ", "").split("+")
  reac, prod = balance(edukte, produkte)
  
  reac_nice = f"{reac[list(reac.keys())[0]]}{list(reac.keys())[0]}"
  for i in range(len(list(reac.keys()))-1):
    reac_nice += f" + {list(reac.keys())[i+1]}"
  
  prod_nice = f"{prod[list(prod.keys())[0]]}{list(prod.keys())[0]}"
  for i in range(len(list(prod.keys()))-1):
    prod_nice += f" + {list(prod.keys())[i+1]}"
  
  #await ctx.send(f"{str(dict(reac))} = {str(dict(prod))}")
  await ctx.send(f"{reac_nice} = {prod_nice}")


client.run("NzYzODM0OTU4NDIyMjEyNjA4.X39evQ.FzxNFwqe5Z4jHYKGB425V5U4xdE")
