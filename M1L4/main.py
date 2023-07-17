# This example requires the 'message_content' privileged intent to function.

import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')

        
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$hello'):
            await message.reply('Hello!', mention_author=True)

        elif message.content.startswith('$bye'):
            await message.channel.send("Good bye!")

        elif message.content.startswith('$emooji'):
            emojilist = ["\U0001f600","\U0001f642","\U0001F606", "\U0001F923","\U0001F913"]
            await message.channel.send(emojilist)
        
        elif message.content.startswith('$coin'):
            flip = random.randint(1,2)
            
            if flip == 1 :
                await message.channel.send("Heads!")
            else :
                await message.channel.send("Tails!")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Token')
