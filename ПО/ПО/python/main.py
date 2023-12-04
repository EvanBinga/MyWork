
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6696019133:AAE_YsqXn87SBaeSQYOz0-BfqrQdO15TEQ0'
openai.api_key = "akv3JSgYa5utvB6fytNGT3BlbkFJAj98N9hdBbtnYrhX7R6M"
bot = Bot(token)
dp = Dispatcher(bot)

print(openai.Model.list())