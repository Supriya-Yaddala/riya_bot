from telegram.ext import Updater,MessageHandler,Filters
import requests
#Get weather updates for a city
#context par represents the telegram api response in json format
def weather(update,context):
  try:
    city=context.message.text
    weather_api_url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=YOUR_WEATHER_API_TOKEN"
    contents=requests.get(weather_api_url).json()
    weather_data=contents['weather'][0]['description']
    update.send_message(chat_id=context.message.chat_id,text=weather_data)
  except:
      update.send_message(chat_id=context.message.chat_id,text="sorry! I can't fetch it😒")
def main():
    #Intialise our bot whose token is as mentioned below and get updates from it (nothing but access telegram api with bot token)
    updater=Updater(token="YOUR_BOT_TOKEN")
    #dispatcher is used to handle the commands given by user
    dp=updater.dispatcher
    #Filters.text is used to recognise messages other than commands
    weather_handler=MessageHandler(Filters.text,weather)
    #add above weather handler (message_handler object) to dispatcher object
    #which calls  weather() on getting certain msg(city_name or city_name,state)
    dp.add_handler(weather_handler)
    #It is used to make connection stable for certain period of time (i.e, timeout=10)
    updater.start_polling()
    updater.idle()
if __name__=='__main__':
    main()
