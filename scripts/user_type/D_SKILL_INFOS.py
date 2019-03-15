# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class DSkillInfos(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "id": self[0],
            "name": self[1],
            "skill_icon": self[2],
            "skill_damage_chushi": self[3],
            "skill_damage_growth": self[4],
            "skill_ad_chushi": self[5],
            "skill_ad_growth": self[6],
            "skill_ap_chushi": self[7],
            "skill_ap_growth": self[8],
            "skill_type": self[9],
            "skill_ongoing": self[10],
            "skill_sing_time": self[11],
            "skill_cutdown": self[12],
            "skill_cutdownif": self[13],
            "skill_cd": self[14],
            "attack_distance":self[15],
            "aoe_radius":self[16]
        }
        return data

    def createFromDict(self, d):
        self.extend([
            d["id"], d["name"], d["skill_icon"], d["skill_damage_chushi"], d["skill_damage_growth"],
            d["skill_ad_chushi"], d["skill_ad_growth"], d["skill_ap_chushi"], d["skill_ap_growth"], d["skill_type"],
            d["skill_ongoing"], d["skill_sing_time"], d["skill_cutdown"], d["skill_cutdownif"], d["skill_cd"],
            d["attack_distance"],d["aoe_radius"]
        ])
        return self


class D_SKILL_INFOS_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return DSkillInfos().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DSkillInfos)


d_skill_info_inst = D_SKILL_INFOS_PICKLER()


class DSkillInfosList(dict):
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


class D_SKILL_INFOS_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return DSkillInfosList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DSkillInfosList)


d_skill_info_list_inst = D_SKILL_INFOS_LIST_PICKLER()
