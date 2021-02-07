# Sunrise Lamp

DIY sunrise lamp using a Raspberry Pi, Some LEDS and a Flask web application

Raspberry pi is set up as an Nginx server, following [this digital ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)

The flask app allows the settings of the alarm to be changed on a local network, as well as controlling the lamp remotely.

Eat your heart out Lumie

## TODO
-web design for setting an alarm
    -sqlite3 database for storing alarms
    -deleting or overwriting?
-set brightness/colour when selecting on/off (RBG light)
    -sliding scale for brightness, then press on/update
    -need something to hold the state of the lamp and affect webpage (fade out buttons/set slider etc.) (database?)
-authentication/login page to control lamp?

