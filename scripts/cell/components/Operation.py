# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Operation(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)
	

	def onAttached(self, owner):
		"""
		"""			
		INFO_MSG("Operation::onAttached(): owner=%i" % (owner.id))


	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("Operation::onDetached(): owner=%i" % (owner.id))


	def reqReady(self, exposed,ready):
		"""
		exposed.
		客户端准备
		"""
		if exposed != self.owner.id:
			return

		room = self.owner.getCurrRoom()
		if room:
			room.reqReady(self.owner,ready)

		#DEBUG_MSG("Operation[%i].reqReady:%d ." % (self.owner.id,ready))

	def reqGamePause(self,exposed):

		if exposed != self.owner.id:
			return
		room = self.owner.getCurrRoom()
		if room:
			room.reqGamePause(self.owner)

	def reqGameRunning(self,exposed):

		if exposed != self.owner.id:
			return
		room = self.owner.getCurrRoom()
		if room:
			room.reqGameRunning(self.owner)

	def reqHeroConf(self,exposed):
		"""

		:param exposed:
		:param table: csv file name
		:return:
		"""
		room = self.owner.getCurrRoom()
		if room:
			room.reqHeroInfo(self.owner,"d_hero.csv")

	def reqPropsConf(self,exposed):
		"""

		:param exposed:
		:param table: csv file name
		:return:
		"""
		room = self.owner.getCurrRoom()
		if room:
			room.reqPropsInfo(self.owner,'d_props.csv')

	def reqRoadConf(self,exposed):
		"""

		:param exposed:
		:param table: csv file name
		:return:
		"""
		room = self.owner.getCurrRoom()
		if room:
			room.reqRoadInfo(self.owner,'d_road.csv')


	def reqShopConf(self,exposed):
		"""

		:param exposed:
		:param table: csv file name
		:return:
		"""
		room = self.owner.getCurrRoom()
		if room:
			room.reqShopInfo(self.owner,'d_shop.csv')


	def reqSkillConf(self,exposed):
		"""

		:param exposed:
		:param table: csv file name
		:return:
		"""
		room = self.owner.getCurrRoom()
		if room:
			room.reqSkillInfo(self.owner,'d_skill.csv')

	def reqTeamConf(self,exposed):
		"""

		:param exposed:
		:param table: csv file name
		:return:
		"""
		room = self.owner.getCurrRoom()
		if room:
			room.reqTeamInfo(self.owner,'d_team.csv')


	def downLoadFile(self,exposed,fileName):
		"""

		:param exposed:
		:param fileName: download file name
		:return:
		"""
		fullFileName = KBEngine.open("data/"+fileName,"r+")
		self.client.streamFileToClient(fullFileName)




