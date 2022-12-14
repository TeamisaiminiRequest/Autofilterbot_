import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", '')
    START_TXT = environ.get("START_TXT", '''<b>Hello {} šš»\nāÆ My Name is Teamisaimini Request
āÆ I Can Provide MOVIES,SERIES And Lot More
āÆ Don't Waste Your Time Looking To Add ME To Your Group , I'm Only For @Teamisaimini
āÆ TEAM - @Teamisaimini</b>''')
    HELP_TXT = """<b>Hi {}
I have that Features.
Create One Link This :
Ā» I will Create For One Bot You. But Paid
Ā» Contact Me <a href=https://t.me/teamisaimini><b>teamisaimini</b></a></b>"""
    ABOUT_TXT = """<b>š¤ My Name : Teamisaimini\n
š§š»āš» Developer : <a href=https://t.me/teamisaimini><b>teamisaimini</b></a>\n
š Language : Pyrogram\n
š Framework : Python3\n
š” Hosted on : VPS\n
š¢ Updates Channel : <a href=https://t.me/Teamisaimini><b></b>Teamisaimini</a>"""
    SOURCE_TXT = """<b>Create One Like This :</b>
Ā» I will Create One Bot For You. But Paid<b>
Ā» Contact Me</b> <a href=https://t.me/teamisaimini><b>Teamisaimini</b></a>"""
    MANUELFILTER_TXT = """<b>Help :</b> <b>Filters</b>

<b>- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message</b>

<b>NOTE :</b>
<b>1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.</b>

<b>Commands and Usage :</b>
<b>ā¢ /filter - add a filter in chat
ā¢ /filters - list all the filters of a chat
ā¢ /del - delete a specific filter in chat
ā¢ /delall - delete the whole filters in a chat (chat owner only)</b>"""
    BUTTON_TXT = """<b>Help :</b> <b>Buttons</b>

<b>- Search Bot Supports both url and alert inline buttons.</b>

<b>NOTE :</b>
<b>1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format</b>

<b>URL buttons :</b>
<code>[Button Text](buttonurl:https://t.me/Teamisaimini)</code>

<b>Alert buttons :</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>Help :</b> <b>Auto Filter</b>

<b>NOTE :</b>
<b>1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.</b>"""
    CONNECTION_TXT = """<b>Help :</b> <b>Connections</b>

<b>- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.</b>

<b>NOTE :</b>
<b>1. Only admins can add a connection.
2. Send</b> <code>/connect</code> <b>for connecting me to ur PM</b>

<b>Commands and Usage :</b>
<b>ā¢ /connect  - connect a particular chat to your PM
ā¢ /disconnect  - disconnect from a chat
ā¢ /connections - list all your connections</b>"""
    EXTRAMOD_TXT = """<b>Help :</b> <b>Extra Modules</b>

<b>NOTE :</b>
<b>these are the extra features of Auto Filter Bot (Movie Search Bot)</b>

<b>Commands and Usage :</b>
<b>ā¢ /id - get id of a specified user.
ā¢ /info  - get information about a user.
ā¢ /imdb  - get the film information from IMDb source.
ā¢ /search  - get the film information from various sources.</b>"""
    ADMIN_TXT = """<b>Help :</b> <b>Admin mods</b>

<b>NOTE :</b>
<b>This module only works for my admins</b>

<b>Commands and Usage :</b>
<b>ā¢ /logs - to get the rescent errors
ā¢ /stats - to get status of files in db.
ā¢ /delete - to delete a specific file from db.
ā¢ /users - to get list of my users and ids.
ā¢ /chats - to get list of the my chats and ids 
ā¢ /leave  - to leave from a chat.
ā¢ /disable  -  do disable a chat.
ā¢ /ban  - to ban a user.
ā¢ /unban  - to unban a user.
ā¢ /channel - to get list of total connected channels
ā¢ /broadcast - to broadcast a message to all users</b>"""
    STATUS_TXT = """<b>ā¦ļø Total Files :</b> <code>{}</code>
<b>ā¦ļø Total Users :</b> <code>{}</code>
<b>ā¦ļø Total Chats :</b> <code>{}</code>
<b>ā¦ļø Used Storage :</b> <code>{}</code>
<b>ā¦ļø Free Storage :</b> <code>{}</code>"""
    LOG_TEXT_G = """<b>#New_Group</b>
    
<b>įāŗ Group āŖ¼ {}(<code>{}</code>)</b>
<b>įāŗ Total Members āŖ¼ <code>{}</code></b>
<b>įāŗ Added By āŖ¼ {}</b>
"""
    LOG_TEXT_P = """<b>#New_User</b>
    
<b>įāŗ ID - <code>{}</code></b>
<b>įāŗ Name - {}</b>
"""
M_NT_FND = """<b>This Movie Not Found my Database or Not Released This Movie \n\nRequest to Admin</b>"""

