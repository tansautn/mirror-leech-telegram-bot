import time
from pprint import pprint

from telethon import TelegramClient
from telethon.tl.types import PeerChannel, DocumentAttributeFilename

# Get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
#  or from https://tjhorner.dev/webogram/#/login
TELEGRAM_API = 13861474
TELEGRAM_HASH = "4296cbe26b464183f8b7d83840cc174c"
api_id = TELEGRAM_API
api_hash = TELEGRAM_HASH

client = TelegramClient('session_name1', api_id, api_hash)
client.start()
GROUP_CHAT_ID = 1673858762
# with TelegramClient('session_name', api_id, api_hash) as client:
#     all_chats = client(functions.messages.GetAllChatsRequest(except_ids = []))
#     print(all_chats)
#     for _, chat in enumerate(all_chats.chats):
#         print(chat)
#         print(chat.title)
# messages = client.get_admin_log()
# print(messages)
group = client.get_entity(PeerChannel(GROUP_CHAT_ID))
# print(group)
file1 = open("dump.json", "w")
c = 0
m = 0
# print(group)
for event in client.iter_admin_log(group, limit=None):
    # print(event)
    # print(type(event))
    # print(hasattr(event, 'to_dict'))
    # print('===============================================')
    # print('')
    # print('')
    # if isinstance(event, ChannelAdminLogEvent):
    #     pprint(event.to_dict())
    if event.deleted_message:
        # print("Dumping message",c, "(", event.old.id, event.old.date,")")
        # file1.write(event.old.to_json() + ",")
        c += 1
        # if "media" in event or event.old.media:
        if hasattr(event.old, 'media') or hasattr(event.old, "document"):
            m += 1
            fname = None
            # curMedia = event.media  if "media" in event else event.old.media
            curMedia = event.old.media if event.old.media else event.old.document
            print('===============================================')
            print('CASE ' + f'{"media" if event.old.media else "document"}')
            pprint(event.old.to_dict())
            if (callable(getattr(curMedia, "to_dict", None))):
                pprint(curMedia.to_dict())
            print(type(curMedia))
            # pprint(curMedia.to_dict())
            print('===============================================')
            if hasattr(curMedia, 'attributes'):
                print(type(curMedia.attributes))
            if hasattr(curMedia, 'attributes'):
                for attr in curMedia.attributes:
                    if isinstance(attr, DocumentAttributeFilename):
                        fname = attr.file_name
            pprint(fname if fname else "nope")
            # client.download_media(curMedia, str(curMedia.attributes.file_name))
            # print(" Dumped media", m)
            print('')
            print('')
            print('')
        time.sleep(3)
