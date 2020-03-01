from pyrogram import Client , Message , Filters
from db import r
import time , requests
from bs4 import BeautifulSoup


@Client.on_message(Filters.me &  Filters.regex("^([Pp]) (.*)$") , group=17)
def myid(app : Client ,msg : Message):

    name = msg.text.split(" ")[1]
    if name == "dollar":
        url = requests.get("https://tejaratnews.com/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1").content
        soup = BeautifulSoup(url,features="lxml")
        data = soup.select(".price-table .responsive-table td")

        dollar = data[1].text
        dollar_change = data[2].text
        dollar_txt = f"┏**Dollar** : `{dollar}`\n┗**Change** : `{dollar_change}`"

        euro = data[4].text
        euro_change = data[5]
        euro_txt = f"┏**Euro** : `{euro}`\n┗**Change_** : `{euro_change}`"

        pound = data[7].text
        pound_change = data[8].text
        pound_txt = f"┏**Pound** : `{pound}`\n┗**Change** : `{pound_change}`"

        app.edit_message_text(
            text = f"{dollar_txt}\n{euro_txt}\n{pound_txt}",
            chat_id=msg.chat.id,
            message_id=msg.message_id
        )
    else:
        try:
            url = requests.get(f"https://api.coinmarketcap.com/v1/ticker/{name}/")
            change1h = url.json()[0]["percent_change_1h"]
            change24h = url.json()[0]["percent_change_24h"]
            change7d = url.json()[0]["percent_change_7d"]
            price = url.json()[0]["price_usd"]
            app.edit_message_text(text="**-{}-** \n__Price__ : `${}`\n__Change 1h__ : `{}%`\n__Change 24h__ : `{}%`\n__Change 7d__ : `{}%`\n**#Tkar**".format(name,price,change1h,change24h,change7d),
                chat_id=msg.chat.id,
                message_id=msg.message_id,)
        except:
            pass
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)