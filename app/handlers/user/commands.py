from aiogram import Router, types, F, Bot
from aiogram.filters import Command
from aiogram.utils.markdown import hide_link

from app.keyboards.reply import kb_menu
from app.text.main import greeting_text
from app.database.models import check_user_to_db

router = Router()


@router.message(Command("start"))
async def start_cmd(msg: types.Message):
    name = msg.from_user.first_name
    chat_id = msg.from_user.id
    await check_user_to_db(name, chat_id)
    await msg.answer(greeting_text.format(link=f"{hide_link('https://sun9-24.userapi.com/impg/k65JBTDFe98W3J47Qt1E1eqimhqyI08pHCU4bA/71TL-fcSHmI.jpg?size=1600x1066&quality=95&sign=fe8b9e67d3e0934d706639543bcf6441&type=album')}"),
                     reply_markup=kb_menu)
