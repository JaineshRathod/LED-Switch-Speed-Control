# LED-Switch-Speed-Control

Here I have uploaded 2 codes, 1 for Arduino(Any Version) and the other for Raspberry Pi(Any Version). The main aim of the project is to connect and control LED's using the keyboard inputs. So, you can control the LED's using the following menu in the code:

1. LED Switch Speed Control (Title).
2. Press '1' to select LED 1.
3. Press '2' to select LED 2.
4. Press '3' to select LED 3.
5. Press '4' to select LED 4.
6. Press '+' to Increase LED Speed.
7. Press '-' to Decrease LED Speed.
8. Press '0' to Turn OFF selected LED.
9. Press '.' to TURN OFF all LEDs.

The code doesnot uses delay() for Arduino and timer() for Raspberry Pi, instead it uses millis() for Arduino and threading() for Raspberry Pi. You can use delay()/timer() also or challenge yourself by trying to use the concept of interrupts in the same code.

Now, the project is for beginners who are starting to learn interfacing of Arduino or Raspberry Pi. You just have to connect 4 LED's with your Arduino/RPi board, upload the code and then you are ready to control the LED's using your keyboard.

The practical implementation of the video can be seen [here](https://youtu.be/NS8_LTwasKA).

