from discord.ext import commands
import discord

class Talks(commands.Cog):
    """" Talks with user """

    def __init__(self, bot):
        self.bot = bot

    # bot.command => commands.command
    @commands.command(name='oii', help='Envia um caloroso olá | Não requer parâmetros')
    async def send_hello(self, ctx):
        name = ctx.author.name

        if name == 'Mattsz':
            response = 'Olá criador'
        else:
            response = 'Olá, ' + name

        await ctx.send(response)

    @commands.command(name='sobre', help='Envia no privado informações sobre o bot | Não requer parâmetros')
    async def secret(self, ctx):
        try:
            await ctx.author.send('Hi, i\'m matthew bot')
            await ctx.author.send('developed by @mattsz#3426, if you want more information about me go to the server: https://discord.gg/DuKwavh9Df')
            await ctx.author.send('Thanks ;)')
        except discord.errors.Forbidden:
            await ctx.send('Não posso te mandar o sobre, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade e segurança > Permitir mensagens diretas de membros do servidor')

def setup(bot):
    bot.add_cog(Talks(bot))
