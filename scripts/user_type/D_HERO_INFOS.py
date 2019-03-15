# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class DHeroInfos(list):
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
            "nick_name": self[2],
            "race": self[3],
            "race_desc": self[4],
            "skill_1": self[5],
            "skill_2": self[6],
            "skill_3": self[7],
            "skill_4": self[8],
            "hero_hp": self[9],
            "hero_mp": self[10],
            "hero_strength": self[11],
            "hero_agile": self[12],
            "hero_intelligence": self[13],
            "hero_attacktime": self[14],
            "hero_speed": self[15],
            "hero_attackfront": self[16],
            "hero_attackback": self[17],
            "hero_skillfront": self[18],
            "hero_skillback": self[19],
            "hero_scope": self[20],
            "hero_attack": self[21],
            "hero_armor": self[22],
            "hero_unarmor": self[23],
            "hero_magic": self[24],
            "hero_magicresist": self[25],
            "hero_hprestored": self[26],
            "hero_mprestored": self[27],
            "hero_crit": self[28],
            "hero_uncrit": self[29],
            "hero_critunmber": self[30],
            "hero_evade": self[31],
            "hero_unevade": self[32],
            "hero_parry": self[33],
            "hero_unparry": self[34],
            "hero_parrynumber": self[35],
            "hero_xixue": self[36],
            "atk_power": self[37],
            "hurt_power": self[38],
            "kill_power": self[39],
            "hero_energe": self[40],
            "head_icon":self[41]
        }
        return data

    def createFromDict(self, d):
        self.extend([
            d["id"], d["name"], d["nick_name"], d["race"], d["race_desc"],
            d["skill_1"], d["skill_2"], d["skill_3"], d["skill_4"], d["hero_hp"],
            d["hero_mp"], d["hero_strength"], d["hero_agile"], d["hero_intelligence"], d["hero_attacktime"],
            d["hero_speed"], d["hero_attackfront"], d["hero_attackback"], d["hero_skillfront"], d["hero_skillback"],
            d["hero_scope"], d["hero_attack"], d["hero_armor"], d["hero_unarmor"], d["hero_magic"],
            d["hero_magicresist"], d["hero_hprestored"], d["hero_mprestored"], d["hero_crit"], d["hero_uncrit"],
            d["hero_critunmber"], d["hero_evade"], d["hero_unevade"], d["hero_parry"], d["hero_unparry"],
            d["hero_parrynumber"], d["hero_xixue"], d["atk_power"], d["hurt_power"], d["kill_power"],
            d["hero_energe"],d["head_icon"]
        ])
        return self


class D_HERO_INFOS_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return DHeroInfos().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DHeroInfos)


d_hero_info_inst = D_HERO_INFOS_PICKLER()


class DHeroInfosList(dict):
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


class D_HERO_INFOS_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return DHeroInfosList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DHeroInfosList)


d_hero_info_list_inst = D_HERO_INFOS_LIST_PICKLER()
