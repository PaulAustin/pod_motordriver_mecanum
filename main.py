def on_received_number(receivedNumber):
    Move(receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    Move(100)
    radio.send_value("power", 100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    Move(0)
    radio.send_value("power", 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Move(-100)
    radio.send_value("power", 100)
input.on_button_pressed(Button.B, on_button_pressed_b)

def Move(num: number):
    basic.show_number(0)
    if num > 0:
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, 100)
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, 100)
    elif num < 0:
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, 100)
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, 100)
    else:
        motor.motor_stop_all()
p = 0
basic.show_icon(IconNames.STICK_FIGURE)
radio.set_group(7)
pins.digital_write_pin(DigitalPin.P14, 1)
pins.digital_write_pin(DigitalPin.P16, 1)

def on_forever():
    global p
    p = 0
    serial.write_numbers([pins.digital_read_pin(DigitalPin.P14),
            pins.digital_read_pin(DigitalPin.P16)])
    pins.digital_write_pin(DigitalPin.P14, 1)
    pins.digital_write_pin(DigitalPin.P16, 1)
basic.forever(on_forever)
