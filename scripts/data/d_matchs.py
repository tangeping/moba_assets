# -*- coding: utf-8 -*-
matchRuleDatas={
    100001:{'id':100001,'utype': 'player' ,'name':'5v5','teamACount':5,'teamBCount':5,'minPlayers':10,'maxPlayers':10},
    100002:{'id':100002,'utype': 'player' ,'name':'1v1','teamACount':1,'teamBCount':1,'minPlayers':2,'maxPlayers':10},
    100003:{'id':100003,'utype': 'player' ,'name':'3v3','teamACount':3,'teamBCount':3,'minPlayers':6,'maxPlayers':10},
    100004:{'id':100004,'utype': 'npc' ,'name':'3v3','teamACount':3,'teamBCount':3,'minPlayers':6,'maxPlayers':10},
    100005:{'id':100005,'utype': 'npc' ,'name':'3v3','teamACount':3,'teamBCount':3,'minPlayers':6,'maxPlayers':10},
    100006:{'id':100006,'utype': 'npc' ,'name':'3v3','teamACount':3,'teamBCount':3,'minPlayers':6,'maxPlayers':10},
    100007:{'id':100007,'utype': 'customize' ,'name':'3v3','teamACount':3,'teamBCount':3,'minPlayers':6,'maxPlayers':10},
    100008:{'id':100008,'utype': 'customize' ,'name':'3v3','teamACount':3,'teamBCount':3,'minPlayers':6,'maxPlayers':10},
    100009:{'id':100009,'utype': 'customize' ,'name':'3v3','teamACount':3,'teamBCount':3,'minPlayers':6,'maxPlayers':10},
}

roomRuleDatas={
    1001:{'id':1001,'roomType':'SummonerCanyon','name':'召唤师峡谷','resPath': 'terrains/SummonerCanyon'},
    1002:{'id':1002,'roomType':'TwistedJungle','name':'扭曲丛林','resPath': 'terrains/TwistedJungle'},
    1003:{'id':1003,'roomType':'PolarChaos','name':'极地大乱斗','resPath': 'terrains/PolarChaos'},
    1004:{'id':1004,'roomType':'CryingAbyss','name':'嚎哭深渊','resPath': 'terrains/CryingAbyss'},
}

datas = {
    10001:{'id':10001,'matchRule':100002,'roomRule':1001},
    10002:{'id':10002,'matchRule':100001,'roomRule':1002},
    10003:{'id':10003,'matchRule':100001,'roomRule':1003},
    10004:{'id':10004,'matchRule':100002,'roomRule':1004},
}