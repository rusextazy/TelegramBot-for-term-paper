from aiogram.fsm.state import State, StatesGroup


class Statement(StatesGroup):
    Child_Name = State()
    Child_DateOfBirth = State()
    Child_Education = State()
    Child_Contacts = State()
    Mother_Name = State()
    Father_Name = State()
    Parents_Contacts = State()
