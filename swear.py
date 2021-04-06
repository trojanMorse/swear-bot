import logging
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
import requests
from bs4 import BeautifulSoup
import smtplib
import random
import emoji

# for random emoji generator
# from itertools import accumulate
# from bisect import bisect
# from unicodedata import name as unicode_name

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(
    token='1758925987:AAH8OJtwQ-Xds0n8d6Rt2vzE987DspdWjTE', use_context=True)
dispatcher = updater.dispatcher


def generate_swear_word():
    adjectives = ["LIBTARD", "RUSTLER", "ROCKET", "HUSTLER", "UNCLE", "CASKET", "BASKET", "HANDS", "LANCE", "MYSTIC", "NUMPTY", "WIZARD", "CRANK", "SQUID", "MUNCHER", "ROCKET", "ROCKET", "ALLEY", "NAZI", "BANDIT", "JEW", "AGRAM", "HANDLE", "MORE", "DREDGER", "BANDIT", "COBBLER", "FOOT", "GOBBLER", "UTENSIL", "TOOL", "BUCKET", "LAWYER", "BOX", "BOX", "JAR", "OCTOPUSS", "PIG", "COFFIN", "LORD", "BISCUIT", "CAKE", "FLASK", "FUDGEPACKER", "GRINDER", "STIRRER", "QUICHE", "LORD", "BORE", "TRUMPET", "CHEESE", "MOLE", "HOBBIT", "MIDGET", "GNOME", "BADGER", "MONK", "FISH", "ZOO", "PIPE", "LOBSTER", "ARTIST", "SHEEP", "FACE", "NOSE", "MUSTARD", "BARON", "STAIN", "SPAMMER", "FIDDLER", "NERD", "STABBER", "MONKEY", "BURGER", "ZIP", "HOLSTER", "TURKEY", "TWIZZLER", "BAT", "SQUIRREL", "BLIZZARD", "JUNKIE", "WIG", "SNORTER", "BOGLE", "WAGON", "WHEEL", "LOAD", "PLANK", "GOBLIN", "PANTS", "SMEAR", "WEASEL", "WIT", "PIANIST", "CELLIST", "NARCISSIST", "LORD", "BINDIPPER",
                  "TOAD", "BREATH", "SUPERHIGHWAY", "TERRORIST", "NINJA", "BOTTLE", "EATER", "PIMP", "PEDANT", "TORTOISE", "BANK", "CAPTAIN", "PUMPKIN", "BIKE", "BOY", "CAFE", "BUNNY", "YAK", "TROMBONE", "BANJO", "HARMONICA", "BRICK", "PRINCESS", "STORM", "FETTLER", "TWIDDLER", "SPANNER", "JELLYFISH", "PILLOW", "FEET", "TOES", "STORE", "MASTER", "LOVER", "SNIFFER", "CHASER", "GEEK", "FINAGLER", "MONSTER", "FUCKER", "CLOWN", "PIRATE", "JACKER", "TEASER", "KISSER", "SUCKER", "WIPE", "BAG", "WAD", "WAFFLE", "SPITTER", "NUTS", "DWARF", "HUMPER", "TROLL", "FUCKER", ".COM", "BOY", "COCKTASTIC", "McSHITSHIT", "SUPREMACIST", "CLAMP", "SUPPORTER", "PEASANT", "OCTO", "NUGGET", "WOMBLE", "DIDDLER", "NIBBLER", "HOSE", "TOUCHER", "BLIZZARD", "TWIZZLER", "JESUS", "BUBBLE", "HEAD", "FLAPS", "WEED", "TITS", "DUMPSTER", "POUCH", "RECEPTICLE", "WIPE", "SORCERER", "PUDDLE", "FERRET", "FACE", "MAGNET", "CANOE", "SANDWICH", "BAGEL", "NUBBIN", "LICKER", "BUTTER", "WHISTLE", "TOKER"]
    nouns = ["BUGGER", "HERPES", "TOSS", "TUMOR", "PISSY", "BENDER", "PISS", "BOLLOCK", "SHAG", "FUCK", "SHIT", "CUNT", "ASS", "PEDO", "TWAT", "COCK", "POOP", "CRAP", "PRICK", "SNOT", "FAG", "ARSEHOLE", "BITCH", "PENIS", "HEPATITIS", "DICK", "STD", "WANK", "JIZZ", "PAP", "GYPSY", "SHITTER", "BUM", "PUKE", "WHORE", "SLAG", "HO", "SAUSAGE", "SCHLONG", "TURKEY", "BAT", "SQUIRREL", "BUTT", "ASSHOLE", "ARSE", "WEINER", "SKANK", "SPECIAL", "TRANNY", "HERMAPHRODITE", "TOTAL", "SYPHILLIS", "VOM", "VOMIT", "ANOREXIC", "KNOB", "PORN", "BASTARD", "PLUM", "BUTTHOLE", "FUCKY", "FUCKING", "BLOODY", "CUM", "WANG", "PILLOW BITING", "FUDGE TUNNEL", "PUBIC", "DOUCHE", "DILDO", "DYKE", "LESBO", "DUMB", "POO", "POOP", "SNATCH", "SKEET", "SHITTY", "SCROTE", "VAG", "BONER", "RIMJOB", "NUTSACK", "GAY", "GAYWAD",
             "HOMO", "POO PIPE", "FANNY", "PIKEY", "CAMELTOE", "BITCH", "HAIRY CLAM", "ASSHAT", "BUTTPLUG", "BOLLOCKING", "DUMBSHIT", "DIPSHIT", "ASSWIPE", "ASSMONKEY", "BUTTMONKEY", "SANDY VAG", "SANDY VAGINA", "FUCKSTICK", "STAIN", "VAG", "STANKY VAG", "STANKY BUTT", "CHEESY BALLS", "MOUTH BREATHER", "REDNECK", "BUTTCRACK", "CRACK", "METH SMOKIN", "PIPE HITTIN", "CRAB", "TINY HANDED", "ERECTION", "CLIT", "WANKER", "WAZZOCK", "BELLEND", "QUIM", "FUCKWIT", "TOSSPOT", "CACK", "GIT", "BUMHOLE", "SHITE", "SHITHOUSE", "GOBSHITE", "TODGER", "CHOAD", "CLUSTERFUCK", "FUCKSTICK", "PECKER", "MANGINA", "STUMP", "TRUMP", "MAGA", "DICKBAG", "CUNTHOOK", "TURD", "SHART", "FART", "CUNTY", "CUNTYBOLLOCK", "CUNTWHISTLE", "THUNDERCUNT", "CUNTFOOT", "SOPPY", "NONCE", "CRAB", "CORONAVIRUS", "PANDEMIC", "COVID-19"]

    swear_word = random.choice(adjectives)+" "+random.choice(nouns)
    return swear_word


def get_swear_word(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=generate_swear_word()+" "+emoji.emojize(':face_with_symbols_on_mouth:'))


swear_handler = CommandHandler('swear', get_swear_word)
dispatcher.add_handler(swear_handler)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a Swear bot motherf**ker"+emoji.emojize(':face_with_symbols_on_mouth:')+"." +
        "   Type /swear to generate a random swear word or just send a message and we'll append a swear word for you "+emoji.emojize(":two_hearts:")+"."+" Type /help if you need help with this bot")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Swear bot motherf**ker"+emoji.emojize(':face_with_symbols_on_mouth:')+"." +
                             "Type /swear to generate a random swear word or just send a message and we'll append a swear word for you "+emoji.emojize(':two_hearts:'))


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text+" "+generate_swear_word() + " ")


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()


# def random_emoji_generator():
#     UNICODE_VERSION = 6

#     # Sauce: http://www.unicode.org/charts/PDF/U1F300.pdf
#     EMOJI_RANGES_UNICODE = {
#         6: [
#             ('\U0001F300', '\U0001F320'),
#             ('\U0001F330', '\U0001F335'),
#             ('\U0001F337', '\U0001F37C'),
#             ('\U0001F380', '\U0001F393'),
#             ('\U0001F3A0', '\U0001F3C4'),
#             ('\U0001F3C6', '\U0001F3CA'),
#             ('\U0001F3E0', '\U0001F3F0'),
#             ('\U0001F400', '\U0001F43E'),
#             ('\U0001F440', ),
#             ('\U0001F442', '\U0001F4F7'),
#             ('\U0001F4F9', '\U0001F4FC'),
#             ('\U0001F500', '\U0001F53C'),
#             ('\U0001F540', '\U0001F543'),
#             ('\U0001F550', '\U0001F567'),
#             ('\U0001F5FB', '\U0001F5FF')
#         ],
#         7: [
#             ('\U0001F300', '\U0001F32C'),
#             ('\U0001F330', '\U0001F37D'),
#             ('\U0001F380', '\U0001F3CE'),
#             ('\U0001F3D4', '\U0001F3F7'),
#             ('\U0001F400', '\U0001F4FE'),
#             ('\U0001F500', '\U0001F54A'),
#             ('\U0001F550', '\U0001F579'),
#             ('\U0001F57B', '\U0001F5A3'),
#             ('\U0001F5A5', '\U0001F5FF')
#         ],
#         8: [
#             ('\U0001F300', '\U0001F579'),
#             ('\U0001F57B', '\U0001F5A3'),
#             ('\U0001F5A5', '\U0001F5FF')
#         ]
#     }

#     NO_NAME_ERROR = '(No name found for this codepoint)'

#     def random_emoji(unicode_version=6):
#         if unicode_version in EMOJI_RANGES_UNICODE:
#             emoji_ranges = EMOJI_RANGES_UNICODE[unicode_version]
#         else:
#             emoji_ranges = EMOJI_RANGES_UNICODE[-1]

#         # Weighted distribution
#         count = [ord(r[-1]) - ord(r[0]) + 1 for r in emoji_ranges]
#         weight_distr = list(accumulate(count))

#         # Get one point in the multiple ranges
#         point = randrange(weight_distr[-1])

#         # Select the correct range
#         emoji_range_idx = bisect(weight_distr, point)
#         emoji_range = emoji_ranges[emoji_range_idx]

#         # Calculate the index in the selected range
#         point_in_range = point
#         if emoji_range_idx != 0:
#             point_in_range = point - weight_distr[emoji_range_idx - 1]

#         # Emoji 😄
#         emoji = chr(ord(emoji_range[0]) + point_in_range)
#         emoji_name = unicode_name(emoji, NO_NAME_ERROR).capitalize()
#         emoji_codepoint = "U+{}".format(hex(ord(emoji))[2:].upper())

#         return (emoji, emoji_codepoint, emoji_name)
#     return(random_emoji(UNICODE_VERSION))
