import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

token = 'YOUR_TOKEN'

bot = commands.Bot(command_prefix='>', intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    
    
    if message.content == '31':
        await message.channel.send("Biri 31 dedi!")
    await bot.process_commands(message)


@bot.slash_command(name="okulhakkinda",description="Okulumuzun hakkındaki herşeyi öğrenin.")
async def okulhakkinda(ctx, bilgi: discord.Option(str, choices=['Tarihçe', 'Vizyon', 'Misyon', 'Bilgi']) ):
    if bilgi == 'Tarihçe':
        embed=discord.Embed(title="Zühtü Kurtulmuş Tarihçe", description="İş insanı Zühtü Kurtulmuş tarafından yaptırılmış olan okulumuz 2003 yılı Eylül ayında gerçekleştirilen, dönemin İstanbul Valisi ve İl Milli Eğitim Müdürü’nün de hazır bulunduğu bir törenle açılarak 2003-2004 Eğitim-Öğretim yılında faaliyete geçmiştir. O yıllarda Zühtü Kurtulmuş Lisesi adıyla faaliyete geçen okulumuz 2013-2014 Eğitim-Öğretim yılından itibaren Anadolu Lisesine dönüştürülmüştür. Okulumuz 1000 m2 kapalı alan üzerine kurulmuş olup, 3800 m2 okul bahçesi bulunmaktadır. Okulumuz 28 derslik, 1 Fizik Laboratuvarı, 1 Kimya Laboratuvarı, 1 Kütüphane, 1 Konferans Salonu, 1 Bilgisayar Laboratuvarı, 1 Resim Atölyesi, 1 Rehberlik Servisi’nden oluşan öğretim binasına sahiptir. Okulumuz içerisinde engelli öğrencilerimizin kullanımına yönelik olarak hazırlanmış olan asansör de bulunmaktadır. Bununla birlikte okulumuzda kız ve erkek öğrencilerimizin kullanımına açık olan öğrenci mescitleri de yer almaktadır. Ayrıca okulumuzda 2008 yılı itibariyle hizmete giren bir Kapalı Spor Salonu bulunmaktadır. Spor salonu ders saatleri içinde öğrencilerimize hizmet vermekte, ders saatleri dışında ise çevre halkının kullanımına sunulmaktadır. Okulumuz açıldığı tarihten itibaren öğrencilerimizin katılmış olduğu çeşitli sportif, kültürel ve bilimsel yarışmalara ait birçok dereceleri bulunmaktadır. Atletizm, karate, taekwondo, basketbol, voleybol, futbol, masa tenisi gibi spor branşlarında öğrencilerimiz il ve ilçe çapında önemli dereceler elde etmişlerdir. Bununla birlikte okulumuz açıldığı günden bu yana öğrencilerimiz çok sayıda kültürel ve bilimsel yarışmada da il ve ilçe çapında dereceye girmişlerdir. Okulumuz öğrencileri üniversite sınavlarında da yüksek başarılar elde etmektedirler. Uzman eğitim kadromuz sayesinde öğrencilerimizin akademik başarıları yükselmekte ve hayal ettikleri mesleklere ulaşmalarına katkı sunulmaktadır. Tarihimizden ilham alarak geleceği inşa etme düsturunu şiar edinen okulumuz, köklü geçmişiyle güçlü bir geleceğe emin adımlarla yürümektedir. Zeytinburnu'nun merkezi noktalarından birinde yer alan okulumuz tramvay, metro, otobüs ve minibüs hattına oldukça yakın konumdadır.", color=0xff0000)
        await ctx.respond(embed=embed)
    elif bilgi == 'Vizyon':
        embed=discord.Embed(title="Zühtü Kurtulmuş Vizyon", description="Bilimin ve teknolojinin farkında olan, Değişime ve gelişime açık, öğrenmeyi temel ihtiyaç kabul eden, Değerlerini yaşayan ve yaşatan, hoşgörü sahibi, ahlaklı ve erdemli, farklılıkları zenginlik kabul eden, Ülkesini ve medeniyet coğrafyasını tanıyan, köklerine bağlı, Atatürk ilkelerini ve Cumhuriyet değerlerini özümseyen, Yabancı dili dünyadaki bilimsel ve teknolojik gelişmeleri izleyebilecek düzeyde kullanabilen, Sosyal ve kültürel faaliyetlere katılımcı, etkili ve nitelikli, Kendine güvenen, kendini sorgulayan, Ülkesine ve milletine bağlı bireyler yetiştirmektir.", color=0xff0000)
        await ctx.respond(embed=embed)
    elif bilgi == 'Misyon':
        embed=discord.Embed(title="Zühtü Kurtulmuş Misyon", description="İnsana ve öğrenciye öncelik vermek, Çağın ihtiyaçlarına cevap verebilecek bilgi ve becerilere sahip, çevresi ile iyi ilişkiler kurabilen, toplumsal değerlere duyarlı ve çözüm üretebilen öğrenciler yetiştirmek, Milletin mutluluğunun kişisel mutluluğun üzerinde olduğu bilincini kazandırmak, Atatürkçü düşünce sistemini ve demokratik yaşamı benimsetmek, Bilimi, sevgiyi ve hoşgörüyü hayat felsefesi olarak öğretmek, Katılımcı ve paylaşımcı takım ruhunu yerleştirmek, Öğrenmeyi öğretmek ve bilgiyi kullandırtmak, Öğretmenlerin rehberliği ve öğrencilerimizin çalışmalarıyla bilim ve teknolojinin imkânlarını kullanarak bilimde, sanatta, edebiyatta ortaya koyulan proje ve çalışmalarla ülkemizi daha ileriye taşımak için çaba sarf etmek, Tarihimizden ilham alarak geleceği inşa etmektir.", color=0xff0000)
        await ctx.respond(embed=embed)
    elif bilgi == 'Bilgi':
        embed=discord.Embed(title="Zühtü Kurtulmuş Bilgi", description="Saatler: 08:25 - 13:00\nIsınma: Kalorifer\nBağlantı: ADSL\nYabancı Dil: İNGİLİZCE / ALMANCA\nPuan Bilgileri: 6,7 ve 8. sınıf OBP: 92.0122 Hesaplamak için https://lisepuan.glitch.me/ adrese girebilirsiniz", color=0xff0000)
        await ctx.respond(embed=embed)
    
        


@bot.slash_command(name="ping",description="Discord botumuza ping gönderir")
async def ping(ctx):
    await ctx.respond(f'Pong! Discord botumuz {bot.latency}ms alıyor.')

@bot.slash_command(name="itiraf", description="İtiraf sistemi")
async def itiraf(ctx: discord.ApplicationContext):
    channel = bot.get_channel(1242892739008270396)

    class MyView(discord.ui.View):
        @discord.ui.button(label="Kendini belli ederek itiraf et", style=discord.ButtonStyle.primary)
        async def reveal_confession(self, button: discord.ui.Button, interaction: discord.Interaction):
            class RevealModal(discord.ui.Modal):
                def __init__(self, *args, **kwargs) -> None:
                    super().__init__(*args, **kwargs)
                    self.add_item(discord.ui.InputText(label="İtirafım"))

                async def callback(self, interaction: discord.Interaction):
                    embed = discord.Embed(title="İtiraf")
                    embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar)
                    embed.add_field(name="İtirafım", value=self.children[0].value, inline=False)
                    await channel.send(embeds=[embed])

            modal = RevealModal(title="İtiraf")
            await interaction.response.send_modal(modal)

        @discord.ui.button(label="Anonim olarak itiraf et", style=discord.ButtonStyle.secondary)
        async def anonymous_confession(self, button: discord.ui.Button, interaction: discord.Interaction):
            class AnonymousModal(discord.ui.Modal):
                def __init__(self, *args, **kwargs) -> None:
                    super().__init__(*args, **kwargs)
                    self.add_item(discord.ui.InputText(label="İtirafım"))

                async def callback(self, interaction: discord.Interaction):
                    embed = discord.Embed(title="İtiraf")
                    embed.set_author(name="Anonim (Gizli)")
                    embed.add_field(name="İtirafım", value=self.children[0].value, inline=False)
                    await channel.send(embeds=[embed])

            modal = AnonymousModal(title="İtiraf")
            await interaction.response.send_modal(modal)

    view = MyView()
    await ctx.respond("Bir itiraf seçeneği seçin:", view=view)


# @bot.slash_command(name="reality",description="Wake up to reality")
# async def reality(ctx):
    


bot.run(token)
