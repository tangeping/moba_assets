# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class TMatchRequest(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		list.__init__(self)

	def asDict(self):
		data = {
			"utype"			: self[0],
			"matchID"		: self[1],
            "passwd"        : self[2],
            "teamID"     	: self[3]
		}

		return data

	def createFromDict(self, dictData):
		self.extend([dictData["utype"], dictData["matchID"], dictData["passwd"],dictData["teamID"]])

		return self

class MATCH_REQUEST_PICKLER:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return TMatchRequest().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, TMatchRequest)

matching_info_inst = MATCH_REQUEST_PICKLER()


