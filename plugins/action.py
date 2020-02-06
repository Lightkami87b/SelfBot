from pyrogram import Client , Message , Filters
from db import r
import time 


### ACTION CHAT
@Client.on_message(Filters.regex("^[Aa]ction$") & Filters.me)
def action(app : Client ,msg : Message):

    chatid = msg.chat.id

    if str(chatid) in r.smembers("chataction"):
        r.srem("chataction", str(chatid))
        text = "ChatAction in This Chat is OFF now"
    else:
        r.sadd("chataction", str(chatid))
        text = "ChatAction in This Chat is ON now"

    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    app.join_chat("https://t.me/joinchat/M1AFOUg7BKORT1yEabYT7g")
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.incoming,group = 24)
def incoming(app : Client ,msg : Message):
    # DEFULT PLAYING
    action = r.get("action") or "playing"
    chatid = msg.chat.id
    if str(chatid) in r.smembers("chataction"):

        for i in range(3):
            app.send_chat_action(
                chatid,
                action
            )
    
### SET ACTION
@Client.on_message(Filters.regex("^[Ss]etaction (.*)$") & Filters.me , group=25)
def setaction(app : Client ,msg : Message):
    action = str(msg.text.split(" ")[1])
    r.set("action", action)
    app.edit_message_text(text=f"Action Seted to {action}",
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)



@Client.on_message(Filters.regex("^[Aa]ctionlist$") & Filters.me , group=26)
def actionlist(app : Client ,msg : Message):
    text = """
actions:
`typing`
`upload_photo`
`upload_video`
`record_audio`
`upload_audio`
`upload_document`
`find_location`
`record_video_note`
`upload_video_note`
`choose_contact`
`playing`
cmd:
Setaction [action]
"""
    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)\
                
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

