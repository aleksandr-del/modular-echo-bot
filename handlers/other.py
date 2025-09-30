#!/usr/bin/env python3


from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon import LEXICON_RU

router = Router(name=__name__)


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU["send_echo"])
