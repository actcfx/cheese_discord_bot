import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Deleted_mes(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild.id == 978680658740260865:
            channel = self.bot.get_channel(1077322125641252996)
            embed = nextcord.Embed(title="Message Deleted", color=0xFF0000)
            embed.add_field(name="Author", value=message.author.mention, inline=False)
            embed.add_field(name="Channel", value=message.channel.mention, inline=False)
            if message.content:
                embed.add_field(name="Content", value=message.content, inline=False)
            for attachment in message.attachments:
                embed.add_field(name="Attachment", value=attachment.url, inline=False)
            del_mes = await channel.send(embed=embed)
            del_mes_url = del_mes.jump_url

            dest_guild_id = 1022573475552055337
            dest_channel_id = 1077379233799753858
            dest_guild = self.bot.get_guild(dest_guild_id)
            dest_channel = dest_guild.get_channel(dest_channel_id)

            if len(message.attachments) > 0:
                for attachment in message.attachments:
                    await dest_channel.send(
                        "↓ " + del_mes_url, file=await attachment.to_file()
                    )


def setup(bot):
    bot.add_cog(Deleted_mes(bot))
