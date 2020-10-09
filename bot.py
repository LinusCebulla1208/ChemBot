import discord
from discord.ext import commands as cmd
from chempy import balance_stoichiometry as balance
from chempy import Substance

client = cmd.Bot(command_prefix="-")

@client.event
async def on_ready():
  print(f"{client.user.name} ist nun online!")

async def tief(eq):
    ret = ""
    for i in eq:
        ret+=i.replace("1", "\u2081").replace("2", "\u2082").replace("3", "\u2083").replace("4", "\u2084").replace("5", "\u2085").replace("6", "\u2086").replace("7", "\u2087").replace("8", "\u2088").replace("9", "\u2089").replace("0", "\u2080")
    return ret

@client.command(name="balance")
async def balance_(ctx, equation):
  edukte = equation.split("=")[0].replace(" ", "").split("+")
  produkte = equation.split("=")[1].replace(" ", "").split("+")
  reac, prod = balance(edukte, produkte)
  
  reac_nice = f"{reac[list(reac.keys())[0]]}`{await tief(list(reac.keys())[0])}`"
  for i in range(len(list(reac.keys()))-1):
    reac_nice += f" + {reac[list(reac.keys())[0]]}`{await tief(list(reac.keys())[i+1])}`"
  
  prod_nice = f"{prod[list(prod.keys())[0]]}`{await tief(list(prod.keys())[0])}`"
  for i in range(len(list(prod.keys()))-1):
    prod_nice += f" + {prod[list(prod.keys())[0]]}`{await tief(list(prod.keys())[i+1])}`"
  
  #await ctx.send(f"{str(dict(reac))} = {str(dict(prod))}")
  await ctx.send(f"{reac_nice} = {prod_nice}")

client.run("NzYzODM0OTU4NDIyMjEyNjA4.X39evQ.FzxNFwqe5Z4jHYKGB425V5U4xdE")
