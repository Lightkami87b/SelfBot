from pyrogram import Client , Message , Filters
from db import r
import time

@Client.on_message(Filters.me & Filters.regex("^[Aa]utodel? ?(\d*)$") , group=36)
def autodel(app : Client ,msg : Message):
    if " " in msg.text:
        timer = msg.text.split(" ")[1]
        r.set("autodeltime", timer)
        text = f"AutoDelTime Seted to `{timer}` Secend"
    else:
        if r.get("autodel") == "on":
            r.set("autodel", "off")
            text = "Auto Delete Is **OFF** Now"
        else:
            r.set("autodel", "on")
            text = "Auto Delete Is **ON** Now"
        
    app.edit_message_text(msg.chat.id,msg.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)