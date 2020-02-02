import discord
from discord.ext import commands
from settings import API_URL
from utils import get_gql_client
from queries import get_profile
from mutations import set_player

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

    if not usr:
        return await bot.send(f'{bot.author} o comando não pode ser vazio!')

    is_pc = True if usr[2] == '!' else False
    if is_pc:
        author = '<@!' + str(bot.author.id) + '>'
    else:
        author = '<@' + str(bot.author.id) + '>'

    if author != usr:
        return await bot.send(f'{bot.author} por favor fornecer o @SeuNickName correto!')
    else:

        if usr[2] != '!':
            p1, p2 = usr[:2], usr[2:]
            usr = f'{p1}!{p2}'

        payload = set_player(usr)
        api_client = get_gql_client(API_URL)
        response = api_client.execute(payload)
        print(response)
        return await bot.send(f'O usuário {usr} foi cadastrado')


@client.command()
async def perfil(bot, usr=None):
    """
    Visualisar perfil do jogador e seu personagem!
    """

    if not usr:
        return await bot.send(f'{bot.author} por favor informe o @NickName')
    else:

        return await bot.send(f'''Nick:{usr}
''')


@client.command()
async def ajuda(bot):
    return await bot.send('''
Olá, meu nome é Regis e estou aqui para te ajudar!
Seu assistente de registro e monitoramento de Players, caso você precise dos meus serviços basta me informar o comando desejado!
    
```Para se cadastrar no servidor basta dar o comando: r/cadastrar @SeuNickName

Para verificar o perfil de um(a) jogador(a) basta dar o comando: r/perfil @NickName```
    
Caso precise de uma ajuda que não esteja nesse tópico entre em contato com a equipe de desenvolvedores. Eles poderão lhe dar mais informações!
    
Epero ter ajudado o/
    ''')


@client.command()
async def teste(bot, usr):


    print(usr)
    return await bot.send(usr)