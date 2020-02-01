import discord
from discord.ext import commands

# Ultima edição feita por @Grievon

client = commands.Bot(command_prefix='r/')


@client.event
async def on_ready():
    print("Let's to work!")


@client.command()
async def cadastrar(bot, usr=None):
    """
    Use registrar para adicionar novos jogadores no server!
    """
    author = '<@!' + str(bot.author.id) + '>'
    if not usr or usr != author:
        return await bot.send(f'{bot.author} por favor fornecer o @NickUser correto!')
    else:
        return await bot.send(f'{bot.author} adicionou {usr} no server!')


@client.command()
async def perfil(bot, usr=None):
    """
    Visualisar perfil do jogador e seu personagem!
    """
    if not usr:
        return await bot.send(f'{bot.author} por favor informe o @NickUser')
    else:
        return await bot.send(f'''Nick:{usr}
Ranking: Imagine um número
Vitórias: Imagine outro número
Derrotas: Imagine mais um número
''')


@client.command()
async def ajuda(bot):
    return await bot.send('''
Olá, meu nome é Regis e estou aqui para te ajudar!
Seu assistente de registro e monitoramento de Players, caso você precise dos meus serviços basta me informar o comando desejado!
    
```Para se cadastrar no servidor basta dar o comando: r/cadastrar @SeuNickName

Para verificar o perfil de um(a) jogador(a) basta dar o comando: r/perfil @NickName```
    
Caso precise de uma ajuda que não esteja nesse tópico entre em contato com a equipe de desenvolvedores. Eles poderão lhe dar mais informações!
    
o/
    ''')
