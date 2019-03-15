# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class DShopInfos(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "shop_id": self[0],
            "shop_des": self[1],
            "shop_refreshstart": self[2],
            "shop_refreshtime": self[3],
            "shop_needid": self[4],
            "shop_needdes": self[5],
            "shop_amount": self[6],
            "shop_refreshtime1": self[7],
            "open_lv": self[8]
        }
        return data

    def createFromDict(self, d):
        self.extend([
            d["shop_id"], d["shop_des"], d["shop_refreshstart"], d["shop_refreshtime"], d["shop_needid"],
            d["shop_needdes"], d["shop_amount"], d["shop_refreshtime1"], d["open_lv"]
        ])
        return self


class D_SHOP_INFOS_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return DShopInfos().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DShopInfos)


d_shop_info_inst = D_SHOP_INFOS_PICKLER()


class DShopInfosList(dict):
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


class D_SHOP_INFOS_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return DShopInfosList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, DShopInfosList)


d_shop_info_list_inst = D_SHOP_INFOS_LIST_PICKLER()
