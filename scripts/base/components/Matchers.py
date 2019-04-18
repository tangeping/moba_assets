# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import d_matchs
from Matcher import *
import GlobalDefine
import ErrorCode

class Matchers(KBEngine.EntityComponent):
    def __init__(self):
        KBEngine.EntityComponent.__init__(self)
        self.matchers = {}
        self.matcherIDsMapUtype = {}
        self.lastNewRoomKey = 0
        self.lastRoomNumber = 100000

    def onAttached(self, owner):
        """
        """
        INFO_MSG("matchers::onAttached(): owner=%i" % (owner.id))

    def onDetached(self, owner):
        """
        """
        INFO_MSG("matchers::onDetached(): owner=%i" % (owner.id))


    def onClientEnabled(self):
        """
        KBEngine method.
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
        cell部分。
        """
        INFO_MSG("matchers[%i]::onClientEnabled:entities enable." % (self.ownerID))

    def onClientDeath(self):
        """
        KBEngine method.
        客户端对应实体已经销毁
        """
        DEBUG_MSG("Test[%i].onClientDeath:" % self.ownerID)

    def onTimer(self, tid, userArg):
        """
        KBEngine method.
        引擎回调timer触发
        """
        DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.name, self.ownerID, tid, userArg))


    def createMatcher(self,utype,passwd = 0):

        datas = d_matchs.datas.get(utype)
        if datas is None:
            ERROR_MSG("matchers::createMatcher get matchData error , d_matchs.datas hava on key : %d" % utype)
            return None

        DEBUG_MSG("%s::createMatcher: self.lastNewRoomKey=%i, self.matchers:%s" % (self.name, self.lastNewRoomKey,str(self.matchers.keys())))

        """
        if self.lastNewRoomKey  in self.matchers.keys():
            ERROR_MSG("matchers::createMatcher have in mathers ,self.lastNewRoomKey : %d" % self.lastNewRoomKey)
            return self.matchers[self.lastNewRoomKey]
        """
        self.lastNewRoomKey = KBEngine.genUUID64()
        matherData = Matcher(self.lastNewRoomKey)

        matchType = datas.get('matchRule',None)
        if matchType is None:
            ERROR_MSG("matchers::createMatcher matchType:%d is None d_matchs.datas " % datas)
            return None
        else:
            ruleData =  d_matchs.matchRuleDatas.get(matchType,None)
            if ruleData is None:
                ERROR_MSG("matchers::createMatcher d_matchs.matchRuleDatas.get(matchType,None) matchType: %d" % matchType)
                return None
            if ruleData['utype'] == "player":
                matherData.matchRule = PlayerMatchRule(ruleData['id'],ruleData['name'],ruleData['teamACount'],ruleData['teamBCount'],\
                                                  ruleData['minPlayers'],ruleData['maxPlayers'])
            elif ruleData['utype'] == 'npc':
                matherData.matchRule = NPCMatchRule(ruleData['id'],ruleData['name'],ruleData['teamACount'],ruleData['teamBCount'],\
                                                  ruleData['minPlayers'],ruleData['maxPlayers'])
            elif ruleData['utype'] == 'customize':
                matherData.matchRule = CustomizeMatchRule(ruleData['id'],ruleData['name'],ruleData['teamACount'],ruleData['teamBCount'],\
                                                  ruleData['minPlayers'],ruleData['maxPlayers'])
            else:
                ERROR_MSG("matchers::createMatcher d_matchs.ruleData.get(utype,None) utype: %s" % ruleData['utype'])
                return None

        roomType = datas.get('roomRule',None)
        if roomType is None:
            ERROR_MSG("matchers::createMatcher roomType:%d is None d_matchs.datas " % datas)
            return None
        else:
            ruleData =  d_matchs.roomRuleDatas.get(roomType,None)
            if ruleData is None:
                ERROR_MSG("matchers::createMatcher d_matchs.roomRuleDatas.get(roomType,None) roomType: %d" % roomType)
                return None

            if ruleData['roomType'] == "SummonerCanyon":
                matherData.roomRule = SummonerCanyonRule(self.lastNewRoomKey,self.lastRoomNumber,ruleData,passwd)
            elif ruleData['roomType'] == 'TwistedJungle':
                matherData.roomRule = TwistedJungleRule(self.lastNewRoomKey,self.lastRoomNumber,ruleData,passwd)
            elif ruleData['roomType'] == 'PolarChaos':
                matherData.roomRule = PolarChaosRule(self.lastNewRoomKey, self.lastRoomNumber, ruleData,passwd)
            elif ruleData['roomType'] == 'CryingAbyss':
                matherData.roomRule = CryingAbyssRule(self.lastNewRoomKey, self.lastRoomNumber, ruleData,passwd)
            else:
                ERROR_MSG("matchers::createMatcher d_matchs.roomRuleDatas.get(utype,None) utype: %s" % ruleData['roomType'])
                return None
            self.lastRoomNumber += 1

        self.matcherIDsMapUtype[matherData.matchID] = utype
        self.matchers[matherData.matchID] = matherData
        DEBUG_MSG("%s::createMatcher: matchID=%i, utype:%i" % (self.name, matherData.matchID, utype))
        return  matherData

    def findMatcher(self,matchID):
        """

        :param matchID:
        :return:
        """
        if matchID not in self.matchers.keys():
            DEBUG_MSG("matchers::findMatcher,matchID:%d have not found !" % matchID)
            return None
        return  self.matchers[matchID]

    def randomMatcher(self,utype):
        """
        随机加入匹配器，条件满足就加入
        :return:
        """
        DEBUG_MSG("%s::randomMatcher: self.matcherIDsMapUtype:%s" % (self.name, str(self.matcherIDsMapUtype)))


        matherData = None
        for mather in self.matchers.values():
            DEBUG_MSG("%s::randomMatcher: mather.state:%d" % (self.name, mather.state))
            if mather.state == GlobalDefine.MATCHER_STATE_FREE and utype in self.matcherIDsMapUtype.values():
                matchID = list(self.matcherIDsMapUtype.keys())[list(self.matcherIDsMapUtype.values()).index(utype)]
                return  self.findMatcher(matchID)

        DEBUG_MSG("matchers::randomJoinMather utype:%d have not found !" % utype)
        return None

    def joinMatcher(self,compMatchCall,entityReqs, notCreate = False):
        """
        加入匹配器
        :param compMatchCall: 玩家compMatchCall
        :param entityReqs: 一个字典包含了 teamID 等匹配信息
        :param utype: 匹配类型，在 d_matcher.datas 的key
        :param matchID: 匹配ID，如果等于0，就默认随机匹配一个
        :return:
        """
        DEBUG_MSG("matchers::joinMatcher entityReqs:%s  !" % str(entityReqs))

        utype = entityReqs['utype']
        matchID = entityReqs['matchID']
        passwd = entityReqs['passwd']

        matcher = None
        if matchID == 0:
            matcher = self.randomMatcher(utype) #随机查找一个匹配器
        else:
            matcher = self.findMatcher(matchID)

        if matcher is None:
            if notCreate:
                return ErrorCode.ERROR_MATCHER_NOT_FOUND
            else:
                matcher = self.createMatcher(utype,passwd)
                if matcher is None:
                    return ErrorCode.ERROR_MATCHER_CREATE_FAILD

        matcher.reqJoinMatch(compMatchCall,entityReqs)

        #if matcher.state == GlobalDefine.MATCHER_STATE_CREATE_ROOM:

    def exitMatcher(self,comMatchCall,matchID):
        """

        :param comMatchCall:
        :param matchID:
        :return:
        """
        DEBUG_MSG("matchers::exitMatcher comMatchCall.id:%i  !" % comMatchCall.ownerID)
        matcher = self.findMatcher(matchID)
        if matcher is None:
            return

        matcher.exitMatcherRoom(comMatchCall)

        if matcher.roomRule is None:
            del self.matchers[matchID]


    def onRoomGetCell(self,compMatchCall,matherID):
        """

        :param compMatchCall:
        :param matherID:
        :return:
        """
        DEBUG_MSG("matchers::onRoomGetCell comMatchCall.id:%i  !" % compMatchCall.ownerID)

        matcher = self.findMatcher(matherID)
        if matcher is None:
            return ErrorCode.ERROR_MATCHER_NOT_FOUND

        matcher.onRoomGetCell(compMatchCall)



