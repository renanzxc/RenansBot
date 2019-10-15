# RenansBot
>Bot for Telegram with some functions
* Usining:
   * Python 3.7
   * Telepot

## For running:
Need you create a file with the name `tokenBot.py` and this function inside:
```
def returnToken():
    return "TOKEN"
```
Replace `TOKEN` with your token

## Release History
* v2.0
  * Commands: `/aprende /nome`.
  * Command change for bot learns names, `/nome`, then the user submits your name.
  * Learn phrases using: `/aprende messageSendByUser=BotResponse`.
  * Check learned phrases and send response learned.
* v1.0
  * Commands: `/start /pillarmen`.
  * Receive and send the image back.
  * Learn names.
  * User sends: `seu nome` the bot to learn his name.
  * If the bot has learned the username it will respond with your username.
  * If the bot receives an unanswered message it sends: `Tendi foi nada`.
  * Or receive an unknown file sends: `Ainda não fui programado para isso`.
  * Math operations: +, -, *, /.
