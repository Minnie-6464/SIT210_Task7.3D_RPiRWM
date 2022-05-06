import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 4
ECHO = 17
LED = 16
BUZZER = 21

print ("Distance Measurement in Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

buzzerpwm = GPIO.PWM(BUZZER, 1000)
buzzerpwm.start(0)

while True:
    GPIO.output(TRIG, False)
    print("waiting for sensor to settle")
    time.sleep(0.5)
    
    GPIO.output(TRIG, True)
    time.sleep(0.1)
    GPIO.output(TRIG, False)
    
    #to get pulse
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
     #calcualte distance   
    pulse_duration = pulse_end-pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    print(distance)
    if distance > 20:
        GPIO.output(LED, GPIO.LOW)
        buzzerpwm.ChangeDutyCycle(0)
         
    elif (distance < 20) and (distance > 10):
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
        buzzerpwm.ChangeDutyCycle(10)
        buzzerpwm.ChangeFrequency(523)
        
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
        
    elif (distance < 10) and (distance > 5):
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.25)
        buzzerpwm.ChangeDutyCycle(50)
        buzzerpwm.ChangeFrequency(659)
          
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.25)
        
    elif (distance < 5) and (distance > 1):
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.02)
        buzzerpwm.ChangeDutyCycle(100)
        buzzerpwm.ChangeFrequency(784)
        
        
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.02)    
        
    else:
        GPIO.output(LED, GPIO.HIGH)
        buzzerpwm.stop()
        





