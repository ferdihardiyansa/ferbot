from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@bot.on(man_cmd(outgoing=True, pattern="p(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**PUNTEN SLURRRR**")
    sleep(2)
    await edit_or_reply(event, "**ASSALAMUALAIKUM UKHTI**")


@bot.on(man_cmd(outgoing=True, pattern="makan(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**KAMU UDAH MAKAN BELUM**")
    sleep(2)
    await edit_or_reply(event, "**KALAU BELUM MATI AJA SEKALIAN**")
    sleep(3)
    await edit_or_reply(event, "**BECANDA**")
   

@bot.on(man_cmd(outgoing=True, pattern=r"pe(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**PUNTEN MAMANG**")
    sleep(2)
    await edit_or_reply(event, "**ASSALAMUALAIKUM**")


@bot.on(man_cmd(outgoing=True, pattern="jawab(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**Haii Salken Saya {ALIVE_NAME}**")
    sleep(2)
    await edit_or_reply(event, "**wa'laikumsalam**")


@bot.on(man_cmd(outgoing=True, pattern=r"sama(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**SAMA SAMA SAYANG**")


@bot.on(man_cmd(outgoing=True, pattern=r"gombalan(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**IKAN HIU MELAYANG LAYANG**")
    sleep(2)
    await edit_or_reply(event, "**I LOVE YOU SAYANG JIAKHHH**")


@bot.on(man_cmd(outgoing=True, pattern=r"kabar(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**HALLO**")
    sleep(2)
    await edit_or_reply(event, "**GIMANA KABARNYA?**")


@bot.on(man_cmd(outgoing=True, pattern=r"wala(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**w**")
    sleep(0.5)
    await edit_or_reply(event, "**wa**")
    sleep(0.5)
    await edit_or_reply(event, "**waa**")
    sleep(0.5)
    await edit_or_reply(event, "**waal**")
    sleep(0.5)
    await edit_or_reply(event, "**waala**")
    sleep(0.5)
    await edit_or_reply(event, "**waalai**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaik**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaiku**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikum**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikums**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsa**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsal**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsala**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsalam**")
    
    

@bot.on(man_cmd(outgoing=True, pattern=r"cukup(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "**my happiness?**")
    sleep(3)
    await edit_or_reply(event, "**cukup**")
    sleep(1)
    await edit_or_reply(event, "**CUKUP KAU DI SAMPING KU**")
    sleep(4)
    await edit_or_reply(event, "**SEMPURNAHKAN LANGKAH KU TUK MENYUSURI WAKTU**")
    sleep(3)
    await edit_or_reply(event, "**CUKUP KAU DI SAMPING KU**")
    sleep(3)
    await edit_or_reply(event, "**BERJALAN BERSAMA KU PASTIKAN KAU BAHAGIA**")
    
    
CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}sama`\
        \n  •  **Function : **nMenampilkan sama sama syang\
        \n\n  •  **Syntax :** `{cmd}makan`\
        \n  •  **Function : ** `nanyain kabar makan`\
        \n\n  •  **Syntax :** `{cmd}kabar`\
        \n  •  **Function : **nanyain kabar\
        \n\n  •  **Syntax :** `{cmd}wala`\
        \n  •  **Function : **waalaikumsalam\
        \n\n  •  **Syntax :** `{cmd}cukup`\
        \n  •  **Function : **nyanyi lagunya rizky febian\
     "
    }
)
