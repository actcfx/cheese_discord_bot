import json
import time
import nextcord
import collections
from nextcord.ext import commands
from core.classes import Cog_Extension

# roles = {}
# with open("data/roles.json", "r", encoding="utf-8") as f:
#     roles = json.load(f)

# role_mes_deque = collections.deque(roles["role_mes"].values())

# role_deques = [
#     collections.deque(list(roles["world_level"].values())[:-1]),
#     collections.deque(list(roles["server"].values())[:-1]),
#     collections.deque(list(roles["announcement"].values())[:-1]),
#     collections.deque(list(roles["guild_roles"].values())[:-1]),
#     collections.deque(list(roles["eyes"].values())[:-1]),
#     collections.deque(list(roles["destiny"].values())[:-1]),
#     collections.deque(list(roles["attributes"].values())[:-1]),
#     collections.deque(list(roles["parity_level"].values())[:-1]),
#     collections.deque(list(roles["track_server"].values())[:-1]),
# ]

# emoji_deques = [
#     # for title in roles["role_mes"]:
#     #     collections.deque(list(roles[f"{title}"])[:-1]),
#     collections.deque(list(roles["world_level"])[:-1]),
#     collections.deque(list(roles["server"])[:-1]),
#     collections.deque(list(roles["announcement"])[:-1]),
#     collections.deque(list(roles["guild_roles"])[:-1]),
#     collections.deque(list(roles["eyes"])[:-1]),
#     collections.deque(list(roles["destiny"])[:-1]),
#     collections.deque(list(roles["attributes"])[:-1]),
#     collections.deque(list(roles["parity_level"])[:-1]),
#     collections.deque(list(roles["track_server"])[:-1]),
# ]

# repeatable_deque = collections.deque(
#     [
#         list(roles["world_level"].values())[-1],
#         list(roles["server"].values())[-1],
#         list(roles["announcement"].values())[-1],
#         list(roles["guild_roles"].values())[-1],
#         list(roles["eyes"].values())[-1],
#         list(roles["destiny"].values())[-1],
#         list(roles["attributes"].values())[-1],
#         list(roles["parity_level"].values())[:-1],
#         list(roles["track_server"].values())[-1],
#     ],
# )


class Role(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     guild = self.bot.get_guild(978680658740260865)
    #     for member in guild.members:
    #         # Give the "member" role to all members
    #         if guild.get_role(978732220154007613) not in member.roles:
    #             await member.add_roles(guild.get_role(978732220154007613))

    #         # Give the three roles to all members
    #         if guild.get_role(1148349321666887782) not in member.roles:
    #             await member.add_roles(guild.get_role(1148349321666887782))
    #         if guild.get_role(1148349956273479781) not in member.roles:
    #             await member.add_roles(guild.get_role(1148349956273479781))
    #         if guild.get_role(1148352076351545475) not in member.roles:
    #             await member.add_roles(guild.get_role(1148352076351545475))

    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self, payload):
    #     # Checking if the message ID is in the defined list
    #     if payload.message_id in roles["reaction_roles_mes"].values():
    #         # Getting the member who reacted
    #         member = payload.member
    #         # Assigning the roles to the member
    #         for role_id in [
    #             "1148349321666887782",
    #             "1148349956273479781",
    #             "1148352076351545475",
    #         ]:
    #             role = member.guild.get_role(int(role_id))
    #             if role and role not in member.roles:
    #                 await member.add_roles(role)

    #     try:
    #         mes_id_index = role_mes_deque.index(payload.message_id)
    #         mes_id = payload.message_id
    #     except:
    #         return

    #     mem_roles = []
    #     guild = self.bot.get_guild(payload.guild_id)
    #     channel = guild.get_channel(payload.channel_id)
    #     mes = channel.get_partial_message(mes_id)

    #     role_index = emoji_deques[mes_id_index].index(str(payload.emoji))
    #     await payload.member.add_roles(
    #         guild.get_role(role_deques[mes_id_index][role_index])
    #     )

    #     if guild.get_role(978732220154007613) not in payload.member.roles:
    #         await payload.member.add_roles(guild.get_role(978732220154007613))

    #     if repeatable_deque[mes_id_index] == True:
    #         return
    #     for mem_role in payload.member.roles:
    #         mem_roles.append(mem_role.id)
    #     set_mem_roles = set(mem_roles)
    #     set_role_list = set(role_deques[mes_id_index])
    #     set_repeat_role = set_mem_roles & set_role_list
    #     if any(set_repeat_role):
    #         repeat_roles = list(set_repeat_role)
    #         repeat_index = role_deques[mes_id_index].index(repeat_roles[0])
    #         await mes.remove_reaction(
    #             emoji_deques[mes_id_index][repeat_index], payload.member
    #         )

    # @commands.Cog.listener()
    # async def on_raw_reaction_remove(self, payload):
    #     try:
    #         mes_id_index = role_mes_deque.index(payload.message_id)
    #     except:
    #         return

    #     guild = self.bot.get_guild(payload.guild_id)
    #     member = guild.get_member(payload.user_id)

    #     role_index = emoji_deques[mes_id_index].index(str(payload.emoji))
    #     await member.remove_roles(guild.get_role(role_deques[mes_id_index][role_index]))

def setup(bot):
    bot.add_cog(Role(bot))
