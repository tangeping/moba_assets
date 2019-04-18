# -*- coding: utf-8 -*-
import KBEngine
import Functor
from KBEDebug import *
import GlobalDefine

FIND_ROOM_NOT_FOUND = 0
FIND_ROOM_CREATING = 1

class Halls(KBEngine.Entity):
	"""
	这是一个脚本层封装的房间管理器
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		
		# 向全局共享数据中注册这个管理器的entityCall以便在所有逻辑进程中可以方便的访问
		KBEngine.globalData["Halls"] = self

		# 所有房间，是个字典结构，包含 {"roomEntityCall", "PlayerCount", "enterRoomReqs"}
		# enterRoomReqs, 在房间未创建完成前， 请求进入房间和登陆到房间的请求记录在此，等房间建立完毕将他们扔到space中


	def enterRoom(self, entityCall, position, direction, roomKey):
		"""
		defined method.
		请求进入某个Room中
		"""
		pass

	def leaveRoom(self, avatarID, roomKey):
		"""
		defined method.
		某个玩家请求登出服务器并退出这个space
		"""
		pass
			
	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onRoomCreatedCB(self, roomKey, roomEntityCall):
		"""
		一个space创建好后的回调
		"""
		DEBUG_MSG("Halls::onRoomCreatedCB: space %i. entityID=%i" % (roomKey, roomEntityCall.id))

	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		pass
		
	def onRoomLoseCell(self, roomKey):
		"""
		defined method.
		Room的cell销毁了
		"""
		DEBUG_MSG("Halls::onRoomLoseCell: space %i." % (roomKey))


	def onRoomGetCell(self, roomEntityCall, roomKey):
		"""
		defined method.
		Room的cell创建好了
		"""
		DEBUG_MSG("Halls::onRoomGetCell: space %i." % (roomKey))