from pyrogram import Client, filters
from info import CHANNELS, LOG_CHANNEL
from database.ia_filterdb import save_file2, save_file3, save_file4, save_file5, check_file

media_filter = filters.document | filters.video | filters.audio

recent_movies = []

@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption
    
    if message.id % 4 == 0:
        tru = await check_file(media)
        if tru == "okda":
            await save_file2(media)
        else:
            print("skipped duplicate file from saving to db 😌")
    elif message.id % 4 == 1:
        tru = await check_file(media)
        if tru == "okda":
            await save_file3(media)
        else:
            print("skipped duplicate file from saving to db 😌")
    elif message.id % 4 == 2:
        tru = await check_file(media)
        if tru == "okda":
            await save_file4(media)
        else:
            print("skipped duplicate file from saving to db 😌")
    else:
        tru = await check_file(media)
        if tru == "okda":
            await save_file5(media)
        else:
            print("skipped duplicate file from saving to db 😌")
        if success_sts == 'suc':
            latest_movie = await formatted_name(file_name=media.file_name, caption=media.caption)
            if latest_movie in recent_movies:
                return
            recent_movies.append(latest_movie)
            if await db.get_send_movie_update_status(bot_id):
                file_id, file_ref = unpack_new_file_id(media.file_id)
                await send_movie_updates(bot, file_name=media.file_name, caption=media.caption, file_id=file_id)


async def formatted_name(file_name, caption):
    year_match = re.search(r"\b(19|20)\d{2}\b", caption)
    year = year_match.group(0) if year_match else None      
    pattern = r"(?i)(?:s|season)0*(\d{1,2})"
    season = re.search(pattern, caption)
    if not season:
        season = re.search(pattern, file_name) 
    if year:
        file_name = file_name[:file_name.find(year) + 4]      
    if not year:
        if season:
            season = season.group(1) if season else None       
            file_name = file_name[:file_name.find(season) + 1]
    movie_name = await movie_name_format(file_name)    
    return movie_name


@Client.on_message(filters.command(["latest"]))
async def latest_movies(bot, message):
 try:
     last_movies = list(recent_movies)[-20:]
     message_text = "<b>List of New Added Movies In DB:</b>\n\n"
     for num, movie_name in enumerate(last_movies, start=1):
         message_text += f"<b>{num}. {movie_name}✅️</b>\n"
     await message.reply_text(message_text)
 except Exception as e:
     print(f"Error showing latest movies: {e}")
     await bot.send_message(LOG_CHANNEL, f"Error showing latest movies: {e}")

