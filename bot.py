import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='b.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.hybrid_command(name="tips-masalah-lingkungan", description="tips buat masalah lingkungan")
async def lingkungan(ctx:commands.Context):
    await ctx.send(embed=discord.Embed(
        title="tips buat masalah lingkungan",
        description="1. kurangin penggunaan plastik sekali pake\n"
        "2. daur ulang sampah dan pake lagi barang-barang yang masih bisa dipake\n"
        "3. pake transportasi umum, sepeda, atau jalan kaki buat ngurangin emisi karbon segala macem kaya gitu dh\n"
        "4. tanem pohon trus ya gitu lh\n"
        "5. hemat energi\n"
        "6. pake produk ramah lingkungan dan hindarin produk yang ngerusak lingkungan\n"
        "7. edukasi diri sendiri dan orang lain tentang pentingnya jaga lingkungan\n"
        "8. masih ada lagi sih tapi nanti aja",
        color=discord.Color.green()
    ))

@bot.hybrid_command(name="tips-menghindari-abu-vulkanik", description="tips menghindari abu vulkanik")
async def vulkanik(ctx:commands.Context):
    await ctx.send(embed=discord.Embed(
        title="tips menghindari abu vulkanik",
        description="1. pake masker buat nutupin mulut dan hidung\n"
        "2. kalo bisa jangan keluar rumah dulu\n"
        "3. tutup jendela dan pintu rumah biar abu ga masuk\n"
        "4. bersihin atap rumah dari abu vulkanik biar ga nambah beban\n"
        "5. bersihin mobil dari abu vulkanik biar ga ngerusak cat mobil\n"
        "6. kalo kena kulit, bilas pake air bersih\n"
        "7. kalo kena mata, bilas pake air bersih juga\n"
        "8. kalo kena pakaian, cuci pake air bersih juga\n",
        color=discord.Color.brand_red()
    ))

@bot.hybrid_command(name="bahaya-merokok", description="bahaya merokok")
async def merokok(ctx:commands.Context):
    await ctx.send(embed=discord.Embed(
        title="bahaya merokok",
        description="1. ngerusak paru-paru\n"
        "2. ngerusak jantung\n"
        "3. ngerusak pembuluh darah\n"
        "4. ngerusak kulit\n"
        "5. ngerusak gigi dan mulut\n"
        "6. ngerusak sistem reproduksi\n"
        "7. ngerusak sistem pencernaan\n"
        "8. ngerusak sistem saraf\n"
        "9. ngerusak sistem kekebalan tubuh\n"
        "10. ngerusak sistem endokrin\n\n"
        "tapi yang dah ngerokok bertahun2 tapi gapapa, efeknya belum kerasa, itu cuma keberuntungan aja, bukan berarti aman buat ngerokok",
        color=discord.Color.brand_red()
    ))

@bot.hybrid_command(name="bahaya-narkoba", description="bahaya narkoba")
async def narkoba(ctx:commands.Context):
    await ctx.send(embed=discord.Embed(
        title="bahaya narkoba",
        description="1. ngerusak otak\n"
        "2. ngerusak hati\n"
        "3. ngerusak ginjal\n"
        "4. ngerusak paru-paru\n"
        "5. ngerusak jantung\n"
        "6. ngerusak pembuluh darah\n"
        "7. ngerusak sistem reproduksi\n"
        "8. ngerusak sistem pencernaan\n"
        "9. ngerusak sistem saraf\n"
        "10. ngerusak sistem kekebalan tubuh\n"
        "11. ngerusak sistem endokrin\n\n"
        "yang belum pernah nyoba ya jangan dicoba takutnya ketagihan",
        color=discord.Color.brand_red()
    ))

bot.run(os.getenv('TOKEN'))