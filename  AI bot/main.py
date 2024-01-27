import discord
from discord.ext import commands 
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as{bot.user}')


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            fille_url = attachment.url
            await attachment.save(f"/{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send('Вы забыли загрузить картинку')        
        


@bot.command()
async def check_mashin(ctx):
    await ctx.send('bmw, audi, mercedes, chevrolet, ford, toyota, porshe, volvo. Я могу рассказать об о всех машинах')


@bot.command()
async def bmw(ctx):
    await ctx.send(' немецкий производитель автомобилей, мотоциклов, двигателей, а также велосипедов. Более 45 % акций принадлежит семье Квандт[4]. Председателем правления компании является Оливер Ципсе. Главный дизайнер — Йозеф Кабан[5]. В списке крупнейших публичных компаний мира Forbes Global 2000 за 2022 год BMW Group заняла 64-е место[6], а в списке Fortune Global 500 — 59-е место[7].Девиз компании — «Freude am Fahren», с нем. — «С удовольствием за рулём». Для англоязычных стран был придуман также девиз «The Ultimate Driving Machine» (с англ. — «Идеальная машина для вождения»).')
    

@bot.command()
async def audi(ctx):
    await ctx.send('audi в переводе с латынского языка — «слушай»[3]) — немецкая[4] автомобилестроительная компания в составе концерна Volkswagen Group, специализирующаяся на выпуске автомобилей под маркой Audi. Штаб-квартира расположена в городе Ингольштадт (Германия). Девиз — Vorsprung durch Technik (с нем. — «Прогресс через технологии»). Объём производства в 2016 году составил около 1 903 259 автомобилей.')


@bot.command()
async def mercedes(ctx):
    await ctx.send('В 2018 году бренд Mercedes-Benz оценивался в 48,601 млрд долларов, удерживая второе место (после Toyota) среди компаний-производителей автомобилей и восьмое место среди всех брендов мира[5]. По оценке BrandZ, в 2018 году марка входила в список Top 100 Most Valuable Global Brands, где занимала 46 место среди наиболее дорогих брендов со стоимостью в 25,684 млрд долларов[7]. В 2019 году бренд Mercedes-Benz оценивался в 60,355 млрд долларов, тем самым занимая первое место в рейтинге компаний-производителей автомобилей[8].')

@bot.command()
async def chevrolet(ctx):
    await ctx.send('Chevrolet (в США также неофициально Chevy[2]), — американская марка автомобилей, производимых и реализуемых одноимённым экономически самостоятельным подразделением корпорации General Motors.Chevrolet является самой популярной среди марок концерна GM.')


@bot.command()
async def ford(ctx):
    await ctx.send('Ford Motor Company, «Форд мотор компани» — американская автомобилестроительная компания. Четвёртый в мире производитель автомобилей по объёму выпуска за весь период существования. Штаб-квартира компании располагается в городе Дирборн в пригороде Детройта в штате Мичиган.')


@bot.command()
async def toyota(ctx):
    await ctx.send('Toyota Motor Corporation кратко: Toyota [тоёта], на русском чаще пишется Тойота — крупнейшая японская автомобилестроительная корпорация, также предоставляющая финансовые услуги и имеющая несколько дополнительных направлений в бизнесе. Является крупнейшей автомобилестроительной публичной компанией в мире[3], а также крупнейшей публичной компанией в Японии[4]. Главный офис компании находится в городе Тоёта, префектура Айти, Япония. В списке крупнейших публичных компаний мира Forbes Global 2000 за 2022 год Toyota Motor заняла 10-е место[5], а в списке Fortune Global 500 — 13-е место[6].')



@bot.command()
async def porshe(ctx):
    await ctx.send('Porsche AG (немецкое произношение [ˈpɔʁʃə][5] — Пóрше[6]; полное наименование Doktor Ingenieur honoris causa Ferdinand Porsche Aktiengesellschaft) — немецкий производитель автомобилей, основанный конструктором Фердинандом Порше в 1931 году[⇨], в настоящее время — дочерняя структура Porsche Automobil Holding. Штаб-квартира и основной завод находятся в Штутгарте, Германия[7].')

@bot.command()
async def volvo(ctx):
    await ctx.send('Volvo (Volvokoncernen, Volvo Group) — концерн, производящий коммерческие и грузовые автомобили, автобусы, двигатели и различное оборудование. Головной компанией концерна является компания AB Volvo. Ранее концерн Volvo производил также легковые автомобили, но в 1999 продал своё отделение легковых автомобилей под именем Volvo Personvagnar (Volvo Cars) концерну Ford, который в 2010 году перепродал его Geely.')

bot.run('')