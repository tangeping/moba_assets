# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import GlobalDefine
import ErrorCode

class RoomRule:
    """
    房间内的规则
    """
    def __init__(self,roomKey,roomNumber,roomData,passwd):
        self.roomKey = roomKey #
        self.roomNumber = roomNumber#房间号
        self.roomPasswd = passwd#房间密码
        self.roomData = roomData


    def check(self):
        if self.roomKey <= 0:
            return ErrorCode.ERROR_ROOM_RULE_KEY
        elif self.roomNumber <= 0:
            return ErrorCode.ERROR_ROOM_RULE_NUMBER
        else:
            return ErrorCode.ERROR_OK

    def destroySelf(self):
        """

        :return:
        """
        roomCompEntity = self.roomData.get('roomCompCall',None)
        if roomCompEntity is None or roomCompEntity.owner is None:
            return
        roomCompEntity.owner.destroySelf()


class SummonerCanyonRule(RoomRule):
    """
    召唤师峡谷房间规则
    """

    def __init__(self,roomKey,roomNumber,roomData={}, passwd = 0):
        RoomRule.__init__(self,roomKey,roomNumber,roomData,passwd)

        if RoomRule.check(self) != ErrorCode.ERROR_OK:
            ERROR_MSG("SummonerCanyonRule Error Code = %d" % RoomRule.check(self))


    def enterRoomReqs(self, entityCall, entityReqs: dict):
        """
        玩家进入房间请求
        :param entityCall:
        :param entityReqs:
        :return:
        """
        DEBUG_MSG("SummonerCanyonRule，enterRoomReqs ::entityID = %d,entityReqs:%s" % (entityCall.id, str(entityReqs)))

        if self.roomPasswd > 0 and self.roomPasswd != entityReqs['passwd']: # roomPasswd == 0不需要密码
            return ErrorCode.ERROR_ROOM_RULE_ENTER_PASSWD
        else:
            return ErrorCode.ERROR_OK


class TwistedJungleRule(RoomRule):
    """
    扭曲丛林房间规则
    """

    def __init__(self,roomKey,roomNumber,roomData={}, passwd = 0):
        RoomRule.__init__(self,roomKey,roomNumber,roomData,passwd)

        if RoomRule.check(self) != ErrorCode.ERROR_OK:
            ERROR_MSG("TwistedJungleRule Error Code = %d" % RoomRule.check(self))


    def enterRoomReqs(self, entityCall, entityReqs: dict):
        """
        玩家进入房间请求
        :param entityCall:
        :param entityReqs:
        :return:
        """
        DEBUG_MSG("TwistedJungleRule.enterRoomReqs::entityID = %d,entityReqs:%s" % (entityCall.id, str(entityReqs)))

        if self.roomPasswd > 0 and self.roomPasswd != entityReqs['passwd']: # roomPasswd == 0不需要密码
            return ErrorCode.ERROR_ROOM_RULE_ENTER_PASSWD
        else:
            return ErrorCode.ERROR_OK

class PolarChaosRule(RoomRule):
    """
    极地大乱斗房间规则
    """

    def __init__(self,roomKey,roomNumber,roomData={}, passwd = 0):
        RoomRule.__init__(self,roomKey,roomNumber,roomData,passwd)

        if RoomRule.check(self) != ErrorCode.ERROR_OK:
            ERROR_MSG("PolarChaosRule Error Code = %d" % RoomRule.check(self))


    def enterRoomReqs(self, entityCall, entityReqs: dict):
        """
        玩家进入房间请求
        :param entityCall:
        :param entityReqs:
        :return:
        """
        DEBUG_MSG("PolarChaosRule.enterRoomReqs::entityID = %d,entityReqs:%s" % (entityCall.id, str(entityReqs)))

        if self.roomPasswd > 0 and self.roomPasswd != entityReqs['passwd']: # roomPasswd == 0不需要密码
            return ErrorCode.ERROR_ROOM_RULE_ENTER_PASSWD
        else:
            return ErrorCode.ERROR_OK

class CryingAbyssRule(RoomRule):
    """
    嚎哭深渊房间规则
    """

    def __init__(self,roomKey,roomNumber,roomData={}, passwd = 0):
        RoomRule.__init__(self,roomKey,roomNumber,roomData,passwd)

        if RoomRule.check(self) != ErrorCode.ERROR_OK:
            ERROR_MSG("CryingAbyssRule Error Code = %d" % RoomRule.check(self))


    def enterRoomReqs(self, entityCall, entityReqs: dict):
        """
        玩家进入房间请求
        :param entityCall:
        :param entityReqs:
        :return:
        """
        DEBUG_MSG("CryingAbyssRule.enterRoomReqs::entityID = %d,entityReqs:%s" % (entityCall.id, str(entityReqs)))

        if self.roomPasswd > 0 and self.roomPasswd != entityReqs['passwd']: # roomPasswd == 0不需要密码
            return ErrorCode.ERROR_ROOM_RULE_ENTER_PASSWD
        else:
            return ErrorCode.ERROR_OK
