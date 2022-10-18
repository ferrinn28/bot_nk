from telegram.ext import *
from telegram import *

import response as r

#Name Bot : BMRI_NK Bot
#ID Bot   : mandirink_bot

#Check bot_ChatID (id)
#https://api.telegram.org/bot5455134682:AAGmcx_NxOPULbR9_tkoT0RhG_v3uQKdLbc/getUpdates

print("Bot is Running")

bot_token = '5455134682:AAGmcx_NxOPULbR9_tkoT0RhG_v3uQKdLbc'

#bot = Bot(bot_token)


def start_command(update, context):
    #Data User
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    #bot.send_message(chat_id=chat_id, text='Hi')

    update.message.reply_text(
        f"""
        Selamat Datang {first_name} {last_name}
        Bank Mandiri KC Nindya Karya
        /jadwal -> Jam Operasional Kantor
        /lokasi -> Lokasi Kantor
        /promo  -> Promo On Going
        /help   -> Tentang Bot

        Ada yang kami bisa bantu?
        (terkait pembukaan tabungan now dan kredit)
        """
    )


    #print(f"{first_name} { last_name} : {chat_id}")


def jadwal(update, context):
    update.message.reply_text(
        """
        Senin - Jumat
        Jam Operasional 08:00 WIB - 15:00 WIB
        """
    )

def lokasi(update, context):
    update.message.reply_text(
        """
        https://goo.gl/maps/m6i4vHpgsYCjXiwd7
        """
    )

def help(update, context):
    update.message.reply_text(
        """
        Perintah Dasar:
        - Tabungan NOW
        - Kredit

        Bot is still Beta
        """
    )


def promo(update, context):
    update.message.reply_text(
        """
        🥳 KPR Special HUT Bank Mandiri ke-24 🥳

Yuk..kepoin promo menariknyaa..

🎉 BUNGA HUT ke- 24 🎉
✓ 2.4% fix 1th min tenor 5 Tahun
✓ 3.24% fix 3th min tenor 10 Tahun
✓ 4.24% fix 5th min tenor 12 Tahun 

🎊 BUNGA FIX BERJENJANG 🎊
✓ 3.98% tahun 1-3
✓ 7.68% tahun 4-6
✓ 9.68% tahun 7-10
min tenor 12th

🌟 Bunga Spesial Tengah Tahun 🌟
✓ 4.18% fix 3th min tenor 8 Tahun
✓ 3.88% fix 3th min tenor 12 Tahun
✓ 4.88% fix 5th min tenor 15 Tahun

🌟 Bunga Super Promo 🌟
✓ 4.50% fix 1th min tenor 5 Tahun
✓ 5.50% fix 3th min tenor 10 Tahun
✓ 6.25% fix 5th min tenor 12 Tahun 

✅ 🌟 FIX 10th 🌟
✓ 8.50% min tenor 10 Tahun
(khusus jobtype pegawai)

Segera wujudkan Rumah impian anda dengan KPR mandiri🏘️
        """
    )

def handle_message(update, context):
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    name = first_name + " " + last_name

    text = str(update.message.text).lower()

    response = r.sample_responses(text, name)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("jadwal", jadwal))
    dp.add_handler(CommandHandler("lokasi", lokasi))
    dp.add_handler(CommandHandler("promo", promo))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()