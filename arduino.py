import time

def changeDelay():
    while True:
        with open('C:\\Users\\Billy\\Documents\\GitHub\\thirdyearproject\\HeartRate\\HeartRate_v0\\HeartRate_v0.ino', 'r') as file:
            data = file.readlines()
        delayTimeStr = input("How many seconds delay would you like? ")

        try:
            delayTimeInt = int(delayTimeStr)
            time.sleep(1)
            print("\nThe delay has been changed to ", delayTimeInt)
            data[7] = "int delay = " + str(delayTimeInt) + ";\n"
            time.sleep(1)

        except ValueError:
            time.sleep(1)
            print("\nThis is not a valid number. Please try again.\n")
            time.sleep(1)
            continue

        else:
            with open('C:\\Users\\Billy\\Documents\\GitHub\\thirdyearproject\\HeartRate\\HeartRate_v0\\HeartRate_v0.ino', 'w') as file:
                file.writelines(data)
            break

def changeNumReadings():
    while True:
        with open('C:\\Users\\Billy\\Documents\\GitHub\\thirdyearproject\\HeartRate\\HeartRate_v0\\HeartRate_v0.ino', 'r') as file:
            data = file.readlines()
        numReadingsStr = input("\nHow many readings would you like to take? ")

        try:
            numReadingsInt = int(numReadingsStr)
            time.sleep(1)
            print("\nThe number of readings you will take is ", numReadingsInt)
            data[8] = "int readings = " + str(numReadingsInt) + ";\n"
            time.sleep(1)

        except ValueError:
            time.sleep(1)
            print("\nThis is not a valid number. Please try again.\n")
            time.sleep(1)
            continue

        else:
            with open('C:\\Users\\Billy\\Documents\\GitHub\\thirdyearproject\\HeartRate\\HeartRate_v0\\HeartRate_v0.ino', 'w') as file:
                file.writelines(data)
            break

changeDelay()
changeNumReadings()
