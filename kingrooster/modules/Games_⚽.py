from kingrooster import CMD_HELP, OWNER_ID
import os
from kingrooster import tbot
from telethon import *
from telethon import events
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *

from kingrooster import *

from kingrooster.events import register, kingroosterbot

from pymongo import MongoClient
from kingrooster import MONGO_DB_URI

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["kingroosterbot"]
approved_users = db.approve


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


async def inline_query(client, bot, query):
    from telethon import custom

    return custom.InlineResults(
        client,
        await client(
            functions.messages.GetInlineBotResultsRequest(
                bot=bot,
                peer="me",
                query=query,
                offset="",
                geo_point=types.InputGeoPointEmpty(),
            )
        ),
    )


## -- THANKS TO LONAMI FOR THIS FUNCTION --#

# -- MADE BY @Misskingrooster_Robot


@kingroosterbot(pattern="^/gameed")
async def ramdomgames(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "1+2=3"))[0].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/mathbattle$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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

    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/gameed")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/jsusxjxhxhxshsjs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "MotoFX"))[0].click("kingroosterbot")


@register(pattern="^/motofx$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsusxjxhxhxshsjs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/jsuskhfkhdxjzhsjs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Penalty Shooter"))[0].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/penaltyshooter$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsuskhfkhdxjzhsjs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/jslgggfsslaxvuoqdjlxvqs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "F1"))[0].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/racingcar$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jslgggfsslaxvuoqdjlxvqs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/jsdndbbduoqdjlxvqs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Karate"))[1].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/karate$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsdndbbduoqdjlxvqs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/jsdndbafjaffajlxvqs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Football"))[0].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/footballstar$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsdndbafjaffajlxvqs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/jsddjdhiwws")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Neon Blaster"))[0].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/neonblaster$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsddjdhiwws")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/whwyywwhewws")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Disco"))[0].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/discoball$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/whwyywwhewws")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@kingroosterbot(pattern="^/wssksskxxskss")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Gravity"))[0].click(
        "kingroosterbot", hide_via=True
    )


@register(pattern="^/gravityninja$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
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
    chat = "@kingroosterbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/wssksskxxskss")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
**Here are some cool games for you enjoy them, more coming in the future !**

 - /motofx
 - /mathbattle
 - /penaltyshooter
 - /racingcar
 - /karate
 - /footballstar
 - /gravityninja
 - /discoball
 - /neonblaster
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
