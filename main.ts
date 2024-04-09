radio.onReceivedNumber(function (receivedNumber) {
    Move(receivedNumber)
})
input.onButtonPressed(Button.A, function () {
    Move(100)
    radio.sendValue("power", 100)
})
input.onButtonPressed(Button.AB, function () {
    Move(0)
    radio.sendValue("power", 0)
})
input.onButtonPressed(Button.B, function () {
    Move(-100)
    radio.sendValue("power", 100)
})
function Move (num: number) {
    basic.showNumber(0)
    if (num > 0) {
        motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 100)
        motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 100)
    } else if (num < 0) {
        motor.MotorRun(motor.Motors.M1, motor.Dir.CCW, 100)
        motor.MotorRun(motor.Motors.M1, motor.Dir.CCW, 100)
    } else {
        motor.motorStopAll()
    }
}
let p = 0
basic.showIcon(IconNames.StickFigure)
radio.setGroup(7)
pins.digitalWritePin(DigitalPin.P14, 1)
pins.digitalWritePin(DigitalPin.P16, 1)
basic.forever(function () {
    p = 0
    serial.writeNumbers([pins.digitalReadPin(DigitalPin.P14), pins.digitalReadPin(DigitalPin.P16)])
    pins.digitalWritePin(DigitalPin.P14, 1)
    pins.digitalWritePin(DigitalPin.P16, 1)
})
