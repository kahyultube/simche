# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("태국감"))

@client.event
async def on_message(message):
    if message.content == "텔포": # 메세지 감지
        await message.channel.send ("{} | {}, 안녕하십네까 여기는 공산적인 텔포 팬클럽입네다".format(message.author, message.author.mention))


# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('OTMyMDc5ODI3MjcwMzgxNjUw.YeNw_A.oKKdNfsNgCy8k3gCUXEHDTCFhus')