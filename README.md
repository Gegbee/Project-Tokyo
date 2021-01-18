# Project Tokyo
Project Tokyo is a passion project by programmer and robotics enjoyer Greg Baldwin.

### What is Project Tokyo?
An **RC car** but with a *twist*. Instead of using the normie techniques of most RC car manufacturers, I decided to think outside of the box.

Specifically, I eliminated the option of using a servo to rotate the wheels allowing the car to turn. Instead, I programmed a script (keyboardCommands.py) to take in controller input and output values (to each of my two DC motors) that would emulate steering and speed of an RC car. In essence, this gave me much higher control over the RC car because I could change different variables to allow the car to turn faster or slower, have a larger or smaller turn radius, and accelerate at different speeds.

### The parts I am using:

- Arduino Uno
- L298N motor controller
- Two DC Motors
- 9V battery
- HC-05 Bluetooth module (to be swapped out with a radio transmitter and reciever later on)

### The software I am using:

- VSCode
- Arduino IDE
- *pygame* library for Python
- *serial* library for Python
