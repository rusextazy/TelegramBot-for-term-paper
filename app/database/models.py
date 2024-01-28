import aiosqlite


async def check_user_to_db(name, chat_id):
    async with aiosqlite.connect('app/database/unior_new.db') as connect:
        cursor = await connect.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
        existing_user = await cursor.fetchone()
        if not existing_user:
            await connect.execute('INSERT INTO users (username, chat_id) VALUES (?, ?)', (name, chat_id))
            await connect.commit()
            await cursor.close()


async def check_user_zayvka_to_db(Child_Name_DB, Child_DateOfBirth_DB, Child_Education_DB, Child_Contacts_DB,
                                  Mother_Name_DB, Father_Name_DB, Parents_Contacts_DB):
    async with aiosqlite.connect('app/database/unior_new.db') as connect:
        cursor = await connect.execute(
            'INSERT INTO users_zayvka (Child_Name, Child_DateOfBirth, Child_Education, Child_Contacts, Mother_Name, Father_Name, Parents_Contacts) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (Child_Name_DB, Child_DateOfBirth_DB, Child_Education_DB, Child_Contacts_DB, Mother_Name_DB, Father_Name_DB, Parents_Contacts_DB))
        await connect.commit()
        await cursor.close()
