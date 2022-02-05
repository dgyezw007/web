from PCANBasic import *
import time
objPCAN = PCANBasic()
result = objPCAN.Initialize(PCAN_USBBUS1, PCAN_BAUD_500K)
if result != PCAN_ERROR_OK:
    # An error occurred, get a text describing the error and show it
    #
    result = objPCAN.GetErrorText(result)
    print(result[1])
else:
    print ("PCAN-USB (Ch-1) was initialized")


time.sleep(5)
result = objPCAN.Uninitialize(PCAN_USBBUS1)
if result != PCAN_ERROR_OK:
    # An error occurred, get a text describing the error and show it
    #
    result = objPCAN.GetErrorText(result)
    print (result[1])
else:
    print ("PCAN-USB (Ch-1) was released")