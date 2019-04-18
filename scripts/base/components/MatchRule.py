# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import GlobalDefine
import ErrorCode

class MatchRule:
    """
    匹配规则
    """
    def __init__(self,id):
        self.ID = id
        self.minPlayers = -1
        self.maxPlayers = -1

    def check(self):
        """
        检测匹配规则
        :return:
        """
        DEBUG_MSG("MatchRule::check,ID = %d,minPlayers:%d,maxPlayers=%d" % (self.ID, self.minPlayers,self.maxPlayers))
        if self.ID <= 0:
            return ErrorCode.ERROR_MATCHER_ARGS_ID
        elif self.minPlayers == -1 or self.maxPlayers == -1 :
            return ErrorCode.ERROR_MATCHER_ARGS_MIN_MAX_UNSET
        elif self.minPlayers > self.maxPlayers:
            return ErrorCode.ERROR_MATCHER_ARGS_MIN_GREATER_MAX
        else:
            return ErrorCode.ERROR_OK

    def playerReqsReady(self, entityCall, entityReqs: dict):
        """

        :param entityCall:
        :param entityReqs:
        :return:
        """
        pass

    def playerReqsCancel(self, entityCall):
        """

        :param entityCall:
        :return:
        """
        pass

class NPCMatchRule(MatchRule):
    """
    人机对战
    """

    def __init__(self,id,name,teamA,teamB,minPlayers,maxPlayers):
        MatchRule.__init__(self,id)
        self.name = name
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.teamACountMax = teamA
        self.teamBCountMax = teamB

        self.clearPlayerData()

    def clearPlayerData(self):
        """

        :return:
        """
        #-------player request data
        self.playerIDs = []
        self.teamAIDs = []
        self.teamBIDs = []

    def playerReqsReady(self,entityCall,entityReqs:dict):
        """

        :param entityCall:
        :param entityreqs:
        :return:
        """
        DEBUG_MSG("NPCMatchRule::playerReqsReady,entityID = %d,entityReqs:%s" % (entityCall.id,str(entityReqs)))

        if entityCall.id not in self.playerIDs:
            self.playerIDs.append(entityCall.id)
        if  entityCall.id not in self.teamAIDs:
            self.teamAIDs.append(entityCall.id)
            entityCall.teamIDChanged(GlobalDefine.TEAM_A_ID)

    def playerReqsCancel(self,entityCall):
        """

        :param entityCall:
        :param entityreqs:
        :return:
        """
        DEBUG_MSG("NPCMatchRule::playerReqsCancel,entityID = %d" % (entityCall.id))

        if entityCall.id  in self.playerIDs:
            self.playerIDs.remove(entityCall.id)
        if entityCall.id  in self.teamAIDs:
            self.teamAIDs.remove(entityCall.id)


    def checkPlayerCount(self):
        """

        :return:
        """
        return self.minPlayers <= len(self.playerIDs) <= self.maxPlayers and len(self.playerIDs) > 0

    def checkTeamACount(self):
        """

        :return:
        """
        return len(self.teamAIDs) == self.teamACountMax


    def check(self):
        """
        检测是否可以创建房间
        :return:
        """
        DEBUG_MSG("NPCMatchRule::check,self.playerIDs = %s ,self.teamAIDs = %s,self.teamBIDs=%s"
                  % (str(self.playerIDs),str(self.teamAIDs),str(self.teamBIDs)))

        if MatchRule.check(self) != ErrorCode.ERROR_OK:
            ERROR_MSG("NPCMatchRule::check,Error Code = %d" % MatchRule.check(self))
            return ErrorCode.ERROR_MATCH_RULE_INIT_CHECK

        if self.checkPlayerCount() and self.checkTeamCount():
            return ErrorCode.ERROR_OK
        else:
            return ErrorCode.ERROR_MATCH_RULE_NOT_CHECK


class PlayerMatchRule(MatchRule):
    """
    玩家对战
    """
    def __init__(self,id,name,teamA,teamB,minPlayers,maxPlayers):
        MatchRule.__init__(self,id)
        self.name = name
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.teamACountMax = teamA
        self.teamBCountMax = teamB

        self.clearPlayerData()

    def clearPlayerData(self):
        """

        :return:
        """
        # -------player request data
        self.playerIDs = []
        self.teamAIDs = []
        self.teamBIDs = []

    def playerReqsReady(self,entityCall,entityReqs:dict):
        """

        :param entityCall:
        :param entityreqs:
        :return:
        """
        DEBUG_MSG("PlayerMatchRule::playerReqsReady,entityID = %d,entityReqs:%s" % (entityCall.id, str(entityReqs)))

        #只要人数够了就开始，自动分配teamID给玩家
        if entityCall.id not in self.playerIDs:
            self.playerIDs.append(entityCall.id)
            if not self.checkTeamACount() and entityCall.id not  in self.teamAIDs:
                self.teamAIDs.append(entityCall.id)
                entityCall.teamIDChanged(GlobalDefine.TEAM_A_ID)
            elif not self.checkTeamBCount() and entityCall.id not in self.teamBIDs:
                self.teamBIDs.append(entityCall.id)
                entityCall.teamIDChanged(GlobalDefine.TEAM_B_ID)

        """
        if entityReqs['teamID'] == GlobalDefine.TEAM_R_ID:
            teamlist =  self.teamBIDs if (len(self.teamAIDs) > len(self.teamBIDs) ) else self.teamAIDs
            if entityCall.id not in teamlist:
                entityCall.teamID = GlobalDefine.TEAM_B_ID if (len(self.teamAIDs) > len(self.teamBIDs)) else GlobalDefine.TEAM_A_ID
                teamlist.append(entityCall.id)
            if entityCall.id not in self.playerIDs:
                self.playerIDs.append(entityCall.id)
        elif entityReqs["teamID"] == GlobalDefine.TEAM_A_ID:
            if entityCall.id not in self.playerIDs:
                self.playerIDs.append(entityCall.id)
            if entityCall.id not in self.teamAIDs:
                self.teamAIDs.append(entityCall.id)
                entityCall.teamID = GlobalDefine.TEAM_A_ID
        elif entityReqs["teamID"] == GlobalDefine.TEAM_B_ID:
            if entityCall.id not in self.playerIDs:
                self.playerIDs.append(entityCall.id)
            if entityCall.id not in self.teamBIDs:
                self.teamBIDs.append(entityCall.id)
                entityCall.teamID = GlobalDefine.TEAM_B_ID
        else:
            ERROR_MSG("PlayerMatchRule entityReqs have no teamID key")
        """

    def playerReqsCancel(self,entityCall):
        """

        :param entityCall:
        :param entityreqs:
        :return:
        """
        DEBUG_MSG("PlayerMatchRule::playerReqsCancel::entityID = %d" % (entityCall.id))

        if entityCall.id  in self.playerIDs:
            self.playerIDs.remove(entityCall.id)
        if entityCall.id  in self.teamAIDs:
            self.teamAIDs.remove(entityCall.id)
        if entityCall.id  in self.teamBIDs:
            self.teamBIDs.remove(entityCall.id)


    def checkPlayerCount(self):
        """

        :return:
        """
        return self.minPlayers <= len(self.playerIDs) <= self.maxPlayers and len(self.playerIDs) > 0

    def checkTeamACount(self):
        """

        :return:
        """
        return len(self.teamAIDs) == self.teamACountMax

    def checkTeamBCount(self):
        """

        :return:
        """
        return len(self.teamBIDs) == self.teamBCountMax

    def check(self):
        """
        检测是否可以创建房间
        :return:
        """
        DEBUG_MSG("PlayerMatchRule::check,self.playerIDs = %s ,self.teamAIDs = %s,self.teamBIDs=%s"
                  % (str(self.playerIDs),str(self.teamAIDs),str(self.teamBIDs)))

        if MatchRule.check(self) != ErrorCode.ERROR_OK:
            ERROR_MSG("PlayerMatchRule::check, Error Code = %d" % MatchRule.check(self))
            return ErrorCode.ERROR_MATCH_RULE_INIT_CHECK
        if self.checkPlayerCount() and self.checkTeamACount() and self.checkTeamBCount():
            return ErrorCode.ERROR_OK
        else:
            return ErrorCode.ERROR_MATCH_RULE_NOT_CHECK

class CustomizeMatchRule(MatchRule):
    """
    自定义匹配
    """
    def __init__(self,id,name,teamA,teamB,minPlayers,maxPlayers):
        MatchRule.__init__(self,id)
        self.name = name
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers

        self.clearPlayerData()

    def clearPlayerData(self):
        """

        :return:
        """
        # -------player request data
        self.playerIDs = []



    def playerReqsReady(self,entityCall,entityReqs:dict):
        """

        :param entityCall:
        :param entityreqs:
        :return:
        """
        DEBUG_MSG("CustomizeMatchRule::playerReqsReady,entityID = %d,entityReqs:%s" % (entityCall.id, str(entityReqs)))

        if entityCall.id not in self.playerIDs:
            self.playerIDs.append(entityCall.id)
        entityCall.teamIDChanged(entityReqs['teamID'])

    def playerReqsCancel(self,entityCall):
        """

        :param entityCall:
        :param entityreqs:
        :return:
        """
        DEBUG_MSG("CustomizeMatchRule::playerReqsCancel,entityID = %d " % (entityCall.id))

        if entityCall.id in self.playerIDs:
            self.playerIDs.remove(entityCall.id)


    def checkPlayerCount(self):
        """

        :return:
        """
        return self.minPlayers <= len(self.playerIDs) <= self.maxPlayers and len(self.playerIDs) > 0



    def check(self):
        """
        检测是否可以创建房间
        :return:
        """
        DEBUG_MSG("CustomizeMatchRule::check,self.playerIDs = %s ,self.teamAIDs = %s,self.teamBIDs=%s"
                  % (str(self.playerIDs),str(self.teamAIDs),str(self.teamBIDs)))

        if MatchRule.check(self) != ErrorCode.ERROR_OK:
            ERROR_MSG("CustomizeMatchRule::check,Error Code = %d" % MatchRule.check(self))
            return ErrorCode.ERROR_MATCH_RULE_INIT_CHECK

        if self.checkPlayerCount():
            return ErrorCode.ERROR_OK
        else:
            return ErrorCode.ERROR_MATCH_RULE_NOT_CHECK