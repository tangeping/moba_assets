# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import SCDefine
import CSV_Helper

from D_ROAD_INFOS import DRoadInfos
from D_ROAD_INFOS import DRoadInfosList

from D_HERO_INFOS import DHeroInfos
from D_HERO_INFOS import DHeroInfosList

from D_PROPS_INFOS import DPropsInfos
from D_PROPS_INFOS import DPropsInfosList

from D_SHOP_INFOS import DShopInfos
from D_SHOP_INFOS import DShopInfosList

from D_SKILL_INFOS import DSkillInfos
from D_SKILL_INFOS import DSkillInfosList

from D_TEAM_INFOS import DTeamInfos
from D_TEAM_INFOS import DTeamInfosList



TEAM_MAX_PLAYER = 5

class Room(KBEngine.Entity):
    """
    游戏场景
    """
    def __init__(self):
        KBEngine.Entity.__init__(self)


        # 告诉客户端加载地图
        #KBEngine.addSpaceGeometryMapping(self.spaceID, None, "spaces/gameMap")

        DEBUG_MSG('created space[%d] entityID = %i, res = %s.' % (self.roomKeyC, self.id, "spaces/gameMap"))

        # 让baseapp和cellapp都能够方便的访问到这个房间的entityCall
        KBEngine.globalData["Room_%i" % self.spaceID] = self.base

        # 开始记录一局游戏时间， 时间结束后将玩家踢出空间同时销毁自己和空间
        self.addTimer(SCDefine.ROOM_ROUND_TIME, 0, SCDefine.TIMER_TYPE_ROOM_DESTORY)

        self.avatars = {}

        self.conf = CSV_Helper.inst

    def reqReady(self,entityCall,ready):
        """
        玩家开始准备
        """
        if entityCall.component2.state !=  0:
            return

        entityCall.component2.state = 1

        readCount = 0
        for e in self.avatars.values():
            readCount = readCount + e.component2.state

        canBegin = (readCount == len(self.avatars))

        if not canBegin or len(self.avatars)%2 != 0:
            return

        self.setGroup()
        self.component1.start()

        for e in self.avatars.values():
            e.component2.client.readyResult(0)

    def reqGamePause(self,entityCall):
        """
        游戏暂停
        """
        if entityCall.component2.state != 1:
            return
        entityCall.component2.state = 2
        self.component1.stop()

    def reqGameRunning(self,entityCall):
        """
        游戏运行
        """
        if entityCall.component2.state != 2:
            return
        entityCall.component2.state = 1
        self.component1.run()


    def setGroup(self):
        '''
        设置分组
        :return: None
        '''

        if len(self.avatars) % 2 !=0:
            return

        datas = self.conf.getTable('d_team.csv')

        if datas is None:
            return

        count = 1
        for e in self.avatars.values():
            index = 0
            if count % 2 != 0:
                index = count + 1
            else:
                index = count + 1 + TEAM_MAX_PLAYER
            count = count + 1
            row_data = datas.get(index,None)
            if row_data is None:
                continue
            e.teamID = row_data['team_id']
            e.position = (row_data['position_x'],row_data['position_y'],row_data['position_z'])
            e.direction = (row_data['direction_x'],row_data['direction_y'],row_data['direction_z'])

    def reqHeroInfo(self,entityCall,tableName):
        """

        :param entityCall:
        :param tableName:
        :return:
        """
        if entityCall is None or entityCall.component2 is None:
            return

        datas = self.conf.getTable(tableName)
        if datas is None:
            return
        info_list = DHeroInfosList();
        for key, value in datas.items():
            infos = DHeroInfos().createFromDict(value)
            info_list[infos[0]] = infos
        entityCall.component2.client.rspHeroInfo(info_list)

    def reqPropsInfo(self,entityCall,tableName):
        """

        :param entityCall:
        :param tableName:
        :return:
        """
        if entityCall is None or entityCall.component2 is None:
            return
        datas = self.conf.getTable(tableName)
        if datas is None:
            return
        info_list = DPropsInfosList();
        for key, value in datas.items():
            infos = DPropsInfos().createFromDict(value)
            info_list[infos[0]] = infos
        entityCall.component2.client.rspPropsInfo(info_list)

    def reqRoadInfo(self,entityCall,tableName):
        """

        :param entityCall:
        :param tableName:
        :return:
        """
        if entityCall is None or entityCall.component2 is None:
            return

        datas = self.conf.getTable(tableName)
        if datas is None:
            return

        info_list = DRoadInfosList();
        for key, value in datas.items():
            infos = DRoadInfos().createFromDict(value)
            info_list[infos[0]] = infos

        entityCall.component2.client.rspRoadInfo(info_list)

    def reqShopInfo(self,entityCall,tableName):
        """

        :param entityCall:
        :param tableName:
        :return:
        """
        if entityCall is None or entityCall.component2 is None:
            return
        datas = self.conf.getTable(tableName)
        if datas is None:
            return

        info_list = DShopInfosList();
        for key, value in datas.items():
            infos = DShopInfos().createFromDict(value)
            info_list[infos[0]] = infos
        entityCall.component2.client.rspShopInfo(info_list)

    def reqSkillInfo(self,entityCall,tableName):
        """

        :param entityCall:
        :param tableName:
        :return:
        """
        if entityCall is None or entityCall.component2 is None:
            return
        datas = self.conf.getTable(tableName)
        if datas is None:
            return

        info_list = DSkillInfosList();
        for key, value in datas.items():
            infos = DSkillInfos().createFromDict(value)
            info_list[infos[0]] = infos
        entityCall.component2.client.rspSkillInfo(info_list)

    def reqTeamInfo(self,entityCall,tableName):
        """

        :param entityCall:
        :param tableName:
        :return:
        """
        if entityCall is None or entityCall.component2 is None:
            return
        datas = self.conf.getTable(tableName)
        if datas is None:
            return

        info_list = DTeamInfosList();
        for key, value in datas.items():
            infos = DTeamInfos().createFromDict(value)
            info_list[infos[0]] = infos
        entityCall.component2.client.rspTeamInfo(info_list)

    #--------------------------------------------------------------------------------------------
    #                              Callbacks
    #--------------------------------------------------------------------------------------------
    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        if SCDefine.TIMER_TYPE_ROOM_DESTORY == userArg:
            self.onDestroyTimer()

    def onDestroy(self):
        """
        KBEngine method.
        """
        DEBUG_MSG("Room::onDestroy: %i" % (self.id))
        del KBEngine.globalData["Room_%i" % self.spaceID]

    def onDestroyTimer(self):
        DEBUG_MSG("Room::onDestroyTimer: %i" % (self.id))
        # 请求销毁引擎中创建的真实空间，在空间销毁后，所有该空间上的实体都被销毁
        self.destroySpace()


    def onEnter(self, entityCall):
        """
        defined method.
        进入场景
        """
        DEBUG_MSG('Room::onEnter space[%d] entityID = %i.' % (self.spaceID, entityCall.id))

        self.avatars[entityCall.id] = entityCall


    def onLeave(self, entityID):
        """
        defined method.
        离开场景
        """
        DEBUG_MSG('Room::onLeave space[%d] entityID = %i.' % (self.spaceID, entityID))

        if entityID in self.avatars:
            del self.avatars[entityID]





