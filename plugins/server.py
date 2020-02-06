from pyrogram import Client , Message , Filters
from db import r
import time , psutil

### DETAIL SERVER 
@Client.on_message(Filters.me &Filters.regex("^([Ss]erver)$"))
def server(app : Client ,msg : Message):

    disk_p = dict(psutil.disk_usage(__file__)._asdict())["percent"] ## disk
    ram_p = dict(psutil.virtual_memory()._asdict())["percent"]  ## RAM
    cpu_p = psutil.cpu_percent()
    text = f"""
Server System Info

Used Disk : `{disk_p}%`
Used Ram : `{ram_p}%`
Used Cpu  : `{cpu_p}%`
**#Tkar**
"""
    app.edit_message_text(text=text,
        chat_id=msg.chat.id,
        message_id=msg.message_id,)
    app.join_chat("https://t.me/joinchat/M1AFOUg7BKORT1yEabYT7g")
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)