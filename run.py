from app.discord_bot.discord__api import client, discord_token


if __name__ == '__main__':
    client.run(discord_token)