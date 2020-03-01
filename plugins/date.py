
from pyrogram import Client , Filters , Message 
import requests , time
from bs4 import BeautifulSoup
from db import r

@Client.on_message(Filters.regex("^[Tt]oday$")& Filters.me)
def today(app : Client , msg : Message):
    req=requests.get("https://www.time.ir").content
    clock = requests.get("http://gahshomar-api.herokuapp.com/zone/Asia-Tehran").text[:11]

    soup     =BeautifulSoup(req,features="lxml")
    data=soup.select(".panel-footer .normal ")
    Gdate = data[0].text
    Qdate = data[1].text
    Sdate = data[2].text
    text = f"┏ **Clock** : __{clock}__\n┣ **Shamsi** : __{Sdate}__\n┣ **Qamari** : __{Qdate}__\n┗ **Miladi** : __{Gdate}__\n**#Tkar**"
    app.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text = text,
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
