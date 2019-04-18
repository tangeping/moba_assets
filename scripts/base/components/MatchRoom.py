# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class MatchRoom(KBEngine.EntityComponent):
    def __init__(self):
        KBEngine.EntityComponent.__init__(self)


    def onAttached(self, owner):
        """
        """

        INFO_MSG("MatchRoom::onAttached(): owner=%i" % (owner.id))

    def onDetached(self, owner):
        """
        """
        INFO_MSG("MatchRoom::onDetached(): owner=%i" % (owner.id))

    def enterMatchRoom(self, compEntityCall):
        """
        defined method.
        请求进入某个space中
        """
        compEntityCall.createCell(self.owner.cell,self.roomKey)

    def leaveMatchRoom(self, entityID):
        """
        defined method.
        某个玩家请求退出这个space
        """
        pass

    def onClientEnabled(self):
        """
        KBEngine method.
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
        cell部分。
        """
        INFO_MSG("Test[%i]::onClientEnabled:entities enable." % (self.ownerID))

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

    def onGetCell(self):
        """
        KBEngine method.
        entity的cell部分实体被创建成功
        """
        DEBUG_MSG("Room::onGetCell: %i" % self.ownerID)

        KBEngine.globalData["Halls"].compMatchers.onRoomGetCell(self,self.roomKey)

