# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Chat(KBEngine.EntityComponent):
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


    def say(self,exposed,name, context):
        '''
        帧同步开始
        '''
        if self.id != exposed:
            return

        room = self.owner.getCurrRoom()
        if room:
            room.say(name, context)

