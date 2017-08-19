import modem
import random

def sendAtCommand(cmd):
    return modem.sendAtCommand(cmd)

def getCurrentValue(param):
    return sendAtCommand(param).replace("AT%%%s" % param, "").replace("OK", "").strip()

def setNewValue(param, newValue):
    return sendAtCommand(param + "=%s" % newValue)

def luhnResidue(digits):
    return sum(sum(divmod(int(d) * (1 + i % 2), 10)) for i, d in enumerate(digits[::-1])) % 10

def getValidImei():
    part = ''.join(str(random.randrange(0, 9)) for _ in range(14))
    res = luhnResidue('{}{}'.format(part, 0))
    return '{}{}'.format(part, -res % 10)

def getValidMacAddress():
    mac = [0xC4, random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ','.join(''.join(map(lambda x: "%02X" % x, mac)))

def applyUlcw():
    return setNewValue("ULCW", "1,1234567812345678,2,1234567812345678,4,1234567812345678,8,1234567812345678,16,1234567812345678")

def applySlType():
    currentSlType = getCurrentValue("SLTYPE")
    if currentSlType == "0":
        slType = setNewValue("SLTYPE", "1")
    else:
        slType = setNewValue("SLTYPE", "0")
    return slType
