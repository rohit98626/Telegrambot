import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to xtr bot.")

# Define the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Available commands:\n/start - Welcome message\n/help - List commands\n/files - List available files and projects\n/getfile <file_name> - Get a specific file or project link\n/social - List social media links")

# File paths or Project links
files_and_projects = {
    "portfolio": "https://github.com/rohit98626/portfolio",
    "YoutubeClone": "https://github.com/rohit98626/youtubeclone",
    "WeatherApp": "https://github.com/rohit98626/weather"
}

# Social Media Links
social_media_links = {
    "LinkedIn": "https://www.linkedin.com/in/rohit-prajapat-878bb2255/",
    "GitHub": "https://github.com/rohit98626",
    "X": "https://x.com/rohitk2319",
    "Instagram": "https://www.instagram.com/rohitk_98/"
}

# Define the /social command
async def social(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "My Social Media Links:\n"
    for key in social_media_links:
        message += f"- {key}: {social_media_links[key]}\n"
    await update.message.reply_text(message)


# /files command to list available files and projects
async def files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Available Files and Projects:\n"
    for key in files_and_projects:
        message += f"- {key}\n"
    message += "Type /getfile <file_name> to download a file or get a project link."
    await update.message.reply_text(message)

# /getfile command to send the requested file or project link
async def getfile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide the file or project name. Example: /getfile project1")
        return

    file_key = context.args[0].lower()
    if file_key in files_and_projects:
        file_path_or_link = files_and_projects[file_key]
        if file_path_or_link.startswith("http"):
            await update.message.reply_text(f"Here is the project link: {file_path_or_link}")
        else:
            try:
                await update.message.reply_document(document=open(file_path_or_link, "rb"))
            except FileNotFoundError:
                await update.message.reply_text("The requested file could not be found on the server.")
            except Exception as e:
                await update.message.reply_text(f"An error occurred: {e}")
    else:
        await update.message.reply_text("File or project not found. Please check the name.")

# Main function to start the bot
def main():
    # Replace 'YOUR_TOKEN' with the token you got from BotFather
    BOT_TOKEN = "7381808982:AAFJ4686wdxzKbUxG7zKVDFG2vRKiRJruwI"  # Store your bot token in an environment variable
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("files", files))
    application.add_handler(CommandHandler("getfile", getfile))
    application.add_handler(CommandHandler("social", social))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()