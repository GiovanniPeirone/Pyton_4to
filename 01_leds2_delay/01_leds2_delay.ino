// 01_leds2_delay
const int ledpin1 = 10;
const int ledpin2 = 9;
const int tiempo = 25;//milisegundos

void setup() {
  pinMode (ledpin1, OUTPUT);
  pinMode (ledpin2, OUTPUT);
}

void loop() {
digitalWrite (ledpin1,HIGH); 
digitalWrite (ledpin2,LOW); 
delay(tiempo);
digitalWrite (ledpin1,LOW); 
digitalWrite (ledpin2, HIGH); 
delay(tiempo);
}
