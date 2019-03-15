# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class DRoadInfos(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "id": self[0],
            "group": self[1],
            "position_x": self[2],
            "position_y": self[3],
            "position_z": self[4],
            "eulerAngles_x": self[5],
            "eulerAngles_y": self[6],
            "eulerAngles_z": self[7],
            "born": self[8]
        }
        return data

    def createFromDict(self, d):
        self.extend([
            d["id"], d["group"], d["position_x"], d["position_y"], d["position_z"],
            d["eulerAngles_x"], d["eulerAngles_y"], d["eulerAngles_z"], d["born"]
        ])
        return self


class D_ROAD_INFOS_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return DRoadInfos().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DRoadInfos)


d_road_info_inst = D_ROAD_INFOS_PICKLER()


class DRoadInfosList(dict):
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


class D_ROAD_INFOS_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return DRoadInfosList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DRoadInfosList)


d_road_info_list_inst = D_ROAD_INFOS_LIST_PICKLER()
