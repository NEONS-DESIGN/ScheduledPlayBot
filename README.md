<h1 align="center">ScheduledPlayBot</h1>

<p align="center">
  <a href="https://pycord.dev/"><img src="https://img.shields.io/badge/Pycord-v2.6.0-3498db" alt="/Pycord"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-v3.11.x-ffdc52" alt="/Pycord"></a>
</p>

## About

設定された時間に、設定された音声ファイルを、Discordのボイスチャットで自動再生してくれるBotです。
最初は月曜日が近いことを知らせる目的で制作していました。

## Config
Botのトークンを<a href="https://discord.com/developers/applications">ここから</a>取得し、記入してください。
```ini
discord_api = XXXXXXXXXXXXXXXXXXXXXXX
```
<br>
<a href="https://note.com/bardbot/n/na70832cb70a3">こちら</a>を参考に、botで再生させたいチャンネルのIDを設定してください。

```ini
guild_id = 0000000000000000000
voice_channel_id = 0000000000000000000
```
<br>
Botの状態を変更できます。

```ini
active_name = 月曜が近いよ
active_type = 3
active_status = online
```
下記の表を参考にしてください。
```python
# active_type
unknown = -1
playing = 0
streaming = 1
listening = 2
watching = 3
custom = 4
competing = 5

# active_status
online = "online"
offline = "offline"
idle = "idle"
dnd = "dnd"
do_not_disturb = "dnd"
invisible = "invisible"
streaming = "streaming"
```
<br>
再生する音声ファイルを指定してください。FFmpegの対応コーデックなら、だいたい再生できるかと思います。<br>

```ini
music_file_name = 月曜が近いよ.mp3
music_volume = 50
```



