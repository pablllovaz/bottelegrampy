#!/usr/bin/python coding: UTF-8 -*-
# Code: Pabllovaz

# IMPORTAÇÕES DE BIBLIOTECAS
import os
import dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# CAMINHO TOKEN DOTENV
dotenv.load_dotenv(dotenv.find_dotenv())

# TOKEN DE ACESSO
token = os.getenv('TOKEN_ACESSO')

bot = Bot(token=token)
dp = Dispatcher(bot)

# BOTÕES CONTROLERS

# BOTÕES MENU PRINCIPAL
botao1 = InlineKeyboardButton(text='🤨Loja', callback_data='LOJA')
botao2 = InlineKeyboardButton(text='🤠Seu Perfil', callback_data='PERFIL')
botoesmenu = InlineKeyboardMarkup().add(botao1, botao2)
# BOTÕES LOJA
botao4 = InlineKeyboardButton(text='<<voltar', callback_data='VOLTAR')
botoesloja = InlineKeyboardMarkup().add(botao4)
# SUB BOTÕES PERFIL
botao3 = InlineKeyboardButton(text='💠Recargas Pix', callback_data='recargapix')
botoesperfil = InlineKeyboardMarkup().add(botao3)

@dp.message_handler(commands=['start'])
async def iniciando(message: types.Message):
  #print(message)
  await message.reply(f'Ola {message.from_user.first_name}', reply_markup=botoesmenu)
  
@dp.callback_query_handler(text= ['LOJA'])
async def menu(call: types.CallbackQuery):
  if call.data == 'LOJA':
    await call.message.edit_text('Opa amigão ainda estou em desenvolvimento🤠📸!', reply_markup=botoesloja)

@dp.callback_query_handler(text= ['PERFIL'])
async def perfil(call: types.CallbackQuery):
  if call.data == 'PERFIL':
    await call.message.edit_text(f'🗿Suas Informações\n \n ✨Nome: {call.from_user.first_name} \n 🌐User: @{call.from_user.username}', reply_markup=botoesperfil)

@dp.callback_query_handler(text= ['VOLTAR'])
async def voltar(call: types.CallbackQuery):
  if call.data == 'VOLTAR':
    await call.message.edit_text('ISSO DEVERIA VOLTAR AO ULTIMO MENU')
  await call.answer()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)