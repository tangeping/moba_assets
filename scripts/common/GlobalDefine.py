# -*- coding: utf-8 -*-

"""
"""

# ------------------------------------------------------------------------------
# room rule
# ------------------------------------------------------------------------------

#  一个房间最大人数
ROOM_MAX_PLAYER = 35



# A队伍ID
TEAM_A_ID = 1

# B队伍ID
TEAM_B_ID = 2

# 随机队伍ID
TEAM_R_ID = 3

#--------------matcher- state ----------------------

MATCHER_STATE_UNKOWN = -1
MATCHER_STATE_FREE = 0
MATCHER_STATE_JOINING = 1
MATCHER_STATE_CREATE_ROOM = 2
MATCHER_STATE_ROOM_READY= 3
MATCHER_STATE_ROOM_PLAYING = 4
MATCHER_STATE_ROOM_GAME_OVER = 5

#--------------Matcher avatar state------------------

MATCHER_AVATAR_STATE_FREE = 0
MATCHER_AVATAR_STATE_ENTER = 1
