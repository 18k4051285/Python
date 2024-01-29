
import datetime #for logtime
import logging #for logging
from decouple import config #for .env
import mysql.connector #for mysql connection
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


#Sql info
DB_HOST = config('DB_HOST')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.

# Start Funtion
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    user_id = user.id
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Your Telegram ID is {user_id}.",
        #reply_markup=ForceReply(selective=True),
    )
    help_text = """
    Trung tâm trợ giúp
    /start - Hướng dẫn sử dụng
    /id - Thông tin theo ID
    /phone - Thông tin theo sdt
    """
    await update.message.reply_text(help_text)

# Log commands
def log_command(parameter, user_id, command):
    """Log the executed command to a text file."""
    log_file_path = 'command_log.txt'
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{current_time} - User ID: {user_id} , Command: {command}, Parameter: {parameter}\n")

# ID , Find data with ID
async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /info is issued."""
    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME  # Add your actual database name
        )

        # Extract the parameter from the command
        id = context.args[0] if context.args else None
        log_command(id, update.effective_user.id, "/id")
        # Execute a SELECT query with the parameter
        cursor = mydb.cursor()
        #if username:
        cursor.execute("SELECT * FROM tb_users WHERE ID = %s", (id,))
        #else:
        #   cursor.execute("SELECT * FROM tb_users")

        # Fetch the results
        result = cursor.fetchall()

        # Display the results in the chat
        if result:
            message = f"Data for user {id}:\n" if id else "Data from the database:\n"
            for row in result:
                id, name, phone, address = row
                message += f" ID: {id} \n Name: {name} \n Phone : {phone} \n Address: {address}\n"

            # Check if the message length exceeds the limit
            if len(message) > 4096:
                message = "Data from the database is too large to display. Consider refining your query."

            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Can't Find.")

    except mysql.connector.Error as err:
        await update.message.reply_text(f"Error: {err}")
    finally:
        # Close the database connection
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
        #    await update.message.reply_text("MySQL connection closed.")

# Phone , Find data with phone
async def phone_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /info is issued."""
    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME  # Add your actual database name
        )

        # Extract the parameter from the command
        phone = context.args[0] if context.args else None
        log_command(phone, update.effective_user.id, "/phone")
        # Execute a SELECT query with the parameter
        cursor = mydb.cursor()
        #if username:
        cursor.execute("SELECT * FROM tb_users WHERE phone = %s", (phone,))
        #else:
        #   cursor.execute("SELECT * FROM tb_users")

        # Fetch the results
        result = cursor.fetchall()

        # Display the results in the chat
        if result:
            message = f"Data for phone number {phone}:\n" if phone else "Data from the database:\n"
            for row in result:
                id, name, phone, address = row
                message += f" ID: {id} \n Name: {name} \n Phone : {phone} \n Address: {address}\n"

            # Check if the message length exceeds the limit
            if len(message) > 4096:
                message = "Data from the database is too large to display. Consider refining your query."

            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Can't Find.")

    except mysql.connector.Error as err:
        await update.message.reply_text(f"Error: {err}")
    finally:
        # Close the database connection
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
        #    await update.message.reply_text("MySQL connection closed.")
# name , Find data with name
async def name_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /info is issued."""
    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME  # Add your actual database name
        )

        # Extract the parameter from the command
        name = context.args[0] if context.args else None
        log_command(name, update.effective_user.id, "/name")
        # Execute a SELECT query with the parameter
        cursor = mydb.cursor()
        #if username:
        cursor.execute("SELECT * FROM tb_users WHERE name = %s", (name,))
        #else:
        #   cursor.execute("SELECT * FROM tb_users")

        # Fetch the results
        result = cursor.fetchall()

        # Display the results in the chat
        if result:
            message = f"Data for user {name}:\n" if name else "Data from the database:\n"
            for row in result:
                id, name, phone, address = row
                message += f" ID: {id} \n Name: {name} \n Phone : {phone} \n Address: {address}\n"

            # Check if the message length exceeds the limit
            if len(message) > 4096:
                message = "Data from the database is too large to display. Consider refining your query."

            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Can't Find.")

    except mysql.connector.Error as err:
        await update.message.reply_text(f"Error: {err}")
    finally:
        # Close the database connection
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
        #    await update.message.reply_text("MySQL connection closed.")
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Trung tâm trợ giúp
/info - Hồ sơ và số dư
/help - Trung tâm trợ giúp
/id - Thông tin ID

"""

    await update.message.reply_text(help_text)
# Echo for test

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("1451276513:AAESGi6khiOLAehox_linvMhjOpGvtjz3nU").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("phone", phone_command))
    application.add_handler(CommandHandler("id", id_command))
    application.add_handler(CommandHandler("name", name_command))
    application.add_handler(CommandHandler("help", help_command))
    #application.add_handler(CommandHandler("echo", echo))
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
