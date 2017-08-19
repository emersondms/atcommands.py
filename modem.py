import serial
import serial.tools.list_ports
import time

ser = serial.Serial()

def getNumberOfUsbModemsConnected():
    ports = list(serial.tools.list_ports.comports())
    modemsConnected = 0
    for comPort, description, address in ports:
        if 'USB' in description:
            modemsConnected += 1
    return modemsConnected

def getComPortsAvailable():
    comPortsAvailable = []
    for port in range(400):
        try:
            ser = serial.Serial(port)
            comPortsAvailable.append((port))
            ser.close()
        except serial.SerialException:
            pass
    return comPortsAvailable

def getConnectedComPort():
    for port in range(len(getComPortsAvailable())):
        connectedComPort = getComPortsAvailable()[port]
        try:
            ser = serial.Serial(connectedComPort, timeout=1)
            ser.write("AT\r")
            time.sleep(0.5)
            result = ser.read()
            ser.close()
            if result != "":
                return connectedComPort
        except:
            pass

def sendAtCommand(cmd):
    ser.port = getConnectedComPort()
    if not ser.isOpen(): ser.open()
    ser.write("AT%" +cmd+ "\r")
    time.sleep(0.5)
    result = ser.read(ser.inWaiting()).replace("", "").replace("", "")
    ser.close()
    return result
