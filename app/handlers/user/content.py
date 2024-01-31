from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command


from app.keyboards.reply import kb_menu, kb_exit
from app.text.main import information
from app.utils.state import Statement
from app.text.main import reply
from app.database.models import check_user_zayvka_to_db

router = Router()


@router.message(F.text.in_(("🔙 Главное меню", "Отмена", "Меню")))
async def main_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.reply(text="Вы вернулись на главное меню!", reply_markup=kb_menu)


@router.message(F.text == "☕️ Связаться с нами")
@router.message(Command("information"))
async def get_information(msg: Message):
    await msg.answer(text=information)


@router.message(F.text == "👨‍💻 Подача заявления на обучение")
@router.message(Command("statement"))
async def get_statement(msg: Message, state: FSMContext):
    await msg.answer("Форма подачи заявления (Пожалуйста будьте внимательны при заполнении)👇\n"
                     "Вы всегда сможете вернуться на главное меню и заполнить анкету заново.")
    await msg.answer("Введите полное ФИО ребенка.", reply_markup=kb_exit)
    await state.set_state(Statement.Child_Name)


@router.message(Statement.Child_Name)
async def get_name_child(msg: Message, state: FSMContext):
    if len(msg.text) <= 10:
        await msg.answer(text="Извините, я не думаю что у вашего ребенка такое ФИО")
    else:
        await state.update_data(child_name=msg.text)
        child_name = await state.get_data()
        print(child_name['child_name'])
        await msg.answer(text="Введите дату рождения ребенка в формате: 11.02.2005")
        await state.set_state(Statement.Child_DateOfBirth)


@router.message(Statement.Child_DateOfBirth)
async def get_data_child(msg: Message, state: FSMContext):
    if len(msg.text) <= 9 or len(msg.text) >= 11:
        await msg.answer(text="Введите дату корректнее! Пример: 11.02.2005")
    else:
        await state.update_data(child_data=msg.text)
        child_data = await state.get_data()
        print(child_data['child_data'])
        await msg.answer(text="Введите место обучения ребенка (Школа/Детский садик/Колледж, к примеру "
                              "Школа №8 или же Нижнекамский политехнический колледж имени Е.Н.Королёва)")
        await state.set_state(Statement.Child_Education)


@router.message(Statement.Child_Education)
async def get_education_child(msg: Message, state: FSMContext):
    await state.update_data(child_education=msg.text)
    child_education = await state.get_data()
    print(child_education['child_education'])
    await msg.answer(text="Введите контактный номер телефона ребенка (Если нет напишите: Нет)\n"
                          "Формат: 89503352178")
    await state.set_state(Statement.Child_Contacts)


@router.message(Statement.Child_Contacts)
async def get_contacts_child(msg: Message, state: FSMContext):
    await state.update_data(child_contacts=msg.text)
    child_contacts = await state.get_data()
    print(child_contacts['child_contacts'])
    await msg.answer(text="Введите ФИО (полное) мамы")
    await state.set_state(Statement.Mother_Name)


@router.message(Statement.Mother_Name)
async def get_name_mother(msg: Message, state: FSMContext):
    await state.update_data(mother_name=msg.text)
    mother_name = await state.get_data()
    print(mother_name['mother_name'])
    await msg.answer(text="Введите ФИО (полное) папы")
    await state.set_state(Statement.Father_Name)


@router.message(Statement.Father_Name)
async def get_name_father(msg: Message, state: FSMContext):
    await state.update_data(father_name=msg.text)
    father_name = await state.get_data()
    print(father_name['father_name'])
    await msg.answer(text="Введите контактный номер телефона для связи с родителями "
                          "Формат: 89503352178")
    await state.set_state(Statement.Parents_Contacts)


@router.message(Statement.Parents_Contacts)
async def get_parents_contacts(msg: Message, bot: Bot, state: FSMContext):
    if len(msg.text) <= 10 or len(msg.text) >= 12:
        await msg.answer(text="Введите корректный номер телефона\n"
                              "Формат: 89503352178")
    else:
        await state.update_data(parents_contacts=msg.text)
        child_name = await state.get_data()
        child_data = await state.get_data()
        child_education = await state.get_data()
        child_contacts = await state.get_data()
        mother_name = await state.get_data()
        father_name = await state.get_data()
        parents_contacts = await state.get_data()
        get_child_name = child_name['child_name']
        get_child_data = child_data['child_data']
        get_child_education = child_education['child_education']
        get_child_contacts = child_contacts['child_contacts']
        get_mother_name = mother_name['mother_name']
        get_father_name = father_name['father_name']
        get_parents_contact = parents_contacts['parents_contacts']
        await check_user_zayvka_to_db(get_child_name, get_child_data, get_child_education, get_child_contacts, get_mother_name, get_father_name, get_parents_contact)
        await msg.answer(text="Ваше заявление успешно отправлено! Спасибо и ожидайте ответа!", reply_markup=kb_menu)
        await bot.send_message(chat_id="-1001993774077", text=reply.format(id=msg.from_user.username, Child_Name=get_child_name, Child_DateOfBirth=get_child_data,
                                                                           Child_Education=get_child_education, Child_Contacts=get_child_contacts,
                                                                           Mother_Name=get_mother_name, Father_Name=get_father_name,
                                                                           Parents_Contacts=get_parents_contact))
        await state.clear()
