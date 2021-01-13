import discord
from discord.ext import commands as cmd
from chempy import balance_stoichiometry as balance
from chempy import Substance

#for Giphy API 
import giphy_client
from giphy_client.rest import ApiException
from random import randint

client = cmd.Bot(command_prefix="-")

#for Giphy API
api_instance = giphy_client.DefaultApi()
api_key = 'Zatacs6tRlzuFhS006ls0P8IAQ0Rh01t' # str | Giphy API Key.
q = 'chemistry' # str | Search query term or prhase.

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

def remove_duplicates(_list):
    return list(dict.fromkeys(_list)) #Convert list into dictionary and back --> duplicates get removed


@client.command(name="balance")
async def _balance(ctx, equation):
  edukte = equation.split("=")[0].replace(" ", "").split("+")
  produkte = equation.split("=")[1].replace(" ", "").split("+")
  reac, prod = balance(edukte, produkte)
  await ctx.send(f"{await form(dict(reac))} = {await form(dict(prod))}")

@client.command(name="hey")
async def _hey(ctx):
    await ctx.channel.send("older than you")

@client.command(name="gif")
async def gif(ctx):
    try: 
        api_response = api_instance.gifs_search_get(api_key, q, limit=1, offset=randint(1, 100), lang="en", fmt="gif")
        gif_id = api_response.data[0]
        gif_url = gif_id.images.downsized.url
        await ctx.send(gif_url)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(name="lookup")
async def lookup(ctx, formula, property):
    f = open("data_output_file_v2.csv" ,"r")
    
        #search
    found_lines=[]
    for i in f.readlines():
        if(i.split(",")[0] == formula):
            found_lines.append(i)
    if not found_lines:
        await ctx.send("Compound not found.")
    
    if property:
        #search for property
        line_with_property = ""
        for line in found_lines:
            if property == line.split(",")[1]:
                await ctx.send(line.split(",")[1] + " of " + line.split(",")[0] + " = " + line.split(",")[2] + " " + line.split(",")[3].replace("NoUnits", ""))
                break
    else:        
       #format
        emb = discord.Embed()
        for i in remove_duplicates(found_lines): #Remove duplicates (not sure why but there're some)
            property=i.split(",")[1]
            value = i.split(",")[-2]
            unit=i.split(",")[-1].replace("NoUnit", "")
            emb.add_field(name=i.split(",")[1], value=f"{value}{unit}")
        await ctx.send(embed=emb)
    
client.run("NzYzODM0OTU4NDIyMjEyNjA4.X39evQ.FzxNFwqe5Z4jHYKGB425V5U4xdE")