
from pyrogram import Client , Message , Filters
from db import r
import time


@Client.on_message(Filters.me & (Filters.private | Filters.group) & Filters.regex("^[Cc]lear$") , group=47)
def clear (app : Client ,msg : Message):
    chatid = msg.chat.id
    messageid = msg.message_id
    msglist = []
    for message in app.iter_history(chatid, limit=1000):
        count = int(message.message_id)
        msglist.append(count)
    try:
        app.delete_messages(
            chatid,
            msglist
        )
    except:

        app.delete_messages(
            chatid,
            msglist
        )

    