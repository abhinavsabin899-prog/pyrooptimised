import asyncio
import logging

from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle

from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, PORT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

assistant = Client(
    "Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
)

calls = PyTgCalls(assistant)


@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Music Bot is online! Use /ping.")


@bot.on_message(filters.command("ping"))
async def ping_command(client, message):
    await message.reply_text("Pong! Bot is running.")


async def health_server():
    async def handle(reader, writer):
        writer.write(
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Length: 2\r\n"
            b"Connection: close\r\n\r\nOK"
        )
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    return await asyncio.start_server(
        handle, "0.0.0.0", PORT
    )


async def main():
    server = None
    try:
        await bot.start()
        await assistant.start()
        calls.start()

        server = await health_server()
        logger.info("Bot started successfully")

        await idle()

    finally:
        if server:
            server.close()
            await server.wait_closed()

        calls.stop()
        await assistant.stop()
        await bot.stop()


if __name__ == "__main__":
    asyncio.run(main())
