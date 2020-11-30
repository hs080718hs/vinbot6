import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('!도움')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0x80E12A)
                channel = 781896362798219315
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출근 알림', value='모든문의 주세요!')
                embed.set_image(url="https://cdn.discordapp.com/avatars/758473474129133589/a_4021bd6081f973db3e8051dd6f570978.png?size=128%22")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("/퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0xFF0000)
                channel = 781896388719411211
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 퇴근 알림', value='문의들 못받습니다.')
                embed.set_image(url="https://cdn.discordapp.com/avatars/758473474129133589/a_4021bd6081f973db3e8051dd6f570978.png?size=128%22")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

client.run(os.environ['token'])
