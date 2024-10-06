# RaspberryPi Webserver

In this project, we aim to build a web server using the Raspberry Pi Pico to remotely control an LED module. The Raspberry Pi Pico will host a simple web server, allowing users to toggle the LED on and off through a web browser. The project combines embedded systems with IoT concepts to showcase how low-cost microcontrollers can be used for real-time hardware control via a web interface. 

### Key Components:
1. Raspberry Pi Pico: The microcontroller serves as the central control unit, executing the server-side logic and handling GPIO operations.
2. LED Module: A basic LED connected to the Raspberry Pi Pico’s GPIO pins, acting as the output device.
3. MicroPython: The programming language used to implement the web server and control the hardware.

### Functional Overview:
1. Web Server Setup: The Raspberry Pi Pico will run a lightweight web server written in MicroPython. This server will host a simple web page with buttons for controlling the LED state.
2. LED Control: Users can access the web page from any browser on the network. By pressing the "ON" or "OFF" button on the web page, the Raspberry Pi Pico will receive the request and adjust the LED's state accordingly using its GPIO pins.
3. Real-Time Feedback: The web interface will provide feedback to the user, showing the current status of the LED (either "ON" or "OFF") in real-time.

By using the Raspberry Pi Pico as a web server for controlling an LED, this project demonstrates how microcontrollers can be utilized to interact with physical hardware over a network, laying the groundwork for more complex IoT applications.
