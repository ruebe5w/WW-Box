conditions = [c, c, c]
commands = [c, c, c, c]


def testConditions(conditions):
    for c in conditions:
        if testCondition(c) == False:
            return False

    return True


def testCondition(condition):
    v1 = getValue(condition[0])
    v2 = getValue(condition[2])
    if condition[1] == "=":
        return v1 == v2;
    # TODO


def getValue(valueKey):
    type = valueKey["type"]
    if type == "e":
        return getEffect(valueKey["data"])
    if type == "p":
        return getPlayer(valueKey["data"])
    if type == "s":
        return valueKey["data"]
    # TODO


def getEffect(effectKey):
    player = getPlayer(effectKey["player"])
    effectName = effectKey["effectname"]
    # TODO


def getPlayer(playerKey):
    getter = playerKey["getter"]
    data = playerKey["data"]
    oo = False;
    if "onlyone" in playerKey:
        oo = playerKey["onlyone"]

    if getter == "self":


# TODO

def executeCommands(commands):
    for c in commands:
        executeCommand(c)


def executeCommand(command):
    id = command["id"]
    attributes = []
    for v in command["attributes"]:
        attributes.append(getValue(v))
    game.command_switch(id, attributes)
