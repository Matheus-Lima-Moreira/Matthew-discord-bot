import datetime

import requests
import discord

from decouple import config

from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

bot = commands.Bot("mtw!")


@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'palavrão' in message.content:
        await message.channel.send(
            f'Por favor, {message.author.name}, vai tomar no seu cu!'
        )

        await message.delete()

    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    if reaction.emoji == '👍':
        role = user.guild.get_role(846438050443165749)
        await user.add_roles(role)
    elif reaction.emoji == '👌':
        role = user.guild.get_role(846438050443165749)
        await user.add_roles(role)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send('Favor enviar todos os Argumentos. Digite mtw!help para ver os parâmetros de cada comando')
    elif isinstance(error, CommandNotFound):
        await ctx.send('O comando não foi encontrado ou não existe. Digite mtw!help para ver todos os comandos')
    else:
        raise error


@bot.command(name='oii', help='Envia um caloroso olá | Não requer parâmetros')
async def send_hello(ctx):
    name = ctx.author.name

    if name == 'Mattsz':
        response = 'Olá criador lindo'
    else:
        response = 'Olá, ' + name

    await ctx.send(response)


@bot.command(name='calcular', help='Calcula expressões matématicas | Parâmetros: <expressão>')
async def calculate_expression(ctx, expression):
    expression = "".join(expression)

    print(expression)

    response = eval(expression)

    await ctx.send('A resposta é: ' + str(response))


@bot.command(help='Verifica o valor de um par na binance | Parâmetros: <moeda>,<base>')
async def binance(ctx, coin, base):
    try:
        response = requests.get(
            f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

        data = response.json()
        price = data.get('price')

        if price:
            await ctx.send(f'O valor do par {coin}/{base} é {price}')
        else:
            await ctx.send(f'O valor do par {coin}/{base} é inválido')
    except Exception as error:
        await ctx.send('Ops.. deu algum erro!')
        print(error)


@bot.command(name='sobre', help='Envia no privado informações sobre o bot | Não requer parâmetros')
async def secret(ctx):
    try:
        await ctx.author.send('Curta o canal do matheus')
        await ctx.author.send('Lá eu so foda')
        await ctx.author.send(
            'UHUUUUUUUUUUUUUUUUUUUHHUUHUHUU'
        )
    except discord.errors.Forbidden:
        await ctx.send('Não posso te mandar o sobre, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade e segurança > Permitir mensagens diretas de membros do servidor')


@bot.command(name='foto', help='Envia uma foto aleátoria | Não requer parâmetros')
async def get_random_image(ctx):
    url_image = 'https://picsum.photos/1920/1080'

    embed = discord.Embed(
        title='Resultado da busca de imagem',
        description='PS: A busca é totalmente aleatória',
        color=0x0000FF
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text='Feito por ' + bot.user.name,
                     icon_url=bot.user.avatar_url)

    embed.add_field(name='Api', value='Usei a API do https://picsum.photos')
    embed.add_field(name='Parâmetros', value='{largura}/{altura}')

    embed.add_field(name='Exemplo', value=url_image, inline=False)

    embed.set_image(url=url_image)

    await ctx.send(embed=embed)


@tasks.loop(seconds=1800)
async def current_time():
    # now = datetime.datetime.now()

    # now = now.strftime('%d/%m/%Y às %H:%M:%S')

    channel = bot.get_channel(776954714663026722)

    # await channel.send('Data atual: ' + now)
    await channel.send('Estou pronto capitão!')

TOKEN = config('TOKEN')
bot.run(TOKEN)
