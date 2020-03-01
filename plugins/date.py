
from pyrogram import Client , Filters , Message
import requests , time
import jdatetime
from db import r

@Client.on_message(Filters.regex("^[Tt]oday$")& Filters.me)
def today(app : Client , msg : Message):

    date = jdatetime.datetime.now().strftime('%d %b %Y')
    clock = clock = requests.get("http://gahshomar-api.herokuapp.com/zone/Asia-Tehran").text[:11]
    text = f"Clock : **{clock}**\nDate : **{date}**\n#Tkar"
    app.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text = text,
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
