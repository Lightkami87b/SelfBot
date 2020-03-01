from pyrogram import Client , Message , Filters
from db import r
import time

helptext = """
HELP:
[Mm] [media] (mute)
[Aa]ddf [fosh]
[Dd]elf [fosh]
[Ll]istf
[Cc]learf
[Cc]k (remove)
[Pp]in
[Rr]eload0 | [Rr]eload1
[Pp]y (run python3 Scripts)
[Dd] (delete)
[Pp] [money] (price)
[Ii]d
[Ss]erver (Srver information)
[Aa]ction
[Aa]ction [all|users|off|clear|list]
[Ss]ettings
[Ss]etaction ([Aa]ctionlist)
[Ss]pamf [reply] (fosh)
[Ss]pam [reply] [count]
[Nn]obody OR [Ee]verybody (LastSeen)
cmd: set [cmd] {reply} | cmdlist | dcmd [cmd]
[Aa]utodel ?[NUM]
[Aa]ddserver [reply] -> USERNAME@IP;PASSWORD
+[Cc]onnect (Connect to SHH addedserver)
    ...
    cmds
    ...
-exit() (Disconnect)
[Mm]ark [INCHAT] - mark anyway
[Tt]oday 
"""
@Client.on_message(Filters.regex("^[hH]elp$") & Filters.me, group=32)
def help(app : Client ,msg : Message):
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        helptext)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)