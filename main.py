import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"SpaceCraft Bot online as {bot.user}")

# --- Basic command ---
@bot.command()
async def status(ctx):
    await ctx.send("🚀 SpaceCraft Bot is online and operational.")

@bot.command()
async def working(ctx, *, task="unknown"):
    await ctx.send(f"👨‍🚀 {ctx.author.name} is now working on: {task}")

@bot.command()
async def location(ctx, *, place="unknown location"):
    await ctx.send(f"📍 {ctx.author.name} is now at: {place}")

@bot.command()
async def needhelp(ctx, *, message="No details"):
    await ctx.send(f"⚠️ HELP REQUEST from {ctx.author.name}: {message}")

# --- Run bot ---
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
