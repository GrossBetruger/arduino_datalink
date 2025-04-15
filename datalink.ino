const int RED_LED = 2;
const int LIGHT_SENSOR = A5;
const int SAMPLES_PER_UI = 5; // # samples in unit interval 
const int DELAY = 333;
const int LIGHT_RISE_TIME = 30; // Delay time for red light input high/low to take effect

void setup() {
  pinMode(RED_LED, OUTPUT);
  pinMode(LIGHT_SENSOR, INPUT);
  Serial.begin(9600);

}

void sample() {
  int ldrValue = analogRead(LIGHT_SENSOR);
  Serial.println(ldrValue);
  delay(DELAY / SAMPLES_PER_UI);
}

void loop() {
  digitalWrite(RED_LED, LOW);
  delay(LIGHT_RISE_TIME);
  // int ldrValue = analogRead(LIGHT_SENSOR);
  for (int i=0; i < SAMPLES_PER_UI; i++) {
      sample();
  }

  digitalWrite(RED_LED, HIGH);
  delay(LIGHT_RISE_TIME);
  for (int i=0; i < SAMPLES_PER_UI; i++) {
      sample();
  }
}

