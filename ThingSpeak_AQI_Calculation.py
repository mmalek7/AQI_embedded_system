import json
import thingspeak
import numpy as np

channel_id = 1842256
write_key = 'E6ULUS197VX1OMEA'
channel = thingspeak.Channel(id=channel_id, api_key=write_key)

PM2_5_JSON= '{"channel":{"id":628559,"name":"AirMonitor_e9bb","latitude":"0.0","longitude":"0.0","field1":"PM1.0 (ATM)","field2":"PM2.5 (ATM)","field3":"PM10.0 (ATM)","field4":"Uptime","field5":"RSSI","field6":"Temperature","field7":"Humidity","field8":"PM2.5 (CF=1)","created_at":"2018-11-15T23:39:47Z","updated_at":"2019-03-20T17:03:58Z","last_entry_id":634549},"feeds":[{"created_at":"2022-08-03T18:06:41Z","entry_id":634450,"field2":"5.80"},{"created_at":"2022-08-03T18:08:41Z","entry_id":634451,"field2":"5.46"},{"created_at":"2022-08-03T18:10:40Z","entry_id":634452,"field2":"5.77"},{"created_at":"2022-08-03T18:12:40Z","entry_id":634453,"field2":"5.81"},{"created_at":"2022-08-03T18:14:41Z","entry_id":634454,"field2":"5.26"},{"created_at":"2022-08-03T18:16:41Z","entry_id":634455,"field2":"4.82"},{"created_at":"2022-08-03T18:18:41Z","entry_id":634456,"field2":"4.82"},{"created_at":"2022-08-03T18:20:41Z","entry_id":634457,"field2":"5.94"},{"created_at":"2022-08-03T18:22:41Z","entry_id":634458,"field2":"5.93"},{"created_at":"2022-08-03T18:24:41Z","entry_id":634459,"field2":"5.93"},{"created_at":"2022-08-03T18:26:41Z","entry_id":634460,"field2":"5.39"},{"created_at":"2022-08-03T18:28:41Z","entry_id":634461,"field2":"6.12"},{"created_at":"2022-08-03T18:30:41Z","entry_id":634462,"field2":"5.71"},{"created_at":"2022-08-03T18:32:41Z","entry_id":634463,"field2":"5.33"},{"created_at":"2022-08-03T18:34:41Z","entry_id":634464,"field2":"5.44"},{"created_at":"2022-08-03T18:36:41Z","entry_id":634465,"field2":"5.45"},{"created_at":"2022-08-03T18:38:41Z","entry_id":634466,"field2":"5.75"},{"created_at":"2022-08-03T18:40:41Z","entry_id":634467,"field2":"5.31"},{"created_at":"2022-08-03T18:42:41Z","entry_id":634468,"field2":"5.26"},{"created_at":"2022-08-03T18:44:41Z","entry_id":634469,"field2":"5.07"},{"created_at":"2022-08-03T18:46:41Z","entry_id":634470,"field2":"5.20"},{"created_at":"2022-08-03T18:48:41Z","entry_id":634471,"field2":"5.46"},{"created_at":"2022-08-03T18:50:41Z","entry_id":634472,"field2":"5.59"},{"created_at":"2022-08-03T18:52:41Z","entry_id":634473,"field2":"5.07"},{"created_at":"2022-08-03T18:54:41Z","entry_id":634474,"field2":"4.98"},{"created_at":"2022-08-03T18:56:41Z","entry_id":634475,"field2":"4.49"},{"created_at":"2022-08-03T18:58:43Z","entry_id":634476,"field2":"5.43"},{"created_at":"2022-08-03T19:00:41Z","entry_id":634477,"field2":"4.55"},{"created_at":"2022-08-03T19:02:41Z","entry_id":634478,"field2":"4.30"},{"created_at":"2022-08-03T19:04:41Z","entry_id":634479,"field2":"4.77"},{"created_at":"2022-08-03T19:06:41Z","entry_id":634480,"field2":"4.39"},{"created_at":"2022-08-03T19:08:41Z","entry_id":634481,"field2":"4.04"},{"created_at":"2022-08-03T19:10:43Z","entry_id":634482,"field2":"3.65"},{"created_at":"2022-08-03T19:12:41Z","entry_id":634483,"field2":"4.50"},{"created_at":"2022-08-03T19:14:41Z","entry_id":634484,"field2":"4.56"},{"created_at":"2022-08-03T19:16:41Z","entry_id":634485,"field2":"4.60"},{"created_at":"2022-08-03T19:18:41Z","entry_id":634486,"field2":"4.16"},{"created_at":"2022-08-03T19:20:41Z","entry_id":634487,"field2":"4.33"},{"created_at":"2022-08-03T19:22:41Z","entry_id":634488,"field2":"4.91"},{"created_at":"2022-08-03T19:24:41Z","entry_id":634489,"field2":"4.93"},{"created_at":"2022-08-03T19:26:41Z","entry_id":634490,"field2":"5.12"},{"created_at":"2022-08-03T19:28:41Z","entry_id":634491,"field2":"4.17"},{"created_at":"2022-08-03T19:30:41Z","entry_id":634492,"field2":"4.67"},{"created_at":"2022-08-03T19:32:41Z","entry_id":634493,"field2":"4.75"},{"created_at":"2022-08-03T19:34:41Z","entry_id":634494,"field2":"5.09"},{"created_at":"2022-08-03T19:36:41Z","entry_id":634495,"field2":"5.20"},{"created_at":"2022-08-03T19:38:41Z","entry_id":634496,"field2":"5.17"},{"created_at":"2022-08-03T19:40:41Z","entry_id":634497,"field2":"4.95"},{"created_at":"2022-08-03T19:42:43Z","entry_id":634498,"field2":"4.98"},{"created_at":"2022-08-03T19:44:41Z","entry_id":634499,"field2":"5.57"},{"created_at":"2022-08-03T19:46:41Z","entry_id":634500,"field2":"4.76"},{"created_at":"2022-08-03T19:48:41Z","entry_id":634501,"field2":"5.07"},{"created_at":"2022-08-03T19:50:41Z","entry_id":634502,"field2":"6.02"},{"created_at":"2022-08-03T19:52:41Z","entry_id":634503,"field2":"5.98"},{"created_at":"2022-08-03T19:54:41Z","entry_id":634504,"field2":"5.24"},{"created_at":"2022-08-03T19:56:41Z","entry_id":634505,"field2":"4.28"},{"created_at":"2022-08-03T19:58:41Z","entry_id":634506,"field2":"4.12"},{"created_at":"2022-08-03T20:00:41Z","entry_id":634507,"field2":"3.91"},{"created_at":"2022-08-03T20:02:41Z","entry_id":634508,"field2":"3.75"},{"created_at":"2022-08-03T20:04:41Z","entry_id":634509,"field2":"4.15"},{"created_at":"2022-08-03T20:06:41Z","entry_id":634510,"field2":"4.09"},{"created_at":"2022-08-03T20:08:41Z","entry_id":634511,"field2":"4.04"},{"created_at":"2022-08-03T20:10:41Z","entry_id":634512,"field2":"3.80"},{"created_at":"2022-08-03T20:12:41Z","entry_id":634513,"field2":"3.68"},{"created_at":"2022-08-03T20:14:41Z","entry_id":634514,"field2":"3.87"},{"created_at":"2022-08-03T20:16:41Z","entry_id":634515,"field2":"4.53"},{"created_at":"2022-08-03T20:18:41Z","entry_id":634516,"field2":"4.04"},{"created_at":"2022-08-03T20:20:41Z","entry_id":634517,"field2":"4.81"},{"created_at":"2022-08-03T20:22:41Z","entry_id":634518,"field2":"5.21"},{"created_at":"2022-08-03T20:24:41Z","entry_id":634519,"field2":"3.54"},{"created_at":"2022-08-03T20:26:41Z","entry_id":634520,"field2":"3.62"},{"created_at":"2022-08-03T20:28:43Z","entry_id":634521,"field2":"4.04"},{"created_at":"2022-08-03T20:30:41Z","entry_id":634522,"field2":"4.30"},{"created_at":"2022-08-03T20:32:41Z","entry_id":634523,"field2":"3.95"},{"created_at":"2022-08-03T20:34:41Z","entry_id":634524,"field2":"5.18"},{"created_at":"2022-08-03T20:36:41Z","entry_id":634525,"field2":"4.20"},{"created_at":"2022-08-03T20:38:41Z","entry_id":634526,"field2":"4.30"},{"created_at":"2022-08-03T20:40:41Z","entry_id":634527,"field2":"4.39"},{"created_at":"2022-08-03T20:42:41Z","entry_id":634528,"field2":"4.72"},{"created_at":"2022-08-03T20:44:41Z","entry_id":634529,"field2":"4.35"},{"created_at":"2022-08-03T20:46:41Z","entry_id":634530,"field2":"3.94"},{"created_at":"2022-08-03T20:48:41Z","entry_id":634531,"field2":"4.55"},{"created_at":"2022-08-03T20:50:41Z","entry_id":634532,"field2":"5.00"},{"created_at":"2022-08-03T20:52:41Z","entry_id":634533,"field2":"4.49"},{"created_at":"2022-08-03T20:54:41Z","entry_id":634534,"field2":"5.17"},{"created_at":"2022-08-03T20:56:41Z","entry_id":634535,"field2":"5.28"},{"created_at":"2022-08-03T20:58:41Z","entry_id":634536,"field2":"5.30"},{"created_at":"2022-08-03T21:00:41Z","entry_id":634537,"field2":"5.28"},{"created_at":"2022-08-03T21:02:41Z","entry_id":634538,"field2":"5.07"},{"created_at":"2022-08-03T21:04:41Z","entry_id":634539,"field2":"4.93"},{"created_at":"2022-08-03T21:06:41Z","entry_id":634540,"field2":"4.58"},{"created_at":"2022-08-03T21:08:41Z","entry_id":634541,"field2":"3.96"},{"created_at":"2022-08-03T21:10:41Z","entry_id":634542,"field2":"4.96"},{"created_at":"2022-08-03T21:12:41Z","entry_id":634543,"field2":"5.28"},{"created_at":"2022-08-03T21:14:41Z","entry_id":634544,"field2":"4.62"},{"created_at":"2022-08-03T21:16:41Z","entry_id":634545,"field2":"4.29"},{"created_at":"2022-08-03T21:18:41Z","entry_id":634546,"field2":"4.71"},{"created_at":"2022-08-03T21:20:41Z","entry_id":634547,"field2":"4.02"},{"created_at":"2022-08-03T21:22:41Z","entry_id":634548,"field2":"5.05"},{"created_at":"2022-08-03T21:24:41Z","entry_id":634549,"field2":"4.59"}]}'
PM2_5 = json.loads(PM2_5_JSON)
PM10_JSON= '{"channel":{"id":628559,"name":"AirMonitor_e9bb","latitude":"0.0","longitude":"0.0","field1":"PM1.0 (ATM)","field2":"PM2.5 (ATM)","field3":"PM10.0 (ATM)","field4":"Uptime","field5":"RSSI","field6":"Temperature","field7":"Humidity","field8":"PM2.5 (CF=1)","created_at":"2018-11-15T23:39:47Z","updated_at":"2019-03-20T17:03:58Z","last_entry_id":634549},"feeds":[{"created_at":"2022-08-03T18:06:41Z","entry_id":634450,"field3":"5.80"},{"created_at":"2022-08-03T18:08:41Z","entry_id":634451,"field3":"5.50"},{"created_at":"2022-08-03T18:10:40Z","entry_id":634452,"field3":"6.14"},{"created_at":"2022-08-03T18:12:40Z","entry_id":634453,"field3":"6.08"},{"created_at":"2022-08-03T18:14:41Z","entry_id":634454,"field3":"5.41"},{"created_at":"2022-08-03T18:16:41Z","entry_id":634455,"field3":"5.11"},{"created_at":"2022-08-03T18:18:41Z","entry_id":634456,"field3":"4.95"},{"created_at":"2022-08-03T18:20:41Z","entry_id":634457,"field3":"6.08"},{"created_at":"2022-08-03T18:22:41Z","entry_id":634458,"field3":"6.02"},{"created_at":"2022-08-03T18:24:41Z","entry_id":634459,"field3":"6.09"},{"created_at":"2022-08-03T18:26:41Z","entry_id":634460,"field3":"5.48"},{"created_at":"2022-08-03T18:28:41Z","entry_id":634461,"field3":"6.34"},{"created_at":"2022-08-03T18:30:41Z","entry_id":634462,"field3":"5.83"},{"created_at":"2022-08-03T18:32:41Z","entry_id":634463,"field3":"5.33"},{"created_at":"2022-08-03T18:34:41Z","entry_id":634464,"field3":"5.53"},{"created_at":"2022-08-03T18:36:41Z","entry_id":634465,"field3":"5.57"},{"created_at":"2022-08-03T18:38:41Z","entry_id":634466,"field3":"5.92"},{"created_at":"2022-08-03T18:40:41Z","entry_id":634467,"field3":"5.44"},{"created_at":"2022-08-03T18:42:41Z","entry_id":634468,"field3":"5.35"},{"created_at":"2022-08-03T18:44:41Z","entry_id":634469,"field3":"5.07"},{"created_at":"2022-08-03T18:46:41Z","entry_id":634470,"field3":"5.24"},{"created_at":"2022-08-03T18:48:41Z","entry_id":634471,"field3":"5.54"},{"created_at":"2022-08-03T18:50:41Z","entry_id":634472,"field3":"5.59"},{"created_at":"2022-08-03T18:52:41Z","entry_id":634473,"field3":"5.40"},{"created_at":"2022-08-03T18:54:41Z","entry_id":634474,"field3":"4.98"},{"created_at":"2022-08-03T18:56:41Z","entry_id":634475,"field3":"4.49"},{"created_at":"2022-08-03T18:58:43Z","entry_id":634476,"field3":"5.43"},{"created_at":"2022-08-03T19:00:41Z","entry_id":634477,"field3":"4.68"},{"created_at":"2022-08-03T19:02:41Z","entry_id":634478,"field3":"4.39"},{"created_at":"2022-08-03T19:04:41Z","entry_id":634479,"field3":"4.87"},{"created_at":"2022-08-03T19:06:41Z","entry_id":634480,"field3":"4.39"},{"created_at":"2022-08-03T19:08:41Z","entry_id":634481,"field3":"4.09"},{"created_at":"2022-08-03T19:10:43Z","entry_id":634482,"field3":"3.82"},{"created_at":"2022-08-03T19:12:41Z","entry_id":634483,"field3":"4.80"},{"created_at":"2022-08-03T19:14:41Z","entry_id":634484,"field3":"4.65"},{"created_at":"2022-08-03T19:16:41Z","entry_id":634485,"field3":"4.60"},{"created_at":"2022-08-03T19:18:41Z","entry_id":634486,"field3":"4.16"},{"created_at":"2022-08-03T19:20:41Z","entry_id":634487,"field3":"4.59"},{"created_at":"2022-08-03T19:22:41Z","entry_id":634488,"field3":"5.04"},{"created_at":"2022-08-03T19:24:41Z","entry_id":634489,"field3":"4.95"},{"created_at":"2022-08-03T19:26:41Z","entry_id":634490,"field3":"5.12"},{"created_at":"2022-08-03T19:28:41Z","entry_id":634491,"field3":"4.20"},{"created_at":"2022-08-03T19:30:41Z","entry_id":634492,"field3":"4.78"},{"created_at":"2022-08-03T19:32:41Z","entry_id":634493,"field3":"4.87"},{"created_at":"2022-08-03T19:34:41Z","entry_id":634494,"field3":"5.30"},{"created_at":"2022-08-03T19:36:41Z","entry_id":634495,"field3":"5.20"},{"created_at":"2022-08-03T19:38:41Z","entry_id":634496,"field3":"5.41"},{"created_at":"2022-08-03T19:40:41Z","entry_id":634497,"field3":"5.16"},{"created_at":"2022-08-03T19:42:43Z","entry_id":634498,"field3":"5.07"},{"created_at":"2022-08-03T19:44:41Z","entry_id":634499,"field3":"5.57"},{"created_at":"2022-08-03T19:46:41Z","entry_id":634500,"field3":"4.78"},{"created_at":"2022-08-03T19:48:41Z","entry_id":634501,"field3":"5.18"},{"created_at":"2022-08-03T19:50:41Z","entry_id":634502,"field3":"6.25"},{"created_at":"2022-08-03T19:52:41Z","entry_id":634503,"field3":"5.98"},{"created_at":"2022-08-03T19:54:41Z","entry_id":634504,"field3":"5.24"},{"created_at":"2022-08-03T19:56:41Z","entry_id":634505,"field3":"4.28"},{"created_at":"2022-08-03T19:58:41Z","entry_id":634506,"field3":"4.38"},{"created_at":"2022-08-03T20:00:41Z","entry_id":634507,"field3":"4.20"},{"created_at":"2022-08-03T20:02:41Z","entry_id":634508,"field3":"3.85"},{"created_at":"2022-08-03T20:04:41Z","entry_id":634509,"field3":"4.24"},{"created_at":"2022-08-03T20:06:41Z","entry_id":634510,"field3":"4.13"},{"created_at":"2022-08-03T20:08:41Z","entry_id":634511,"field3":"4.21"},{"created_at":"2022-08-03T20:10:41Z","entry_id":634512,"field3":"3.96"},{"created_at":"2022-08-03T20:12:41Z","entry_id":634513,"field3":"3.68"},{"created_at":"2022-08-03T20:14:41Z","entry_id":634514,"field3":"3.91"},{"created_at":"2022-08-03T20:16:41Z","entry_id":634515,"field3":"4.78"},{"created_at":"2022-08-03T20:18:41Z","entry_id":634516,"field3":"4.05"},{"created_at":"2022-08-03T20:20:41Z","entry_id":634517,"field3":"5.17"},{"created_at":"2022-08-03T20:22:41Z","entry_id":634518,"field3":"5.27"},{"created_at":"2022-08-03T20:24:41Z","entry_id":634519,"field3":"3.73"},{"created_at":"2022-08-03T20:26:41Z","entry_id":634520,"field3":"3.84"},{"created_at":"2022-08-03T20:28:43Z","entry_id":634521,"field3":"4.15"},{"created_at":"2022-08-03T20:30:41Z","entry_id":634522,"field3":"4.63"},{"created_at":"2022-08-03T20:32:41Z","entry_id":634523,"field3":"3.95"},{"created_at":"2022-08-03T20:34:41Z","entry_id":634524,"field3":"5.18"},{"created_at":"2022-08-03T20:36:41Z","entry_id":634525,"field3":"4.26"},{"created_at":"2022-08-03T20:38:41Z","entry_id":634526,"field3":"4.30"},{"created_at":"2022-08-03T20:40:41Z","entry_id":634527,"field3":"4.78"},{"created_at":"2022-08-03T20:42:41Z","entry_id":634528,"field3":"4.81"},{"created_at":"2022-08-03T20:44:41Z","entry_id":634529,"field3":"4.35"},{"created_at":"2022-08-03T20:46:41Z","entry_id":634530,"field3":"3.98"},{"created_at":"2022-08-03T20:48:41Z","entry_id":634531,"field3":"4.61"},{"created_at":"2022-08-03T20:50:41Z","entry_id":634532,"field3":"5.22"},{"created_at":"2022-08-03T20:52:41Z","entry_id":634533,"field3":"4.49"},{"created_at":"2022-08-03T20:54:41Z","entry_id":634534,"field3":"5.17"},{"created_at":"2022-08-03T20:56:41Z","entry_id":634535,"field3":"5.28"},{"created_at":"2022-08-03T20:58:41Z","entry_id":634536,"field3":"5.30"},{"created_at":"2022-08-03T21:00:41Z","entry_id":634537,"field3":"5.33"},{"created_at":"2022-08-03T21:02:41Z","entry_id":634538,"field3":"5.15"},{"created_at":"2022-08-03T21:04:41Z","entry_id":634539,"field3":"5.02"},{"created_at":"2022-08-03T21:06:41Z","entry_id":634540,"field3":"4.72"},{"created_at":"2022-08-03T21:08:41Z","entry_id":634541,"field3":"3.96"},{"created_at":"2022-08-03T21:10:41Z","entry_id":634542,"field3":"4.96"},{"created_at":"2022-08-03T21:12:41Z","entry_id":634543,"field3":"5.28"},{"created_at":"2022-08-03T21:14:41Z","entry_id":634544,"field3":"4.62"},{"created_at":"2022-08-03T21:16:41Z","entry_id":634545,"field3":"4.47"},{"created_at":"2022-08-03T21:18:41Z","entry_id":634546,"field3":"4.93"},{"created_at":"2022-08-03T21:20:41Z","entry_id":634547,"field3":"4.13"},{"created_at":"2022-08-03T21:22:41Z","entry_id":634548,"field3":"5.15"},{"created_at":"2022-08-03T21:24:41Z","entry_id":634549,"field3":"4.83"}]}'
PM10 = json.loads(PM10_JSON)
x2 = []
y2 = []
x3 = []
y3 = []
for i in PM2_5["feeds"]:
    y2= y2 + [float(i["field2"])]
    ih1 = 50
    il1 = 0
    chp1 = 12
    clp1 = 0
    cm1 = np.array(y2)
    AQI1=((((ih1-il1)/(chp1-clp1))*(cm1-clp1))+51)
    x2= x2 + [PM2_5["feeds"].index(i)]

for i in PM10["feeds"]:
    y3= y3 + [float(i["field3"])]
    ih3 = 50
    il3 = 0
    chp3 = 54
    clp3 = 0
    cm3 = np.array(y3)
    AQI2=((((ih3-il3)/(chp3-clp3))*(cm3-clp3))+51)
    x3= x3 + [PM10["feeds"].index(i)]
print ("PM2_5 Entries")
# print(x2)
print(y2)
print("AQI1 Values PM2.5")
print(AQI1)
print('======================================================================================================')
print ("PM10 Entries")
# print(x3)
print(y3)
print("AQI2 Values PM10")
print(AQI2)
print('======================================================================================================')

channel.update({'field1': AQI1, 'field2': AQI2})
print(channel)
read_key = 'S83Z6FBVY67HHICY'  # PUT YOUR READ KEY HERE
channelread = thingspeak.Channel(id=channel_id, api_key=read_key)

read = channelread.get_field_last(3)
#print("Read:", read)
GetStr = read.split('"')
Value = float(GetStr[len(GetStr)-2])
#print(GetStr)
print("Average humidity from cloud: %-3.1f %%" % np.array(AQI1))

print('------------------------------------------------------------------------------------------------')
print(Value)

# time.sleep(10)



print('======================================================================================================')
# for i in AQI1:
#     MAX_AQI = max(np.array(AQI1), np.array(AQI2))
#     print(MAX_AQI)
# #     if not print(AQI2):
# #         print("right")

print('======================================================================================================')

