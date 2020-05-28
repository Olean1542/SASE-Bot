import discord
import asyncio
import random
import os


client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("사세를 따뜻하게"))
    print("3분 데운 사세")
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "사세야":
        await message.channel.send("왜 불러")

    if message.content.startswith("사세야 뱅행"):
        await message.channel.send("왜 시비지")

    if message.content.startswith("사세야 왜 시비지"):
        await message.channel.send("뱅행")

    if message.content == "사세야 명령어":
        embed = discord.Embed(title="▧ 사세 명령어 ▨", description="「 니들 채팅에 사세가 친절히 대답해줍니다 」", color=0xffe400)
        embed.set_thumbnail(url="https://i.imgur.com/feD446z.png")
        embed.add_field(name="Ⅰ.사세와 대화하기", value="● ``뱅행`` ``왜 시비지``", inline=False)
        embed.add_field(name="Ⅱ.사세와 놀기", value="● ``가위바위보`` ``가위`` ``바위`` ``보`` ``주사위``", inline=False)
        embed.add_field(name="Ⅲ.사세의 갤러리", value="● ``사세 버팔로윙``", inline=False)
        embed.set_footer(text="º 명령어 앞에 '사세야'는 무조건 들어가야함")
        await message.channel.send("", embed=embed)

    if message.content == "사세야 가위" or message.content == "사세야 바위" or message.content == "사세야 보":
        bot_response = random.randint(1, 3)

        if bot_response == 1:
            await message.channel.send("```● 사세가 가위를 냈습니다.```")
            if message.content == "사세야 가위":
                await message.channel.send("이걸 비기네")
            elif message.content == "사세야 바위":
                await message.channel.send("졌노")
            else:
                await message.channel.send("내가 이겼다~")
        elif bot_response == 2:
            await message.channel.send("```● 사세가 바위를 냈습니다.```")
            if message.content == "사세야 가위":
                await message.channel.send("내가 이겼다~")
            elif message.content == "사세야 바위":
                await message.channel.send("이걸 비기네")
            else:
                await message.channel.send("졌노")
        else:
            await message.channel.send("```● 사세가 보를 냈습니다.```")
            if message.content == "사세야 가위":
                await message.channel.send("졌노")
            elif message.content == "사세야 바위":
                await message.channel.send("내가 이겼다~")
            else:
                await message.channel.send("이걸 비기네")

    if message.content.startswith("사세야 가위바위보"):
        embed = discord.Embed(title="▧ 사세와 가위바위보 하기 ▨", description="그냥 ``가위`` ``바위`` ``보``중에 하나를 내면 됨", color=0xffe400)
        embed.set_footer(text="º 명령어 앞에 '사세야'는 무조건 들어가야함")
        await message.channel.send("", embed=embed)

    if message.content == "사세야 주사위":
        bot_response = random.randint(1, 6)
        if bot_response == 1:
            await message.channel.send("```● 주사위 눈금 1!```")
        elif bot_response == 2:
            await message.channel.send("```● 주사위 눈금 2!```")
        elif bot_response == 3:
            await message.channel.send("```● 주사위 눈금 3!```")
        elif bot_response == 4:
            await message.channel.send("```● 주사위 눈금 4!```")
        elif bot_response == 5:
            await message.channel.send("```● 주사위 눈금 5!```")
        elif bot_response == 6:
            await message.channel.send("```● 주사위 눈금 6!```")
            
    if message.content == "사세야 사세 버팔로윙":
        embed = discord.Embed(title="", description="", color=0xffe400)
        embed.set_image(url="https://i.imgur.com/iXDlyRn.jpg")
        embed.set_footer(text="")
        await message.channel.send("", embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
