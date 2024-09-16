import configparser
import datetime
import discord
from discord import *
from discord.ext import tasks

# configファイルの読み込み
global config
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

# Discord APIToken取得
discordToken = str(config.get("settings", "discord_api"))

# 許可する権限
intents = discord.Intents.all()  # 全てのインテンツを利用できるようにする
intents.message_content = True  # メッセージの読み書きを許可

bot = discord.Bot(description="Wake Up", intents=intents)

# 再生ファイル
filePath = f'./{str(config.get("settings", "music_file_name"))}'
volume = int(config.get("settings", "music_volume")) / 100

# 再生曜日日時
weekday = int(config.get("settings", "play_weekday"))
hour = int(config.get("settings", "play_hour"))
minute = int(config.get("settings", "play_minute"))

# BOTのステータスを変更する
async def active_status():
    activity = discord.Activity(type=int(config.get("settings", "active_type")), name=str(config.get("settings", "active_name")))
    await bot.change_presence(status=str(config.get("settings", "active_status")), activity=activity)

# VCに接続し、曲を再生する
async def play(vcId):
    await vcId.connect()
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(filePath), volume=volume)
    vcId.guild.voice_client.play(source)

@tasks.loop(seconds=1)
async def check_task(vcId):
    if str(config.get("settings", "realtime_config")) == "True": # リアルタイムコンフィグ読み取り処理
        global weekday,hour,minute
        config.read('./config.ini', 'UTF-8')
        weekday = int(config.get("settings", "play_weekday"))
        hour = int(config.get("settings", "play_hour"))
        minute = int(config.get("settings", "play_minute"))
    if vcId.guild.voice_client is None:
        # 現在日時取得
        dt = datetime.datetime.now()
        if dt.weekday() == weekday:
            if dt.hour == hour and dt.minute == minute:
                await play(vcId)

@tasks.loop(seconds=60)
async def playing_check():
    for vc in bot.voice_clients:
        if vc.is_playing():
            return
        await vc.disconnect()
    return

@bot.event  # 起動時に自動的に動くメソッド
async def on_ready():
    # BOTのステータスを変更する
    await active_status()
    # BOTの情報表示
    print(f"name: {str(bot.user.name)}")
    print(f"id: {str(bot.user.id)}")
    # ギルド・ボイスチャンネルの取得
    guildId = bot.get_guild(int(config.get("settings", "guild_id")))
    vcId = guildId.get_channel(int(config.get("settings", "voice_channel_id")))
    # 定期実行の開始
    check_task.start(vcId)
    playing_check.start()

# BOT起動
bot.run(discordToken)