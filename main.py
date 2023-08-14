from pyrogram import Client, filters
from datetime import datetime

app = Client("my_bot", bot_token="token", api_id=111111,
             api_hash='api_hash')


@app.on_message(filters.command("timer") & filters.group)
def timer_command(_, message):
    target_date = datetime(2023, 8, 17, 12, 0, 0)
    now = datetime.now()

    time_remaining = target_date - now

    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    response = (
        f"زمان باقی مانده تا اعلام نتایج کنکور @rootsina\n"
        f"{days} روز، {hours} ساعت، {minutes} دقیقه، {seconds} ثانیه"
    )

    message.reply(response)


app.run()
