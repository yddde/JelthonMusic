# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("الصفحه الرئيسيه")
    await query.edit_message_text(
        f"""✶ **مرحبا عزيزي -「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
✶ **انا بوت استطيع تشغيل الموسيقي والفيديو في محادثتك الصوتية**

✶ تعلم طريقة تشغيلي واوامر التحكم بي عن طريق  ✶ الاوامر !

✶ لتعلم طريقة تشغيلي بمجموعتك اضغط علي ✶ طريقة التفعيل !
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اضف البوت الى مجموعتك •",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("• طريقه التفعيل •", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("• الاوامر •", callback_data="cbcmds"),
                    InlineKeyboardButton("• المطورين •", callback_data="cbsudo"),
                ],
                [
                    InlineKeyboardButton(
                        "• قناة السورس •", url=f"https://t.me/Jelthon"
                    ),
                    InlineKeyboardButton(
                        "• قناة البوت •", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "• قروب الدعم •", url="https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("- طريقه الاستخدام. ")
    await query.edit_message_text(
        f""" الدليل الأساسي لاستخدام هذا البوت:

 1 - أولاً ، أضفني إلى مجموعتك
 2 - بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
 3 - بعد ترقيتي ، اكتب /reload مجموعة لتحديث بيانات المشرفين
 4 - أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /userbotjoin لدعوة حساب المساعد
 5 - قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 6 - في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر /reload في إصلاح بعض المشكلات
 ✶ إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب /userbotleave ثم اكتب /userbotjoin مرة أخرى

 ✶ إذا كانت لديك أسئلة  حول هذا البوت ، فيمكنك إخبارنا من خلال قروب الدعم هنا - @{GROUP_SUPPORT}

✶ قناة البوت @{UPDATES_CHANNEL}
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✶ رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("قائمة الاوامر")
    await query.edit_message_text(
        f"""✶ **قم بالضغط علي الزر الذي تريده لمعرفه الاوامر لكل فئه منهم !**

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• اوامر المشرفين •", callback_data="cbadmin"),
                ],[
                    InlineKeyboardButton("• اوامر اساسيه •", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("✶ رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("الاوامر الاساسيه")
    await query.edit_message_text(
        f"""
✶ /play +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
او /تشغيل  +「اسم الأغنية / رابط 」
✶ /vplay +「اسم الفيديو / رابط 」 لتشغيل الفيديو داخل المكالمة
✶ /vstream 「رابط」 تشغيل فيديو مباشر من اليوتيوب
✶ /playlist 「تظهر لك قائمة التشغيل」
           او /القائمه    
✶ /end「لإنهاء الموسيقى / الفيديو في الكول」
 او /انهاء 「لإنهاء الموسيقى / الفيديو في الكول」
✶ /song + 「الاسم تنزيل صوت من youtube」
او /تحميل + 「الاسم تنزيل صوت من يوتيوب」
✶/vsong + 「الاسم  تنزيل فيديو من youtube」
او /فيديو + 「الاسم فيديو تحميل من يوتيوب」
✶ /skip「للتخطي إلى التالي」
او /تخطي 「للتخطي إلى التالي」
✶ /search + اسم التي تريد بحث عنه !
✶ /ping 「إظهار حالة البوت بينغ」
✶ /uptime 「لعرض مده التشغيل للبوت」
✶ /alive「اظهار معلومات البوت(في المجموعه)」

✶ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✶ رجوع", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه")
    await query.edit_message_text(
        f"""🏮 هنا أوامر الادمنيه:

✶ /pause 「ايقاف التشغيل موقتآ」
✶ /resume 「استئناف التشغيل」
✶ /stop「لإيقاف التشغيل」
✶ /vmute 「لكتم البوت」
✶ /vunmute 「لرفع الكتم عن البوت」
✶ /volume 「ضبط مستوئ الصوت」
او /تحكم + مستوي الصوت
✶ /reload「لتحديث البوت و قائمة المشرفين」
او /تحديث 
✶ /userbotjoin「لاستدعاء الحساب المساعد」
او /انضم 
✶ /userbotleave「لطرد الحساب المساعد」
او /غادر

✶ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✶ رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("المطورين")
    await query.edit_message_text(
        f"""- **مرحبًا تم برمجة هذا البوت وتطويره من قبل:
        
✶ [𝒌𝒐𝒌𝒐](t.me/T_G_L) & [ㅤㅤ𝚉𝚊𝚒𝚍 ₁₆](t.me/MDDDP) ✶

✶ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✶ رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("✶ المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("✶ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("✶ المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
