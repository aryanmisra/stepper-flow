import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.cleanup()

delay = 5
add = 30

coil_A_1_pin = 27   #replace
coil_A_2_pin = 26   #replace
coil_B_1_pin = 23   #replace
coil_B_2_pin = 24   #replace
coil_A_x1_pin = 22  #replace
coil_A_x2_pin = 5   #replace
coil_B_x1_pin = 6   #replace
coil_B_x2_pin = 13  #replace

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.setup(coil_A_x1_pin, GPIO.OUT)
GPIO.setup(coil_A_x2_pin, GPIO.OUT)
GPIO.setup(coil_B_x1_pin, GPIO.OUT)
GPIO.setup(coil_B_x2_pin, GPIO.OUT)


def forward(delay, steps):
  for i in range(0, steps):
    setStep(1, 1, 0, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 0, 1, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)

def backwards(delay, steps):
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 0, 1, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 1, 0, 0)
    time.sleep(delay)

def left(delay, steps):
    for i in range(0, steps):
      setTurnLeft(1, 0, 0, 1, 1, 1, 0, 0)
      time.sleep(delay)
      setTurnLeft(0, 0, 1, 1, 0, 1, 1, 0)
      time.sleep(delay)
      setTurnLeft(0, 1, 1, 0, 0, 0, 1, 1)
      time.sleep(delay)
      setTurnLeft(1, 1, 0, 0, 1, 0, 0, 1)
      time.sleep(delay)

def right(delay, steps):
    for i in range(0, steps):
      setTurnRight(1, 1, 0, 0, 1, 0, 0, 1)
      time.sleep(delay)
      setTurnRight(0, 1, 1, 0, 0, 0, 1, 1)
      time.sleep(delay)
      setTurnRight(0, 0, 1, 1, 0, 1, 1, 0)
      time.sleep(delay)
      setTurnRight(1, 0, 0, 1, 1, 1, 0, 0)
      time.sleep(delay)


def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_x1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_A_x2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_x1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)
  GPIO.output(coil_B_x2_pin, w4)

def setTurnLeft(w1,w2,w3,w4,w5,w6,w7,w8):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)
  GPIO.output(coil_A_x1_pin, w5)
  GPIO.output(coil_A_x2_pin, w6)
  GPIO.output(coil_B_x1_pin, w7)
  GPIO.output(coil_B_x2_pin, w8)

def setTurnRight(w1,w2,w3,w4,w5,w6,w7,w8):
  GPIO.output(coil_A_1_pin, w8)
  GPIO.output(coil_A_2_pin, w7)
  GPIO.output(coil_B_1_pin, w6)
  GPIO.output(coil_B_2_pin, w5)
  GPIO.output(coil_A_x1_pin, w4)
  GPIO.output(coil_A_x2_pin, w3)
  GPIO.output(coil_B_x1_pin, w2)
  GPIO.output(coil_B_x2_pin, w1)


#use forward,backward,right,left, to control movement

