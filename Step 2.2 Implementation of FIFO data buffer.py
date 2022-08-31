import RPi.GPIO as RPi
import dht11
import time
import json
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from statistics import mean

RPi.setwarnings(False)
RPi.setmode(RPi.BCM)
RPi.cleanup()

HumidityJSON = '{"channel":{"id":628559,"name":"AirMonitor_e9bb","latitude":"0.0","longitude":"0.0","field1":"PM1.0 (ATM)","field2":"PM2.5 (ATM)","field3":"PM10.0 (ATM)","field4":"Uptime","field5":"RSSI","field6":"Temperature","field7":"Humidity","field8":"PM2.5 (CF=1)","created_at":"2018-11-15T23:39:47Z","updated_at":"2019-03-20T17:03:58Z","last_entry_id":634553},"feeds":[{"created_at":"2022-08-03T18:14:41Z","entry_id":634454,"field7":"29"},{"created_at":"2022-08-03T18:16:41Z","entry_id":634455,"field7":"29"},{"created_at":"2022-08-03T18:18:41Z","entry_id":634456,"field7":"30"},{"created_at":"2022-08-03T18:20:41Z","entry_id":634457,"field7":"30"},{"created_at":"2022-08-03T18:22:41Z","entry_id":634458,"field7":"30"},{"created_at":"2022-08-03T18:24:41Z","entry_id":634459,"field7":"29"},{"created_at":"2022-08-03T18:26:41Z","entry_id":634460,"field7":"29"},{"created_at":"2022-08-03T18:28:41Z","entry_id":634461,"field7":"29"},{"created_at":"2022-08-03T18:30:41Z","entry_id":634462,"field7":"29"},{"created_at":"2022-08-03T18:32:41Z","entry_id":634463,"field7":"29"},{"created_at":"2022-08-03T18:34:41Z","entry_id":634464,"field7":"29"},{"created_at":"2022-08-03T18:36:41Z","entry_id":634465,"field7":"29"},{"created_at":"2022-08-03T18:38:41Z","entry_id":634466,"field7":"30"},{"created_at":"2022-08-03T18:40:41Z","entry_id":634467,"field7":"30"},{"created_at":"2022-08-03T18:42:41Z","entry_id":634468,"field7":"29"},{"created_at":"2022-08-03T18:44:41Z","entry_id":634469,"field7":"29"},{"created_at":"2022-08-03T18:46:41Z","entry_id":634470,"field7":"29"},{"created_at":"2022-08-03T18:48:41Z","entry_id":634471,"field7":"29"},{"created_at":"2022-08-03T18:50:41Z","entry_id":634472,"field7":"29"},{"created_at":"2022-08-03T18:52:41Z","entry_id":634473,"field7":"29"},{"created_at":"2022-08-03T18:54:41Z","entry_id":634474,"field7":"29"},{"created_at":"2022-08-03T18:56:41Z","entry_id":634475,"field7":"29"},{"created_at":"2022-08-03T18:58:43Z","entry_id":634476,"field7":"28"},{"created_at":"2022-08-03T19:00:41Z","entry_id":634477,"field7":"28"},{"created_at":"2022-08-03T19:02:41Z","entry_id":634478,"field7":"28"},{"created_at":"2022-08-03T19:04:41Z","entry_id":634479,"field7":"28"},{"created_at":"2022-08-03T19:06:41Z","entry_id":634480,"field7":"28"},{"created_at":"2022-08-03T19:08:41Z","entry_id":634481,"field7":"28"},{"created_at":"2022-08-03T19:10:43Z","entry_id":634482,"field7":"28"},{"created_at":"2022-08-03T19:12:41Z","entry_id":634483,"field7":"28"},{"created_at":"2022-08-03T19:14:41Z","entry_id":634484,"field7":"28"},{"created_at":"2022-08-03T19:16:41Z","entry_id":634485,"field7":"27"},{"created_at":"2022-08-03T19:18:41Z","entry_id":634486,"field7":"27"},{"created_at":"2022-08-03T19:20:41Z","entry_id":634487,"field7":"29"},{"created_at":"2022-08-03T19:22:41Z","entry_id":634488,"field7":"29"},{"created_at":"2022-08-03T19:24:41Z","entry_id":634489,"field7":"29"},{"created_at":"2022-08-03T19:26:41Z","entry_id":634490,"field7":"30"},{"created_at":"2022-08-03T19:28:41Z","entry_id":634491,"field7":"30"},{"created_at":"2022-08-03T19:30:41Z","entry_id":634492,"field7":"30"},{"created_at":"2022-08-03T19:32:41Z","entry_id":634493,"field7":"31"},{"created_at":"2022-08-03T19:34:41Z","entry_id":634494,"field7":"31"},{"created_at":"2022-08-03T19:36:41Z","entry_id":634495,"field7":"31"},{"created_at":"2022-08-03T19:38:41Z","entry_id":634496,"field7":"31"},{"created_at":"2022-08-03T19:40:41Z","entry_id":634497,"field7":"31"},{"created_at":"2022-08-03T19:42:43Z","entry_id":634498,"field7":"31"},{"created_at":"2022-08-03T19:44:41Z","entry_id":634499,"field7":"31"},{"created_at":"2022-08-03T19:46:41Z","entry_id":634500,"field7":"32"},{"created_at":"2022-08-03T19:48:41Z","entry_id":634501,"field7":"31"},{"created_at":"2022-08-03T19:50:41Z","entry_id":634502,"field7":"31"},{"created_at":"2022-08-03T19:52:41Z","entry_id":634503,"field7":"31"},{"created_at":"2022-08-03T19:54:41Z","entry_id":634504,"field7":"31"},{"created_at":"2022-08-03T19:56:41Z","entry_id":634505,"field7":"30"},{"created_at":"2022-08-03T19:58:41Z","entry_id":634506,"field7":"28"},{"created_at":"2022-08-03T20:00:41Z","entry_id":634507,"field7":"28"},{"created_at":"2022-08-03T20:02:41Z","entry_id":634508,"field7":"28"},{"created_at":"2022-08-03T20:04:41Z","entry_id":634509,"field7":"28"},{"created_at":"2022-08-03T20:06:41Z","entry_id":634510,"field7":"28"},{"created_at":"2022-08-03T20:08:41Z","entry_id":634511,"field7":"28"},{"created_at":"2022-08-03T20:10:41Z","entry_id":634512,"field7":"28"},{"created_at":"2022-08-03T20:12:41Z","entry_id":634513,"field7":"27"},{"created_at":"2022-08-03T20:14:41Z","entry_id":634514,"field7":"28"},{"created_at":"2022-08-03T20:16:41Z","entry_id":634515,"field7":"28"},{"created_at":"2022-08-03T20:18:41Z","entry_id":634516,"field7":"30"},{"created_at":"2022-08-03T20:20:41Z","entry_id":634517,"field7":"30"},{"created_at":"2022-08-03T20:22:41Z","entry_id":634518,"field7":"29"},{"created_at":"2022-08-03T20:24:41Z","entry_id":634519,"field7":"30"},{"created_at":"2022-08-03T20:26:41Z","entry_id":634520,"field7":"29"},{"created_at":"2022-08-03T20:28:43Z","entry_id":634521,"field7":"28"},{"created_at":"2022-08-03T20:30:41Z","entry_id":634522,"field7":"29"},{"created_at":"2022-08-03T20:32:41Z","entry_id":634523,"field7":"29"},{"created_at":"2022-08-03T20:34:41Z","entry_id":634524,"field7":"29"},{"created_at":"2022-08-03T20:36:41Z","entry_id":634525,"field7":"29"},{"created_at":"2022-08-03T20:38:41Z","entry_id":634526,"field7":"29"},{"created_at":"2022-08-03T20:40:41Z","entry_id":634527,"field7":"29"},{"created_at":"2022-08-03T20:42:41Z","entry_id":634528,"field7":"29"},{"created_at":"2022-08-03T20:44:41Z","entry_id":634529,"field7":"28"},{"created_at":"2022-08-03T20:46:41Z","entry_id":634530,"field7":"29"},{"created_at":"2022-08-03T20:48:41Z","entry_id":634531,"field7":"30"},{"created_at":"2022-08-03T20:50:41Z","entry_id":634532,"field7":"30"},{"created_at":"2022-08-03T20:52:41Z","entry_id":634533,"field7":"30"},{"created_at":"2022-08-03T20:54:41Z","entry_id":634534,"field7":"32"},{"created_at":"2022-08-03T20:56:41Z","entry_id":634535,"field7":"32"},{"created_at":"2022-08-03T20:58:41Z","entry_id":634536,"field7":"32"},{"created_at":"2022-08-03T21:00:41Z","entry_id":634537,"field7":"33"},{"created_at":"2022-08-03T21:02:41Z","entry_id":634538,"field7":"33"},{"created_at":"2022-08-03T21:04:41Z","entry_id":634539,"field7":"34"},{"created_at":"2022-08-03T21:06:41Z","entry_id":634540,"field7":"34"},{"created_at":"2022-08-03T21:08:41Z","entry_id":634541,"field7":"34"},{"created_at":"2022-08-03T21:10:41Z","entry_id":634542,"field7":"34"},{"created_at":"2022-08-03T21:12:41Z","entry_id":634543,"field7":"34"},{"created_at":"2022-08-03T21:14:41Z","entry_id":634544,"field7":"34"},{"created_at":"2022-08-03T21:16:41Z","entry_id":634545,"field7":"35"},{"created_at":"2022-08-03T21:18:41Z","entry_id":634546,"field7":"35"},{"created_at":"2022-08-03T21:20:41Z","entry_id":634547,"field7":"35"},{"created_at":"2022-08-03T21:22:41Z","entry_id":634548,"field7":"36"},{"created_at":"2022-08-03T21:24:41Z","entry_id":634549,"field7":"37"},{"created_at":"2022-08-03T21:26:41Z","entry_id":634550,"field7":"37"},{"created_at":"2022-08-03T21:28:41Z","entry_id":634551,"field7":"37"},{"created_at":"2022-08-03T21:30:41Z","entry_id":634552,"field7":"38"},{"created_at":"2022-08-03T21:32:41Z","entry_id":634553,"field7":"37"}]}'
Humidity = json.loads(HumidityJSON)
x7 = []
y7 = []
for i in Humidity["feeds"]:
    y7 = y7 + [float(i["field7"])]
    x7 = x7 + [Humidity["feeds"].index(i)]
    humidity = [round(a, 2) for a in y7]
print("Humidity Sensor readings:")
print(humidity)
meanvalueHumidity = (mean(y7))
print(meanvalueHumidity)

temperatureJSON = '{"channel":{"id":628559,"name":"AirMonitor_e9bb","latitude":"0.0","longitude":"0.0","field1":"PM1.0 (ATM)","field2":"PM2.5 (ATM)","field3":"PM10.0 (ATM)","field4":"Uptime","field5":"RSSI","field6":"Temperature","field7":"Humidity","field8":"PM2.5 (CF=1)","created_at":"2018-11-15T23:39:47Z","updated_at":"2019-03-20T17:03:58Z","last_entry_id":634552},"feeds":[{"created_at":"2022-08-03T18:12:40Z","entry_id":634453,"field6":"103"},{"created_at":"2022-08-03T18:14:41Z","entry_id":634454,"field6":"102"},{"created_at":"2022-08-03T18:16:41Z","entry_id":634455,"field6":"102"},{"created_at":"2022-08-03T18:18:41Z","entry_id":634456,"field6":"102"},{"created_at":"2022-08-03T18:20:41Z","entry_id":634457,"field6":"102"},{"created_at":"2022-08-03T18:22:41Z","entry_id":634458,"field6":"103"},{"created_at":"2022-08-03T18:24:41Z","entry_id":634459,"field6":"102"},{"created_at":"2022-08-03T18:26:41Z","entry_id":634460,"field6":"103"},{"created_at":"2022-08-03T18:28:41Z","entry_id":634461,"field6":"103"},{"created_at":"2022-08-03T18:30:41Z","entry_id":634462,"field6":"103"},{"created_at":"2022-08-03T18:32:41Z","entry_id":634463,"field6":"103"},{"created_at":"2022-08-03T18:34:41Z","entry_id":634464,"field6":"102"},{"created_at":"2022-08-03T18:36:41Z","entry_id":634465,"field6":"102"},{"created_at":"2022-08-03T18:38:41Z","entry_id":634466,"field6":"102"},{"created_at":"2022-08-03T18:40:41Z","entry_id":634467,"field6":"103"},{"created_at":"2022-08-03T18:42:41Z","entry_id":634468,"field6":"103"},{"created_at":"2022-08-03T18:44:41Z","entry_id":634469,"field6":"103"},{"created_at":"2022-08-03T18:46:41Z","entry_id":634470,"field6":"103"},{"created_at":"2022-08-03T18:48:41Z","entry_id":634471,"field6":"103"},{"created_at":"2022-08-03T18:50:41Z","entry_id":634472,"field6":"102"},{"created_at":"2022-08-03T18:52:41Z","entry_id":634473,"field6":"103"},{"created_at":"2022-08-03T18:54:41Z","entry_id":634474,"field6":"103"},{"created_at":"2022-08-03T18:56:41Z","entry_id":634475,"field6":"103"},{"created_at":"2022-08-03T18:58:43Z","entry_id":634476,"field6":"103"},{"created_at":"2022-08-03T19:00:41Z","entry_id":634477,"field6":"103"},{"created_at":"2022-08-03T19:02:41Z","entry_id":634478,"field6":"103"},{"created_at":"2022-08-03T19:04:41Z","entry_id":634479,"field6":"103"},{"created_at":"2022-08-03T19:06:41Z","entry_id":634480,"field6":"103"},{"created_at":"2022-08-03T19:08:41Z","entry_id":634481,"field6":"103"},{"created_at":"2022-08-03T19:10:43Z","entry_id":634482,"field6":"103"},{"created_at":"2022-08-03T19:12:41Z","entry_id":634483,"field6":"104"},{"created_at":"2022-08-03T19:14:41Z","entry_id":634484,"field6":"104"},{"created_at":"2022-08-03T19:16:41Z","entry_id":634485,"field6":"104"},{"created_at":"2022-08-03T19:18:41Z","entry_id":634486,"field6":"104"},{"created_at":"2022-08-03T19:20:41Z","entry_id":634487,"field6":"104"},{"created_at":"2022-08-03T19:22:41Z","entry_id":634488,"field6":"104"},{"created_at":"2022-08-03T19:24:41Z","entry_id":634489,"field6":"103"},{"created_at":"2022-08-03T19:26:41Z","entry_id":634490,"field6":"103"},{"created_at":"2022-08-03T19:28:41Z","entry_id":634491,"field6":"101"},{"created_at":"2022-08-03T19:30:41Z","entry_id":634492,"field6":"101"},{"created_at":"2022-08-03T19:32:41Z","entry_id":634493,"field6":"101"},{"created_at":"2022-08-03T19:34:41Z","entry_id":634494,"field6":"102"},{"created_at":"2022-08-03T19:36:41Z","entry_id":634495,"field6":"102"},{"created_at":"2022-08-03T19:38:41Z","entry_id":634496,"field6":"102"},{"created_at":"2022-08-03T19:40:41Z","entry_id":634497,"field6":"102"},{"created_at":"2022-08-03T19:42:43Z","entry_id":634498,"field6":"102"},{"created_at":"2022-08-03T19:44:41Z","entry_id":634499,"field6":"101"},{"created_at":"2022-08-03T19:46:41Z","entry_id":634500,"field6":"100"},{"created_at":"2022-08-03T19:48:41Z","entry_id":634501,"field6":"101"},{"created_at":"2022-08-03T19:50:41Z","entry_id":634502,"field6":"102"},{"created_at":"2022-08-03T19:52:41Z","entry_id":634503,"field6":"102"},{"created_at":"2022-08-03T19:54:41Z","entry_id":634504,"field6":"102"},{"created_at":"2022-08-03T19:56:41Z","entry_id":634505,"field6":"102"},{"created_at":"2022-08-03T19:58:41Z","entry_id":634506,"field6":"102"},{"created_at":"2022-08-03T20:00:41Z","entry_id":634507,"field6":"103"},{"created_at":"2022-08-03T20:02:41Z","entry_id":634508,"field6":"103"},{"created_at":"2022-08-03T20:04:41Z","entry_id":634509,"field6":"102"},{"created_at":"2022-08-03T20:06:41Z","entry_id":634510,"field6":"103"},{"created_at":"2022-08-03T20:08:41Z","entry_id":634511,"field6":"104"},{"created_at":"2022-08-03T20:10:41Z","entry_id":634512,"field6":"104"},{"created_at":"2022-08-03T20:12:41Z","entry_id":634513,"field6":"104"},{"created_at":"2022-08-03T20:14:41Z","entry_id":634514,"field6":"104"},{"created_at":"2022-08-03T20:16:41Z","entry_id":634515,"field6":"104"},{"created_at":"2022-08-03T20:18:41Z","entry_id":634516,"field6":"103"},{"created_at":"2022-08-03T20:20:41Z","entry_id":634517,"field6":"103"},{"created_at":"2022-08-03T20:22:41Z","entry_id":634518,"field6":"103"},{"created_at":"2022-08-03T20:24:41Z","entry_id":634519,"field6":"103"},{"created_at":"2022-08-03T20:26:41Z","entry_id":634520,"field6":"103"},{"created_at":"2022-08-03T20:28:43Z","entry_id":634521,"field6":"103"},{"created_at":"2022-08-03T20:30:41Z","entry_id":634522,"field6":"102"},{"created_at":"2022-08-03T20:32:41Z","entry_id":634523,"field6":"102"},{"created_at":"2022-08-03T20:34:41Z","entry_id":634524,"field6":"102"},{"created_at":"2022-08-03T20:36:41Z","entry_id":634525,"field6":"102"},{"created_at":"2022-08-03T20:38:41Z","entry_id":634526,"field6":"102"},{"created_at":"2022-08-03T20:40:41Z","entry_id":634527,"field6":"102"},{"created_at":"2022-08-03T20:42:41Z","entry_id":634528,"field6":"103"},{"created_at":"2022-08-03T20:44:41Z","entry_id":634529,"field6":"103"},{"created_at":"2022-08-03T20:46:41Z","entry_id":634530,"field6":"102"},{"created_at":"2022-08-03T20:48:41Z","entry_id":634531,"field6":"102"},{"created_at":"2022-08-03T20:50:41Z","entry_id":634532,"field6":"102"},{"created_at":"2022-08-03T20:52:41Z","entry_id":634533,"field6":"102"},{"created_at":"2022-08-03T20:54:41Z","entry_id":634534,"field6":"100"},{"created_at":"2022-08-03T20:56:41Z","entry_id":634535,"field6":"100"},{"created_at":"2022-08-03T20:58:41Z","entry_id":634536,"field6":"99"},{"created_at":"2022-08-03T21:00:41Z","entry_id":634537,"field6":"99"},{"created_at":"2022-08-03T21:02:41Z","entry_id":634538,"field6":"98"},{"created_at":"2022-08-03T21:04:41Z","entry_id":634539,"field6":"98"},{"created_at":"2022-08-03T21:06:41Z","entry_id":634540,"field6":"98"},{"created_at":"2022-08-03T21:08:41Z","entry_id":634541,"field6":"98"},{"created_at":"2022-08-03T21:10:41Z","entry_id":634542,"field6":"98"},{"created_at":"2022-08-03T21:12:41Z","entry_id":634543,"field6":"98"},{"created_at":"2022-08-03T21:14:41Z","entry_id":634544,"field6":"98"},{"created_at":"2022-08-03T21:16:41Z","entry_id":634545,"field6":"97"},{"created_at":"2022-08-03T21:18:41Z","entry_id":634546,"field6":"97"},{"created_at":"2022-08-03T21:20:41Z","entry_id":634547,"field6":"96"},{"created_at":"2022-08-03T21:22:41Z","entry_id":634548,"field6":"96"},{"created_at":"2022-08-03T21:24:41Z","entry_id":634549,"field6":"95"},{"created_at":"2022-08-03T21:26:41Z","entry_id":634550,"field6":"95"},{"created_at":"2022-08-03T21:28:41Z","entry_id":634551,"field6":"95"},{"created_at":"2022-08-03T21:30:41Z","entry_id":634552,"field6":"94"}]}'
temperature = json.loads(temperatureJSON)

temperature = json.loads(temperatureJSON)
x6 = []
y6 = []
tempInCelsius = []

for i in temperature["feeds"]:
    x6 = x6 + [temperature["feeds"].index(i)]
    y6 = y6 + [float(i["field6"])]
    tempInCelsius = [round((y - 32) / 1.8, 2) for y in y6]

while True:
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    temp = result.temperature
    tempInCelsius.append(temp)
    tempInCelsius.pop(0)

    hum = result.humidity
    humidity.append(hum)
    humidity.pop(0)

    x = range(0, len(tempInCelsius))
    y = tempInCelsius

    a = range(0, len(humidity))
    b = humidity

    meanvalueTemp = (mean(tempInCelsius))
    print("Mean value Temperature:")
    print(meanvalueTemp)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Temperature')

    ax1.plot(x, y, color='brown', linewidth=1, linestyle='solid', marker='.', markersize=3)
    ax1.axhline(meanvalueTemp, 0, 100, color='black', linewidth=1, linestyle='dashed')
    ax1.set_ylabel('Degree Celsius')

    ax2.plot(a, b, color='green', linewidth=1, linestyle='solid', marker='.', markersize=3)
    ax2.set_xlabel('Humidity')
    ax2.axhline(meanvalueHumidity, 0, 100, color='black', linewidth=1, linestyle='dashed')
    ax2.set_ylabel('Percentage')

    plt.show()

    print("After pop Temperature ", tempInCelsius)
    print("After pop Humidity ", humidity)
    time.sleep(3)



