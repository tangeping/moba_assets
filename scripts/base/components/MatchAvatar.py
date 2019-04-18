# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import GlobalDefine


class MatchAvatar(KBEngine.EntityComponent):
    """

    """

    def __init__(self):
        KBEngine.EntityComponent.__init__(self)


    def onAttached(self, owner):
        """
        """
        INFO_MSG("MatchAvatar::onAttached(): owner=%i" % (owner.id))


    def onDetached(self, owner):
        """
        """
        INFO_MSG("MatchAvatar::onDetached(): owner=%i" % (owner.id))

    def createCell(self, space, roomKey):
        """
		defined method.
		创建cell实体
		"""
        self.roomKey = roomKey
        self.owner.createCell(space,roomKey)

    def onClientEnabled(self):
        """
        KBEngine method.
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
        cell部分。
        """

        INFO_MSG("MatchAvatar[%i]::onClientEnabled:entities enable." % (self.ownerID))

    def onClientDeath(self):
        """
        KBEngine method.
        客户端对应实体已经销毁
        """
        DEBUG_MSG("MatchAvatar[%i].onClientDeath:" % self.ownerID)

        compMatchers = KBEngine.globalData["Halls"].compMatchers
        compMatchers.exitMatcher(self, self.roomKey)

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
        DEBUG_MSG("MatchAvatar::onGetCell: %i" % self.ownerID)



    def reqJoinMatch(self,requstData):
        """

        :param requstData:
        :return:
        """

        compMatchers = KBEngine.globalData["Halls"].compMatchers
        compMatchers.joinMatcher(self, requstData.asDict(),False)


    def reqExitMatch(self):
        """

        :return:
        """

        compMatchers = KBEngine.globalData["Halls"].compMatchers
        compMatchers.exitMatcher(self, self.roomKey)