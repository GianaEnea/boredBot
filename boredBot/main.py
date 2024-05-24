import requestHandler
import time

# init bot 
bot = requestHandler.rh()
lastUpdateId = None
# bot in funzione
while True:
    
    updates = bot.getUpdates(lastUpdateId)
    if updates['ok'] == False:
        print("errore telegram -> " + updates['description'])
    else:
        updates = updates['result']
        # se il messaggio non è vuoto
        if len(updates) > 0:
            # controllo se nel messaggio c'è il campo text che vuol dire che il mesaggio è un testo e non una posizione o un'immagine
            if 'text' in updates[-1]['message']:
                text = updates[-1]['message']['text']
                chat_id = updates[-1]['message']['chat']['id']
                user_id = updates[-1]['message']['from']['id']
                lastUpdateId = updates[-1]['update_id'] + 1
                # avvio del bot
                if text == 'Bored':
                    data = bot.getactivity()
                    activity = str(data['activity'])
                    type = str(data['type'])
                    participants = str(data['participants'])
                    bot.sendMessage(chat_id, "Ok, here's an activity you can do to not be bored anymore: " + activity + "\r\n"
                                    "Type of activity: " + type + "\r\n" + 
                                    "Minimum participants for the activity: " + participants+ "\r\n")

        time.sleep(5)
