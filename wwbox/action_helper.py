has = "has"


def value(in_data):
    vtype = ""
    data = in_data

    if type(in_data) is str:
        vtype = "s"

    elif type(in_data) is bool:
        vtype = "b"

    elif type(in_data) is int:
        vtype = "i"

    elif type(in_data) is dict:
        if "effectname" in in_data:
            vtype = "e"
        elif "getter" in in_data:
            vtype = "p"

    out = {}
    out["type"] = vtype
    out["data"] = data
    return out


# poll data
def pd(targets, txt, players):
    out = {}
    out["targets"] = targets
    out["txt"] = txt
    out["players"] = players
    return out


def player(getter, data=None, oo=False):
    out = {}
    out["onlyone"] = oo
    if getter == "self" or getter == "saved":
        out["getter"] = getter
	
    elif getter == "role" or getter == "team" or getter == "status" or getter == "poll":
        out["getter"] = getter
        out["data"] = data

    elif getter.startswith("effect"):
        out["getter"] = "effect"
        data_out = {}
        sg = getter.split(" ")
        data_out["name"] = sg[1]
        data_out["operator"] = sg[2]

        if sg[2] == "has" or sg[2] == "equals":
            data_out["value"] = value(data)

        out["data"] = data_out

    return out


def effect(player, effectname):
    out = {}
    out["player"] = player
    out["effectname"] = effectname
    return out


def playsound(location):
    out = {}
    out["id"] = "playsound"
    out["attributes"] = [value(location)]
    return out

def saveplayer(player):
    out = {}
    out["id"] = "saveplayer"
    out["attributes"] = [value(player)]
    return out


def directkill(player):
    out = {}
    out["id"] = "dk"
    out["attributes"] = [value(player)]
    return out


def addeffect(players, effectname, evalue):
    out = {}
    out["id"] = "ae"
    out["attributes"] = [value(players), value(effectname), value(evalue)]
    return out


def append_to_effect(player,effectname,key,value):
    out = {}
    out["id"]="ate"
    out["attributes"]=[effectname,key,value]
    return out


def executeaction(action_id,players):
    out = {}
    out["id"] = "executeaction"
    out["attributes"] = [value(action_id),players]
    return out

def removeeffect(player, effectname):
    out = {}
    out["id"] = "rme"
    out["attributes"] = [value(player), value(effectname)]
    return out


def sendinfo(player, txt, img=""):
    out = {}
    out["id"] = "si"
    out["attributes"] = [value(player), value(txt), value(img)]
    return out


def condition(v1, o, v2):
    return [value(v1), o, value(v2)]


def action(conditions, commands):
    out = {}
    out["conditions"] = conditions
    out["commands"] = commands
    return out








'''
Action abstimmung der Wölfe

'''




print(action([
    condtion(effect(player("self"),"attacked by"),has,"Werewolves")
], [
    sendinfo(player("status", 2), "Hört hört"),
    playsound("sound.wav")]))
#Ausgabe:
'''
{'conditions': [
    [{'type': 'e', 'data': {'player': {'onlyone': False, 'getter': 'self'}, 'effectname': 'attacked by'}}, 'has', {'type': 's', 'data': 'Werewolves'}]
], 'commands': [
    {'id': 'si', 'attributes': [
        {'type': 'p', 'data': {'onlyone': False, 'getter': 'status', 'data': 2}}, 
        {'type': 's', 'data': 'Hört hört'},
        {'type': 's', 'data': ''}]}, 
    {'id': 'playsound', 'attributes': [
        {'type': 's', 'data': 'sound.wav'}]}]}
'''