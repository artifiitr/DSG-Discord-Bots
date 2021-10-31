import json
import random
from discord.ext import commands
from Caption import Result

def caption_bot(data): 

    Discord_Token = data['Token']
    bot = commands.Bot(command_prefix=data['Prefix'])

    @bot.listen('on_message')
    async def if_someone_mentions_me(msg):
        if msg.author == bot.user:
            return
        if bot.user.mentioned_in(msg):
            await msg.reply(random.choice(data['if_someone_mentions_me']))    

    @bot.command(name='captn', help=random.choice(data['commands']['captn']))
    async def analyze(ctx):
        try:
            if ctx.message.attachments:
                image_url = ctx.message.attachments[0].url
                if image_url[-3:].lower()=='jpg' or image_url[-3:].lower()=='png' or image_url[-4:].lower()=='jpeg':
                    await ctx.reply(Result(image_url))
                else:
                    await ctx.reply(random.choice(data['invalid_attachment']))                     
            else:
                await ctx.reply(random.choice(data['no_attachment']))
        except Exception as e:
            await ctx.reply(e)

    bot.run(Discord_Token)


def main():
    file = 'config.json'
    with open(file) as f:
        data = json.load(f)
    caption_bot(data)


if __name__ == "__main__":
    main()