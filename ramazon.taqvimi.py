import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types , F 
from aiogram.types import KeyboardButton
from aiogram.types import Message , FSInputFile
from aiogram.filters import Command
from aiogram.enums import ParseMode
from bs4 import BeautifulSoup as BS
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import and_f
logging.basicConfig(level=logging.INFO)
import time


from datetime import datetime, timedelta
hozirgi_vaqt = datetime.utcnow() + timedelta(hours=5)
# hozirgi_vaqt = datetime(2024, 3, 15, 7, 0)
print("vaqt", hozirgi_vaqt)

bot = Bot(token="6962226645:AAFAqHPQ81_ngiLRhCUXUvlQpC5jyw-44HQ")
dp = Dispatcher()
kb = [
       [KeyboardButton(text="🌦 𝗢𝗯-𝗵𝗮𝘃𝗼")],
        [KeyboardButton(text="🕌 𝗥𝗮𝗺𝗮𝘇𝗼𝗻 𝘁𝗮𝗾𝘃𝗶𝗺𝗶")],
        [KeyboardButton(text="👨🏻‍💻 𝗗𝗮𝘀𝘁𝘂𝗿𝗰𝗵𝗶"),
        KeyboardButton(text="💡 𝗤𝗼'𝗹𝗹𝗮𝗻𝗺𝗮")
         ]
    ]


@dp.message(Command("start"))
async def rasmy(message: types.Message):
    p="https://t.me/databazatg/10"
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,)
    await bot.send_photo(message.chat.id, photo=p)
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard)


async def send_message():
    while True:
        now = datetime.utcnow() + timedelta(hours=5)
        if now.hour == 1 and now.minute == 5:
            await bot.send_message(chat_id='6167775229', text='Saharlik vaqti!')
        elif now.hour == 1 and now.minute == 5:
            await bot.send_message(chat_id='-1001245719246', text='Iftorlik vaqti!')
        


    


@dp.message(F.text == "🔙 𝗼𝗿𝗾𝗮𝗴𝗮")
async def orqaga(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,)
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard)


#Urganch
t = requests.get('https://sinoptik.ua/погода-Ургенч')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]
    print(t_min, t_max)
response = BS(t.content, 'html.parser')
def obi_xovo():
    obixovo = ''
    for i in range(0,7):
        for res in response.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
hafta1 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h1")]])
@dp.callback_query(F.data == "h1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo()}",
        show_alert=True)  
@dp.message(F.text == "🌦 𝗨𝗿𝗴𝗮𝗻𝗰𝗵")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELkixl3zW56O_99cUVfYBRKdHXUt2RqgAC8QIAAvLOeEUX5ebln59E_jQE")
    await message.reply(f"⛅️ Bugun Urganchda Ob Havo \n\n 🌝 Kunduzi  {t_max} \n 🌚Kechqurun {t_min} \n\n 💫 Boʻlishi kutilmoqda",
        reply_markup=hafta1)




# Andijon
t1 = requests.get('https://sinoptik.ua/погода-андижан')
html_t = BS(t1.content, 'html.parser')

for el in html_t.select('#content'):
    min1 = el.select('.temperature .min')[0].text
    max1 = el.select('.temperature .max')[0].text
    t_min1 = min1[4:]
    t_max1 = max1[5:]
@dp.message(F.text == "🌦 𝗔𝗻𝗱𝗶𝗷𝗼𝗻")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELn85l6GyHGXnnJwmsewYbsm7Qkb90owACiQMAAkrxcUW4MSXnTX-zpDQE")
    await message.reply(f"⛅️ Bugun Andijonda Ob Havo \n\n 🌝 Kunduzi  {t_max1} \n 🌚Kechqurun {t_min1} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta2)
t1 = requests.get('https://sinoptik.ua/погода-андижан')
response1 = BS(t1.content, 'html.parser')
def obi_xovo1():
    obixovo = ''
    for i in range(0,7):
        for res in response1.select("#content"):
            hmin1 = res.select(".temperature .min")[i].text
            min1 = hmin1[4:]
            hmax1 = res.select(".temperature .max")[i].text
            max1 = hmax1 [5:]
            sana1 = res.select(".month")[i].text
            sana= res.select(".date")[i].text
        obixovo += sana + " " + sana1 + " " + "🏞 Kun :" + " " +  max1 + ' ' + "🌃 Tun :" + " " + min1 + '\n'
    return obixovo
hafta2 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h2")]])
@dp.callback_query(F.data == "h2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo1()}",
        show_alert=True)





# *********
t2 = requests.get('https://sinoptik.ua/погода-бухара')
html_t = BS(t2.content, 'html.parser')
for el in html_t.select('#content'):
    min2 = el.select('.temperature .min')[0].text
    max2 = el.select('.temperature .max')[0].text
    t_min2 = min2[4:]
    t_max2 = max2[5:]
@dp.message(F.text == "🌦 𝗕𝘂𝘅𝗼𝗿𝗼")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELkixl3zW56O_99cUVfYBRKdHXUt2RqgAC8QIAAvLOeEUX5ebln59E_jQE")
    await message.reply(f"⛅️ Bugun Buxoroda Ob Havo \n\n 🌝 Kunduzi  {t_max2} \n 🌚Kechqurun {t_min2} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta3)
response2 = BS(t2.content, 'html.parser')
def obi_xovo2():
    obixovo = ''
    for i in range(0,7):
        for res in response2.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
hafta3 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h3")]])
@dp.callback_query(F.data == "h3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo2()}",
        show_alert=True)
    







# **********
t3 = requests.get('https://sinoptik.ua/погода-фергана')
html_t = BS(t3.content, 'html.parser')

for el in html_t.select('#content'):
    min3 = el.select('.temperature .min')[0].text
    max3 = el.select('.temperature .max')[0].text
    t_min3 = min3[4:]
    t_max3 = max3[5:]
@dp.message(F.text == "🌦 𝗙𝗮𝗿𝗴'𝗼𝗻𝗮")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELkixl3zW56O_99cUVfYBRKdHXUt2RqgAC8QIAAvLOeEUX5ebln59E_jQE")   
    await message.reply(f"⛅️ Bugun Farg'onada Ob Havo \n\n 🌝 Kunduzi  {t_max3} \n 🌚Kechqurun {t_min3} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta4)
response3 = BS(t3.content, 'html.parser')
def obi_xovo3():
    obixovo = ''
    for i in range(0,7):
        for res in response3.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
hafta4 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h4")]])
@dp.callback_query(F.data == "h4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo3()}",
        show_alert=True)
    





# **********
t4 = requests.get('https://sinoptik.ua/погода-гулистан')
html_t = BS(t4.content, 'html.parser')

for el in html_t.select('#content'):
    min4 = el.select('.temperature .min')[0].text
    max4 = el.select('.temperature .max')[0].text
    t_min4 = min4[4:]
    t_max4 = max4[5:]
@dp.message(F.text == "🌦 𝗚𝘂𝗹𝗶𝘀𝘁𝗼𝗻")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELn9Bl6GzWMB2RCDE57bCq4W-bc2qyzwACawMAAg3qGUQoC2o9htJrQTQE")
    await message.reply(f"⛅️ Bugun Gulistonda Ob Havo \n\n 🌝 Kunduzi  {t_max4} \n 🌚Kechqurun {t_min4} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta5)

response4 = BS(t4.content, 'html.parser')
def obi_xovo4():
    obixovo = ''
    for i in range(0,7):
        for res in response4.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
    
hafta5 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h5")]])

@dp.callback_query(F.data == "h5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo4()}",
        show_alert=True)
    





# **********
t5 = requests.get('https://sinoptik.ua/погода-джизак')
html_t = BS(t5.content, 'html.parser')

for el in html_t.select('#content'):
    min5 = el.select('.temperature .min')[0].text
    max5 = el.select('.temperature .max')[0].text
    t_min5 = min5[4:]
    t_max5 = max5[5:]
@dp.message(F.text == "🌦 𝗝𝗶𝘇𝘇𝗮𝘅")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELkixl3zW56O_99cUVfYBRKdHXUt2RqgAC8QIAAvLOeEUX5ebln59E_jQE")
    await message.reply(f"⛅️ Bugun Jizzaxda Ob Havo \n\n 🌝 Kunduzi  {t_max5} \n 🌚Kechqurun {t_min5} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta6)

response5 = BS(t5.content, 'html.parser')
def obi_xovo5():
    obixovo = ''
    for i in range(0,7):
        for res in response5.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
    

hafta6 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h6")]])

@dp.callback_query(F.data == "h6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo5()}",
        show_alert=True)
    





# **********
t6 = requests.get('https://sinoptik.ua/погода-наманган')
html_t = BS(t6.content, 'html.parser')

for el in html_t.select('#content'):
    min6 = el.select('.temperature .min')[0].text
    max6 = el.select('.temperature .max')[0].text
    t_min6 = min6[4:]
    t_max6 = max6[5:]
@dp.message(F.text == "🌦 𝗡𝗮𝗺𝗮𝗻𝗴𝗮𝗻")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Namanganda Ob Havo \n\n 🌝 Kunduzi  {t_max6} \n 🌚Kechqurun {t_min6} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta7)

response6 = BS(t6.content, 'html.parser')
def obi_xovo7():
    obixovo = ''
    for i in range(0,7):
        for res in response6.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
    

hafta7 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h7")]])

@dp.callback_query(F.data == "h7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo7()}",
        show_alert=True)






t7 = requests.get('https://sinoptik.ua/погода-Навои')
html_t = BS(t7.content, 'html.parser')

for el in html_t.select('#content'):
    min7 = el.select('.temperature .min')[0].text
    max7 = el.select('.temperature .max')[0].text
    t_min7 = min7[4:]
    t_max7 = max7[5:]
@dp.message(F.text == "🌦 𝗡𝗮𝘃𝗼𝗶")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELn8Bl6GZdGHWcUu6fR1J-mD3jNmcuGgACEwIAAsNveUU2phWUZqEYXDQE")
    await message.reply(f"⛅️ Bugun Navoida Ob Havo \n\n 🌝 Kunduzi  {t_max7} \n 🌚Kechqurun {t_min7} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta8)

response7 = BS(t7.content, 'html.parser')
def obi_xovo8():
    obixovo = ''
    for i in range(0,7):
        for res in response7.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
    

hafta8 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h8")]])

@dp.callback_query(F.data == "h8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo8()}",
        show_alert=True)
    





t13 = requests.get('https://sinoptik.ua/погода-хива')
html_t = BS(t13.content, 'html.parser')

for el in html_t.select('#content'):
    min13 = el.select('.temperature .min')[0].text
    max13 = el.select('.temperature .max')[0].text
    t_min13 = min13[4:]
    t_max13 = max13[5:]
@dp.message(F.text == "🌦 𝗫𝗶𝘃𝗮")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELn85l6GyHGXnnJwmsewYbsm7Qkb90owACiQMAAkrxcUW4MSXnTX-zpDQE")
    await message.reply(f"⛅️ Bugun Qarshida Ob Havo \n\n 🌝 Kunduzi  {t_max13} \n 🌚Kechqurun {t_min13} \n\n 💫 Boʻlishi kutilmoqda ",
                         reply_markup=hafta13)

#haftalik
response13 = BS(t13.content, 'html.parser')
def obi_xovo13():
    obixovo = ''
    for i in range(0,7):
        for res in response13.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
hafta13 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h13")]])
@dp.callback_query(F.data == "h13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo13()}",
        show_alert=True)







t8 = requests.get('https://sinoptik.ua/погода-самарканд')
html_t = BS(t8.content, 'html.parser')

for el in html_t.select('#content'):
    min9 = el.select('.temperature .min')[0].text
    max9 = el.select('.temperature .max')[0].text
    t_min9 = min9[4:]
    t_max9 = max9[5:]
@dp.message(F.text == "🌦 𝗦𝗮𝗺𝗮𝗿𝗾𝗮𝗻𝗱")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELkixl3zW56O_99cUVfYBRKdHXUt2RqgAC8QIAAvLOeEUX5ebln59E_jQE")
    await message.reply(f"⛅️ Bugun Samarqandda Ob Havo \n\n 🌝 Kunduzi  {t_max9} \n 🌚Kechqurun {t_min9} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta9)
#haftalik
response8 = BS(t8.content, 'html.parser')
def obi_xovo9():
    obixovo = ''
    for i in range(0,7):
        for res in response8.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
hafta9 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h9")]])
@dp.callback_query(F.data == "h9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo9()}",
        show_alert=True)







t9 = requests.get('https://sinoptik.ua/погода-термез')
html_t = BS(t9.content, 'html.parser')

for el in html_t.select('#content'):
    min10 = el.select('.temperature .min')[0].text
    max10 = el.select('.temperature .max')[0].text
    t_min10 = min10[4:]
    t_max10 = max10[5:]
@dp.message(F.text == "🌦 𝗧𝗲𝗿𝗺𝗶𝘇") 
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELn7xl6GYgPglg7He07e3zcBaez_g30QACawMAAg3qGUQoC2o9htJrQTQE")
    await message.reply(f"⛅️ Bugun Termizda Ob Havo \n\n 🌝 Kunduzi  {t_max10} \n 🌚Kechqurun {t_min10} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta10)

#haftalik
response9 = BS(t9.content, 'html.parser')
def obi_xovo10():
    obixovo = ''
    for i in range(0,7):
        for res in response9.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
hafta10 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h10")]])
@dp.callback_query(F.data == "h10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo10()}",
        show_alert=True)
#погода-ташкент
    




t10 = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(t10.content, 'html.parser')

for el in html_t.select('#content'):
    min11 = el.select('.temperature .min')[0].text
    max11 = el.select('.temperature .max')[0].text
    t_min11 = min11[4:]
    t_max11 = max11[5:]
@dp.message(F.text == "🌦 𝗧𝗼𝘀𝗵𝗸𝗲𝗻𝘁")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELkixl3zW56O_99cUVfYBRKdHXUt2RqgAC8QIAAvLOeEUX5ebln59E_jQE") 
    await message.reply(f"⛅️ Bugun Toshkentda Ob Havo \n\n 🌝 Kunduzi  {t_max11} \n 🌚Kechqurun {t_min11} \n\n 💫 Boʻlishi kutilmoqda ",
                        reply_markup=hafta11)
#haftalik
response10 = BS(t10.content, 'html.parser')
def obi_xovo11():
    obixovo = ''
    for i in range(0,7):
        for res in response10.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo






hafta11 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h11")]])
@dp.callback_query(F.data == "h11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo11()}",
        show_alert=True)   
#погода-зарафшан
t11 = requests.get('https://sinoptik.ua/погода-зарафшан')
html_t = BS(t11.content, 'html.parser')

for el in html_t.select('#content'):
    min12 = el.select('.temperature .min')[0].text
    max12 = el.select('.temperature .max')[0].text
    t_min12 = min12[4:]
    t_max12 = max12[5:]
@dp.message(F.text == "🌦 𝗭𝗮𝗿𝗮𝗳𝘀𝗵𝗼𝗻")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELn8Bl6GZdGHWcUu6fR1J-mD3jNmcuGgACEwIAAsNveUU2phWUZqEYXDQE")
    await message.reply(f"⛅️ Bugun Zarafshonda Ob Havo \n\n 🌝 Kunduzi  {t_max12} \n 🌚Kechqurun {t_min12} \n\n 💫 Boʻlishi kutilmoqda",
                        reply_markup=hafta12)
 
#haftalik
response11 = BS(t11.content, 'html.parser')
def obi_xovo12():
    obixovo = ''
    for i in range(0,7):
        for res in response11.select("#content"):
            hmin = res.select(".temperature .min")[i].text
            min = hmin[4:]
            hmax = res.select(".temperature .max")[i].text
            max = hmax [5:]
            sana = res.select(".month")[i].text
            sana1 = res.select(".date")[i].text
            hafta = res.select('.day-link')[i].text
        obixovo += sana1 + " " + sana + " " + "🏞 Kun :" + " " +  max + ' ' + "🌃 Tun :" + " " + min + '\n'
    return obixovo
hafta12 = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓 Haftalik Ob-Havo",callback_data = "h12")]])
@dp.callback_query(F.data == "h12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text=f"      🗓 Haftalik Ob-Havo:\n\n{obi_xovo12()}",
        show_alert=True)




@dp.message(F.text == "🌦 𝗢𝗯-𝗵𝗮𝘃𝗼")
async def obhavo(message: types.Message):
    
    knopka = [
            [
                types.KeyboardButton(text="🌦 𝗨𝗿𝗴𝗮𝗻𝗰𝗵"),
        ],
        [
                types.KeyboardButton(text="🌦 𝗔𝗻𝗱𝗶𝗷𝗼𝗻"),
                types.KeyboardButton(text="🌦 𝗕𝘂𝘅𝗼𝗿𝗼"),
                types.KeyboardButton(text="🌦 𝗙𝗮𝗿𝗴'𝗼𝗻𝗮"),
        ],
        [
                types.KeyboardButton(text="🌦 𝗚𝘂𝗹𝗶𝘀𝘁𝗼𝗻"),
                types.KeyboardButton(text="🌦 𝗝𝗶𝘇𝘇𝗮𝘅"),
                types.KeyboardButton(text="🌦Namangan"),
        ],
         [
                types.KeyboardButton(text="🌦 𝗡𝗮𝘃𝗼𝗶"),
                types.KeyboardButton(text="🌦 𝗫𝗶𝘃𝗮"),
                types.KeyboardButton(text="🌦 𝗦𝗮𝗺𝗮𝗿𝗾𝗮𝗻𝗱"),
        ],
         [
                types.KeyboardButton(text="🌦 𝗧𝗲𝗿𝗺𝗶𝘇"),
                types.KeyboardButton(text="🌦 𝗧𝗼𝘀𝗵𝗸𝗲𝗻𝘁"),
                types.KeyboardButton(text="🌦 𝗭𝗮𝗿𝗮𝗳𝘀𝗵𝗼𝗻"),
        ],
        [       types.KeyboardButton(text="🔙 𝗼𝗿𝗾𝗮𝗴𝗮")]
        ]


    keyboard = types.ReplyKeyboardMarkup(
        keyboard=knopka,
        resize_keyboard=True, )
    
    gif_url = 'https://t.me/databazatg/4'
    await bot.send_document(message.chat.id, gif_url)

    await message.answer(f"<b>{message.from_user.full_name}</b> \n 🤔hududni tanlang",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard)



@dp.message(F.text == "💡 𝗤𝗼'𝗹𝗹𝗮𝗻𝗺𝗮")
async def with_puree(message: types.Message):
    v="https://t.me/databazatg/12"
    await bot.send_video(message.chat.id, video=v)



@dp.message(F.text == "👨🏻‍💻 𝗗𝗮𝘀𝘁𝘂𝗿𝗰𝗵𝗶")
async def with_puree(message: types.Message):
 await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELkiBl3zLcrgq4tpZcpCC8x9ZZ34J5ygACBQMAArAxGUQ-kCLtqQSXiTQE",
                        reply_markup=dasturchi)
dasturchi = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="👨🏻‍💻 Dasturch",url="https://t.me/j_dev")]])


grtugma = types.InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="🗓𝗵𝗮𝗳𝘁𝗮𝗹𝗶𝗸 𝗼𝗯-𝗵𝗮𝘃𝗼",url="https://t.me/Ob_havo_jbot")],
                    [ types.InlineKeyboardButton(text="🤲𝗦𝗮𝗵𝗮𝗿𝗹𝗶𝗸 𝗱𝘂𝗼𝘀𝗶",callback_data = "gr1")],
                    [ types.InlineKeyboardButton(text="🤲𝗜𝗳𝘁𝗼𝗿𝗹𝗶𝗸 𝗱𝘂𝗼𝘀𝗶",callback_data = "gr2")],
                    [ types.InlineKeyboardButton(text="💡 𝗤𝗼'𝗹𝗹𝗮𝗻𝗺𝗮",callback_data = "gr3")],
    ])

@dp.message(F.text.lower()=="salom",F.chat.type=="supergroup")
async def yordam(message:Message):
    await message.reply("🤔Bugun Ramazon oyining \n   nechanchi kuni?\nTartib raqamini yozib yuboring")

@dp.callback_query(F.data == "gr1")
async def grt(callback: types.CallbackQuery):
    await callback.answer(text="""🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.""",show_alert=True)

@dp.callback_query(F.data == "gr2")
async def grt(callback: types.CallbackQuery):
    await callback.answer(text="""🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.""",show_alert=True)

@dp.callback_query(F.data == "gr3")
async def grt(callback: types.CallbackQuery):
    await callback.answer(text=f"💡 𝗤𝗼'𝗹𝗹𝗮𝗻𝗺𝗮\n\nGuruhda Ramazon Taqvimi\nkoʻrish uchun Tartib raqam \nyuboring . 1dan 30gacha ♻️\n(bu Ramazon oyining kunlari)",show_alert=True)


@dp.message(F.text=="1", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
        #saharlik
    saharlik1 = datetime(2024, 3, 11, 6, 1)
    qoldi = saharlik1 - hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik1 = datetime(2024, 3, 11, 18, 59)
    qoldi1 = iftorlik1 - hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60


    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 11:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 11-Mart , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 1-kuni \n🌝Saharlik : 06:01 \n🌚Iftorlik  18:59\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete()         
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 11-Mart , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 1-kuni \n🌝Saharlik : 06:01 \n🌚Iftorlik  18:59\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete()             
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="2", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
        
        #saharlik
    saharlik2 = datetime(2024, 3, 12, 5, 59)
    qoldi = saharlik2 - hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 12, 19, 00)
    qoldi1 = iftorlik2 - hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 12:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 12-Mart , Seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 2-kuni \n🌝Saharlik : 5:59 \n🌚Iftorlik  19:00\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev,",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 12-Mart , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 2-kuni \n🌝Saharlik : 5:59 \n🌚Iftorlik  19:00\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 


@dp.message(F.text=="3", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
        #saharlik
    saharlik2 = datetime(2024, 3, 13, 5, 58)
    qoldi = saharlik2 - hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 13, 19, 1)
    qoldi1 = iftorlik2 - hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    gif_url = 'https://t.me/databazatg/9'
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 13:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 13-Mart , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 3-kuni \n🌝Saharlik : 5:58 \n🌚Iftorlik  19:01\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 13-Mart , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 3-kuni \n🌝Saharlik : 5:58 \n🌚Iftorlik  19:01\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    




@dp.message(F.text=="4", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 14, 5, 56)
    qoldi = saharlik2 - hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 14, 19, 2)
    qoldi1 = iftorlik2 - hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 14:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 14-Mart , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 4-kuni \n🌝Saharlik : 5:56 \n🌚Iftorlik  19:02\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 14-Mart , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 4-kuni \n🌝Saharlik : 5:56 \n🌚Iftorlik  19:02\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 

@dp.message(F.text=="5", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/11'
            #saharlik
    saharlik2 = datetime(2024, 3, 15, 5, 54)
    qoldi = saharlik2 - hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 15, 19, 4)
    qoldi1 = iftorlik2 - hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    
    await bot.send_photo(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 15:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 15-Mart , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 5-kuni \n🌝Saharlik : 5:54 \n🌚Iftorlik  19:04\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 15-Mart , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 5-kuni \n🌝Saharlik : 5:54 \n🌚Iftorlik  19:04\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 



@dp.message(F.text=="6", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 16, 5, 53)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 16, 19, 5)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 16:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 16-Mart , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 6-kuni \n🌝Saharlik : 5:53 \n🌚Iftorlik  19:05\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                  reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 16-Mart , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 6-kuni \n🌝Saharlik : 5:53 \n🌚Iftorlik  19:05\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    




@dp.message(F.text=="7", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 17, 5, 51)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 17, 19, 6)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 17:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 17-Mart , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 7-kuni \n🌝Saharlik : 5:51 \n🌚Iftorlik  19:06\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 17-Mart , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 7-kuni \n🌝Saharlik : 5:51 \n🌚Iftorlik  19:06\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="8", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 18, 5, 49)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 18, 19, 7)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 18:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 18-Mart , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 8-kuni \n🌝Saharlik : 5:49 \n🌚Iftorlik  19:07\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 18-Mart , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 8-kuni \n🌝Saharlik : 5:49 \n🌚Iftorlik  19:07\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="9", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 19, 5, 47)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 19, 19, 8)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 19:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 19-Mart , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 9-kuni \n🌝Saharlik : 5:47 \n🌚Iftorlik  19:08\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 19-Mart , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 9-kuni \n🌝Saharlik : 5:47 \n🌚Iftorlik  19:08\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    


@dp.message(F.text=="10", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 20, 5, 46)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 20, 19, 9)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 20:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 20-Mart , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 10-kuni \n🌝Saharlik : 5:46 \n🌚Iftorlik  19:09\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 20-Mart , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 10-kuni \n🌝Saharlik : 5:46 \n🌚Iftorlik  19:09\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="11", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 21, 5, 44)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 21, 19, 10)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 21:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 21-Mart , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 11-kuni \n🌝Saharlik : 5:44 \n🌚Iftorlik  19:10\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 21-Mart , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 11-kuni \n🌝Saharlik : 5:44 \n🌚Iftorlik  19:10\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    




@dp.message(F.text=="12", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 22, 5, 42)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 22, 19, 11)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    gif_url = 'https://t.me/databazatg/11'
    await bot.send_photo(message.chat.id, gif_url)

    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 22:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 22-Mart , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 12-kuni \n🌝Saharlik : 5:42 \n🌚Iftorlik  19:11\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 22-Mart , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 12-kuni \n🌝Saharlik : 5:42 \n🌚Iftorlik  19:11\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    


@dp.message(F.text=="13", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 23, 5, 40)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 23, 19, 12)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 23:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 23-Mart , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 13-kuni \n🌝Saharlik : 5:40 \n🌚Iftorlik  19:12\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 23-Mart , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 13-kuni \n🌝Saharlik : 5:40 \n🌚Iftorlik  19:12\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="14", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 24, 5, 38)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 24, 19, 13)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 24:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 24-Mart , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 14-kuni \n🌝Saharlik : 5:38 \n🌚Iftorlik  19:13\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 24-Mart , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 14-kuni \n🌝Saharlik : 5:38 \n🌚Iftorlik  19:13\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="15", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 25, 5, 37)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 25, 19, 15)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 25:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 25-Mart , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 15-kuni \n🌝Saharlik : 5:37 \n🌚Iftorlik  19:15\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 25-Mart , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 15-kuni \n🌝Saharlik : 5:37 \n🌚Iftorlik  19:15\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 



@dp.message(F.text=="16", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 26, 5, 35)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 26, 19, 16)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 26:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 26-Mart , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 16-kuni \n🌝Saharlik : 5:35 \n🌚Iftorlik  19:16\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 26-Mart , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 16-kuni \n🌝Saharlik : 5:35 \n🌚Iftorlik  19:16\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="17", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 27, 5, 33)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 27, 19, 17)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 27:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 27-Mart , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 17-kuni \n🌝Saharlik : 5:33 \n🌚Iftorlik  19:17\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 27-Mart , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 17-kuni \n🌝Saharlik : 5:33 \n🌚Iftorlik  19:17\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="18", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 28, 5, 31)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 28, 19, 18)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 28:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 28-Mart , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 18-kuni \n🌝Saharlik : 5:31 \n🌚Iftorlik  19:18\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 28-Mart , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 18-kuni \n🌝Saharlik : 5:31 \n🌚Iftorlik  19:18\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    



@dp.message(F.text=="19", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):

            #saharlik
    saharlik2 = datetime(2024, 3, 29, 5, 29)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 29, 19, 19)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    gif_url = 'https://t.me/databazatg/11'
    await bot.send_photo(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 29:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 29-Mart , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 19-kuni \n🌝Saharlik : 5:29 \n🌚Iftorlik  19:19\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 29-Mart , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 19-kuni \n🌝Saharlik : 5:29 \n🌚Iftorlik  19:19\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 




@dp.message(F.text=="20", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 30, 5, 27)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 30, 19, 20)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 30:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 30-Mart , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 20-kuni \n🌝Saharlik : 5:27 \n🌚Iftorlik  19:20\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 30-Mart , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 20-kuni \n🌝Saharlik : 5:27 \n🌚Iftorlik  19:2\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    


@dp.message(F.text=="21", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 3, 31, 5, 25)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 3, 31, 19, 21)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 3 and hozirgi_vaqt.day == 31:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 31-Mart , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 21-kuni \n🌝Saharlik : 5:25 \n🌚Iftorlik  19:21\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 31-Mart , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 21-kuni \n🌝Saharlik : 5:25 \n🌚Iftorlik  19:21\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 



@dp.message(F.text=="22", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 1, 5, 24)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 1, 19, 22 )
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 1:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 1-Aprel , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 22-kuni \n🌝Saharlik : 5:24 \n🌚Iftorlik  19:22\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 1-Aprel , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 22-kuni \n🌝Saharlik : 5:24 \n🌚Iftorlik  19:22\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 


@dp.message(F.text=="23", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 2, 5, 22)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 2, 19, 23 )
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 2:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 2-Aprel , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 23-kuni \n🌝Saharlik : 5:22 \n🌚Iftorlik  19:23\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 2-Aprel , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 23-kuni \n🌝Saharlik : 5:22 \n🌚Iftorlik  19:23\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    

@dp.message(F.text=="24", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 3, 5, 20)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 3, 19, 24 )
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 3:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 3-Aprel , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 24-kuni \n🌝Saharlik : 5:20 \n🌚Iftorlik  19:24\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 3-Aprel , chorshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 24-kuni \n🌝Saharlik : 5:20 \n🌚Iftorlik  19:24\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",
                                 reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    


@dp.message(F.text=="25", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 4, 5, 18)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 4, 19, 25 )
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 4:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 4-Aprel , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 25-kuni \n🌝Saharlik : 5:18 \n🌚Iftorlik  19:25\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 4-Aprel , payshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 25-kuni \n🌝Saharlik : 5:18 \n🌚Iftorlik  19:25\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    

@dp.message(F.text=="26", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):

            #saharlik
    saharlik2 = datetime(2024, 4, 5, 5, 16)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 5, 19, 27)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    gif_url = 'https://t.me/databazatg/11'
    await bot.send_photo(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 5:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 5-Aprel , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 26-kuni \n🌝Saharlik : 5:16 \n🌚Iftorlik  19:27\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 5-Aprel , juma 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 26-kuni \n🌝Saharlik : 5:16 \n🌚Iftorlik  19:27\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 


@dp.message(F.text=="27", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 6, 5, 14)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 6, 19, 28)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 6:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 6-Aprel , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 27-kuni \n🌝Saharlik : 5:14 \n🌚Iftorlik  19:28\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 6-Aprel , shanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 27-kuni \n🌝Saharlik : 5:14 \n🌚Iftorlik  19:28\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 


@dp.message(F.text=="28", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 7, 5,12)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 7, 19, 29)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 7:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 7-Aprel , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 28-kuni \n🌝Saharlik : 5:12 \n🌚Iftorlik  19:29\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 7-Aprel , yakshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 28-kuni \n🌝Saharlik : 5:12 \n🌚Iftorlik  19:29\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    

@dp.message(F.text=="29", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 8, 5, 11)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 8, 19, 30)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 8:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 8-Aprel , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 29-kuni \n🌝Saharlik : 5:11 \n🌚Iftorlik  19:30\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 8-Aprel , Dushanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 29-kuni \n🌝Saharlik : 5:11 \n🌚Iftorlik  19:30\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    

@dp.message(F.text=="30", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    gif_url = 'https://t.me/databazatg/9'
            #saharlik
    saharlik2 = datetime(2024, 4, 9, 5, 9)
    qoldi = saharlik2- hozirgi_vaqt
    kun = qoldi.days
    soat = qoldi.seconds//3600
    minut=(qoldi.seconds%3600)//60
    #iftorlik
    iftorlik2 = datetime(2024, 4, 9, 19, 31)
    qoldi1 = iftorlik2- hozirgi_vaqt
    kun1 = qoldi1.days
    soat1 = qoldi1.seconds//3600
    minut1=(qoldi1.seconds%3600)//60
    await bot.send_document(message.chat.id, gif_url)
    if hozirgi_vaqt.month == 4 and hozirgi_vaqt.day == 9:
        if qoldi.seconds < qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 9-Aprel , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 30-kuni \n🌝Saharlik : 5:09 \n🌚Iftorlik  19:31\n\n⏳ Saharlikgacha : \n ⏰ {soat} soat , {minut} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
        elif qoldi.seconds > qoldi1.seconds:
            await message.answer(f"Assalomu alaykum 👋😇\nBugun 9-Aprel , seshanba 🗓\n     📍Urganch shaharida\n\n   🌦 Ob-havo \n🏞 Kunduzi: {t_max}  \n🌃Kechqurun: {t_min} \n\n🕌Ramazon oyi 30-kuni \n🌝Saharlik : 5:09 \n🌚Iftorlik  19:31\n\n⏳ Iftorlikgacha : \n ⏰ {soat1} soat , {minut1} qoldi \n\n🤖 @Ob_havo_jbot 👨🏻‍💻 @J_Dev",reply_markup=grtugma)
            await message.delete() 
    else:
        await message.answer(f"Bu buyruq 😕\n⏳ {kun} kun ⏰{soat} soatdan\n    keyin ishlaydi") 
    

@dp.message(F.text == "🕌 𝗥𝗮𝗺𝗮𝘇𝗼𝗻 𝘁𝗮𝗾𝘃𝗶𝗺𝗶")
async def with_puree(message: types.Message):
    
    knopka = [
            [KeyboardButton(text="🗓 𝗨𝗿𝗴𝗮𝗻𝗰𝗵"),],
        
            [KeyboardButton(text="🗓 𝗔𝗻𝗱𝗶𝗷𝗼𝗻"),
            KeyboardButton(text="🗓 𝗕𝘂𝘅𝗼𝗿𝗼"),
            KeyboardButton(text="🗓 𝗙𝗮𝗿𝗴'𝗼𝗻𝗮")],
        
            [KeyboardButton(text="🗓 𝗚𝘂𝗹𝗶𝘀𝘁𝗼𝗻"),
            KeyboardButton(text="🗓 𝗝𝗶𝘇𝘇𝗮𝘅"),
            KeyboardButton(text="🗓 𝗦𝗮𝗺𝗮𝗿𝗾𝗮𝗻𝗱")],

            [KeyboardButton(text="🗓 𝗖𝗵𝗶𝗿𝗰𝗵𝗶𝗾"),
            KeyboardButton(text="🗓 𝗧𝗼𝘀𝗵𝗸𝗲𝗻𝘁"),
            KeyboardButton(text="🗓 𝗡𝗮𝘃𝗼𝗶")],
            
            [KeyboardButton(text="🗓 𝗡𝗮𝗺𝗮𝗻𝗴𝗮𝗻"),
            KeyboardButton(text="🗓 𝗧𝗲𝗿𝗺𝗶𝘇"),
            KeyboardButton(text="🗓 𝗤𝗮𝗿𝘀𝗵𝗶")],
    
            [KeyboardButton(text="🔙 𝗼𝗿𝗾𝗮𝗴𝗮")]
            ]
    keyboard = types.ReplyKeyboardMarkup( keyboard=knopka,resize_keyboard=True,)


    gif_url = 'https://t.me/databazatg/9'
    await bot.send_document(message.chat.id, document=gif_url)
    await message.answer(f"Biror Hududni tanlang🙂",

    parse_mode=ParseMode.HTML,
    reply_markup=keyboard)




import requests

from bs4 import BeautifulSoup as B 





@dp.message(F.text == "🗓 𝗨𝗿𝗴𝗮𝗻𝗰𝗵")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗔𝗻𝗱𝗶𝗷𝗼𝗻")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu1)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗕𝘂𝘅𝗼𝗿𝗼")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu2)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗙𝗮𝗿𝗴'𝗼𝗻𝗮")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu3)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗚𝘂𝗹𝗶𝘀𝘁𝗼𝗻")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu4)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗝𝗶𝘇𝘇𝗮𝘅")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu5)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓Namangan")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu6)

@dp.message(F.text == "🗓 𝗡𝗮𝘃𝗼𝗶")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu7)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗤𝗮𝗿𝘀𝗵𝗶")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu11)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')

@dp.message(F.text == "🗓 𝗡𝗮𝗺𝗮𝗻𝗴𝗮𝗻")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu6)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')


@dp.message(F.text == "🗓 𝗦𝗮𝗺𝗮𝗿𝗾𝗮𝗻𝗱")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu10)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗧𝗲𝗿𝗺𝗶𝘇")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu8)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')


@dp.message(F.text == "🗓 𝗧𝗼𝘀𝗵𝗸𝗲𝗻𝘁")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu9)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')
@dp.message(F.text == "🗓 𝗖𝗵𝗶𝗿𝗰𝗵𝗶𝗾")
async def cmd_random(message: types.Message):
    await message.answer("Biror kunni tanlang",reply_markup=menyu12)
    await message.answer('''🤲Saharlik: og‘iz yopish duosi :

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

😊Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.


🤲Iftorlik: og‘iz ochish duosi : 

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

😇Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.''')



menyu = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "1"),
        types.InlineKeyboardButton(text="2",callback_data = "2"),
        types.InlineKeyboardButton(text="3",callback_data = "3"),
        types.InlineKeyboardButton(text="4",callback_data = "4"),
        types.InlineKeyboardButton(text="5",callback_data = "5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "6"),
        types.InlineKeyboardButton(text="7",callback_data = "7"),
        types.InlineKeyboardButton(text="8",callback_data = "8"),
        types.InlineKeyboardButton(text="9",callback_data = "9"),
        types.InlineKeyboardButton(text="10",callback_data = "10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "11"),
        types.InlineKeyboardButton(text="12",callback_data = "12"),
        types.InlineKeyboardButton(text="13",callback_data = "13"),
        types.InlineKeyboardButton(text="14",callback_data = "14"),
        types.InlineKeyboardButton(text="15",callback_data = "15")],

        [types.InlineKeyboardButton(text="16",callback_data = "16"),
        types.InlineKeyboardButton(text="17",callback_data = "17"),
        types.InlineKeyboardButton(text="18",callback_data = "18"),
        types.InlineKeyboardButton(text="19",callback_data = "19"),
        types.InlineKeyboardButton(text="20",callback_data = "20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "21"),
        types.InlineKeyboardButton(text="22",callback_data = "22"),
        types.InlineKeyboardButton(text="23",callback_data = "23"),
        types.InlineKeyboardButton(text="24",callback_data = "24"),
        types.InlineKeyboardButton(text="25",callback_data = "25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "26"),
        types.InlineKeyboardButton(text="27",callback_data = "27"),
        types.InlineKeyboardButton(text="28",callback_data = "28"),
        types.InlineKeyboardButton(text="29",callback_data = "29"),
        types.InlineKeyboardButton(text="30",callback_data = "30")]
    ]
        
)



menyu1 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "a1"),
        types.InlineKeyboardButton(text="2",callback_data = "a2"),
        types.InlineKeyboardButton(text="3",callback_data = "a3"),
        types.InlineKeyboardButton(text="4",callback_data = "a4"),
        types.InlineKeyboardButton(text="5",callback_data = "a5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "a6"),
        types.InlineKeyboardButton(text="7",callback_data = "a7"),
        types.InlineKeyboardButton(text="8",callback_data = "a8"),
        types.InlineKeyboardButton(text="9",callback_data = "a9"),
        types.InlineKeyboardButton(text="10",callback_data = "a10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "a11"),
        types.InlineKeyboardButton(text="12",callback_data = "a12"),
        types.InlineKeyboardButton(text="13",callback_data = "a13"),
        types.InlineKeyboardButton(text="14",callback_data = "a14"),
        types.InlineKeyboardButton(text="15",callback_data = "a15")],

        [types.InlineKeyboardButton(text="16",callback_data = "a16"),
        types.InlineKeyboardButton(text="17",callback_data = "a17"),
        types.InlineKeyboardButton(text="18",callback_data = "a18"),
        types.InlineKeyboardButton(text="19",callback_data = "a19"),
        types.InlineKeyboardButton(text="20",callback_data = "a20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "a21"),
        types.InlineKeyboardButton(text="22",callback_data = "a22"),
        types.InlineKeyboardButton(text="23",callback_data = "a23"),
        types.InlineKeyboardButton(text="24",callback_data = "a24"),
        types.InlineKeyboardButton(text="25",callback_data = "a25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "a26"),
        types.InlineKeyboardButton(text="27",callback_data = "a27"),
        types.InlineKeyboardButton(text="28",callback_data = "a28"),
        types.InlineKeyboardButton(text="29",callback_data = "a29"),
        types.InlineKeyboardButton(text="30",callback_data = "a30")]
    ])

menyu2 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "b1"),
        types.InlineKeyboardButton(text="2",callback_data = "b2"),
        types.InlineKeyboardButton(text="3",callback_data = "b3"),
        types.InlineKeyboardButton(text="4",callback_data = "b4"),
        types.InlineKeyboardButton(text="5",callback_data = "b5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "b6"),
        types.InlineKeyboardButton(text="7",callback_data = "b7"),
        types.InlineKeyboardButton(text="8",callback_data = "b8"),
        types.InlineKeyboardButton(text="9",callback_data = "b9"),
        types.InlineKeyboardButton(text="10",callback_data = "b10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "b11"),
        types.InlineKeyboardButton(text="12",callback_data = "b12"),
        types.InlineKeyboardButton(text="13",callback_data = "b13"),
        types.InlineKeyboardButton(text="14",callback_data = "b14"),
        types.InlineKeyboardButton(text="15",callback_data = "b15")],

        [types.InlineKeyboardButton(text="16",callback_data = "b16"),
        types.InlineKeyboardButton(text="17",callback_data = "b17"),
        types.InlineKeyboardButton(text="18",callback_data = "b18"),
        types.InlineKeyboardButton(text="19",callback_data = "b19"),
        types.InlineKeyboardButton(text="20",callback_data = "b20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "b21"),
        types.InlineKeyboardButton(text="22",callback_data = "b22"),
        types.InlineKeyboardButton(text="23",callback_data = "b23"),
        types.InlineKeyboardButton(text="24",callback_data = "b24"),
        types.InlineKeyboardButton(text="25",callback_data = "b25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "b26"),
        types.InlineKeyboardButton(text="27",callback_data = "b27"),
        types.InlineKeyboardButton(text="28",callback_data = "b28"),
        types.InlineKeyboardButton(text="29",callback_data = "b29"),
        types.InlineKeyboardButton(text="30",callback_data = "b30")]
    ])

menyu3 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "f1"),
        types.InlineKeyboardButton(text="2",callback_data = "f2"),
        types.InlineKeyboardButton(text="3",callback_data = "f3"),
        types.InlineKeyboardButton(text="4",callback_data = "f4"),
        types.InlineKeyboardButton(text="5",callback_data = "f5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "f6"),
        types.InlineKeyboardButton(text="7",callback_data = "f7"),
        types.InlineKeyboardButton(text="8",callback_data = "f8"),
        types.InlineKeyboardButton(text="9",callback_data = "f9"),
        types.InlineKeyboardButton(text="10",callback_data = "f10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "f11"),
        types.InlineKeyboardButton(text="12",callback_data = "f12"),
        types.InlineKeyboardButton(text="13",callback_data = "f13"),
        types.InlineKeyboardButton(text="14",callback_data = "f14"),
        types.InlineKeyboardButton(text="15",callback_data = "f15")],

        [types.InlineKeyboardButton(text="16",callback_data = "f16"),
        types.InlineKeyboardButton(text="17",callback_data = "f17"),
        types.InlineKeyboardButton(text="18",callback_data = "f18"),
        types.InlineKeyboardButton(text="19",callback_data = "f19"),
        types.InlineKeyboardButton(text="20",callback_data = "f20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "f21"),
        types.InlineKeyboardButton(text="22",callback_data = "f22"),
        types.InlineKeyboardButton(text="23",callback_data = "f23"),
        types.InlineKeyboardButton(text="24",callback_data = "f24"),
        types.InlineKeyboardButton(text="25",callback_data = "f25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "f26"),
        types.InlineKeyboardButton(text="27",callback_data = "f27"),
        types.InlineKeyboardButton(text="28",callback_data = "f28"),
        types.InlineKeyboardButton(text="29",callback_data = "f29"),
        types.InlineKeyboardButton(text="30",callback_data = "f30")]
    ])

menyu4 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "g1"),
        types.InlineKeyboardButton(text="2",callback_data = "g2"),
        types.InlineKeyboardButton(text="3",callback_data = "g3"),
        types.InlineKeyboardButton(text="4",callback_data = "g4"),
        types.InlineKeyboardButton(text="5",callback_data = "g5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "g6"),
        types.InlineKeyboardButton(text="7",callback_data = "g7"),
        types.InlineKeyboardButton(text="8",callback_data = "g8"),
        types.InlineKeyboardButton(text="9",callback_data = "g9"),
        types.InlineKeyboardButton(text="10",callback_data = "g10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "g11"),
        types.InlineKeyboardButton(text="12",callback_data = "g12"),
        types.InlineKeyboardButton(text="13",callback_data = "g13"),
        types.InlineKeyboardButton(text="14",callback_data = "g14"),
        types.InlineKeyboardButton(text="15",callback_data = "g15")],

        [types.InlineKeyboardButton(text="16",callback_data = "g16"),
        types.InlineKeyboardButton(text="17",callback_data = "g17"),
        types.InlineKeyboardButton(text="18",callback_data = "g18"),
        types.InlineKeyboardButton(text="19",callback_data = "g19"),
        types.InlineKeyboardButton(text="20",callback_data = "g20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "g21"),
        types.InlineKeyboardButton(text="22",callback_data = "g22"),
        types.InlineKeyboardButton(text="23",callback_data = "g23"),
        types.InlineKeyboardButton(text="24",callback_data = "g24"),
        types.InlineKeyboardButton(text="25",callback_data = "g25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "g26"),
        types.InlineKeyboardButton(text="27",callback_data = "g27"),
        types.InlineKeyboardButton(text="28",callback_data = "g28"),
        types.InlineKeyboardButton(text="29",callback_data = "g29"),
        types.InlineKeyboardButton(text="30",callback_data = "g30")]
    ])

menyu5 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "j1"),
        types.InlineKeyboardButton(text="2",callback_data = "j2"),
        types.InlineKeyboardButton(text="3",callback_data = "j3"),
        types.InlineKeyboardButton(text="4",callback_data = "j4"),
        types.InlineKeyboardButton(text="5",callback_data = "j5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "j6"),
        types.InlineKeyboardButton(text="7",callback_data = "j7"),
        types.InlineKeyboardButton(text="8",callback_data = "j8"),
        types.InlineKeyboardButton(text="9",callback_data = "j9"),
        types.InlineKeyboardButton(text="10",callback_data = "j10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "j11"),
        types.InlineKeyboardButton(text="12",callback_data = "j12"),
        types.InlineKeyboardButton(text="13",callback_data = "j13"),
        types.InlineKeyboardButton(text="14",callback_data = "j14"),
        types.InlineKeyboardButton(text="15",callback_data = "j15")],

        [types.InlineKeyboardButton(text="16",callback_data = "j16"),
        types.InlineKeyboardButton(text="17",callback_data = "j17"),
        types.InlineKeyboardButton(text="18",callback_data = "j18"),
        types.InlineKeyboardButton(text="19",callback_data = "j19"),
        types.InlineKeyboardButton(text="20",callback_data = "j20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "j21"),
        types.InlineKeyboardButton(text="22",callback_data = "j22"),
        types.InlineKeyboardButton(text="23",callback_data = "j23"),
        types.InlineKeyboardButton(text="24",callback_data = "j24"),
        types.InlineKeyboardButton(text="25",callback_data = "j25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "j26"),
        types.InlineKeyboardButton(text="27",callback_data = "j27"),
        types.InlineKeyboardButton(text="28",callback_data = "j28"),
        types.InlineKeyboardButton(text="29",callback_data = "j29"),
        types.InlineKeyboardButton(text="30",callback_data = "j30")]
    ])

menyu6 = types.InlineKeyboardMarkup(
    inline_keyboard=[#Namangan
        [types.InlineKeyboardButton(text="1",callback_data = "n1"),
        types.InlineKeyboardButton(text="2",callback_data = "n2"),
        types.InlineKeyboardButton(text="3",callback_data = "n3"),
        types.InlineKeyboardButton(text="4",callback_data = "n4"),
        types.InlineKeyboardButton(text="5",callback_data = "n5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "n6"),
        types.InlineKeyboardButton(text="7",callback_data = "n7"),
        types.InlineKeyboardButton(text="8",callback_data = "n8"),
        types.InlineKeyboardButton(text="9",callback_data = "n9"),
        types.InlineKeyboardButton(text="10",callback_data = "n10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "n11"),
        types.InlineKeyboardButton(text="12",callback_data = "n12"),
        types.InlineKeyboardButton(text="13",callback_data = "n13"),
        types.InlineKeyboardButton(text="14",callback_data = "n14"),
        types.InlineKeyboardButton(text="15",callback_data = "n15")],

        [types.InlineKeyboardButton(text="16",callback_data = "n16"),
        types.InlineKeyboardButton(text="17",callback_data = "n17"),
        types.InlineKeyboardButton(text="18",callback_data = "n18"),
        types.InlineKeyboardButton(text="19",callback_data = "n19"),
        types.InlineKeyboardButton(text="20",callback_data = "n20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "n21"),
        types.InlineKeyboardButton(text="22",callback_data = "n22"),
        types.InlineKeyboardButton(text="23",callback_data = "n23"),
        types.InlineKeyboardButton(text="24",callback_data = "n24"),
        types.InlineKeyboardButton(text="25",callback_data = "n25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "n26"),
        types.InlineKeyboardButton(text="27",callback_data = "n27"),
        types.InlineKeyboardButton(text="28",callback_data = "n28"),
        types.InlineKeyboardButton(text="29",callback_data = "n29"),
        types.InlineKeyboardButton(text="30",callback_data = "n30")]
    ])
menyu7 = types.InlineKeyboardMarkup(
    inline_keyboard=[#Navoi
        [types.InlineKeyboardButton(text="1",callback_data = "N1"),
        types.InlineKeyboardButton(text="2",callback_data = "N2"),
        types.InlineKeyboardButton(text="3",callback_data = "N3"),
        types.InlineKeyboardButton(text="4",callback_data = "N4"),
        types.InlineKeyboardButton(text="5",callback_data = "N5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "N6"),
        types.InlineKeyboardButton(text="7",callback_data = "N7"),
        types.InlineKeyboardButton(text="8",callback_data = "N8"),
        types.InlineKeyboardButton(text="9",callback_data = "N9"),
        types.InlineKeyboardButton(text="10",callback_data = "N10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "N11"),
        types.InlineKeyboardButton(text="12",callback_data = "N12"),
        types.InlineKeyboardButton(text="13",callback_data = "N13"),
        types.InlineKeyboardButton(text="14",callback_data = "N14"),
        types.InlineKeyboardButton(text="15",callback_data = "N15")],

        [types.InlineKeyboardButton(text="16",callback_data = "N16"),
        types.InlineKeyboardButton(text="17",callback_data = "N17"),
        types.InlineKeyboardButton(text="18",callback_data = "N18"),
        types.InlineKeyboardButton(text="19",callback_data = "N19"),
        types.InlineKeyboardButton(text="20",callback_data = "N20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "N21"),
        types.InlineKeyboardButton(text="22",callback_data = "N22"),
        types.InlineKeyboardButton(text="23",callback_data = "N23"),
        types.InlineKeyboardButton(text="24",callback_data = "N24"),
        types.InlineKeyboardButton(text="25",callback_data = "N25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "N26"),
        types.InlineKeyboardButton(text="27",callback_data = "N27"),
        types.InlineKeyboardButton(text="28",callback_data = "N28"),
        types.InlineKeyboardButton(text="29",callback_data = "N29"),
        types.InlineKeyboardButton(text="30",callback_data = "N30")]
    ])

menyu8 = types.InlineKeyboardMarkup(
    inline_keyboard=[#  termiz
        [types.InlineKeyboardButton(text="1",callback_data = "t1"),
        types.InlineKeyboardButton(text="2",callback_data = "t2"),
        types.InlineKeyboardButton(text="3",callback_data = "t3"),
        types.InlineKeyboardButton(text="4",callback_data = "t4"),
        types.InlineKeyboardButton(text="5",callback_data = "t5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "t6"),
        types.InlineKeyboardButton(text="7",callback_data = "t7"),
        types.InlineKeyboardButton(text="8",callback_data = "t8"),
        types.InlineKeyboardButton(text="9",callback_data = "t9"),
        types.InlineKeyboardButton(text="10",callback_data = "t10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "t11"),
        types.InlineKeyboardButton(text="12",callback_data = "t12"),
        types.InlineKeyboardButton(text="13",callback_data = "t13"),
        types.InlineKeyboardButton(text="14",callback_data = "t14"),
        types.InlineKeyboardButton(text="15",callback_data = "t15")],

        [types.InlineKeyboardButton(text="16",callback_data = "t16"),
        types.InlineKeyboardButton(text="17",callback_data = "t17"),
        types.InlineKeyboardButton(text="18",callback_data = "t18"),
        types.InlineKeyboardButton(text="19",callback_data = "t19"),
        types.InlineKeyboardButton(text="20",callback_data = "t20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "t21"),
        types.InlineKeyboardButton(text="22",callback_data = "t22"),
        types.InlineKeyboardButton(text="23",callback_data = "t23"),
        types.InlineKeyboardButton(text="24",callback_data = "t24"),
        types.InlineKeyboardButton(text="25",callback_data = "t25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "t26"),
        types.InlineKeyboardButton(text="27",callback_data = "t27"),
        types.InlineKeyboardButton(text="28",callback_data = "t28"),
        types.InlineKeyboardButton(text="29",callback_data = "t29"),
        types.InlineKeyboardButton(text="30",callback_data = "t30")]
    ])

menyu9 = types.InlineKeyboardMarkup(
    inline_keyboard=[#Toshkent
        [types.InlineKeyboardButton(text="1",callback_data = "T1"),
        types.InlineKeyboardButton(text="2",callback_data = "T2"),
        types.InlineKeyboardButton(text="3",callback_data = "T3"),
        types.InlineKeyboardButton(text="4",callback_data = "T4"),
        types.InlineKeyboardButton(text="5",callback_data = "T5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "T6"),
        types.InlineKeyboardButton(text="7",callback_data = "T7"),
        types.InlineKeyboardButton(text="8",callback_data = "T8"),
        types.InlineKeyboardButton(text="9",callback_data = "T9"),
        types.InlineKeyboardButton(text="10",callback_data = "T10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "T11"),
        types.InlineKeyboardButton(text="12",callback_data = "T12"),
        types.InlineKeyboardButton(text="13",callback_data = "T13"),
        types.InlineKeyboardButton(text="14",callback_data = "T14"),
        types.InlineKeyboardButton(text="15",callback_data = "T15")],

        [types.InlineKeyboardButton(text="16",callback_data = "T16"),
        types.InlineKeyboardButton(text="17",callback_data = "T17"),
        types.InlineKeyboardButton(text="18",callback_data = "T18"),
        types.InlineKeyboardButton(text="19",callback_data = "T19"),
        types.InlineKeyboardButton(text="20",callback_data = "T20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "T21"),
        types.InlineKeyboardButton(text="22",callback_data = "T22"),
        types.InlineKeyboardButton(text="23",callback_data = "T23"),
        types.InlineKeyboardButton(text="24",callback_data = "T24"),
        types.InlineKeyboardButton(text="25",callback_data = "T25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "T26"),
        types.InlineKeyboardButton(text="27",callback_data = "T27"),
        types.InlineKeyboardButton(text="28",callback_data = "T28"),
        types.InlineKeyboardButton(text="29",callback_data = "T29"),
        types.InlineKeyboardButton(text="30",callback_data = "T30")]
    ])

menyu10 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "s1"),
        types.InlineKeyboardButton(text="2",callback_data = "s2"),
        types.InlineKeyboardButton(text="3",callback_data = "s3"),
        types.InlineKeyboardButton(text="4",callback_data = "s4"),
        types.InlineKeyboardButton(text="5",callback_data = "s5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "s6"),
        types.InlineKeyboardButton(text="7",callback_data = "s7"),
        types.InlineKeyboardButton(text="8",callback_data = "s8"),
        types.InlineKeyboardButton(text="9",callback_data = "s9"),
        types.InlineKeyboardButton(text="10",callback_data = "s10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "s11"),
        types.InlineKeyboardButton(text="12",callback_data = "s12"),
        types.InlineKeyboardButton(text="13",callback_data = "s13"),
        types.InlineKeyboardButton(text="14",callback_data = "s14"),
        types.InlineKeyboardButton(text="15",callback_data = "s15")],

        [types.InlineKeyboardButton(text="16",callback_data = "s16"),
        types.InlineKeyboardButton(text="17",callback_data = "s17"),
        types.InlineKeyboardButton(text="18",callback_data = "s18"),
        types.InlineKeyboardButton(text="19",callback_data = "s19"),
        types.InlineKeyboardButton(text="20",callback_data = "s20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "s21"),
        types.InlineKeyboardButton(text="22",callback_data = "s22"),
        types.InlineKeyboardButton(text="23",callback_data = "s23"),
        types.InlineKeyboardButton(text="24",callback_data = "s24"),
        types.InlineKeyboardButton(text="25",callback_data = "s25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "s26"),
        types.InlineKeyboardButton(text="27",callback_data = "s27"),
        types.InlineKeyboardButton(text="28",callback_data = "s28"),
        types.InlineKeyboardButton(text="29",callback_data = "s29"),
        types.InlineKeyboardButton(text="30",callback_data = "s30")]
    ])

menyu11 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "q1"),
        types.InlineKeyboardButton(text="2",callback_data = "q2"),
        types.InlineKeyboardButton(text="3",callback_data = "q3"),
        types.InlineKeyboardButton(text="4",callback_data = "q4"),
        types.InlineKeyboardButton(text="5",callback_data = "q5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "q6"),
        types.InlineKeyboardButton(text="7",callback_data = "q7"),
        types.InlineKeyboardButton(text="8",callback_data = "q8"),
        types.InlineKeyboardButton(text="9",callback_data = "q9"),
        types.InlineKeyboardButton(text="10",callback_data = "q10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "q11"),
        types.InlineKeyboardButton(text="12",callback_data = "q12"),
        types.InlineKeyboardButton(text="13",callback_data = "q13"),
        types.InlineKeyboardButton(text="14",callback_data = "q14"),
        types.InlineKeyboardButton(text="15",callback_data = "q15")],

        [types.InlineKeyboardButton(text="16",callback_data = "q16"),
        types.InlineKeyboardButton(text="17",callback_data = "q17"),
        types.InlineKeyboardButton(text="18",callback_data = "q18"),
        types.InlineKeyboardButton(text="19",callback_data = "q19"),
        types.InlineKeyboardButton(text="20",callback_data = "q20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "q21"),
        types.InlineKeyboardButton(text="22",callback_data = "q22"),
        types.InlineKeyboardButton(text="23",callback_data = "q23"),
        types.InlineKeyboardButton(text="24",callback_data = "q24"),
        types.InlineKeyboardButton(text="25",callback_data = "q25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "q26"),
        types.InlineKeyboardButton(text="27",callback_data = "q27"),
        types.InlineKeyboardButton(text="28",callback_data = "q28"),
        types.InlineKeyboardButton(text="29",callback_data = "q29"),
        types.InlineKeyboardButton(text="30",callback_data = "q30")]
    ])

menyu12 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "z1"),
        types.InlineKeyboardButton(text="2",callback_data = "z2"),
        types.InlineKeyboardButton(text="3",callback_data = "z3"),
        types.InlineKeyboardButton(text="4",callback_data = "z4"),
        types.InlineKeyboardButton(text="5",callback_data = "z5")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "z6"),
        types.InlineKeyboardButton(text="7",callback_data = "z7"),
        types.InlineKeyboardButton(text="8",callback_data = "z8"),
        types.InlineKeyboardButton(text="9",callback_data = "z9"),
        types.InlineKeyboardButton(text="10",callback_data = "z10")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "z11"),
        types.InlineKeyboardButton(text="12",callback_data = "z12"),
        types.InlineKeyboardButton(text="13",callback_data = "z13"),
        types.InlineKeyboardButton(text="14",callback_data = "z14"),
        types.InlineKeyboardButton(text="15",callback_data = "z15")],

        [types.InlineKeyboardButton(text="16",callback_data = "z16"),
        types.InlineKeyboardButton(text="17",callback_data = "z17"),
        types.InlineKeyboardButton(text="18",callback_data = "z18"),
        types.InlineKeyboardButton(text="19",callback_data = "z19"),
        types.InlineKeyboardButton(text="20",callback_data = "z20")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "z21"),
        types.InlineKeyboardButton(text="22",callback_data = "z22"),
        types.InlineKeyboardButton(text="23",callback_data = "z23"),
        types.InlineKeyboardButton(text="24",callback_data = "z24"),
        types.InlineKeyboardButton(text="25",callback_data = "z25")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "z26"),
        types.InlineKeyboardButton(text="27",callback_data = "z27"),
        types.InlineKeyboardButton(text="28",callback_data = "z28"),
        types.InlineKeyboardButton(text="29",callback_data = "z29"),
        types.InlineKeyboardButton(text="30",callback_data = "z30")]
    ])
@dp.callback_query(F.data == "1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Urganchda \n Ramazon 1-Kuni \n\nSaharlik : 6:01 \n Iftorlik  : 18:59",
        show_alert=True)
@dp.callback_query(F.data == "2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Urganchda \n Ramazon 2-Kuni \n\nSaharlik : 5:59 \n Iftorlik  : 19:00",
        show_alert=True)
@dp.callback_query(F.data == "3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Urganchda \n Ramazon 3-Kuni \n\nSaharlik : 5:58 \n Iftorlik  : 19:01",
        show_alert=True)
@dp.callback_query(F.data == "4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Urganchda \n Ramazon 4-Kuni \n\nSaharlik : 5:56 \n Iftorlik  : 19:02",
        show_alert=True)
@dp.callback_query(F.data == "5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Urganchda \n Ramazon 5-Kuni \n\nSaharlik : 5:54 \n Iftorlik  : 19:04",
        show_alert=True)
@dp.callback_query(F.data == "6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Urganchda \n Ramazon 6-Kuni \n\nSaharlik : 5:53 \n Iftorlik  : 19:05",
        show_alert=True)
@dp.callback_query(F.data == "7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Urganchda \n Ramazon 7-Kuni \n\nSaharlik : 5:51 \n Iftorlik  : 19:06",
        show_alert=True)
@dp.callback_query(F.data == "8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Urganchda \n Ramazon 8-Kuni \n\nSaharlik : 5:49 \n Iftorlik  : 19:07",
        show_alert=True)
@dp.callback_query(F.data == "9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Urganchda \n Ramazon 9-Kuni \n\nSaharlik : 5:47 \n Iftorlik  : 19:08",
        show_alert=True)
@dp.callback_query(F.data == "10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Urganchda \n Ramazon 10-Kuni \n\nSaharlik : 5:46 \n Iftorlik  : 19:09",
        show_alert=True)
@dp.callback_query(F.data == "11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Urganchda \n Ramazon 11-Kuni \n\nSaharlik : 5:44 \n Iftorlik  : 19:10",
        show_alert=True)
@dp.callback_query(F.data == "12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Urganchda \n Ramazon 12-Kuni \n\nSaharlik : 5:42 \n Iftorlik  : 19:11",
        show_alert=True)
@dp.callback_query(F.data == "13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Urganchda \n Ramazon 13-Kuni \n\nSaharlik : 5:40 \n Iftorlik  : 19:12",
        show_alert=True)
@dp.callback_query(F.data == "14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Urganchda \n Ramazon 14-Kuni \n\nSaharlik : 5:38 \n Iftorlik  : 19:13",
        show_alert=True)
@dp.callback_query(F.data == "15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Urganchda \n Ramazon 15-Kuni \n\nSaharlik : 5:37 \n Iftorlik  : 19:15",
        show_alert=True)
@dp.callback_query(F.data == "16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Urganchda \n Ramazon 16-Kuni \n\nSaharlik : 5:35 \n Iftorlik  : 19:16",
        show_alert=True)
@dp.callback_query(F.data == "17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Urganchda \n Ramazon 17-Kuni \n\nSaharlik : 5:33 \n Iftorlik  : 19:17",
        show_alert=True)
@dp.callback_query(F.data == "18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Urganchda \n Ramazon 18-Kuni \n\nSaharlik : 5:31 \n Iftorlik  : 19:18",
        show_alert=True)
@dp.callback_query(F.data == "19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Urganchda \n Ramazon 19-Kuni \n\nSaharlik : 5:29 \n Iftorlik  : 19:19",
        show_alert=True)
@dp.callback_query(F.data == "20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Urganchda \n Ramazon 20-Kuni \n\nSaharlik : 5:27 \n Iftorlik  : 19:20",
        show_alert=True)
@dp.callback_query(F.data == "21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Urganchda \n Ramazon 21-Kuni \n\nSaharlik : 5:25 \n Iftorlik  : 19:21",
        show_alert=True)
@dp.callback_query(F.data == "22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Urganchda \n Ramazon 22-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 19:22",
        show_alert=True)
@dp.callback_query(F.data == "23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Urganchda \n Ramazon 23-Kuni \n\nSaharlik : 5:22 \n Iftorlik  : 19:23",
        show_alert=True)
@dp.callback_query(F.data == "24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Urganchda \n Ramazon 24-Kuni \n\nSaharlik : 5:20 \n Iftorlik  : 19:24",
        show_alert=True)
@dp.callback_query(F.data == "25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Urganchda \n Ramazon 25-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 19:26",
        show_alert=True)
@dp.callback_query(F.data == "26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Urganchda \n Ramazon 26-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 19:27",
        show_alert=True)
@dp.callback_query(F.data == "27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Urganchda \n Ramazon 27-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 19:28",
        show_alert=True)
@dp.callback_query(F.data == "28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Urganchda \n Ramazon 28-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 19:29",
        show_alert=True)
@dp.callback_query(F.data == "29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Urganchda \n Ramazon 29-Kuni \n\nSaharlik : 5:11 \n Iftorlik  : 19:30",
        show_alert=True)
@dp.callback_query(F.data == "30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Urganchda \n Ramazon 30-Kuni \n\nSaharlik : 5:09 \n Iftorlik  : 19:31",
        show_alert=True)
    


@dp.callback_query(F.data == "a1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Andijonda \n Ramazon 1-Kuni \n\nSaharlik : 5:15 \n Iftorlik  : 18:12",
        show_alert=True)
@dp.callback_query(F.data == "a2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Andijonda \n Ramazon 2-Kuni \n\nSaharlik : 5:13 \n Iftorlik  : 18:13",
        show_alert=True)
@dp.callback_query(F.data == "a3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Andijonda \n Ramazon 3-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 18:15",
        show_alert=True)
@dp.callback_query(F.data == "a4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Andijonda \n Ramazon 4-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 18:16",
        show_alert=True)
@dp.callback_query(F.data == "a5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Andijonda \n Ramazon 5-Kuni \n\nSaharlik : 5:08 \n Iftorlik  : 18:17",
        show_alert=True)
@dp.callback_query(F.data == "a6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Andijonda \n Ramazon 6-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 18:18",
        show_alert=True)
@dp.callback_query(F.data == "a7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Andijonda \n Ramazon 7-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 18:19",
        show_alert=True)
@dp.callback_query(F.data == "a8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Andijonda \n Ramazon 8-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 18:20",
        show_alert=True)
@dp.callback_query(F.data == "a9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Andijonda \n Ramazon 9-Kuni \n\nSaharlik : 5:01 \n Iftorlik  : 18:21",
        show_alert=True)
@dp.callback_query(F.data == "a10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Andijonda \n Ramazon 10-Kuni \n\nSaharlik : 5:00 \n Iftorlik  : 18:22",
        show_alert=True)
@dp.callback_query(F.data == "a11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Andijonda \n Ramazon 11-Kuni \n\nSaharlik : 4:58 \n Iftorlik  : 18:23",
        show_alert=True)
@dp.callback_query(F.data == "a12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Andijonda \n Ramazon 12-Kuni \n\nSaharlik : 4:56 \n Iftorlik  : 18:24",
        show_alert=True)
@dp.callback_query(F.data == "a13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Andijonda \n Ramazon 13-Kuni \n\nSaharlik : 4:54 \n Iftorlik  : 18:25",
        show_alert=True)
@dp.callback_query(F.data == "a14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Andijonda \n Ramazon 14-Kuni \n\nSaharlik : 4:53 \n Iftorlik  : 18:26",
        show_alert=True)
@dp.callback_query(F.data == "a15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Andijonda \n Ramazon 15-Kuni \n\nSaharlik : 4:51 \n Iftorlik  : 18:27",
        show_alert=True)
@dp.callback_query(F.data == "a16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Andijonda \n Ramazon 16-Kuni \n\nSaharlik : 4:49 \n Iftorlik  : 18:28",
        show_alert=True)
@dp.callback_query(F.data == "a17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Andijonda \n Ramazon 17-Kuni \n\nSaharlik : 4:47 \n Iftorlik  : 18:30",
        show_alert=True)
@dp.callback_query(F.data == "a18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Andijonda \n Ramazon 18-Kuni \n\nSaharlik : 4:45 \n Iftorlik  : 18:31",
        show_alert=True)
@dp.callback_query(F.data == "a19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Andijonda \n Ramazon 19-Kuni \n\nSaharlik : 4:44 \n Iftorlik  : 18:32",
        show_alert=True)
@dp.callback_query(F.data == "a20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Andijonda \n Ramazon 20-Kuni \n\nSaharlik : 4:42 \n Iftorlik  : 18:33",
        show_alert=True)
@dp.callback_query(F.data == "a21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Andijonda \n Ramazon 21-Kuni \n\nSaharlik : 4:40 \n Iftorlik  : 18:34",
        show_alert=True)
@dp.callback_query(F.data == "a22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Andijonda \n Ramazon 22-Kuni \n\nSaharlik : 4:38 \n Iftorlik  : 18:35",
        show_alert=True)
@dp.callback_query(F.data == "a23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Andijonda \n Ramazon 23-Kuni \n\nSaharlik : 4:36 \n Iftorlik  : 18:36",
        show_alert=True)
@dp.callback_query(F.data == "a24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Andijonda \n Ramazon 24-Kuni \n\nSaharlik : 4:35 \n Iftorlik  : 18:37",
        show_alert=True)
@dp.callback_query(F.data == "a25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Andijonda \n Ramazon 25-Kuni \n\nSaharlik : 4:33 \n Iftorlik  : 18:38",
        show_alert=True)
@dp.callback_query(F.data == "a26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Andijonda \n Ramazon 26-Kuni \n\nSaharlik : 4:31 \n Iftorlik  : 18:39",
        show_alert=True)
@dp.callback_query(F.data == "a27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Andijonda \n Ramazon 27-Kuni \n\nSaharlik : 4:29 \n Iftorlik  : 18:40",
        show_alert=True)
@dp.callback_query(F.data == "a28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Andijonda \n Ramazon 28-Kuni \n\nSaharlik : 4:27 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "a29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Andijonda \n Ramazon 29-Kuni \n\nSaharlik : 4:26 \n Iftorlik  : 18:42",
        show_alert=True)
@dp.callback_query(F.data == "a30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Andijonzda \n Ramazon 30-Kuni \n\nSaharlik : 4:24 \n Iftorlik  : 18:43",
        show_alert=True)
    
@dp.callback_query(F.data == "b1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Buxorada \n Ramazon 1-Kuni \n\nSaharlik : 5:47 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "b2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Buxorada \n Ramazon 2-Kuni \n\nSaharlik : 5:46 \n Iftorlik  : 18:45",
        show_alert=True)
@dp.callback_query(F.data == "b3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Buxorada \n Ramazon 3-Kuni \n\nSaharlik : 5:44 \n Iftorlik  : 18:46",
        show_alert=True)
@dp.callback_query(F.data == "b4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Buxorada \n Ramazon 4-Kuni \n\nSaharlik : 5:42 \n Iftorlik  : 18:47",
        show_alert=True)
@dp.callback_query(F.data == "b5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Buxorada \n Ramazon 5-Kuni \n\nSaharlik : 5:41 \n Iftorlik  : 18:48",
        show_alert=True)
@dp.callback_query(F.data == "b6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Buxorada \n Ramazon 6-Kuni \n\nSaharlik : 5:39 \n Iftorlik  : 18:49",
        show_alert=True)
@dp.callback_query(F.data == "b7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Buxorada \n Ramazon 7-Kuni \n\nSaharlik : 5:37 \n Iftorlik  : 18:06",
        show_alert=True)
@dp.callback_query(F.data == "b8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Buxorada \n Ramazon 8-Kuni \n\nSaharlik : 5:36 \n Iftorlik  : 18:07",
        show_alert=True)
@dp.callback_query(F.data == "b9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Buxorada \n Ramazon 9-Kuni \n\nSaharlik : 5:34 \n Iftorlik  : 18:08",
        show_alert=True)
@dp.callback_query(F.data == "b10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Buxorada \n Ramazon 10-Kuni \n\nSaharlik : 5:32 \n Iftorlik  : 18:09",
        show_alert=True)
@dp.callback_query(F.data == "b11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Buxorada \n Ramazon 11-Kuni \n\nSaharlik : 5:31 \n Iftorlik  : 18:10",
        show_alert=True)
@dp.callback_query(F.data == "b12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Buxorada \n Ramazon 12-Kuni \n\nSaharlik : 5:29 \n Iftorlik  : 18:11",
        show_alert=True)
@dp.callback_query(F.data == "b13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Buxorada \n Ramazon 13-Kuni \n\nSaharlik : 5:27 \n Iftorlik  : 18:12",
        show_alert=True)
@dp.callback_query(F.data == "b14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Buxorada \n Ramazon 14-Kuni \n\nSaharlik : 5:26 \n Iftorlik  : 18:13",
        show_alert=True)
@dp.callback_query(F.data == "b15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Buxorada \n Ramazon 15-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 18:15",
        show_alert=True)
@dp.callback_query(F.data == "b16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Buxorada \n Ramazon 16-Kuni \n\nSaharlik : 5:22 \n Iftorlik  : 19:16",
        show_alert=True)
@dp.callback_query(F.data == "b17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Buxorada \n Ramazon 17-Kuni \n\nSaharlik : 5:20 \n Iftorlik  : 19:00",
        show_alert=True)
@dp.callback_query(F.data == "b18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Buxorada \n Ramazon 18-Kuni \n\nSaharlik : 5:19 \n Iftorlik  : 19:01",
        show_alert=True)
@dp.callback_query(F.data == "b19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Buxorada \n Ramazon 19-Kuni \n\nSaharlik : 5:17 \n Iftorlik  : 19:02",
        show_alert=True)
@dp.callback_query(F.data == "b20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Buxorada \n Ramazon 20-Kuni \n\nSaharlik : 5:15 \n Iftorlik  : 19:03",
        show_alert=True)
@dp.callback_query(F.data == "b21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Buxorada \n Ramazon 21-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 19:04",
        show_alert=True)
@dp.callback_query(F.data == "b22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Buxorahda \n Ramazon 22-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 19:06",
        show_alert=True)
@dp.callback_query(F.data == "b23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Buxorada \n Ramazon 23-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 19:07",
        show_alert=True)
@dp.callback_query(F.data == "b24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Buxorada \n Ramazon 24-Kuni \n\nSaharlik : 5:08 \n Iftorlik  : 19:08",
        show_alert=True)
@dp.callback_query(F.data == "b25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Buxorada \n Ramazon 25-Kuni \n\nSaharlik : 5:06 \n Iftorlik  : 19:09",
        show_alert=True)
@dp.callback_query(F.data == "b26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Buxorada \n Ramazon 26-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 19:10",
        show_alert=True)
@dp.callback_query(F.data == "b27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Buxorada \n Ramazon 27-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 19:11",
        show_alert=True)
@dp.callback_query(F.data == "b28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Buxorada \n Ramazon 28-Kuni \n\nSaharlik : 5:01 \n Iftorlik  : 19:12",
        show_alert=True)
@dp.callback_query(F.data == "b29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Buxorada \n Ramazon 29-Kuni \n\nSaharlik : 4:59 \n Iftorlik  : 19:13",
        show_alert=True)
@dp.callback_query(F.data == "b30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Buxorada \n Ramazon 30-Kuni \n\nSaharlik : 4:58 \n Iftorlik  : 19:14",
        show_alert=True)
    
@dp.callback_query(F.data == "f1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Farg'onada \n Ramazon 1-Kuni \n\nSaharlik : 5:17 \n Iftorlik  : 18:15",
        show_alert=True)
@dp.callback_query(F.data == "f2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Farg'onada \n Ramazon 2-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 18:16",
        show_alert=True)
@dp.callback_query(F.data == "f3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Farg'onada \n Ramazon 3-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 18:17",
        show_alert=True)
@dp.callback_query(F.data == "f4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Farg'onada \n Ramazon 4-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 18:18",
        show_alert=True)
@dp.callback_query(F.data == "f5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Farg'onada \n Ramazon 5-Kuni \n\nSaharlik : 5:11 \n Iftorlik  : 18:19",
        show_alert=True)
@dp.callback_query(F.data == "f6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Farg'onada \n Ramazon 6-Kuni \n\nSaharlik : 5:09 \n Iftorlik  : 18:20",
        show_alert=True)
@dp.callback_query(F.data == "f7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart Farg'onada \n Ramazon 7-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 18:21",
        show_alert=True)
@dp.callback_query(F.data == "f8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Farg'onada \n Ramazon 8-Kuni \n\nSaharlik : 5:06 \n Iftorlik  : 18:22",
        show_alert=True)
@dp.callback_query(F.data == "f9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Farg'onada \n Ramazon 9-Kuni \n\nSaharlik : 5:04 \n Iftorlik  : 18:23",
        show_alert=True)
@dp.callback_query(F.data == "f10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Farg'onada \n Ramazon 10-Kuni \n\nSaharlik : 5:02 \n Iftorlik  : 18:24",
        show_alert=True)
@dp.callback_query(F.data == "f11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Farg'onada \n Ramazon 11-Kuni \n\nSaharlik : 5:01 \n Iftorlik  : 18:25",
        show_alert=True)
@dp.callback_query(F.data == "f12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Farg'onada \n Ramazon 12-Kuni \n\nSaharlik : 4:59 \n Iftorlik  : 18:26",
        show_alert=True)
@dp.callback_query(F.data == "f13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Farg'onada \n Ramazon 13-Kuni \n\nSaharlik : 04:57 \n Iftorlik  : 18:27",
        show_alert=True)
@dp.callback_query(F.data == "f14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Farg'onada \n Ramazon 14-Kuni \n\nSaharlik : 04:55 \n Iftorlik  : 18:28",
        show_alert=True)
@dp.callback_query(F.data == "f15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Farg'onada \n Ramazon 15-Kuni \n\nSaharlik : 04:54\n Iftorlik  : 18:30",
        show_alert=True)
@dp.callback_query(F.data == "f16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Farg'onada \n Ramazon 16-Kuni \n\nSaharlik : 04:52 \n Iftorlik  : 18:32",
        show_alert=True)
@dp.callback_query(F.data == "f17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Farg'onada \n Ramazon 17-Kuni \n\nSaharlik : 04:50 \n Iftorlik  : 18:33",
        show_alert=True)
@dp.callback_query(F.data == "f18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Farg'onada \n Ramazon 18-Kuni \n\nSaharlik : 04:48 \n Iftorlik  : 18:34",
        show_alert=True)
@dp.callback_query(F.data == "f19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Farg'onada \n Ramazon 19-Kuni \n\nSaharlik : 04:47 \n Iftorlik  : 18:35",
        show_alert=True)
@dp.callback_query(F.data == "f20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Farg'onada \n Ramazon 20-Kuni \n\nSaharlik : 04:45 \n Iftorlik  : 18:36",
        show_alert=True)
@dp.callback_query(F.data == "f21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Farg'onada \n Ramazon 21-Kuni \n\nSaharlik : 04:43 \n Iftorlik  : 18:37",
        show_alert=True)
@dp.callback_query(F.data == "f22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Farg'onada \n Ramazon 22-Kuni \n\nSaharlik : 04:41 \n Iftorlik  : 18:38",
        show_alert=True)
@dp.callback_query(F.data == "f23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Farg'onada \n Ramazon 23-Kuni \n\nSaharlik : 04:39 \n Iftorlik  : 18:39",
        show_alert=True)
@dp.callback_query(F.data == "f24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Farg'onada \n Ramazon 24-Kuni \n\nSaharlik : 04:38 \n Iftorlik  : 18:40",
        show_alert=True)
@dp.callback_query(F.data == "f25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Farg'onada \n Ramazon 25-Kuni \n\nSaharlik : 04:36 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "f26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Farg'onada \n Ramazon 26-Kuni \n\nSaharlik : 04:34 \n Iftorlik  : 18:42",
        show_alert=True)
@dp.callback_query(F.data == "f27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Farg'onada \n Ramazon 27-Kuni \n\nSaharlik : 04:32 \n Iftorlik  : 18:43",
        show_alert=True)
@dp.callback_query(F.data == "f28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel Farg'onada \n Ramazon 28-Kuni \n\nSaharlik : 04:30 \n Iftorlik  : 18:45",
        show_alert=True)
@dp.callback_query(F.data == "f29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Farg'onada \n Ramazon 29-Kuni \n\nSaharlik : 04:29 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "f30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Farg'onada \n Ramazon 30-Kuni \n\nSaharlik : 04:27 \n Iftorlik  : 18:45",
        show_alert=True)
    


@dp.callback_query(F.data == "g1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Gulistonda \n Ramazon 1-Kuni \n\nSaharlik : 5:29 \n Iftorlik  : 18:27",
        show_alert=True)
@dp.callback_query(F.data == "g2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Gulistonda \n Ramazon 2-Kuni \n\nSaharlik : 5:28 \n Iftorlik  : 18:29",
        show_alert=True)
@dp.callback_query(F.data == "g3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Gulistonda \n Ramazon 3-Kuni \n\nSaharlik : 5:26 \n Iftorlik  : 18:30",
        show_alert=True)
@dp.callback_query(F.data == "g4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Gulistonda \n Ramazon 4-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 18:31",
        show_alert=True)
@dp.callback_query(F.data == "g5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Gulistonhda \n Ramazon 5-Kuni \n\nSaharlik : 5:23 \n Iftorlik  : 18:32",
        show_alert=True)
@dp.callback_query(F.data == "g6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Gulistonda \n Ramazon 6-Kuni \n\nSaharlik : 5:21 \n Iftorlik  : 18:33",
        show_alert=True)
@dp.callback_query(F.data == "g7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Gulistonda \n Ramazon 7-Kuni \n\nSaharlik : 5:19 \n Iftorlik  : 18:34",
        show_alert=True)
@dp.callback_query(F.data == "g8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Gulistonda \n Ramazon 8-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 18:35",
        show_alert=True)
@dp.callback_query(F.data == "g9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Gulistonda \n Ramazon 9-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 18:36",
        show_alert=True)
@dp.callback_query(F.data == "g10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Gulistonda \n Ramazon 10-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 18:37",
        show_alert=True)
@dp.callback_query(F.data == "g11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Gulistonda \n Ramazon 11-Kuni \n\nSaharlik : 5:13 \n Iftorlik  : 18:38",
        show_alert=True)
@dp.callback_query(F.data == "g12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Gulistonda \n Ramazon 12-Kuni \n\nSaharlik : 5:11 \n Iftorlik  : 18:39",
        show_alert=True)
@dp.callback_query(F.data == "g13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Gulistonda \n Ramazon 13-Kuni \n\nSaharlik : 5:09\n Iftorlik  : 18:40",
        show_alert=True)
@dp.callback_query(F.data == "g14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Gulistonda \n Ramazon 14-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "g15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart Gulistonda \n Ramazon 15-Kuni \n\nSaharlik : 5:06 \n Iftorlik  : 18:42",
        show_alert=True)
@dp.callback_query(F.data == "g16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Gulistonda \n Ramazon 16-Kuni \n\nSaharlik : 5:04 \n Iftorlik  : 18:43",
        show_alert=True)
@dp.callback_query(F.data == "g17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Gulistonda \n Ramazon 17-Kuni \n\nSaharlik : 5:02 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "g18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Urganchda \n Ramazon 18-Kuni \n\nSaharlik : 5:00 \n Iftorlik  : 18:45",
        show_alert=True)
@dp.callback_query(F.data == "g19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Gulistonda \n Ramazon 19-Kuni \n\nSaharlik : 4:58 \n Iftorlik  : 18:46",
        show_alert=True)
@dp.callback_query(F.data == "g20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Gulistonda \n Ramazon 20-Kuni \n\nSaharlik : 4:57 \n Iftorlik  : 18:47",
        show_alert=True)
@dp.callback_query(F.data == "g21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Gulistonda \n Ramazon 21-Kuni \n\nSaharlik : 4:55 \n Iftorlik  : 18:48",
        show_alert=True)
@dp.callback_query(F.data == "g22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Gulistonda \n Ramazon 22-Kuni \n\nSaharlik : 4:53 \n Iftorlik  : 18:49",
        show_alert=True)
@dp.callback_query(F.data == "g23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Gulistonda \n Ramazon 23-Kuni \n\nSaharlik : 4:49 \n Iftorlik  : 18:50",
        show_alert=True)
@dp.callback_query(F.data == "g24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Gulistonda \n Ramazon 24-Kuni \n\nSaharlik : 4:48 \n Iftorlik  : 18:51",
        show_alert=True)
@dp.callback_query(F.data == "g25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Gulistonda \n Ramazon 25-Kuni \n\nSaharlik : 4:46 \n Iftorlik  : 18:52",
        show_alert=True)
@dp.callback_query(F.data == "g26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Gulistonda \n Ramazon 26-Kuni \n\nSaharlik : 4:44 \n Iftorlik  : 18:53",
        show_alert=True)
@dp.callback_query(F.data == "g27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Gulistonda \n Ramazon 27-Kuni \n\nSaharlik : 4:42 \n Iftorlik  : 18:54",
        show_alert=True)
@dp.callback_query(F.data == "g28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Gulistonda \n Ramazon 28-Kuni \n\nSaharlik : 4:40 \n Iftorlik  : 18:55",
        show_alert=True)
@dp.callback_query(F.data == "g29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Gulistonda \n Ramazon 29-Kuni \n\nSaharlik : 4:39 \n Iftorlik  : 18:56",
        show_alert=True)
@dp.callback_query(F.data == "g30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Gulistonda \n Ramazon 30-Kuni \n\nSaharlik : 4:99 \n Iftorlik  : 18:57",
        show_alert=True)
    
@dp.callback_query(F.data == "j1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Jizzaxda \n Ramazon 1-Kuni \n\nSaharlik : 5:33 \n Iftorlik  : 18:31",
        show_alert=True)
@dp.callback_query(F.data == "j2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Jizzaxda \n Ramazon 2-Kuni \n\nSaharlik : 5:32 \n Iftorlik  : 18:32",
        show_alert=True)
@dp.callback_query(F.data == "j3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Jizzaxda \n Ramazon 3-Kuni \n\nSaharlik : 5:30 \n Iftorlik  : 19:33",
        show_alert=True)
@dp.callback_query(F.data == "j4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Jizzaxda \n Ramazon 4-Kuni \n\nSaharlik : 5:28 \n Iftorlik  : 19:34",
        show_alert=True)
@dp.callback_query(F.data == "j5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Jizzaxda \n Ramazon 5-Kuni \n\nSaharlik : 5:27 \n Iftorlik  : 19:35",
        show_alert=True)
@dp.callback_query(F.data == "j6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Jizzaxda \n Ramazon 6-Kuni \n\nSaharlik : 5:25 \n Iftorlik  : 19:36",
        show_alert=True)
@dp.callback_query(F.data == "j7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Jizzaxda \n Ramazon 7-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 19:37",
        show_alert=True)
@dp.callback_query(F.data == "j8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Jizzaxda \n Ramazon 8-Kuni \n\nSaharlik : 5:22 \n Iftorlik  : 19:39",
        show_alert=True)
@dp.callback_query(F.data == "j9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Jizzaxda \n Ramazon 9-Kuni \n\nSaharlik : 5:20 \n Iftorlik  : 19:40",
        show_alert=True)
@dp.callback_query(F.data == "j10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Jizzaxda \n Ramazon 10-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 19:41",
        show_alert=True)
@dp.callback_query(F.data == "j11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Jizzaxda \n Ramazon 11-Kuni \n\nSaharlik : 5:17 \n Iftorlik  : 19:42",
        show_alert=True)
@dp.callback_query(F.data == "j12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Jizzaxda \n Ramazon 12-Kuni \n\nSaharlik : 5:15 \n Iftorlik  : 19:43",
        show_alert=True)
@dp.callback_query(F.data == "j13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Jizzaxda \n Ramazon 13-Kuni \n\nSaharlik : 5:13 \n Iftorlik  : 19:44",
        show_alert=True)
@dp.callback_query(F.data == "j14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Jizzaxda \n Ramazon 14-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 19:45",
        show_alert=True)
@dp.callback_query(F.data == "j15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Jizzaxda \n Ramazon 15-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 19:46",
        show_alert=True)
@dp.callback_query(F.data == "j16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Jizzaxda \n Ramazon 16-Kuni \n\nSaharlik : 5:08 \n Iftorlik  : 19:47",
        show_alert=True)
@dp.callback_query(F.data == "j17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Jizzaxda \n Ramazon 17-Kuni \n\nSaharlik : 5:06 \n Iftorlik  : 19:48",
        show_alert=True)
@dp.callback_query(F.data == "j18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Jizzaxda \n Ramazon 18-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 19:49",
        show_alert=True)
@dp.callback_query(F.data == "j19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Jizzaxda \n Ramazon 19-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 19:50",
        show_alert=True)
@dp.callback_query(F.data == "j20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Jizzaxda \n Ramazon 20-Kuni \n\nSaharlik : 5:01 \n Iftorlik  : 19:51",
        show_alert=True)
@dp.callback_query(F.data == "j21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Jizzaxda  \n Ramazon 21-Kuni \n\nSaharlik : 4:59 \n Iftorlik  : 19:52",
        show_alert=True)
@dp.callback_query(F.data == "j22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Jizzaxda \n Ramazon 22-Kuni \n\nSaharlik : 4:57 \n Iftorlik  : 19:53",
        show_alert=True)
@dp.callback_query(F.data == "j23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Jizzaxda \n Ramazon 23-Kuni \n\nSaharlik : 4:56 \n Iftorlik  : 19:54",
        show_alert=True)
@dp.callback_query(F.data == "j24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Jizzaxda \n Ramazon 24-Kuni \n\nSaharlik : 4:54 \n Iftorlik  : 19:55",
        show_alert=True)
@dp.callback_query(F.data == "j25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Jizzaxda \n Ramazon 25-Kuni \n\nSaharlik : 4:52 \n Iftorlik  : 19:56",
        show_alert=True)
@dp.callback_query(F.data == "j26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Jizzaxda \n Ramazon 26-Kuni \n\nSaharlik : 4:50 \n Iftorlik  : 19:57",
        show_alert=True)
@dp.callback_query(F.data == "j27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Jizzaxda \n Ramazon 27-Kuni \n\nSaharlik : 4:49 \n Iftorlik  : 19:58",
        show_alert=True)
@dp.callback_query(F.data == "j28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Jizzaxda \n Ramazon 28-Kuni \n\nSaharlik : 4:47 \n Iftorlik  : 19:59",
        show_alert=True)
@dp.callback_query(F.data == "j29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Jizzaxda \n Ramazon 29-Kuni \n\nSaharlik : 4:15 \n Iftorlik  : 19:00",
        show_alert=True)
@dp.callback_query(F.data == "j30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Jizzaxda \n Ramazon 30-Kuni \n\nSaharlik : 4:43 \n Iftorlik  : 19:01",
        show_alert=True)


@dp.callback_query(F.data == "n1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Namanganda \n Ramazon 1-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 18:15",
        show_alert=True)
@dp.callback_query(F.data == "n2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Namanganda \n Ramazon 2-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 19:16",
        show_alert=True)
@dp.callback_query(F.data == "n3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Namanganda \n Ramazon 3-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 19:17",
        show_alert=True)
@dp.callback_query(F.data == "n4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Namanganda \n Ramazon 4-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 19:18",
        show_alert=True)
@dp.callback_query(F.data == "n5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Namanganda \n Ramazon 5-Kuni \n\nSaharlik : 5:11 \n Iftorlik  : 19:19",
        show_alert=True)
@dp.callback_query(F.data == "n6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Namanganda \n Ramazon 6-Kuni \n\nSaharlik : 5:09 \n Iftorlik  : 19:20",
        show_alert=True)
@dp.callback_query(F.data == "n7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Namanganda \n Ramazon 7-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 19:21",
        show_alert=True)
@dp.callback_query(F.data == "n8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Namanganda \n Ramazon 8-Kuni \n\nSaharlik : 5:49 \n Iftorlik  : 19:22",
        show_alert=True)
@dp.callback_query(F.data == "n9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Namanganda \n Ramazon 9-Kuni \n\nSaharlik : 5:48 \n Iftorlik  : 19:23",
        show_alert=True)
@dp.callback_query(F.data == "n10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Namanganda \n Ramazon 10-Kuni \n\nSaharlik : 5:46 \n Iftorlik  : 19:24",
        show_alert=True)
@dp.callback_query(F.data == "n11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Namanganda \n Ramazon 11-Kuni \n\nSaharlik : 5:44 \n Iftorlik  : 19:25",
        show_alert=True)
@dp.callback_query(F.data == "n12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Namanganda \n Ramazon 12-Kuni \n\nSaharlik : 5:42 \n Iftorlik  : 19:25",
        show_alert=True)
@dp.callback_query(F.data == "n13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Namanganda \n Ramazon 13-Kuni \n\nSaharlik : 5:40 \n Iftorlik  : 19:26",
        show_alert=True)
@dp.callback_query(F.data == "n14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Namanganda \n Ramazon 14-Kuni \n\nSaharlik : 5:38 \n Iftorlik  : 19:27",
        show_alert=True)
@dp.callback_query(F.data == "n15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Namanganda \n Ramazon 15-Kuni \n\nSaharlik : 5:37 \n Iftorlik  : 19:28",
        show_alert=True)
@dp.callback_query(F.data == "n16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Namanganda \n Ramazon 16-Kuni \n\nSaharlik : 5:35 \n Iftorlik  : 19:30",
        show_alert=True)
@dp.callback_query(F.data == "n17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Namanganda \n Ramazon 17-Kuni \n\nSaharlik : 5:33 \n Iftorlik  : 19:31",
        show_alert=True)
@dp.callback_query(F.data == "n18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Namanganda \n Ramazon 18-Kuni \n\nSaharlik : 5:31 \n Iftorlik  : 19:32",
        show_alert=True)
@dp.callback_query(F.data == "n19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Namanganda \n Ramazon 19-Kuni \n\nSaharlik : 5:29 \n Iftorlik  : 19:33",
        show_alert=True)
@dp.callback_query(F.data == "n20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Namanganda \n Ramazon 20-Kuni \n\nSaharlik : 5:27 \n Iftorlik  : 19:34",
        show_alert=True)
@dp.callback_query(F.data == "n21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Namanganda \n Ramazon 21-Kuni \n\nSaharlik : 5:25 \n Iftorlik  : 19:35",
        show_alert=True)
@dp.callback_query(F.data == "n22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Namanganda \n Ramazon 22-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 19:36",
        show_alert=True)
@dp.callback_query(F.data == "n23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Namanganda \n Ramazon 23-Kuni \n\nSaharlik : 5:22 \n Iftorlik  : 19:37",
        show_alert=True)
@dp.callback_query(F.data == "n24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Namanganda \n Ramazon 24-Kuni \n\nSaharlik : 5:20 \n Iftorlik  : 19:38",
        show_alert=True)
@dp.callback_query(F.data == "n25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Namanganda \n Ramazon 25-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 19:39",
        show_alert=True)
@dp.callback_query(F.data == "n26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Namanganda \n Ramazon 26-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 19:40",
        show_alert=True)
@dp.callback_query(F.data == "n27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Namanganda \n Ramazon 27-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 19:41",
        show_alert=True)
@dp.callback_query(F.data == "n28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Namanganda \n Ramazon 28-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 19:42",
        show_alert=True)
@dp.callback_query(F.data == "n29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Namanganda \n Ramazon 29-Kuni \n\nSaharlik : 5:11 \n Iftorlik  : 19:43",
        show_alert=True)
@dp.callback_query(F.data == "n30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Namanganda \n Ramazon 30-Kuni \n\nSaharlik : 5:09 \n Iftorlik  : 19:44",
        show_alert=True)
    

@dp.callback_query(F.data == "N1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Navoida \n Ramazon 1-Kuni \n\nSaharlik : 5:43 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "N2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Navoida \n Ramazon 2-Kuni \n\nSaharlik : 5:41 \n Iftorlik  : 19:42",
        show_alert=True)
@dp.callback_query(F.data == "N3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Navoida \n Ramazon 3-Kuni \n\nSaharlik : 5:39 \n Iftorlik  : 18:43",
        show_alert=True)
@dp.callback_query(F.data == "N4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Navoida \n Ramazon 4-Kuni \n\nSaharlik : 5:37 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "N5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Navoida \n Ramazon 5-Kuni \n\nSaharlik : 5:36 \n Iftorlik  : 18:45",
        show_alert=True)
@dp.callback_query(F.data == "N6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Navoida \n Ramazon 6-Kuni \n\nSaharlik : 5:34 \n Iftorlik  : 18:46",
        show_alert=True)
@dp.callback_query(F.data == "N7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Navoida \n Ramazon 7-Kuni \n\nSaharlik : 5:32 \n Iftorlik  : 18:47",
        show_alert=True)
@dp.callback_query(F.data == "N8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Navoida \n Ramazon 8-Kuni \n\nSaharlik : 5:30 \n Iftorlik  : 18:48",
        show_alert=True)
@dp.callback_query(F.data == "N9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Navoida \n Ramazon 9-Kuni \n\nSaharlik : 5:28 \n Iftorlik  : 18:49",
        show_alert=True)
@dp.callback_query(F.data == "N10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Navoida \n Ramazon 10-Kuni \n\nSaharlik : 5:27 \n Iftorlik  : 18:50",
        show_alert=True)
@dp.callback_query(F.data == "N11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Navoida \n Ramazon 11-Kuni \n\nSaharlik : 5:25 \n Iftorlik  : 18:51",
        show_alert=True)
@dp.callback_query(F.data == "N12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Navoida \n Ramazon 12-Kuni \n\nSaharlik : 5:23 \n Iftorlik  : 18:52",
        show_alert=True)
@dp.callback_query(F.data == "N13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Navoida \n Ramazon 13-Kuni \n\nSaharlik : 5:21 \n Iftorlik  : 18:53",
        show_alert=True)
@dp.callback_query(F.data == "N14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Navoida \n Ramazon 14-Kuni \n\nSaharlik : 5:19 \n Iftorlik  : 18:54",
        show_alert=True)
@dp.callback_query(F.data == "N15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart Navoida \n Ramazon 15-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 18:55",
        show_alert=True)
@dp.callback_query(F.data == "N16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Navoida \n Ramazon 16-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 18:56",
        show_alert=True)
@dp.callback_query(F.data == "N17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Navoida \n Ramazon 17-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 18:57",
        show_alert=True)
@dp.callback_query(F.data == "N18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Navoida \n Ramazon 18-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 18:58",
        show_alert=True)
@dp.callback_query(F.data == "N19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Navoida \n Ramazon 19-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 18:59",
        show_alert=True)
@dp.callback_query(F.data == "N20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Navoida \n Ramazon 20-Kuni \n\nSaharlik : 5:09 \n Iftorlik  : 19:00",
        show_alert=True)
@dp.callback_query(F.data == "N21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Navoida \n Ramazon 21-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 19:01",
        show_alert=True)
@dp.callback_query(F.data == "N22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Navoida \n Ramazon 22-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 19:02",
        show_alert=True)
@dp.callback_query(F.data == "N23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Navoida \n Ramazon 23-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 19:03",
        show_alert=True)
@dp.callback_query(F.data == "N24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Navoida \n Ramazon 24-Kuni \n\nSaharlik : 5:02 \n Iftorlik  : 19:04",
        show_alert=True)
@dp.callback_query(F.data == "N25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Navoida \n Ramazon 25-Kuni \n\nSaharlik : 5:00 \n Iftorlik  : 19:06",
        show_alert=True)
@dp.callback_query(F.data == "N26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Navoida \n Ramazon 26-Kuni \n\nSaharlik : 4:58 \n Iftorlik  : 19:07",
        show_alert=True)
@dp.callback_query(F.data == "N27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Navoida \n Ramazon 27-Kuni \n\nSaharlik : 4:16 \n Iftorlik  : 19:08",
        show_alert=True)
@dp.callback_query(F.data == "N28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Navoida \n Ramazon 28-Kuni \n\nSaharlik : 4:54 \n Iftorlik  : 19:09",
        show_alert=True)
@dp.callback_query(F.data == "N29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Navoida \n Ramazon 29-Kuni \n\nSaharlik : 4:53 \n Iftorlik  : 19:10",
        show_alert=True)
@dp.callback_query(F.data == "N30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Navoida \n Ramazon 30-Kuni \n\nSaharlik : 4:51 \n Iftorlik  : 19:11",
        show_alert=True)
    
@dp.callback_query(F.data == "t1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Termizda \n Ramazon 1-Kuni \n\nSaharlik : 5:37 \n Iftorlik  : 18:34",
        show_alert=True)
@dp.callback_query(F.data == "t2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Termizda \n Ramazon 2-Kuni \n\nSaharlik : 5:35 \n Iftorlik  : 18:35",
        show_alert=True)
@dp.callback_query(F.data == "t3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Termizda \n Ramazon 3-Kuni \n\nSaharlik : 5:33 \n Iftorlik  : 18:36",
        show_alert=True)
@dp.callback_query(F.data == "t4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Termizda \n Ramazon 4-Kuni \n\nSaharlik : 5:31 \n Iftorlik  : 18:37",
        show_alert=True)
@dp.callback_query(F.data == "t5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Termizda \n Ramazon 5-Kuni \n\nSaharlik : 5:30 \n Iftorlik  : 18:38",
        show_alert=True)
@dp.callback_query(F.data == "t6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Termizda \n Ramazon 6-Kuni \n\nSaharlik : 5:28 \n Iftorlik  : 18:39",
        show_alert=True)
@dp.callback_query(F.data == "t7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Termizda \n Ramazon 7-Kuni \n\nSaharlik : 5:26 \n Iftorlik  : 18:40",
        show_alert=True)
@dp.callback_query(F.data == "t8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Termizda \n Ramazon 8-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "t9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Termizda \n Ramazon 9-Kuni \n\nSaharlik : 5:22 \n Iftorlik  : 18:42",
        show_alert=True)
@dp.callback_query(F.data == "t10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Termizda \n Ramazon 10-Kuni \n\nSaharlik : 5:21 \n Iftorlik  : 18:43",
        show_alert=True)
@dp.callback_query(F.data == "t11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Termizda \n Ramazon 11-Kuni \n\nSaharlik : 5:19 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "t12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Termizda \n Ramazon 12-Kuni \n\nSaharlik : 5:17 \n Iftorlik  : 18:45",
        show_alert=True)
@dp.callback_query(F.data == "t13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Termizda \n Ramazon 13-Kuni \n\nSaharlik : 5:15 \n Iftorlik  : 18:46",
        show_alert=True)
@dp.callback_query(F.data == "t14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Termizda \n Ramazon 14-Kuni \n\nSaharlik : 5:13 \n Iftorlik  : 18:47",
        show_alert=True)
@dp.callback_query(F.data == "t15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Termizda \n Ramazon 15-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 18:49",
        show_alert=True)
@dp.callback_query(F.data == "t16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Termizda \n Ramazon 16-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 18:51",
        show_alert=True)
@dp.callback_query(F.data == "t17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Termizda \n Ramazon 17-Kuni \n\nSaharlik : 5:08 \n Iftorlik  : 18:52",
        show_alert=True)
@dp.callback_query(F.data == "t18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Termizda \n Ramazon 18-Kuni \n\nSaharlik : 5:06 \n Iftorlik  : 18:53",
        show_alert=True)
@dp.callback_query(F.data == "t19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Termizda \n Ramazon 19-Kuni \n\nSaharlik : 5:04 \n Iftorlik  : 18:54",
        show_alert=True)
@dp.callback_query(F.data == "t20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Termizda \n Ramazon 20-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 18:55",
        show_alert=True)
@dp.callback_query(F.data == "t21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Termizda \n Ramazon 21-Kuni \n\nSaharlik : 5:01 \n Iftorlik  : 18:56",
        show_alert=True)
@dp.callback_query(F.data == "t22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Termizda \n Ramazon 22-Kuni \n\nSaharlik : 4:59 \n Iftorlik  : 18:57",
        show_alert=True)
@dp.callback_query(F.data == "t23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Termizda \n Ramazon 23-Kuni \n\nSaharlik : 4:57 \n Iftorlik  : 18:58",
        show_alert=True)
@dp.callback_query(F.data == "t24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Termizda \n Ramazon 24-Kuni \n\nSaharlik : 4:55 \n Iftorlik  : 18:59",
        show_alert=True)
@dp.callback_query(F.data == "t25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Termizda \n Ramazon 25-Kuni \n\nSaharlik : 4:54 \n Iftorlik  : 19:00",
        show_alert=True)
@dp.callback_query(F.data == "t26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Termizda \n Ramazon 26-Kuni \n\nSaharlik : 4:52 \n Iftorlik  : 19:01",
        show_alert=True)
@dp.callback_query(F.data == "t27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Termizda \n Ramazon 27-Kuni \n\nSaharlik : 4:50 \n Iftorlik  : 19:02",
        show_alert=True)
@dp.callback_query(F.data == "t28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Termizda \n Ramazon 28-Kuni \n\nSaharlik : 4:48 \n Iftorlik  : 19:03",
        show_alert=True)
@dp.callback_query(F.data == "t29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Termizda \n Ramazon 29-Kuni \n\nSaharlik : 4:46 \n Iftorlik  : 19:04",
        show_alert=True)
@dp.callback_query(F.data == "t30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Termizda \n Ramazon 30-Kuni \n\nSaharlik : 4:44 \n Iftorlik  : 19:05",
        show_alert=True)
 
    
@dp.callback_query(F.data == "q1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Qarshida \n Ramazon 1-Kuni \n\nSaharlik : 5:42 \n Iftorlik  : 18:39",
        show_alert=True)
@dp.callback_query(F.data == "q2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Qarshida \n Ramazon 2-Kuni \n\nSaharlik : 5:40 \n Iftorlik  : 18:40",
        show_alert=True)
@dp.callback_query(F.data == "q3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Qarshida \n Ramazon 3-Kuni \n\nSaharlik : 5:38 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "q4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Qarshida \n Ramazon 4-Kuni \n\nSaharlik : 5:36 \n Iftorlik  : 18:42",
        show_alert=True)
@dp.callback_query(F.data == "q5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Qarshida \n Ramazon 5-Kuni \n\nSaharlik : 5:35 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "q6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Qarshida \n Ramazon 6-Kuni \n\nSaharlik : 5:34 \n Iftorlik  : 18:45",
        show_alert=True)
@dp.callback_query(F.data == "q7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Qarshida \n Ramazon 7-Kuni \n\nSaharlik : 5:32 \n Iftorlik  : 18:46",
        show_alert=True)
@dp.callback_query(F.data == "q8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Qarshida \n Ramazon 8-Kuni \n\nSaharlik : 5:30 \n Iftorlik  : 18:47",
        show_alert=True)
@dp.callback_query(F.data == "q9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Qarshida \n Ramazon 9-Kuni \n\nSaharlik : 5:29 \n Iftorlik  : 18:48",
        show_alert=True)
@dp.callback_query(F.data == "q10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Qarshida \n Ramazon 10-Kuni \n\nSaharlik : 5:27 \n Iftorlik  : 18:49",
        show_alert=True)
@dp.callback_query(F.data == "q11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Qarshida \n Ramazon 11-Kuni \n\nSaharlik : 5:25 \n Iftorlik  : 18:50",
        show_alert=True)
@dp.callback_query(F.data == "q12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Qarshida \n Ramazon 12-Kuni \n\nSaharlik : 5:23 \n Iftorlik  : 18:51",
        show_alert=True)
@dp.callback_query(F.data == "q13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Qarshida \n Ramazon 13-Kuni \n\nSaharlik : 5:21 \n Iftorlik  : 18:52",
        show_alert=True)
@dp.callback_query(F.data == "q14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Qarshida \n Ramazon 14-Kuni \n\nSaharlik : 5:20 \n Iftorlik  : 18:53",
        show_alert=True)
@dp.callback_query(F.data == "q15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Qarshida \n Ramazon 15-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 18:55",
        show_alert=True)
@dp.callback_query(F.data == "q16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Qarshida \n Ramazon 16-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 18:56",
        show_alert=True)
@dp.callback_query(F.data == "q17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Qarshida \n Ramazon 17-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 18:57",
        show_alert=True)
@dp.callback_query(F.data == "q18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Qarshida \n Ramazon 18-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 18:58",
        show_alert=True)
@dp.callback_query(F.data == "q19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Qarshida \n Ramazon 19-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 18:59",
        show_alert=True)
@dp.callback_query(F.data == "q20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Qarshida \n Ramazon 20-Kuni \n\nSaharlik : 5:08 \n Iftorlik  : 19:00",
        show_alert=True)
@dp.callback_query(F.data == "q21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Qarshida \n Ramazon 21-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 19:01",
        show_alert=True)
@dp.callback_query(F.data == "q22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Qarshida \n Ramazon 22-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 19:02",
        show_alert=True)
@dp.callback_query(F.data == "q23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Qarshida \n Ramazon 23-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 19:03",
        show_alert=True)
@dp.callback_query(F.data == "q24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Qarshida \n Ramazon 24-Kuni \n\nSaharlik : 5:01 \n Iftorlik  : 19:04",
        show_alert=True)
@dp.callback_query(F.data == "q25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Qarshida \n Ramazon 25-Kuni \n\nSaharlik : 4:59 \n Iftorlik  : 19:06",
        show_alert=True)
@dp.callback_query(F.data == "q26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Qarshida \n Ramazon 26-Kuni \n\nSaharlik : 4:57 \n Iftorlik  : 19:07",
        show_alert=True)
@dp.callback_query(F.data == "q27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Qarshida \n Ramazon 27-Kuni \n\nSaharlik : 4:56 \n Iftorlik  : 19:08",
        show_alert=True)
@dp.callback_query(F.data == "q28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Qarshida \n Ramazon 28-Kuni \n\nSaharlik : 4:55 \n Iftorlik  : 19:09",
        show_alert=True)
@dp.callback_query(F.data == "q29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Qarshida \n Ramazon 29-Kuni \n\nSaharlik : 4:53 \n Iftorlik  : 19:10",
        show_alert=True)
@dp.callback_query(F.data == "q30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Qarshida \n Ramazon 30-Kuni \n\nSaharlik : 4:51 \n Iftorlik  : 19:11",
        show_alert=True)

@dp.callback_query(F.data == "s1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Samarqandda \n Ramazon 1-Kuni \n\nSaharlik : 5:37 \n Iftorlik  : 18:34",
        show_alert=True)
@dp.callback_query(F.data == "s2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Samarqandda \n Ramazon 2-Kuni \n\nSaharlik : 5:35 \n Iftorlik  : 18:35",
        show_alert=True)
@dp.callback_query(F.data == "s3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Samarqandda \n Ramazon 3-Kuni \n\nSaharlik : 5:33 \n Iftorlik  : 18:36",
        show_alert=True)
@dp.callback_query(F.data == "s4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Samarqandda \n Ramazon 4-Kuni \n\nSaharlik : 5:31 \n Iftorlik  : 18:37",
        show_alert=True)
@dp.callback_query(F.data == "s5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Samarqandda \n Ramazon 5-Kuni \n\nSaharlik : 5:30 \n Iftorlik  : 18:38",
        show_alert=True)
@dp.callback_query(F.data == "s6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Samarqandda \n Ramazon 6-Kuni \n\nSaharlik : 5:28 \n Iftorlik  : 18:39",
        show_alert=True)
@dp.callback_query(F.data == "s7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Samarqandda \n Ramazon 7-Kuni \n\nSaharlik : 5:26 \n Iftorlik  : 18:40",
        show_alert=True)
@dp.callback_query(F.data == "s8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Samarqandda \n Ramazon 8-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "s9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart Samarqandda \n Ramazon 9-Kuni \n\nSaharlik : 5:22 \n Iftorlik  : 18:42",
        show_alert=True)
@dp.callback_query(F.data == "s10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Samarqandda \n Ramazon 10-Kuni \n\nSaharlik : 5:21 \n Iftorlik  : 18:43",
        show_alert=True)
@dp.callback_query(F.data == "s11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Samarqandda \n Ramazon 11-Kuni \n\nSaharlik : 5:19 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "s12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Samarqandda \n Ramazon 12-Kuni \n\nSaharlik : 5:17 \n Iftorlik  : 19:45",
        show_alert=True)
@dp.callback_query(F.data == "s13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Samarqandda \n Ramazon 13-Kuni \n\nSaharlik : 5:15 \n Iftorlik  : 18:46",
        show_alert=True)
@dp.callback_query(F.data == "s14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Samarqandda \n Ramazon 14-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 18:47",
        show_alert=True)
@dp.callback_query(F.data == "s15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Samarqandda \n Ramazon 15-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 18:48",
        show_alert=True)
@dp.callback_query(F.data == "s16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Samarqandda \n Ramazon 16-Kuni \n\nSaharlik : 5:11 \n Iftorlik  : 18:50",
        show_alert=True)
@dp.callback_query(F.data == "s17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Samarqandda \n Ramazon 17-Kuni \n\nSaharlik : 5:09 \n Iftorlik  : 18:51",
        show_alert=True)
@dp.callback_query(F.data == "s18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Samarqandda \n Ramazon 18-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 18:52",
        show_alert=True)
@dp.callback_query(F.data == "s19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Samarqandda \n Ramazon 19-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 18:53",
        show_alert=True)
@dp.callback_query(F.data == "s20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Samarqandda \n Ramazon 20-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 18:54",
        show_alert=True)
@dp.callback_query(F.data == "s21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Samarqandda \n Ramazon 21-Kuni \n\nSaharlik : 5:02 \n Iftorlik  : 18:55",
        show_alert=True)
@dp.callback_query(F.data == "s22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Samarqandda \n Ramazon 22-Kuni \n\nSaharlik : 5:00 \n Iftorlik  : 18:56",
        show_alert=True)
@dp.callback_query(F.data == "s23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Samarqandda \n Ramazon 23-Kuni \n\nSaharlik : 5:59 \n Iftorlik  : 18:57",
        show_alert=True)
@dp.callback_query(F.data == "s24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Samarqandda \n Ramazon 24-Kuni \n\nSaharlik : 5:58 \n Iftorlik  : 18:58",
        show_alert=True)
@dp.callback_query(F.data == "s25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Samarqandda \n Ramazon 25-Kuni \n\nSaharlik : 5:56 \n Iftorlik  : 18:59",
        show_alert=True)
@dp.callback_query(F.data == "s26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Samarqandda \n Ramazon 26-Kuni \n\nSaharlik : 5:54 \n Iftorlik  : 19:00",
        show_alert=True)
@dp.callback_query(F.data == "s27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Samarqandda \n Ramazon 27-Kuni \n\nSaharlik : 5:52 \n Iftorlik  : 19:01",
        show_alert=True)
@dp.callback_query(F.data == "s28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Samarqandda \n Ramazon 28-Kuni \n\nSaharlik : 5:50 \n Iftorlik  : 19:02",
        show_alert=True)
@dp.callback_query(F.data == "s29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Samarqandda \n Ramazon 29-Kuni \n\nSaharlik : 5:48 \n Iftorlik  : 19:03",
        show_alert=True)
@dp.callback_query(F.data == "s30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Samarqandda \n Ramazon 30-Kuni \n\nSaharlik : 5:46 \n Iftorlik  : 19:04",
        show_alert=True)
    
    
@dp.callback_query(F.data == "z1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  ChirChiqda \n Ramazon 1-Kuni \n\nSaharlik : 5:25 \n Iftorlik  : 18:23",
        show_alert=True)
@dp.callback_query(F.data == "z2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  ChirChiqda \n Ramazon 2-Kuni \n\nSaharlik : 5:24 \n Iftorlik  : 18:24",
        show_alert=True)
@dp.callback_query(F.data == "z3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  ChirChiqda \n Ramazon 3-Kuni \n\nSaharlik : 5:22 \n Iftorlik  : 18:25",
        show_alert=True)
@dp.callback_query(F.data == "z4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  ChirChiqda \n Ramazon 4-Kuni \n\nSaharlik : 5:20 \n Iftorlik  : 18:27",
        show_alert=True)
@dp.callback_query(F.data == "z5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  ChirChiqda \n Ramazon 5-Kuni \n\nSaharlik : 5:19 \n Iftorlik  : 18:28",
        show_alert=True)
@dp.callback_query(F.data == "z6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  ChirChiqda \n Ramazon 6-Kuni \n\nSaharlik : 5:17 \n Iftorlik  : 18:29",
        show_alert=True)
@dp.callback_query(F.data == "z7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  ChirChiqda \n Ramazon 7-Kuni \n\nSaharlik : 5:15 \n Iftorlik  : 18:30",
        show_alert=True)
@dp.callback_query(F.data == "z8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  ChirChiqda \n Ramazon 8-Kuni \n\nSaharlik : 5:13 \n Iftorlik  : 18:31",
        show_alert=True)
@dp.callback_query(F.data == "z9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  ChirChiqda \n Ramazon 9-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 18:32",
        show_alert=True)
@dp.callback_query(F.data == "z10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  ChirChiqda \n Ramazon 10-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 18:33",
        show_alert=True)
@dp.callback_query(F.data == "z11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart ChirChiqda \n Ramazon 11-Kuni \n\nSaharlik : 5:08 \n Iftorlik  : 18:34",
        show_alert=True)
@dp.callback_query(F.data == "z12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  ChirChiqda \n Ramazon 12-Kuni \n\nSaharlik : 5:06 \n Iftorlik  : 18:35",
        show_alert=True)
@dp.callback_query(F.data == "z13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  ChirChiqda \n Ramazon 13-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 18:37",
        show_alert=True)
@dp.callback_query(F.data == "z14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  ChirChiqda \n Ramazon 14-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 18:38",
        show_alert=True)
@dp.callback_query(F.data == "z15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  ChirChiqda \n Ramazon 15-Kuni \n\nSaharlik : 5:01 \n Iftorlik  : 18:39",
        show_alert=True)
@dp.callback_query(F.data == "z16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  ChirChiqda \n Ramazon 16-Kuni \n\nSaharlik : 4:59 \n Iftorlik  : 18:40",
        show_alert=True)
@dp.callback_query(F.data == "z17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  ChirChiqda \n Ramazon 17-Kuni \n\nSaharlik : 4:57 \n Iftorlik  : 18:41",
        show_alert=True)
@dp.callback_query(F.data == "z18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  ChirChiqhda \n Ramazon 18-Kuni \n\nSaharlik : 4:55 \n Iftorlik  : 18:42",
        show_alert=True)
@dp.callback_query(F.data == "z19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  ChirChiqda \n Ramazon 19-Kuni \n\nSaharlik : 4:54 \n Iftorlik  : 18:43",
        show_alert=True)
@dp.callback_query(F.data == "z20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  ChirChiqda \n Ramazon 20-Kuni \n\nSaharlik : 4:52 \n Iftorlik  : 18:44",
        show_alert=True)
@dp.callback_query(F.data == "z21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  ChirChiqda \n Ramazon 21-Kuni \n\nSaharlik : 4:50 \n Iftorlik  : 18:45",
        show_alert=True)
@dp.callback_query(F.data == "z22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  ChirChiqda \n Ramazon 22-Kuni \n\nSaharlik : 4:48 \n Iftorlik  : 18:46",
        show_alert=True)
@dp.callback_query(F.data == "z23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  ChirChiqda \n Ramazon 23-Kuni \n\nSaharlik : 4:46 \n Iftorlik  : 18:47",
        show_alert=True)
@dp.callback_query(F.data == "z24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  ChirChiqda \n Ramazon 24-Kuni \n\nSaharlik : 4:44 \n Iftorlik  : 18:48",
        show_alert=True)
@dp.callback_query(F.data == "z25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  ChirChiqda \n Ramazon 25-Kuni \n\nSaharlik : 4:42 \n Iftorlik  : 18:50",
        show_alert=True)
@dp.callback_query(F.data == "z26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel ChirChiqda \n Ramazon 26-Kuni \n\nSaharlik : 4:41 \n Iftorlik  : 18:51",
        show_alert=True)
@dp.callback_query(F.data == "z27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  ChirChiqda \n Ramazon 27-Kuni \n\nSaharlik : 4:39 \n Iftorlik  : 18:52",
        show_alert=True)
@dp.callback_query(F.data == "z28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel ChirChiqda \n Ramazon 28-Kuni \n\nSaharlik : 4:37 \n Iftorlik  : 18:53",
        show_alert=True)
@dp.callback_query(F.data == "z29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  ChirChiqda \n Ramazon 29-Kuni \n\nSaharlik : 4:35 \n Iftorlik  : 18:54",
        show_alert=True)
@dp.callback_query(F.data == "z30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  ChirChiqda \n Ramazon 30-Kuni \n\nSaharlik : 4:33 \n Iftorlik  : 18:55",
        show_alert=True)
    
@dp.callback_query(F.data == "T1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 11-Mart  Toshkentda \n Ramazon 1-Kuni \n\nSaharlik : 5:27 \n Iftorlik  : 18:25",
        show_alert=True)
@dp.callback_query(F.data == "T2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 12-Mart  Toshkentda \n Ramazon 2-Kuni \n\nSaharlik : 5:25 \n Iftorlik  : 18:26",
        show_alert=True)
@dp.callback_query(F.data == "T3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 13-Mart  Toshkentda \n Ramazon 3-Kuni \n\nSaharlik :5:23 \n Iftorlik  : 19:27",
        show_alert=True)
@dp.callback_query(F.data == "T4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 14-Mart  Toshkentda \n Ramazon 4-Kuni \n\nSaharlik : 5:21 \n Iftorlik  : 19:28",
        show_alert=True)
@dp.callback_query(F.data == "T5")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 15-Mart  Toshkentda \n Ramazon 5-Kuni \n\nSaharlik : 5:20 \n Iftorlik  : 19:29",
        show_alert=True)
@dp.callback_query(F.data == "T6")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 16-Mart  Toshkentda \n Ramazon 6-Kuni \n\nSaharlik : 5:18 \n Iftorlik  : 19:30",
        show_alert=True)
@dp.callback_query(F.data == "T7")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 17-Mart  Toshkentda \n Ramazon 7-Kuni \n\nSaharlik : 5:16 \n Iftorlik  : 19:31",
        show_alert=True)
@dp.callback_query(F.data == "T8")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 18-Mart  Toshkentda \n Ramazon 8-Kuni \n\nSaharlik : 5:14 \n Iftorlik  : 19:32",
        show_alert=True)
@dp.callback_query(F.data == "T9")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 19-Mart  Toshkentda \n Ramazon 9-Kuni \n\nSaharlik : 5:12 \n Iftorlik  : 19:33",
        show_alert=True)
@dp.callback_query(F.data == "T10")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 20-Mart  Toshkentda \n Ramazon 10-Kuni \n\nSaharlik : 5:10 \n Iftorlik  : 19:34",
        show_alert=True)
@dp.callback_query(F.data == "T11")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 21-Mart  Toshkentda \n Ramazon 11-Kuni \n\nSaharlik : 5:09 \n Iftorlik  : 19:35",
        show_alert=True)
@dp.callback_query(F.data == "T12")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 22-Mart  Toshkentda \n Ramazon 12-Kuni \n\nSaharlik : 5:07 \n Iftorlik  : 19:36",
        show_alert=True)
@dp.callback_query(F.data == "T13")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 23-Mart  Toshkentda \n Ramazon 13-Kuni \n\nSaharlik : 5:05 \n Iftorlik  : 19:37",
        show_alert=True)
@dp.callback_query(F.data == "T14")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 24-Mart  Toshkentda \n Ramazon 14-Kuni \n\nSaharlik : 5:03 \n Iftorlik  : 19:38",
        show_alert=True)
@dp.callback_query(F.data == "T15")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 25-Mart  Toshkentda \n Ramazon 15-Kuni \n\nSaharlik : 5:02 \n Iftorlik  : 19:39",
        show_alert=True)
@dp.callback_query(F.data == "T16")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 26-Mart  Toshkentda \n Ramazon 16-Kuni \n\nSaharlik : 5:00 \n Iftorlik  : 19:41",
        show_alert=True)
@dp.callback_query(F.data == "T17")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 27-Mart  Toshkentda \n Ramazon 17-Kuni \n\nSaharlik : 4:58 \n Iftorlik  : 19:42",
        show_alert=True)
@dp.callback_query(F.data == "T18")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 28-Mart  Toshkentda \n Ramazon 18-Kuni \n\nSaharlik : 4:56 \n Iftorlik  : 19:43",
        show_alert=True)
@dp.callback_query(F.data == "T19")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 29-Mart  Toshkentda \n Ramazon 19-Kuni \n\nSaharlik : 4:54 \n Iftorlik  : 19:44",
        show_alert=True)
@dp.callback_query(F.data == "T20")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 30-Mart  Toshkentda \n Ramazon 20-Kuni \n\nSaharlik : 4:52 \n Iftorlik  : 19:45",
        show_alert=True)
@dp.callback_query(F.data == "T21")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 31-Mart  Toshkentda \n Ramazon 21-Kuni \n\nSaharlik : 4:50 \n Iftorlik  : 19:46",
        show_alert=True)
@dp.callback_query(F.data == "T22")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 1-aprel  Toshkentda \n Ramazon 22-Kuni \n\nSaharlik : 4:48 \n Iftorlik  : 19:47",
        show_alert=True)
@dp.callback_query(F.data == "T23")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 2-aprel  Toshkentda \n Ramazon 23-Kuni \n\nSaharlik : 4:46 \n Iftorlik  : 19:48",
        show_alert=True)
@dp.callback_query(F.data == "T24")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 3-aprel  Urganchda \n Ramazon 24-Kuni \n\nSaharlik : 4:44 \n Iftorlik  : 19:49",
        show_alert=True)
@dp.callback_query(F.data == "T25")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 4-aprel  Toshkentda \n Ramazon 25-Kuni \n\nSaharlik : 4:43 \n Iftorlik  : 19:50",
        show_alert=True)
@dp.callback_query(F.data == "T26")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 5-aprel Toshkentda \n Ramazon 26-Kuni \n\nSaharlik : 4:41 \n Iftorlik  : 19:51",
        show_alert=True)
@dp.callback_query(F.data == "T27")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 6-aprel  Toshkentda \n Ramazon 27-Kuni \n\nSaharlik : 4:39 \n Iftorlik  : 19:52",
        show_alert=True)
@dp.callback_query(F.data == "T28")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 7-aprel  Toshkentda \n Ramazon 28-Kuni \n\nSaharlik : 4:37 \n Iftorlik  : 19:53",
        show_alert=True)
@dp.callback_query(F.data == "T29")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 8-aprel  Toshkentda \n Ramazon 29-Kuni \n\nSaharlik : 4:35 \n Iftorlik  : 19:54",
        show_alert=True)
@dp.callback_query(F.data == "T30")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(text=f"🗓 9-aprel  Toshkentda \n Ramazon 30-Kuni \n\nSaharlik : 4:34 \n Iftorlik  : 19:55",
        show_alert=True)
    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
