import can

bus1 = can.interface.Bus(bustype='neovi', channel=2, bitrate=500000, app_name='python-can')

'''主动发送报文
msg1 = can.Message(arbitration_id = 0xa1,
                   data = [1, 2, 3, 10, 5, 6, 7, 8],
                   extended_id = False)
msg2 = can.Message(arbitration_id = 0xa3,
                   data = [8, 7, 6, 5, 4, 3, 2, 1],
                   extended_id = False)

task1 = bus1.send_periodic(msg1, 0.1)
task2 = bus1.send_periodic(msg2, 0.1)

time.sleep(10)
task1.stop()
task2.stop()
'''


'''接收CAN报文,并将其保存到asc文件里'''
count = 0
canlogger = can.ASCWriter('trace.asc', channel=2)
for msg in bus1:
    # print(msg.data)
    canlogger.log_event(msg)
    count += 1
    if count >= 100:   #保存100条报文
        count = 0
        break

print("Succeeded!")

bus1.shutdown()
