from fastapi import FastAPI, BackgroundTasks
from decimal import Decimal
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
from config import TOKEN, CHAT_ID, HOST, PORT
from utils import create_order_excel
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
app = FastAPI()



@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):

    chat_id = message.chat.id
    await message.answer(f"Привет! Ваш Chat ID: {chat_id}. Для отправки файла используй команду /send_file")

async def start_application():
    
    await dp.skip_updates()
    await dp.start_polling()





@app.post("/order/")
async def receive_order(order: dict, background_tasks: BackgroundTasks):

    if 'product_info_list' not in order or 'Order_id' not in order:
        return {"error": "Invalid order format"}

    background_tasks.add_task(notify_order, order)
    return {"message": "Order received", "order_id": order['Order_id']}

async def notify_order(order: dict):

    msg = f"Новый заказ: {order['Order_id']}\n от {order['user']}, телефон: {order['user_phone']} :"
    for item in order['product_info_list']:
        msg += f"\n- {item['Товар']},  Колличество: {item['Количество']}, Цена за еденицу: {Decimal(item['Цена за единицу'])}"

    file_path = create_order_excel(order['product_info_list'], order['Order_id'])

    try:
        await bot.send_message(CHAT_ID, msg)
        document = FSInputFile(file_path)
        await bot.send_document(CHAT_ID, document)
        
    except Exception as e:
        print(f"Failed to send message: {e}")

    finally:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Failed to remove file: {e}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_application())


    import uvicorn
    uvicorn.run(app, host = HOST, port = PORT, loop="none")