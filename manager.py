from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
from discord.ext import commands

class Manager(commands.Cog):
    """" Manage the bot """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Estou pronto! Estou conectado como {self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if 'palavrão' in message.content:
            await message.channel.send(
                f'Por favor, {message.author.name}, para de digitar palavrões!'
            )

            await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Favor enviar todos os Argumentos. Digite mtw!help para ver os parâmetros de cada comando')
        elif isinstance(error, CommandNotFound):
            await ctx.send('O comando não foi encontrado ou não existe. Digite mtw!help para ver todos os comandos')
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))