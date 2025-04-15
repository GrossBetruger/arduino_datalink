

const int RED_LED = 2;
const int LIGHT_SENSOR = A5;
const int SAMPLES_PER_UI = 20; // # samples in unit interval 
const int DELAY = 200;
const int LIGHT_RISE_TIME = 60; // Delay time for red light input high/low to take effect

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

void bits(unsigned char byte, unsigned char bits_in_byte[8]){
  unsigned char mask = 1;
  for (int i=7; i>=0; i--) {
    bits_in_byte[i] = byte & mask ? 1: 0;
    mask *= 2;
  }
}

void loop() {
  
  if (Serial.available() > 0) {

    // Read the incoming bytes until newline
    String inputString = Serial.readStringUntil('\n');
    Serial.println(inputString);

    // input string to bytes
    int stringLen = inputString.length();
    int buf_size = stringLen + 1;
    unsigned char byteArray[buf_size]; // Example size, make it appropriate
    // if (stringLen < sizeof(byteArray)) { // Check if buffer is large enough
    inputString.getBytes(byteArray, sizeof(byteArray));  

    for (int byte_idx=0; byte_idx<buf_size; byte_idx++) {
      unsigned char byte = byteArray[byte_idx];
      unsigned char bits_in_byte[8];

      Serial.print("byte: ");
      Serial.println(byte);
      bits(byte, bits_in_byte);
      for (int i=0; i<8; i++) {
        int current_bit = bits_in_byte[i];
        digitalWrite(RED_LED, current_bit);
          delay(LIGHT_RISE_TIME);
          for (int i=0; i < SAMPLES_PER_UI; i++) {
            sample();
          }
        // Serial.print(current_bit);
      }
      digitalWrite(RED_LED, LOW);
      delay(DELAY * 10);
      Serial.println("\n");

    }
  }

  // digitalWrite(RED_LED, LOW);
  // delay(LIGHT_RISE_TIME);
  // int ldrValue = analogRead(LIGHT_SENSOR);
  // for (int i=0; i < SAMPLES_PER_UI; i++) {
  //     sample();
  // }

  // digitalWrite(RED_LED, HIGH);
  // delay(LIGHT_RISE_TIME);
  // for (int i=0; i < SAMPLES_PER_UI; i++) {
  //     sample();
  // }
}

