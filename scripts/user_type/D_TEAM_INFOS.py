# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class DTeamInfos(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "id": self[0],
            "team_id": self[1],
            "position_x": self[2],
            "position_y": self[3],
            "position_z": self[4],
            "direction_x": self[5],
            "direction_y": self[6],
            "direction_z": self[7]
        }
        return data

    def createFromDict(self, d):
        self.extend([
            d["id"], d["team_id"], d["position_x"], d["position_y"], d["position_z"],
            d["direction_x"], d["direction_y"], d["direction_z"],
        ])
        return self


class D_TEAM_INFOS_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return DTeamInfos().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DTeamInfos)


d_team_info_inst = D_TEAM_INFOS_PICKLER()


class DTeamInfosList(dict):
    """
    """

    def __init__(self):
        """
        """
        dict.__init__(self)

    def asDict(self):
        datas = []
        dct = {"values": datas}

        for key, val in self.items():
            datas.append(val)

        return dct

    def createFromDict(self, dictData):
        for data in dictData["values"]:
            self[data[0]] = data
        return self


class D_TEAM_INFOS_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return DTeamInfosList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DTeamInfosList)


d_team_info_list_inst = D_TEAM_INFOS_LIST_PICKLER()
