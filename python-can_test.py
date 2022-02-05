import can
import time

bus1 = can.interface.Bus(bustype='vector', channel=1, bitrate=500000, app_name='python-can')
# bus2 = can.interface.Bus(bustype='vector', channel=1, bitrate=500000, app_name='python-can')

msg1 = can.Message(arbitration_id = 0xa1,
                   data = [1, 2, 3, 4, 5, 6, 7, 8],
                   extended_id = False)
# msg2 = can.Message(arbitration_id = 0xa3,
#                    data = [8, 7, 6, 5, 4, 3, 2, 1],
#                    extended_id = False)
for i in range(5):
    bus1.send(msg1)
    time.sleep(1)
    # bus2.send(msg2)
    print("Succeeded!")

bus1.shutdown()
# bus2.shutdown()