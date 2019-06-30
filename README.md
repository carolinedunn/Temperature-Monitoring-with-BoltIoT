# Temperature-Monitoring-with-BoltIoT

This project uses the [BoltIoT Starter Kit](https://www.boltiot.com/) with included temperature sensor to monitor the temperature and send an SMS and email when there is a change in temperature. The email is sent via [Mailgun](https://www.mailgun.com/), and the text is sent via [Twilio](https://www.twilio.com/). Mailgun requires a credit card to create an account.

Disclaimer: I am not a data scientist, and the formula I am using to calculate temp variations was pulled from here: https://www.hackster.io/iambishal/temperature-monitoring-alert-system-using-bolt-iot-98e7b9
## Materials

For this project, you will need:
- [BoltIoT Starter Kit](https://amzn.to/2ZXAb78), if you do not have a starter kit, you may need to purchase an LM35 IC and 3 male to female jumper cables.
- [Raspberry Pi 3B+ Kit](https://amzn.to/2xmFWiu) This project uses a Raspberry Pi 3B+ to continuously run a Python script. You can always use your existing computer instead of a Raspberry Pi, but your computer will need to be on and running this Python script for the project to work.
- [HDMI Monitor](https://amzn.to/2RH15gw)
or [Raspberry Pi Touchscreen](https://amzn.to/2ZScux4)
- [Mouse/Keyboard](https://amzn.to/2FHZvGK)

## Prerequisites

Before you begin, you will need:
1. Raspberry Pi 3B+ setup with HDMI monitor, mouse/keyboard, and the latest copy of Raspbian OS installed.
2. [Mailgun](https://www.mailgun.com/) account. You will need a Mailgun API Key and Sandbox URL for this project. Mailgun requires a valid credit card to create an account.
3. [Twilio](https://www.twilio.com/) account. You will need a Twillio SSID, Auth Token, and 'From Number' for this project.
4. [BoltIoT](https://www.boltiot.com/) account and [Bolt WiFi Module](https://docs.boltiot.com/docs/setting-up-the-bolt-wifi-module). You will need your API Key and Device ID for this project.
 

## Hardware Assembly
Follow the instructions from the BoltIoT page here: https://docs.boltiot.com/docs/getting-started-with-bolt-temperature-monitoring-system to connect the BoltIoT to the temperature senso with 3 male to female jumper wires.

Follow Schematic Here:

![schematic](https://files.readme.io/bc01f10-3.jpeg)

In the end your hardware setup for your BoltIoT should look like this:

![hardware](https://files.readme.io/bc4efe5-10.jpg)

## Connecting the temp sensor and reporting to the BoltIoT Cloud

Next, you'll need to setup the BoltIoT to read and report temperature readings from the LC35 IC to the [BoltIoT Cloud](https://cloud.boltiot.com) by following the instructions here: https://docs.boltiot.com/docs/getting-started-with-bolt-temperature-monitoring-system#section-step-3-visualising-the-data-plotting-graph-on-the-bolt-cloud

When you complete this step. you should see a blank output plot:

![blank output plot](https://files.readme.io/ce38845-27.jpeg)

After a few hours, you'll see something like this:

![output plot](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/graph.png)

Side Note: I prefer to see everything in Farenheit, so I followed the additional instructions on the tutorial for converting Temperature reading to Farenheit.

Here's what my product code looked like when I was done:
```
setChartLibrary('google-chart');
setChartTitle('Your Graph Title');
setChartType('lineGraph');
add(183);
mul(0.0977);
mul(1.8);
setAxisName('time_stamp','temp');
plotChart('time_stamp','temp');
```

![product code](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/product-code.png)

## Python Software Installation and conf.py

In this section, we will clone the code onto our Raspberry Pi into folder Temperature-Monitoring-with-BoltIot.

Start by opening a command terminal:

```
git clone https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT
```
Next cd into the folder:

```
cd Temperature-Monitoring-with-BoltIoT
```

Your terminal should look something like this:

![terminal after git clone](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/terminalcd.png)

Next, open a File Manager on your Raspberry Pi desktop and find the folder Temperature-Monitoring-with-BoltIot.

![file manager](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/conf-fm.png)

Double-click to open the conf.py file in Geany. Geany should be the default editor.

![confpy](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/conf-screenshot.png)

Now replace all "xxx" values in the conf.py file with the actual values for your accounts.
For example, replace SSID = 'ACIxxxx' with the actual SSID from your Twilio account.

You will need credentials from your Twillio, BoltIoT Cloud, your mobile number, and Mailgun account.

When you have completed this task, you will need to save your conf.py file.

Next go back to your terminal. You will need to install dependencies now.


```
sudo pip install boltiot
sudo pip install statistics
```

After installing all required dependencies, you will need to make your detection.py file executable and then run the file.

```
chmod +x detection.py
python ./detection.py
```

If you've done everything correctly, you should start to see the collection of data in the terminal window.
Once 4 temperatures have been captured, if the temperature is ouside the range of the upper or lower bounds, this will trigger an email and a SMS message as you have set it up in the conf.py file.

Here is what the terminal could look like:

![confpy](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/terminal1.png)

Here is an example of a series text messages:

![confpy](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/sms-example.png)

Here is an example of an email generated by Mailgun:

![confpy](https://github.com/carolinedunn/Temperature-Monitoring-with-BoltIoT/blob/master/images4readme/mailgun.png)


### And coding style tests

Explain what these tests test and why

```

Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
