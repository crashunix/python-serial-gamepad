import vgamepad as vg
import time
import serial
import keyboard

ser = serial.Serial(port = 'COM6', baudrate = 9600, timeout = 10)
if not ser.isOpen():
    ser.open()

running = True

gamepad = vg.VX360Gamepad()

def potToAxis():
    val = (float(ser.readline()) / 1023)
    return val

while running:
    print(potToAxis())
    if potToAxis() > 0.1:
        # gamepad.right_joystick_float(x_value_float=potToAxis(), y_value_float=0)
        gamepad.left_trigger_float(value_float=potToAxis())
        gamepad.update()