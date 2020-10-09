import discord
from discord.ext import commands as cmd
from chempy import balance_stoichiometry as balance
from chempy import Substance

client = cmd.Bot(command_prefix="-")

@client.event
async def on_ready():
  print(f"{client.user.name} ist nun online!")

async def form(_dict):
    format_strings = [] #Fertig formatiert, aber ohne " + "
    for i in _dict.keys():
        subst = Substance.from_formula(i)
        unicode_form = subst.unicode_name
        format_strings.append(f"{_dict[i]}`{unicode_form}`")
    return " + ".join(format_strings)

@client.command(name="balance")
async def _balance(ctx, equation):
  edukte = equation.split("=")[0].replace(" ", "").split("+")
  produkte = equation.split("=")[1].replace(" ", "").split("+")
  reac, prod = balance(edukte, produkte)
  await ctx.send(f"{await form(dict(reac))} = {await form(dict(prod))}")

client.run("NzYzODM0OTU4NDIyMjEyNjA4.X39evQ.FzxNFwqe5Z4jHYKGB425V5U4xdE")
