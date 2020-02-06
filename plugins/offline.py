from pyrogram import Client , Message , Filters
from db import r
import time


###########  OFFLINE OPTIONS  ###########
@Client.on_message(Filters.private , group=50)
def me (app : Client ,msg : Message):
    me = app.get_me()
    status = me.status
    off_mode = r.get("offmode")
    if status == "offline":

        if off_mode =="on":
            try:
                txt = r.get(offtxt)
                print("done!")
                print(txt)
            except:
                txt = "User is offline please send message later!"
            app.send_message(
                msg.chat.id,
                txt,
            )
        else:
            pass
    else:
        pass


@Client.on_message(Filters.me & Filters.regex("^[Oo]fftxt (.*)$"), group=51)
def offline_text (app : Client ,msg : Message):
    txt = msg.text.split(" ")[1:50]
    text = " "
    text = text.join(txt)
    r.set("offtxt" , text)
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        f"`{text}`\nAdded as offline text!"
        )
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

    
@Client.on_message(Filters.me & Filters.regex("^[Oo]ffline$"), group=52)
def offline_mode(app : Client ,msg : Message):

    if r.get("offmode") == "on":
        r.set("offmode","off")
        txt = f"offline mode is OFF now!"
    else:
        r.set("offmode","on")
        txt = f"offline mode is ON now!"

    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        text = txt
    )
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
