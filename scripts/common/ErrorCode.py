# -*- coding: utf-8 -*-

# error code

#matcher_rule_error

ERROR_OK = 0
ERROR_MATCHER_ARGS_ID   = 1          # matherID 必须大于 0
ERROR_MATCHER_ARGS_MIN_MAX_UNSET = 2 # mather 最小人数和最大人数没有设置
ERROR_MATCHER_ARGS_MIN_GREATER_MAX = 3 # mather rule 最小值大于最大值


ERROR_ROOM_RULE_KEY = 100   # roomKey 错误
ERROR_ROOM_RULE_NUMBER = 101 # 房间号错误
ERROR_ROOM_RULE_PASSWD = 102 #房间密码错误
ERROR_ROOM_RULE_ENTER_NUMBER = 101 # 进入房间号错误
ERROR_ROOM_RULE_ENTER_PASSWD = 102 #进入房间密码错误
ERROR_ROOM_RULE_IS_NONE      = 103 #房间匹配器还未创建
ERROR_ROOM_CREATE_NOT_READY  = 104 #还没到达开房的条件

ERROR_MATCHER_RULE_MATCH_FULL = 203  # 匹配条件已经满了
ERROR_MATCHER_NOT_FOUND = 204        #没有匹配的匹配器
ERROR_MATCHER_CREATE_FAILD = 205     #匹配器创建失败
ERROR_MATCHER_NOT_FREE = 206         #匹配器不是空闲
ERROR_MATCH_RULE_INIT_CHECK = 206    #初始化匹配规则错误
ERROR_MATCH_RULE_NOT_CHECK = 207     #匹配规则还不满足

ERROR_MATCHER_ROOM_CREATE_NOT_EXIT = 301         #房间正在创建中，不能退出

ERROR_MATCHER_AVATAR_HVAE_ENTERED = 401         #玩家已经在房间内，不能重复请求