# Created by Orchid Hound, 2019

from requests import get
from json import loads
from shutil import copyfileobj
from dateutil import relativedelta

import datetime
import discord
from discord import app_commands
from discord.ext import commands
import random
import config
import rules


rule_list = rules.rule_list
set_list = [i for i in loads(get(f"https://api.scryfall.com/sets/").text)['data'] if i['set_type'] == 'expansion']


def get_sets(start_date=datetime.datetime(1922, 12, 30), end_date=datetime.datetime.today()):
    output = []
    for mtg_set in set_list:
        set_date = datetime.datetime.strptime(mtg_set['released_at'], "%Y-%m-%d")
        if start_date <= set_date < end_date:
            output.append(mtg_set['name'])
    return output


# Generates a random list of sets and rules based on the specified mode. Used when spinning the wheel.
def generate(mode):
    picked_rules = random.sample(rule_list, 3)
    picked_sets = []
    modern = datetime.datetime(2003, 10, 2)
    post_modern = datetime.datetime.today() - relativedelta.relativedelta(years=7)

    # Generation methods for all modes.
    if mode == 'standard':
        picked_sets.append(random.choice(get_sets(end_date=modern)))
        picked_sets.append(random.choice(get_sets(start_date=modern, end_date=post_modern)))
        picked_sets.append(random.choice(get_sets(start_date=post_modern)))
    elif mode == 'classic':
        picked_sets = random.sample(get_sets(), 3)
    elif mode == 'pre modern':
        picked_sets = random.sample(get_sets(end_date=modern), 3)
    elif mode == 'modern only':
        picked_sets = random.sample(get_sets(start_date=modern, end_date=post_modern), 3)
    elif mode == 'postmodern':
        picked_sets = random.sample(get_sets(start_date=post_modern), 3)
    elif mode == 'modern forward':
        picked_sets = random.sample(get_sets(start_date=modern), 3)
    else:
        print('Invalid mode selected. This should be inaccessible. (line 53)')

    return picked_rules, picked_sets


if __name__ == '__main__':
    # Discord setup
    TOKEN = config.TOKEN
    bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

    # Login confirmation
    @bot.event
    async def on_ready():
        print("Logged in as {0.user}".format(bot))
        print("Version 1.02, August 9th 2020")
        # Sync the command tree and allow slash commands
        await bot.tree.sync()

    @bot.tree.command(name="spin_the_wheel", description="Spin the Wheel of Fortune to get your random sets and rules!")
    @app_commands.choices(choices=[
        app_commands.Choice(name='standard', value='standard'),
        app_commands.Choice(name='classic', value='classic'),
        app_commands.Choice(name='pre-modern', value='pre modern'),
        app_commands.Choice(name='modern only', value='modern only'),
        app_commands.Choice(name='postmodern', value='postmodern'),
        app_commands.Choice(name='modern forward', value='modern forward')
    ])
    async def spin_the_wheel(interaction: discord.Interaction, choices: app_commands.Choice[str]):
        # Main loop that sends the newly generated text to the Discord client.
        full_message = ''  # This is sent at the end of the 'if' statement, and all messages are appended to this.
        full_message = full_message + 'Generating with ' + choices.name + ' mode...\n\n'
        gen_rules, gen_sets = generate(choices.value)  # Depositing rule picks into two sets.
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
        for mtg_set in gen_sets:
            set_message = 'Set ' + str(count) + ': ' + mtg_set
            count += 1
            full_message = full_message + '\n' + set_message

        await interaction.response.send_message(full_message)

    # Bot initiation/logon
    bot.run(TOKEN)
