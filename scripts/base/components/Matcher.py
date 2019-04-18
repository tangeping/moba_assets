# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from MatchRule import *
from RoomRule import *
import GlobalDefine
import ErrorCode
import Functor

class Matcher:

    def __init__(self,mathID):
        self.matchID = mathID
        self.matchRule = None
        self.roomRule = None
        self.state = GlobalDefine.MATCHER_STATE_FREE

    def checkMatchRule(self):
        """
        检测匹配条件
        :return:
        """
        if self.matchRule is None:
            self.state = GlobalDefine.MATCHER_STATE_UNKOWN
        if self.matchRule.check() == ErrorCode.ERROR_OK:
            self.state = GlobalDefine.MATCHER_STATE_CREATE_ROOM
        DEBUG_MSG("Matcher::checkMatchRule: matchID: %i,state:%d"%(self.matchID,self.state))
        return self.state

    def reqJoinMatch(self,compMatchCall,entityReqs):
        """
        玩家请求加入匹配
        :param entityCall:
        :param entityReqs:
        :return:
        """
        DEBUG_MSG("Matcher::reqJoinMatch: matchID: %i. self.state=%i,compMatchCall.ownerID=%i, entityReqs:%s"
                  % (self.matchID, self.state,compMatchCall.ownerID, str(entityReqs)))

        if self.state < GlobalDefine.MATCHER_STATE_ROOM_READY:
            self.checkMatchRule()
            if self.state == GlobalDefine.MATCHER_STATE_CREATE_ROOM:
                return ErrorCode.ERROR_MATCHER_RULE_MATCH_FULL
            elif self.state == GlobalDefine.MATCHER_STATE_UNKOWN:
                return ErrorCode.ERROR_ROOM_RULE_IS_NONE
            elif self.state != GlobalDefine.MATCHER_STATE_FREE:
                return ErrorCode.ERROR_MATCHER_NOT_FREE

            self.matchRule.playerReqsReady(compMatchCall.owner,entityReqs)
            self.checkMatchRule()

        self.enterMatcherRoom(compMatchCall,entityReqs)
        return  ErrorCode.ERROR_OK


    def enterMatcherRoom(self,compMatchCall,entityReqs):
        """
        所有的条件都匹配了，才开始创建房间。
        :param entityCall:
        :param passwd: 房间密码
        :return:
        """
        DEBUG_MSG("Matcher::enterMatcherRoom: matchID: %i. self.state=%i,compMatchCall.ownerID=%i, entityReqs:%s"
                  % (self.matchID, self.state,compMatchCall.ownerID, str(entityReqs)))

        roomDatas = self.roomRule.roomData
        roomCompCall = roomDatas.get('roomCompCall',None)
        if roomCompCall:
            if self.state >= GlobalDefine.MATCHER_STATE_ROOM_READY :
                roomCompCall.enterMatchRoom(compMatchCall)
                DEBUG_MSG("enterMatcherRoom:: entityCall[%i] enter roomEntity[%i]" % (compMatchCall.ownerID,roomCompCall.id))
        elif self.state <= GlobalDefine.MATCHER_STATE_CREATE_ROOM:#
            players = roomDatas.get('players',{})
            players[compMatchCall.ownerID] = compMatchCall #房间暂时没创建好，先把玩家请求缓存起来
            roomDatas['players'] = players
            roomDatas['roomCompCall'] = None

            if self.state == GlobalDefine.MATCHER_STATE_CREATE_ROOM and \
                            self.roomRule.enterRoomReqs(compMatchCall.owner,entityReqs) == ErrorCode.ERROR_OK:
                self.createMatcherRoom()


        DEBUG_MSG("Matcher::enterMatcherRoom: roomDatas: %s" % str(self.roomRule.roomData))

    def exitMatcherRoom(self, compMatchCall):
        """

        :param comMatchCall:
        :return:
        """
        DEBUG_MSG("Matcher::exitMatcherRoom: matchID: %i. self.state=%i,compMatchCall.ownerID=%i," % (self.matchID, self.state,compMatchCall.ownerID))

        if  self.state  == GlobalDefine.MATCHER_STATE_CREATE_ROOM:
            return ErrorCode.ERROR_MATCHER_ROOM_CREATE_NOT_EXIT

        self.matchRule.playerReqsCancel(compMatchCall.owner)

        roomDatas = self.roomRule.roomData
        players = roomDatas.get('players', {})

        if compMatchCall.ownerID in players.keys():
            del players[compMatchCall.ownerID]

        if compMatchCall.owner and compMatchCall.owner.cell :
            compMatchCall.owner.destroyCellEntity()

        if len(players) == 0:
            self.roomRule.destroySelf()
            self.roomRule = None

        return ErrorCode.ERROR_OK

    def createMatcherRoom(self):
        """
        创建房间
        :param entityCall:
        :return:
        """
        DEBUG_MSG("Matcher::createMatcherRoom: matchID: %i. self.state=%i" % (self.matchID, self.state))

        if self.state  != GlobalDefine.MATCHER_STATE_CREATE_ROOM:
            DEBUG_MSG("create room is not MATCHER_STATE_CREATE_ROOM state : %s")
            return ErrorCode.ERROR_ROOM_CREATE_NOT_READY

        params = {
            "compMatchRoom": {"roomKey": self.roomRule.roomKey}
        }
        KBEngine.createEntityAnywhere("Room", params,Functor.Functor(self.onRoomCreatedCB, self.roomRule.roomKey))

        return  ErrorCode.ERROR_OK

    def onRoomCreatedCB(self, roomKey, roomEntityCall):
        """
        一个space创建好后的回调
        """
        DEBUG_MSG("Matcher::onRoomCreatedCB: space %i. entityID=%i" % (roomKey, roomEntityCall.id))
        self.state = GlobalDefine.MATCHER_STATE_ROOM_READY

    def onRoomGetCell(self,roomCompCall):
        """

        :param roomCompCall:
        :return:
        """
        DEBUG_MSG("Matcher::onRoomGetCell: matchID= %i. roomCompCall.id=%i,roomData:%s"
                  % (self.matchID, roomCompCall.ownerID,str(self.roomRule.roomData)))

        if self.state != GlobalDefine.MATCHER_STATE_ROOM_READY:
            return ErrorCode.ERROR_ROOM_CREATE_NOT_READY


        roomDatas = self.roomRule.roomData
        roomDatas['roomCompCall'] = roomCompCall

        players = roomDatas.get('players', {})

        for player in players.values():
            player.createCell(roomCompCall.owner.cell,self.roomRule.roomKey)

        players.clear()

        return ErrorCode.ERROR_OK