import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from suntime import *
from weather import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def weather(update, context):
    update.message.reply_text("Check weather on this link (also available in English too): https://www.eltiempo.es")

def sunrise(update, context):
    verify = getSunrise()
    update.message.reply_text("Sunrise (UTC time):\n" + str(verify)) 

def sunset(update, context):
    verify = getSunset()
    update.message.reply_text("Sunset (UTC time):\n" + str(verify))

def weatherTemperature(update,context):
    verify = convertToCelsius(getWeatherTemperature(getJSON(response)))
    update.message.reply_text("Current temperature: " + str(verify) + "ºC ")

def weatherHumidity(update,context):
    verify = getWeatherHumidity(getWeatherTemperature(getJSON(response)))
    update.message.reply_text("Current humidity: " + str(verify) + "%")

def showHelp(update, context):
    update.message.reply_text("You can use these commands: \n" + "/weather to check the page eltiempo.es\n" + "/sunrise to check the time that will sunrise the next day in Granada (it is showed in UTC time)\n" + "/sunset shows the time that will sunrise in Granada\n" + "/temperature real time temperature in Granada\n" + "/humidity real time humidity in Granada\n")


def main():
    updater = Updater("your_token_here", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(CommandHandler("sunrise",sunrise))
    dp.add_handler(CommandHandler("sunset",sunset))
    dp.add_handler(CommandHandler("temperature",weatherTemperature))
    dp.add_handler(CommandHandler("humidity",weatherHumidity))


    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
