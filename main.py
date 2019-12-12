# Created by Marsify, 2019

import discord
from discord.ext import commands
import random
import config
from sets import wheel_sets
from rules import wheel_rules


# Generates a set of possible rules/sets to pick from, and adds each to a set which is then returned.
def generate():
    rule_list = set()
    set_list = set()

    # Loop that generates 3 random rules and sets to deposit in the return values.
    for num in range(3):
        while True:
            pick = random.choice(tuple(wheel_rules))

            if pick not in rule_list:
                rule_list.add(pick)
                break

        while True:
            pick = random.choice(tuple(wheel_sets))

            if pick not in set_list:
                set_list.add(pick)
                break

    return rule_list, set_list


if __name__ == '__main__':
    TOKEN = config.TOKEN
    client = discord.Client()
    bot = commands.Bot(command_prefix='>')

    @client.event
    async def on_ready():
        print("Logged in as {0.user}".format(client))
        print("Version 1.0, December 8th 2019")

    @client.event
    async def on_message(message):
        # Prevents responding to self.
        if message.author == client.user:
            return

        # Main loop that sends the newly generated text to the Discord client.
        if message.content.startswith('>spin the wheel'):
            full_message = ''  # This is sent at the end of the 'if' statement, and all messages are appended to this.
            gen_rules, gen_sets = generate()  # Depositing rule picks into two sets.
            count = 1

            # Loop that creates a new string message (based on each randomly generated rule)
            # and appends it to full_message.
            full_message = full_message + '**Rules:**'
            for rule in gen_rules:
                rule_message = 'Rule ' + str(count) + ': ' + rule
                count += 1
                full_message = full_message + '\n' + rule_message

            # Same thing as the previous loop, but for sets instead. Dashes are for formatting in Discord.
            full_message = full_message + '\n' + '-------------------------------------------------------------------' \
                                                 '-------------------------------------------------------------------' \
                                                 '-----------------'
            full_message = full_message + '\n' + '**Sets:**'
            count = 1
            for set in gen_sets:
                set_message = 'Set ' + str(count) + ': ' + set
                count += 1
                full_message = full_message + '\n' + set_message

            await message.channel.send(full_message)

        # Prints out a list of base rules for the format.
        if message.content.startswith('>help'):
            await message.channel.send('Hi, my name is Pat Sajak, and this is Wheel of Fortune! '
                                       'At the start, a list of 3 rules and sets are generated randomly. Once they are '
                                       'listed, each player has 30 minutes to construct a deck from the given sets of '
                                       'cards, all while keeping in mind the special rules that could help you build '
                                       'a clever deck idea that otherwise wouldn\'t be possible!'
                                       'Aside from adhering to the random sets and rules, there are additional base '
                                       'rules that must be followed:'
                                       '\n1. Your deck must be 40 cards with a max of 3 copies per card, unless stated '
                                       'otherwise.'
                                       '\n2. Players start with 20 health unless stated otherwise.'
                                       '\n3. Players have 30 minutes to construct a deck. If a player has not finished '
                                       'constructing their deck beyond the 30 minute mark, then for each 1 minute '
                                       'over, that player will start with 1 less life, down to half the total starting '
                                       'amount. If no players have finished their decks, then the time limit is '
                                       'extended until at least one person is finished.'
                                       '\n4. Follow the legacy banlist.'
                                       '\n5. Games are performed in best-of-3 matches.'
                                       '\nJust type \'>spin the wheel\' to get started!')

    client.run(TOKEN)
