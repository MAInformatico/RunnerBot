import logging

from suntime import *
from weather import *

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged

logging.getLogger("httpx").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

async def sunrise(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    verify = get_sunrise()
    await update.message.reply_text("Sunrise (Local time):\n" + str(verify)) 

async def sunset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    verify = get_sunset()
    await update.message.reply_text("Sunset (Local time):\n" + str(verify))

async def weather_temperature(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    verify = convertToCelsius(getWeatherTemperature(getJSON(response)))
    await update.message.reply_text("Current temperature: " + str(verify) + "ºC ")

async def weather_humidity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    verify = getWeatherHumidity(getWeatherTemperature(getJSON(response)))
    await update.message.reply_text("Current humidity: " + str(verify) + "%")

async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("You can use these commands: \n" + "/sunrise to check the time that will sunrise the next day in Granada (in local time)\n" + "/sunset shows the time that will sunrise in Granada\n" + "/temperature real time temperature in Granada\n" + "/humidity real time humidity in Granada\n")


def main():
    application  = Application.builder().token("your_token_here").build()
    
    application.add_handler(CommandHandler("sunrise",sunrise))
    application.add_handler(CommandHandler("sunset",sunset))
    application.add_handler(CommandHandler("temperature",weather_temperature))
    application.add_handler(CommandHandler("humidity",weather_humidity))
    application.add_handler(CommandHandler("help",show_help))
    application.add_error_handler(error)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
