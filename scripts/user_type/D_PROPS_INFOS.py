# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class DPropsInfos(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "prop_id": self[0],
            "prop_name": self[1],
            "prop_icon": self[2],
            "prop_type": self[3],
            "prop_quality": self[4],
            "prop_order": self[5],
            "prop_max": self[6],
            "prop_resale": self[7],
            "prop_diamond": self[8],
            "prop_hanbing": self[9],
            "prop_moba": self[10],
            "prop_jjc": self[11],
            "prop_maoxian": self[12],
            "prop_describe": self[13],
            "prop_function": self[14],
            "prop_parameters1": self[15],
            "prop_parameters2": self[16],
            "prop_parameters3": self[17],
            "prop_parameters4": self[18],
            "prop_parameters5": self[19],
            "prop_parameters6": self[20],
            "prop_drop1": self[21],
            "prop_drop2": self[22],
            "prop_drop3": self[23],
            "prop_drop4": self[24],
            "prop_gm": self[25],
            "prop_buy": self[26]
        }
        return data

    def createFromDict(self, d):
        self.extend([
            d["prop_id"], d["prop_name"], d["prop_icon"], d["prop_type"], d["prop_quality"],
            d["prop_order"], d["prop_max"], d["prop_resale"], d["prop_diamond"], d["prop_hanbing"],
            d["prop_moba"], d["prop_jjc"], d["prop_maoxian"], d["prop_describe"], d["prop_function"],
            d["prop_parameters1"], d["prop_parameters2"], d["prop_parameters3"], d["prop_parameters4"],
            d["prop_parameters5"], d["prop_parameters6"], d["prop_drop1"], d["prop_drop2"], d["prop_drop3"], d["prop_drop4"],
            d["prop_gm"], d["prop_buy"]
        ])
        return self


class D_PROPS_INFOS_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return DPropsInfos().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DPropsInfos)


d_props_info_inst = D_PROPS_INFOS_PICKLER()


class DPropsInfosList(dict):
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


class D_PROPS_INFOS_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return DPropsInfosList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DPropsInfosList)


d_props_info_list_inst = D_PROPS_INFOS_LIST_PICKLER()
