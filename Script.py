class script(object):
    START_TXT = """<b>Hᴇʏ {},

𝗜𝗮𝗺 𝗔𝗻 𝗔𝘄𝗲𝘀𝗼𝗺𝗲 𝗔𝘂𝘁𝗼 𝗙𝗶𝗹𝘁𝗲𝗿 + 𝗠𝗼𝘃𝗶𝗲 𝗦𝗲𝗮𝗿𝗰𝗵 + 𝗠𝗮𝗻𝘂𝗮𝗹 𝗙𝗶𝗹𝘁𝗲𝗿 𝗕𝗼𝘁.

𝗜 𝗖𝗮𝗻 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗚𝗿𝗼𝘂𝗽𝘀. 𝗬𝗼𝘂 𝗖𝗮𝗻 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗼𝘃𝗶𝗲𝘀 𝗕𝗼𝘁 𝗣𝗠. 𝗝𝘂𝘀𝘁 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗦𝗲𝗲 𝗧𝗵𝗲 𝗠𝗮𝗴𝗶𝗰</b>"""
    
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Leomessi_10_19>ᴸᴱᴼ ᴹᴱˢˢᴵ</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
<b>𝟷. 𝙼𝙰𝙺𝙴 𝙼𝙴 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙵 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙵 𝙸𝚃'𝚂 𝙿𝚁𝙸𝚅𝙰𝚃𝙴.
𝟸. 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙳𝙾𝙴𝚂 𝙽𝙾𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙲𝙰𝙼𝚁𝙸𝙿𝚂, 𝙿𝙾𝚁𝙽 𝙰𝙽𝙳 𝙵𝙰𝙺𝙴 𝙵𝙸𝙻𝙴𝚂.
𝟹. 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚀𝚄𝙾𝚃𝙴𝚂.
 𝙸'𝙻𝙻 𝙰𝙳𝙳 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙼𝚈 𝙳𝙱.</b>
<b>★ /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>★ /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>"""

    BOTINFO_TXT = """<b>𝖧𝖾𝗒 𝖡𝗋𝗈 𝖨𝖺𝗆 𝖧𝖺𝗉𝗉𝗒 🖤 𝖳𝗈 𝖧𝖺𝗏𝖾 𝖸𝗈𝗎
 
✪ സിനിമകൾ ഇഷ്ടപ്പെടുന്നവർക്കും സിനിമ ഡൗൺലോഡ് ചെയ്യുന്നവർക്കും വേണ്ടിയുള്ള മാത്രം ഉള്ള ബോട്ടാണ് ആണിത് 🤩

✫ This bot is only for movie lovers and movie downloaders 🤗

✫ 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖲𝖾𝗇𝖽 𝖡𝗈𝗍 𝖠𝖽𝗆𝗂𝗇 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖥𝗈𝗋 𝖴𝗉𝗅𝗈𝖺𝖽𝗂𝗇𝗀 𝖬𝗈𝗏𝗂𝖾𝗌, 𝖯𝖺𝗂𝖽 𝖯𝗋𝗈𝗆𝗈𝗍𝗂𝗈𝗇 𝖾𝗍𝖼</b>"""
    
    SORCE_TXT = """<b>കൊട്ക്ക്ണില്ല്യാ...... [PRIVATE REPO]</b>"""
    
    MOVDOW_TXT = """<b> 1. 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 𝐆𝐫𝐨𝐮𝐩 - 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞

2. 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝖨𝗇 𝖤𝗇𝗀𝗅𝗂𝗌𝗁 𝖫𝖾𝗍𝗍𝖾𝗋𝗌. 𝖬𝗎𝗌𝗍 𝖥𝗈𝗅𝗅𝗈𝗐𝗂𝗇𝗀 𝖧𝗈𝗐 𝖳𝗈 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 ⚙

3. 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖡𝗎𝗍𝗍𝗈𝗇 𝖥𝗂𝗅𝖾𝗌 𝖨𝗇 𝖳𝗁𝖾 𝖰𝗎𝖺𝗅𝗂𝗍𝗒 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 𝖨𝗇 𝖬𝗒 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖳𝗁𝖺𝗍 𝖢𝗈𝗆𝖾𝗌 𝖠𝗌 𝖠 𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖳𝗁𝖾 𝗆𝗈𝗏𝗂𝖾 𝖸𝗈𝗎 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝖾𝖽🎯

4. 𝖳𝗁𝖾𝗇 𝖢𝗅𝗂𝖼𝗄 𝖲𝗍𝖺𝗋𝗍 𝖡𝖾𝗅𝗈𝗐 𝖮𝗋 𝖠𝗎𝗍𝗈 𝖲𝗍𝖺𝗋𝗍. 𝖥𝗂𝗇𝖺𝗅𝗅𝗒 𝖸𝗈𝗁 𝖶𝗂𝗅𝗅 𝖦𝖾𝗍 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌 🌎

𝖭𝖡: 𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖮𝗇𝗅𝗒 𝖨𝗇 𝖬𝗒 𝖬𝗈𝗏𝗂𝖾𝗌 𝖦𝗋𝗈𝗎𝗉 𝖫𝗂𝗇𝗄 𝖢𝗁𝖾𝖼𝗄 𝗂𝗇 𝖠𝖻𝗈𝗏𝖾..!!</b>"""

    MOVREQ_TXT = """<b>⚠️ 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖥𝗈𝗅𝗅𝗈𝗐 𝖱𝗎𝗅𝖾𝗌 👇🏻

𝖠𝗌𝗄 𝖥𝗈𝗋 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀

𝖬𝗎𝗌𝗍 𝖢𝗁𝖾𝖼𝗄 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝗂𝗇 𝖦𝗈𝗈𝗀𝗅𝖾 

𝖠𝗌𝗄 𝖥𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 𝖨𝗇 𝖤𝗇𝗀𝗅𝗂𝗌𝗁 𝖫𝖾𝗍𝗍𝖾𝗋𝗌 𝖮𝗇𝗅𝗒

𝖣𝗈𝗇'𝗍 𝖠𝗌𝗄 𝖥𝗈𝗋 𝖴𝗇𝗋𝖾𝗅𝖾𝖺𝗌𝖾𝖽 𝖬𝗈𝗏𝗂𝖾𝗌

[𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾, 𝖸𝖾𝖺𝗋, 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾] 𝖠𝗌𝗄 𝖳𝗁𝗂𝗌 𝖶𝖺𝗒

𝖣𝗈 𝖭𝗈𝗍 𝖴𝗌𝖾 𝖶𝗈𝗋𝖽𝗌 𝖫𝗂𝗄𝖾 𝖣𝗎𝖻, 𝖬𝗈𝗏𝗂𝖾, 𝖫𝗂𝗇𝗄, 𝖯𝗅𝗌𝗌, 𝖲𝖾𝗇𝗍 𝖾𝗍𝖼 𝖮𝗍𝗁𝖾𝗋 𝖳𝗁𝖺𝗇 𝖳𝗁𝖾 𝖶𝖺𝗒 𝖬𝖾𝗇𝗍𝗂𝗈𝗇𝖾𝖽 𝖠𝖻𝗈𝗏𝖾

𝖣𝗈𝗇'𝗍 𝖴𝗌𝖾 𝖲𝗍𝗒𝗅𝗂𝗌𝗁 𝖥𝗈𝗇𝗍 𝖶𝗁𝗂𝗅𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍

𝖣𝗈𝗇'𝗍 𝖴𝗌𝖾 𝖲𝗒𝗆𝖻𝗈𝗅𝗌 𝖶𝗁𝗂𝗅𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖬𝗈𝗏𝗂𝖾𝗌 𝗅𝗂𝗄𝖾 (+:;'!-|...𝖾𝗍𝖼)

𝖨𝖿 𝖸𝗈𝗎 𝖣𝗈𝗇'𝗍 𝖦𝖾𝗍 𝖬𝗈𝗏𝗂𝖾𝗌 𝖠𝗇𝖽 𝖲𝖾𝗋𝗂𝖾𝗌⌛️
𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖠𝖽𝗆𝗂𝗇 - @tg_tarzan

𝖬𝗈𝗏𝗂𝖾𝗌 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖥𝗈𝗋𝗆𝖺𝗍
𝖪𝗎𝗋𝗎𝗉 𝖬𝗈𝗏𝗂𝖾❌
𝖪𝗎𝗋𝗎𝗉 2021 ✅
𝖪𝗀𝖿: 𝖢𝗁𝖺𝗉𝗍𝖾𝗋 2❌
𝖪𝗀𝖿 𝖢𝗁𝖺𝗉𝗍𝖾𝗋 2✅

𝖲𝖾𝗋𝗂𝖾𝗌 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖱𝗎𝗅𝖾𝗌
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝗌𝖾𝖺𝗌𝗈𝗇 1❌
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝖲01✅
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 1❌
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝖲01𝖤01✅

𝖢𝗅𝗂𝖼𝗄 𝖡𝖾𝗅𝗈𝗐 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝖠𝗇𝖽 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖬𝗈𝗏𝗂𝖾𝗌 𝗈𝗋 𝖲𝖾𝗋𝗂𝖾𝗌 𝖨𝗇 𝖬𝗈𝗏𝗂𝖾𝗌 𝖦𝗋𝗈𝗎𝗉💡</b>"""
 
    COMMUN_TXT = """<b>✰ സിനിമയെ ഇഷ്ടപ്പെടുന്നവർക്കായി നിങ്ങൾക്ക് ഞങ്ങളുടെ സിനിമ കൂട്ടായ്മയിലേക്ക് എല്ലാവരും ജോയിൻ ചെയ്യുക..🤍</b>"""
    
   
    EXTRA_TXT = """<b>കുറെ പ്രത്യേകതയുള്ള ബോട്ടാണ് നിഖില, ⚔

1. ലോകത്തിലെ ഏറ്റവും വേഗത്തിൽ ഓടുന്ന ബോട്ട് ഇതാണ് അതിനൊരു സംശയവും വേണ്ട ❤️‍🔥 

2. നിഖില ഉണ്ടാക്കിയിരിക്കുന്ന കോഡ് തികച്ചും റീ റൈറ്റ് ചെയ്തിരിക്കുന്നതാണ് അതുമാത്രമല്ല ഇതിനെ ഹോസ്റ്റ് ചെയ്തിരിക്കുന്നത് വി പി എസിൽ ആണ്  അതുകൊണ്ട് ഇത് കുതിരനെ കാട്ടിലും  വേഗത്തിലോടും

3. അങ്ങനെ വളരെയധികം ഫ്യൂച്ചേഴ്സ് ആഡ് ചെയ്തിട്ടുണ്ട് 😁🤗

𝑻𝒉𝒆 𝑵𝒊𝒌𝒉𝒊𝒍𝒂, ⚔ 𝑰𝒔 𝑨 𝑹𝒂𝒕𝒉𝒆𝒓 𝑺𝒑𝒆𝒄𝒊𝒂𝒍 𝑩𝒐𝒂𝒕

1. 𝑻𝒉𝒊𝒔 𝑰𝒔 𝑻𝒉𝒆 𝑭𝒂𝒔𝒕𝒆𝒔𝒕 𝑩𝒐𝒂𝒕 𝑰𝒏 𝑻𝒉𝒆 𝑾𝒐𝒓𝒍𝒅 𝑾𝒊𝒕𝒉𝒐𝒖𝒕 𝑨 𝑫𝒐𝒖𝒃𝒕 ❤️‍🔥     

2. 𝑻𝒉𝒆 𝑪𝒐𝒅𝒆 𝑻𝒉𝒂𝒕 𝑴𝒂𝒌𝒆𝒔 𝑵𝒊𝒌𝒉𝒊𝒍𝒂 𝑰𝒔 𝑪𝒐𝒎𝒑𝒍𝒆𝒕𝒆𝒍𝒚 𝑹𝒆𝒘𝒓𝒊𝒕𝒕𝒆𝒏 𝑨𝒏𝒅 𝑵𝒐𝒕 𝑶𝒏𝒍𝒚 𝑰𝒔 𝑰𝒕 𝑯𝒐𝒔𝒕𝒆𝒅 𝑶𝒏 𝑯𝑬𝑹𝑲𝑼𝑶 𝑺𝒐 𝑰𝒕 𝑴𝒂𝒌𝒆𝒔 𝑻𝒉𝒆 𝑯𝒐𝒓𝒔𝒆 𝑾𝒊𝒍𝒅 𝑨𝒏𝒅 𝑭𝒂𝒔𝒕.

3. 𝑺𝒐 𝑴𝒂𝒏𝒚 𝑭𝒖𝒕𝒖𝒓𝒆𝒔 𝑯𝒂𝒗𝒆 𝑩𝒆𝒆𝒏 𝑨𝒅𝒅𝒆𝒅 😁🤗</b>"""
    
    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""
    
    HELP_TXT = """<b>Hᴇʏ {} 𝖨𝖺𝗆 𝖧𝖺𝗉𝗉𝗒 🖤 𝖳𝗈 𝖧𝖺𝗏𝖾 𝖸𝗈𝗎
    
𝖶𝗂𝗍𝗁 𝖳𝗁𝗂𝗌 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖶𝗂𝗅𝗅 𝖴𝗇𝖽𝖾𝗋𝗌𝗍𝖺𝗇𝖽 𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍🏌️
    
𝖢𝗁𝖾𝖼𝗄 𝖡𝖾𝗅𝗈𝗐 𝖧𝖾𝗅𝗉 𝖥𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝗌🤍</b>"""
  
    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : <code>{file_name}</code>

╔═════•✧❅✦❅✧•═════╗
▣ <a href=https://t.me/cinemaworld_123>​𝙲𝙸𝙽𝙴𝙼𝙰 𝚆𝙾𝚁𝙻𝙳</a>
▣ <a href=t.me/cinemaworld_update>𝙲𝙸𝙽𝙴𝙼𝙰 𝚆𝙾𝚁𝙻𝙳 𝚄𝙿𝙳𝙰𝚃𝙴𝚂​</a>
╚═════•✧❅✦❅✧•═════╝</b>""" 
    
    STATUS_TXT = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𒆜  𝗗𝗕 1️⃣
╭ ▸ 𝖴𝗌𝖾𝗋𝗌 : <code>{}</code>
├ ▸ 𝖢𝗁𝖺𝗍𝗌  : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

 𒆜 𝗗𝗕 2️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 :<code>{}</code>
├ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 :<code>{}</code>MB
╰ ▸ Free :<code>{}</code>MB

 𒆜 𝗗𝗕 3️⃣ 
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 :<code>{}</code>
├ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 :<code>{}</code>MB
╰ ▸ Free :<code>{}</code>MB

𒆜  𝗗𝗕 4️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 :<code>{}</code>
├ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 :<code>{}</code>MB
╰ ▸ Free :<code>{}</code>MB

𒆜 𝗗𝗕 5️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 :<code>{}</code>
├ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 :<code>{}</code>MB
╰ ▸ Free :<code>{}</code>MB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>- 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙴𝙻𝚂𝙰 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝙰 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴</b>

<b>NOTE:</b>
<b>𝟷.𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
𝟸. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
𝟹. 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵 𝟼𝟺 𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.</b>

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ʟᴇᴏ ᴍᴇꜱꜱɪ
• ᴜꜱᴇʀɴᴀᴍᴇ : @Leomessi_10_19 
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/Leomessi_10_19'>ʟᴇᴏ ᴍᴇꜱꜱɪ</a></b>"""

    DELETE_TXT = """‼️ 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 ‼️

<blockquote>⚠️ 𝙁𝙞𝙡𝙚 𝙒𝙞𝙡𝙡 𝘽𝙚 𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝙄𝙣 𝟱 𝙈𝙞𝙣𝙪𝙩𝙚𝙨.</blockquote>

𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘁𝗵𝗲𝘀𝗲 𝗳𝗶𝗹𝗲𝘀, 𝗞𝗶𝗻𝗱𝗹𝘆 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗲𝘀𝗲 𝗳𝗶𝗹𝗲𝘀 𝘁𝗼 𝗮𝗻𝘆 𝗰𝗵𝗮𝘁 (𝘀𝗮𝘃𝗲𝗱) 𝗮𝗻𝗱 𝘀𝘁𝗮𝗿𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱...

<blockquote>𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗤𝘂𝗮𝗹𝗶𝘁𝗮𝘁𝗶𝘃𝗲 𝗙𝗶𝗹𝗲𝘀 𝗨𝘀𝗲 𝗕𝗲𝗹𝗼𝘄 𝗕𝗼𝘁𝘀.</blockquote>

𝗧𝗵𝗮𝗻𝗸 𝗬𝗼𝘂 :)"""

