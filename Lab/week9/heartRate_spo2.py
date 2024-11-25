import max30102
import hrcalc, time
m=max30102.MAX30102()
def read_sensor():
    while True:
        red,ir=m.read_sequential()
        hr,hr_valid,spo2,spo2_valid=hrcalc.calc_hr_and_spo2(ir,red)

        if hr_valid and spo2_valid:
            print("Heart Rate: ", hr, "BPM")
            print("SpO2 Level: ", spo2, "%")
        else:
            print("Invalid readings. Please try again.")
        time.sleep(1)

if __name__=="__main__":
    read_sensor()
GPIO.cleanup()