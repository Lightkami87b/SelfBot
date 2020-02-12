from pyrogram import Client , Message , Filters ,errors
from db import r 
import time



@Client.on_message(Filters.regex("^[sS]ettings$") & Filters.me , group=28)
def settings(app : Client ,msg : Message):
    password = r.get("password")
    password = password[0] + "*" * (len(password) - 2) + password[-1]
    if "ssh" in r.keys():
        ip = r.hgetall("ssh")["ip"][:3]

    else:
        ip = "NoServer Seted"

    chatid = msg.chat.id
    text = f"""
**Settings:**

┏ **ChatAction:** `{r.get("action") or "PLAYING"}`
┗ Mode: `{r.get("actionmode")}`
┏ **AntiSpamMode**: `ON`
┗ ifSpam: `BLOCK`
┏ **Password:** `{password}`
┣ **Boss:** [{r.get("boss")}](tg://user?id={r.get("boss")})
┣ **LastSeen:** `{r.get("lastseen")}`
┣ **FilterFosh:** `{r.get("filterfosh")}`
┗ **FoshMaker:** `{r.get("fmaker")}`
┏ AutoDel: `{r.get("autodel")}`
┣ Time: {r.get("autodeltime")}
┗ ThisChatinUnmarks? `{"YES" if str(chatid) in r.smembers("unmark") else "NO"}`
┏ **ServerSet**: `{"YES" if "ssh" in r.keys() else "NO"}`
┣ IP: `{ip}***`
┗ PASS: `{"Hide" if "ssh" in r.keys() else "NotServer Seted"}`
**#Tkar**
"""
    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

