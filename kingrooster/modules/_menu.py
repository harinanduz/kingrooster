from kingrooster import CMD_LIST
from kingrooster import tbot
import io
import re
from math import ceil

from telethon import custom, events, Button

from kingrooster.events import register
from kingrooster import CMD_HELP, BOT_VERSION

from telethon import types
from telethon.tl import functions

from pymongo import MongoClient
from kingrooster import MONGO_DB_URI

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["kingrooster"]
approved_users = db.approve
pagenumber = db.pagenumber


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


PM_START_TEXT = (
    "[kingrooster](https://telegra.ph/file/27ce4145ad9e429899bd6.jpg)"
    + "ഇത് KK ARMY എന്ന കോഴിക്കൂടിൻ്റെ ഒഫീഷ്യൽ group management bot . ഒരു രസത്തിന് വേണ്ടി തുടങ്ങിയത് ആണേലും ഇത് ഞങ്ങൾക്ക് ഇപ്പൊ സ്വന്തം എന്ന് പറയാൻ ഒരു ഫാമിലി ആണ് ."
    + "*ഓണേഴ്സ്*"
    + "*[![heavenhater](https://t.me/heavenhater_007)]*"
    + "*[![darkdevil](https://t.me/vaasukionfire7966)]*"
    + "**"
    + "V"
    + BOT_VERSION
    + "**"
)


@register(pattern="^/start$")
async def start(event):
    approved_userss = approved_users.find({})
    for ch in approved_userss:
        iid = ch["id"]
        userss = ch["user"]
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        elif event.chat_id == iid and event.sender_id == userss:
            pass
        else:
            return

    if not event.is_group:
        await tbot.send_message(
            event.chat_id,
            PM_START_TEXT,
            buttons=[
                [
                    Button.url(
                        "Add To Group  👥", "t.me/kingroosterbot?startgroup=true"
                    ),
                    Button.url(
                        "Support Group 🎙️", "https://t.me/kingroosterbotSupport"
                    ),
                ],
                [
                    Button.inline("Commands ❓", data="help_menu"),
                    Button.url(
                        "Source 📀", "https://github.com/sakhaavvaavaj93/kingrooster"
                    ),
                ],
                [
                    Button.url("🌶 കാന്താരി 🌶", url="https://t.me/kanni_manga"),
                    Button.url("കുടുംബം", "https://t.me/KKK_kovila"),
                    Button.url("for pm issues", "https://t.me/@we_will_help_u_bot"),
                ],
                [Button.inline("Close Menu 🔒", data="start_again")],
            ],
        )
    else:
        await event.reply("🐓കൊക്കര കോ........ കോ........🐓")


@tbot.on(events.CallbackQuery(pattern=r"start_again"))
async def start_again(event):
    if not event.is_group:
        await event.edit(
            "The menu is closed 🔒",
            buttons=[[Button.inline("Reopen Menu 🔑", data="reopen_again")]],
        )
    else:
        await event.reply("🐓കൊക്കര കോ........ കോ........🐓")


@tbot.on(events.CallbackQuery(pattern=r"reopen_again"))
async def reopen_again(event):
    if not event.is_group:
        await event.edit(
            PM_START_TEXT,
            buttons=[
                [
                    Button.url(
                        "Add To Group  👥", "t.me/kingroosterbot?startgroup=true"
                    ),
                    Button.url(
                        "Support Group 🎙️", "https://t.me/kingroosterbotsupport"
                    ),
                ],
                [
                    Button.inline("Commands ❓", data="help_menu"),
                    Button.url(
                        "എൻ്റെ ശരീരം", "https://github.com/sakhaavvaavaj93/kingrooster"
                   ),
                ],
                [
                    Button.url("🌶 കാന്താരി 🌶", url="https://t.me/kanni_manga"),
                    Button.url("കുടുംബം", "https://t.me/KKK_kovila"),
                    Button.url("pm issues", "https://t.me/we_will_help_u_bot"),
                ],
                [Button.inline("Close Menu 🔒", data="start_again")],
            ],
        )
    else:
        await event.reply("🐥കൊക്കര....... കോ....... ക്കൊ.......🐥")


@register(pattern="^/help$")
async def help(event):
    approved_userss = approved_users.find({})
    for ch in approved_userss:
        iid = ch["id"]
        userss = ch["user"]
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        elif event.chat_id == iid and event.sender_id == userss:
            pass
        else:
            return
    if not event.is_group:
        buttons = paginate_help(event, 0, CMD_LIST, "helpme")
        await event.reply(PM_START_TEXT, buttons=buttons)
    else:
        await event.reply(
            "Contact me in PM to get the help menu",
            buttons=[[Button.url("Help ❓", "t.me/kingroosterbot?start=help")]],
        )


@register(pattern="^/start help$")
async def help(event):
    approved_userss = approved_users.find({})
    for ch in approved_userss:
        iid = ch["id"]
        userss = ch["user"]
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        elif event.chat_id == iid and event.sender_id == userss:
            pass
        else:
            return
    if not event.is_group:
        buttons = paginate_help(event, 0, CMD_LIST, "helpme")
        await event.reply(PM_START_TEXT, buttons=buttons)
    else:
        await event.reply(
            "Contact me in PM to get the help menu",
            buttons=[[Button.url("Help ❓", "t.me/kingroosterbot?start=help")]],
        )


@tbot.on(events.CallbackQuery(pattern=r"help_menu"))
async def help_menu(event):
    buttons = paginate_help(event, 0, CMD_LIST, "helpme")
    await event.edit(PM_START_TEXT, buttons=buttons)


@tbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"helpme_next\((.+?)\)")))
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = paginate_help(event, current_page_number + 1, CMD_LIST, "helpme")
    await event.edit(buttons=buttons)


@tbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"helpme_prev\((.+?)\)")))
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = paginate_help(event, current_page_number - 1, CMD_LIST, "helpme")
    await event.edit(buttons=buttons)


@tbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"us_plugin_(.*)")))
async def on_plug_in_callback_query_handler(event):
    plugin_name = event.data_match.group(1).decode("UTF-8")
    help_string = ""
    # By @MisskingroosterBeta_Robot

    for i in CMD_LIST[plugin_name]:
        plugin = plugin_name.replace("_", " ")
        emoji = plugin_name.split("_")[0]
        output = str(CMD_HELP[plugin][1])
        help_string = f"Here is the help for **{emoji}**:\n" + output

    if help_string is None:
        pass  # stuck on click
    else:
        reply_pop_up_alert = help_string
    try:
        await event.edit(
            reply_pop_up_alert, buttons=[[Button.inline("🔙 Back", data="go_back")]]
        )
    except BaseException:
        with io.BytesIO(str.encode(reply_pop_up_alert)) as out_file:
            out_file.name = "{}.txt".format(plugin_name)
            await tbot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=plugin_name,
            )


@tbot.on(events.CallbackQuery(pattern=r"go_back"))
async def go_back(event):
    c = pagenumber.find_one({"id": event.sender_id})
    number = c["page"]
    # print (number)
    buttons = paginate_help(event, number, CMD_LIST, "helpme")
    await event.edit(PM_START_TEXT, buttons=buttons)


def get_page(id):
    return pagenumber.find_one({"id": id})


def paginate_help(event, page_number, loaded_plugins, prefix):
    number_of_rows = 3
    number_of_cols = 2

    to_check = get_page(id=event.sender_id)

    if not to_check:
        pagenumber.insert_one({"id": event.sender_id, "page": page_number})

    else:
        pagenumber.update_one(
            {
                "_id": to_check["_id"],
                "id": to_check["id"],
                "page": to_check["page"],
            },
            {"$set": {"page": page_number}},
        )

    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{}".format(x.replace("_", " ")), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⏮️", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("⏹️", data="reopen_again"),
                custom.Button.inline(
                    "⏭️", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs
