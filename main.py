# Created by Marsify, 2019

import discord
from discord.ext import commands
import random
import config
import rules_and_sets as rns
from database import Table


rules = Table('rules', rns.rule_list)
sets = Table('sets', rns.set_list)

rules.delete_table()
sets.delete_table()

rules.create_table()
sets.create_table()


# Generates a random list of sets and rules based on the specified mode. Used when spinning the wheel.
def generate(mode):
    # Return values
    rule_list = []
    set_list = []
    # Entries from database
    rule_values = []
    set_values = []

    # 'Standard' mode has a separate method of set generation.
    if mode == 'standard':
        rule_values = rules.get_values(1)
        set_list.append(random.choice(sets.get_values(1, 43)))
        set_list.append(random.choice(sets.get_values(44, 79)))
        set_list.append(random.choice(sets.get_values(80)))

        # Loop for rule generation. Appends it to rule_list to later be returned.
        for num in range(3):
            while True:
                pick = random.choice(rule_values)

                if pick not in rule_list:
                    rule_list.append(pick)
                    break

    # Generation methods for everything other than 'standard'.
    else:
        if mode == 'classic':
            rule_values = rules.get_values(1)
            set_values = sets.get_values(1)
        elif mode == 'premodern':
            rule_values = rules.get_values(1)
            set_values = sets.get_values(1, 43)
        elif mode == 'modern':
            rule_values = rules.get_values(1)
            set_values = sets.get_values(44, 79)
        elif mode == 'postmodern':
            rule_values = rules.get_values(1)
            set_values = sets.get_values(80)
        else:
            print('Invalid mode selected. This should be inaccessible. (line 53)')

        # Loop for rule and set generation on non-'standard' modes. Appends it to rule_list and set_list to be returned.
        for num in range(3):
            while True:
                pick = random.choice(rule_values)

                if pick not in rule_list:
                    rule_list.append(pick)
                    break

            while True:
                pick = random.choice(set_values)

                if pick not in set_list:
                    set_list.append(pick)
                    break

    return rule_list, set_list


if __name__ == '__main__':
    # Discord setup
    TOKEN = config.TOKEN
    client = discord.Client()
    bot = commands.Bot(command_prefix='>')

    # Login confirmation
    @client.event
    async def on_ready():
        print("Logged in as {0.user}".format(client))
        print("Version 1.02, August 9th 2020")

    @client.event
    async def on_message(message):
        # Prevents responding to self.
        if message.author == client.user:
            return

        # Main loop that sends the newly generated text to the Discord client.
        if message.content.startswith('>spin the wheel'):
            mode = 'standard'
            message.content = message.content.lower()

            split_message = message.content.split(', ')

            if len(split_message) < 2:
                pass
            elif split_message[1] in ['classic', 'standard', 'premodern', 'modern', 'postmodern']:
                mode = split_message[1]

            full_message = ''  # This is sent at the end of the 'if' statement, and all messages are appended to this.
            gen_rules, gen_sets = generate(mode)  # Depositing rule picks into two sets.
            count = 1

            # Loop that creates a new string message (based on each randomly generated rule)
            # and appends it to full_message.
            full_message = full_message + '**Rules:**'
            for rule in gen_rules:
                rule_message = 'Rule ' + str(count) + ': ' + rule
                count += 1
                full_message = full_message + '\n' + rule_message

            # Same thing as the previous loop, but for sets instead. Dashes are for formatting in Discord.
            full_message = \
                full_message + '\n' + \
                '-------------------------------------------------------------------' \
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
            await message.channel.send(
                'Hi, my name is Pat Sajak, and this is Wheel of Fortune! '
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

    # Bot initiation/logon
    client.run(TOKEN)
