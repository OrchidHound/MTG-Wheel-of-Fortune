# List of all primary sets in Magic the Gathering
set_list = [
    'Alpha [LEA]',
    'Beta [LEB]',
    'Unlimited Edition [2ED]',
    'Arabian Nights [ARN]',
    'Antiquities [ATQ]',
    'Revised Edition [3ED]',
    'Legends [LEG]',
    'The Dark [DRK]',
    'Fallen Empires [FEM]',
    'Fourth Edition [4ED]',
    'Ice Age [ICE]',
    'Chronicles [CHR]',
    'Homelands [HML]',
    'Alliances [ALL]',
    'Mirage [MIR]',
    'Visions [VIS]',
    'Fifth Edition [5ED]',
    'Portal [POR]',
    'Weatherlight [WTH]',
    'Tempest [TMP]',
    'Stronghold [STH]',
    'Exodus [EXO]',
    'Portal Second Age [P02]',
    'Urza\'s Saga [USG]',
    'Urza\'s Legacy [ULG]',
    'Sixth Edition [6ED]',
    'Portal Three Kingdoms [PTK]',
    'Urza\'s Destiny [UDS]',
    'Mercadian Masques [MMQ]',
    'Battle Royale [BRB]',
    'Nemesis [NEM]',
    'Prophecy [PCY]',
    'Invasion [IN]',
    'Beatdown [BTD]',
    'Planeshift [PLS]',
    'Seventh Edition [7ED]',
    'Apocalypse [APC]',
    'Odyssey [ODY]',
    'Torment [TOR]',
    'Judgement [JUD]',
    'Onslaught [ONS]',
    'Legions [LGN]',
    'Scourge [SCG]',
    'Eighth Edition [8ED]',
    'Mirrodin [MRD]',
    'Darksteel [DST]',
    'Fifth Dawn [5DN]',
    'Champions of Kamigawa [CHK]',
    'Betrayers of Kamigawa [BOK]',
    'Saviors of Kamigawa [SOK]',
    'Ninth Edition [9ED]',
    'Ravnica: City of Guilds [RAV]',
    'Guildpact [GPT]',
    'Dissension [DIS]',
    'Coldsnap [CSP]',
    'Time Spiral [TSP]',
    'Planar Chaos [PLC]',
    'Future Sight [FUT]',
    'Tenth Edition [10E]',
    'Lorwyn [LRW]',
    'Morningtide [MOR]',
    'Shadowmoor [SHM]',
    'Eventide [EVE]',
    'Shards of Alara [ALA]',
    'Conflux [CON]',
    'Alara Reborn [ARB]',
    'Magic 2010 [M10]',
    'Zendikar [ZEN]',
    'Worldwake [WWK]',
    'Rise of the Eldrazi [ROE]',
    'Magic 2011 [M11]',
    'Scars of Mirrodin [SOM]',
    'Mirrodin Besieged [MBS]',
    'New Phyrexia [NPH]',
    'Commander [CMD]',
    'Magic 2012 [M12]',
    'Innistrad [ISD]',
    'Dark Ascension [DKA]',
    'Avacyn Restored [AVR]',
    'Magic 2013 [M13]',
    'Return to Ravnica [RTR]',
    'Gatecrash [GTC]',
    'Dragon\'s Maze [DGM]',
    'Magic 2014 [M14]',
    'Theros [THS]',
    'Commander 2013 [C13]',
    'Born of the Gods [BNG]',
    'Journey to Nyx [JOU]',
    'Magic 2015 [M15]',
    'Khans of Tarkir [KTK]',
    'Commander 2014 [C14]',
    'Fate Reforged [FRF]',
    'Dragons of Tarkir [DTK]',
    'Magic Origins [ORI]',
    'Battle for Zendikar [BFZ]',
    'Commander 2015 [C15]',
    'Oath of the Gatewatch [OGW]',
    'Shadows over Innistrad [SOI]',
    'Eldritch Moon [EMN]',
    'Kaladesh [KLD]',
    'Commander 2016 [C16]',
    'Aether Revolt [AER]',
    'Amonkhet [AKH]',
    'Hour of Devestaton [HOU]',
    'Commander 2017 [C17]',
    'Ixalan [XLN]',
    'Rivals of Ixalan [RIX]',
    'Dominaria [DOM]',
    'Battlebond [BBD]',
    'Core Set 2019 [M19]',
    'Commander 2018 [C18]',
    'Guilds of Ravnica [GRN]',
    'Ravnica Allegiance [RNA]',
    'War of the Spark [WAR]',
    'Modern Horizons [MH1]',
    'Core Set 2020 [M20]',
    'Commander 2019 [C19]',
    'Throne of Eldraine [ELD]'
]


# List of all custom game-rules. Lines that are commented out are ones that have been removed because they are not fun
# or too volatile.
rule_list = [
    'If you would lose, you win the game instead.',

    'If a player would draw from an empty library, that player wins the game.',

    # 'Each player begins the game with an Abyssal Persecutor in play.',

    'All creatures have exalted.',

    'All creatures have “{T}: Add one mana of any color.”',

    # 'Each player starts with a Lich\'s Mastery in play.',

    'All spells have delve.',

    'Creature cards in your graveyard have unearth equal to its mana cost.',

    # 'You may play any number of lands on each of your turns.',

    'At the beginning of each player\'s upkeep, that player puts the top 2 cards of their library into '
    'their graveyard.',

    'At the beginning of each player\'s end step, that player puts the cards in their hand on the '
    'bottom of their library in any order, then draws that many cards.',

    'At the beginning of each player\'s end step, if that player has no cards in hand, they draw 7 '
    'cards.',

    'Whenever a non-token creature enters the battlefield, its controller creates a token that\'s a copy '
    'of that creature.',

    'All creatures get +2/+2.',

    'Instant and sorcery cards in graveyards have flashback. The flashback cost is equal to the card\'s '
    'mana cost.',

    'Creature spells cost 2 generic mana less to cast.',

    'Whenever a player casts a spell, that player may draw a card.',

    'All creatures get +1/+1 and have haste.',

    'Whenever a player casts a spell, they take 2 damage. Players start with an additional '
    '10 health.',

    'Players start with an additional 30 health.',

    'Whenever a land enters the battlefield, that land\'s controller creates three 0/1 white Goat '
    'creature tokens.',

    'Each creature assigns combat damage equal to its toughness rather than its power.',

    'Each creature gets +1/+1 for each other creature on the battlefield that shares at least one '
    'creature type with it.',

    'Whenever a player casts a spell, that player may gain 2 life.',

    'All permanents untap during each player\'s untap step.',

    'Whenever a player casts an instant or sorcery spell, that player copies it. The player may choose '
    'new targets for the copy.',

    'Whenever a creature deals combat damage to a player, its controller may draw a card.',

    # 'All creatures get -5/-0.',

    'Whenever a player taps a permanent for mana, that player adds one mana of any type that permanent '
    'produced.',

    # 'Creatures cannot block.',

    'Players play with the top card of their libraries revealed. '
    'You may play the top card of any player’s library.',

    'All lands have “{T}: Add one mana of any color.”',

    'During each player\'s upkeep, that player takes a card at random from their graveyard and puts it '
    'into their hand.',

    # 'If a player casts a spell, they may not attack with creatures until end of turn. '
    # 'If a player attacks with a creature, they may not cast spells until end of turn.',

    'If an effect would create one or more tokens, it creates twice that many of those tokens instead. '
    'If an effect would put one or more counters on a non-planeswalker permanent, it puts twice that '
    'many of those counters on that permanent instead.',

    'Players may cast enchantment spells as though they had flash.',

    # 'Creatures with power 7 or greater can’t attack or block.',

    'Creatures must attack and block each turn if able.',

    'Whenever a player cycles or discards a card, that player '
    'creates a 2/2 blue Drake creature token with flying.',

    'Instant and sorcery spells cost 1 less to cast.',

    'At the beginning of each player\'s end step, if that player has less than 3 cards in hand, they '
    'draw equal to the difference.',

    # 'Players may not cast creature spells if they control 2 or more creatures.',

    # 'Players can only cast 1 spell per turn.',

    # 'Players have Hexproof.',

    'All creatures have Lifelink.',

    'Players may have a maximum of 5 copies per card in their deck.',

    'Artifact spells cost 1 less to cast.',

    'All non-creature artifacts are creatures with power and toughness equal to their casting cost.',

    'If a permanent entering the battlefield causes a triggered ability of a permanent a player '
    'controls to trigger, that ability triggers an additional time.',

    'At the beginning of each player\'s end step, that player proliferates.',

    'Whenever a player attacks with an equipped creature, that player may draw 1 card.',

    'All creatures have Changeling.',

    'Instant and sorcery spells have conspire (When you cast a spell, you may tap two untapped creatures '
    'that share a color with it. When you do, copy it and you may choose different targets for the copy).',

    'At the beginning of each player\'s draw step, that player draws an additional card.',

    'All creatures gain Heroic (Whenever you cast a spell that targets this creature, put a +1/+1 counter '
    'on this creature).',

    'If a source would deal damage to a player or permanent, it deals double that damage instead.  If a '
    'player were to gain life, they gain double that life instead.',

    'At the beginning of the game, each player may search their library for a card, put that card into '
    'their hand, then shuffle their library.',

    'Players may sacrifice two untapped lands to add 5 mana in any combination '
    'of colors to their mana pool."',

    'Whenever a player casts a spell, that player may put a +1/+1 counter on target creature they control.'
]
