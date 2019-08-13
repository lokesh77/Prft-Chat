from bot import TelegramChatbot
import gizoogle
bot = TelegramChatbot("config.cfg")


def make_reply(msg):
    reply = None
    if msg is not None:
        reply = gizoogle.text(msg)
    return reply


def leave_balance(name):
    reply = None
    if name is not None:
        reply = gizoogle.pto(name)
    return reply


def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates = bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                # print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text = 'New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == '/buddy':
                    reply = make_reply(first_chat_text)
                    bot.send_message(first_chat_id, 'Hi ' + first_chat_name + ', ' + reply)
                    new_offset = first_update_id + 1
                elif first_chat_text == '/start':
                    reply = make_reply(first_chat_text)
                    bot.send_message(first_chat_id, reply + '😉..')
                    new_offset = first_update_id + 1
                elif first_chat_text == '/Leave_balances':
                    reply = leave_balance(first_chat_name)
                    if reply == None:
                        bot.send_message(first_chat_id, 'PTO available:10 but its fake ping me @vickyboston20 your username and pto detail ill update within 24hours')
                        new_offset = first_update_id + 1
                    else:
                        bot.send_message(first_chat_id, 'PTO available: ' + str(reply[2]))
                        new_offset = first_update_id + 1
                else:
                    reply = make_reply(first_chat_text)
                    bot.send_message(first_chat_id, reply)
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
