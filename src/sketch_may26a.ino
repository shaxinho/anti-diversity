#include <AFMotor.h>
#include <Servo.h>
#include <NewPing.h>


Servo myservo; 
AF_DCMotor motor4(4);

#define S1Trig A0
#define S2Trig A2
#define S3Trig A4
#define S1Echo A1
#define S2Echo A3
#define S3Echo A5

#define MAX_DISTANCE 300

NewPing sonar1(S1Trig, S1Echo, MAX_DISTANCE);
NewPing sonar2(S2Trig, S2Echo, MAX_DISTANCE);
NewPing sonar3(S3Trig, S3Echo, MAX_DISTANCE);

const int servoPin = 10;
int pos = 0;  // variable to store the servo position

boolean goesForward=false;
int distance1 = 100;
int distance2 = 100;
int distance3 = 100;
int speedSet = 0;

int speed(int percent){

  return map(percent, 0, 100,0,255);  
}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}

bool isStart = false;

void setup() {
  //Set the Trig pins as output pins
    pinMode(S1Trig, OUTPUT);
    pinMode(S2Trig, OUTPUT);
    pinMode(S3Trig, OUTPUT);
  //Set the Echo pins as input pins
    pinMode(S1Echo, INPUT);
    pinMode(S2Echo, INPUT);
    pinMode(S3Echo, INPUT);
    myservo.attach(servoPin);  
    Serial.begin(9600);
     
}

void loop() {
  myservo.write(45);
  delay(2500);
  
  
      
  //myservo.write(45);
  distance1 = sonar1.ping_cm();
  Serial.print("\nFIRST "+String(distance1)+ "\n");

  distance2 = sonar2.ping_cm();
  Serial.print("SECOND "+String(distance2) +"\n"  );

  distance3 = sonar3.ping_cm();
  Serial.print("THIRD "+String(distance3) +"\n"  );


  



}
