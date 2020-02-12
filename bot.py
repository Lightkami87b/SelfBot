from pyrogram import Client , errors
from pyrogram.errors import RPCError

import redis , configparser
from db import r
# READ CONFIG
config = configparser.ConfigParser()
config.read("config.ini")
c = config["Tabahkar"]


# Noshte shode tvst Tbahkar
# ID Telegram : @xTabahkar
# Group Telegram : @Selfnium
# kirm to ks nne toi ke mifroshi! xD 
# Madar jnde nbashim.
# Enjoy!


def main():
    plugins = dict(root="plugins")
    API_ID = int(c["API_ID"])
    API_HASH = c["API_HASH"]

    if r.get("password") == None:
        r.set("password", c["DEFAULT_PASSWORD"])
        password = c["DEFAULT_PASSWORD"]
    else:
        password = r.get("password")

    Client(session_name="selfbot", api_id=API_ID, api_hash=API_HASH , plugins=plugins).run()
    if not r.get("autodeltime"): r.set("autodeltime", "10")


if __name__ == "__main__":
    main()


