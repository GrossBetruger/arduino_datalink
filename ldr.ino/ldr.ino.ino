

const int LIGHT_SENSOR = A5;
const int SAMPLES_PER_UI = 20; // # samples in unit interval 
const int DELAY = 50;
const int LIGHT_RISE_TIME = 40; // Delay time for red light input high/low to take effect


void setup() {
  pinMode(LIGHT_SENSOR, INPUT);
  Serial.begin(9600);
}

void sample() {
  int ldrValue = analogRead(LIGHT_SENSOR);
  Serial.println(ldrValue);
  delay(DELAY / SAMPLES_PER_UI);
}


void loop() {
    sample();
  }