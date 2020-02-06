from pyrogram import Filters , Message , Client
import time
from db import r
reload = [
    "`start reloading`",
    "░░░░░░░░░░░░░░",
    "▓░░░░░░░░░░░░░",
    "▓▓░░░░░░░░░░░░",
    "▓▓▓░░░░░░░░░░░",
    "▓▓▓▓░░░░░░░░░░",
    "▓▓▓▓▓░░░░░░░░░",
    "▓▓▓▓▓▓░░░░░░░░",
    "▓▓▓▓▓▓▓░░░░░░░",
    "▓▓▓▓▓▓▓▓░░░░░░",
    "▓▓▓▓▓▓▓▓▓░░░░░",
    "▓▓▓▓▓▓▓▓▓▓░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
    "reloading.",
    "reloading..",
    "reloading...",
    "reloading.",
    "reloading..",
    "reloading...",
    "reloading.",
    "reloading..",
    "reloading...",
    "`reloaded! :)`",
]

load = [
    "`start Loading`",
    "Load.",
    "lOad..",
    "loAd...",
    "loaD.",
    "Load..",
    "lOad...",
    "loAd.",
    "loaD..",
    "Load...",
    "lOad.",
    "loAd..",
    "loaD...",
    "`Loading! :)`",
]


@Client.on_message(Filters.me & (Filters.group|Filters.private) & Filters.regex("^[Rr]eload$") , group=1)
def cmd_reload(app : Client,msg : Message):
 
    for i in reload:
        time.sleep(0.2)
        app.edit_message_text(msg.chat.id,msg.message_id,i)
        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

@Client.on_message(Filters.me & (Filters.group|Filters.private) & Filters.regex("^[Ll]oad$"), group=2)
def cmd_load(app : Client, msg: Message):
 
    for i in load:
        time.sleep(0.2)
        app.edit_message_text(msg.chat.id,msg.message_id,i)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(msg.chat.id,msg.message_id)