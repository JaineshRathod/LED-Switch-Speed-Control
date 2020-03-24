int led1 = 2;
int led2 = 3;
int led3 = 5;
int led4 = 7;

boolean led1Active = false;
boolean led2Active = false;
boolean led3Active = false;
boolean led4Active = false;

char input;

long previous_time = millis();
long current_time = millis();
long interval = 500;

void setup()
{
  Serial.begin(9600);
  Serial.println("LED Switching Speed Control");
  Serial.println("Press '1' to select LED 1");
  Serial.println("Press '2' to select LED 2");
  Serial.println("Press '3' to select LED 3");
  Serial.println("Press '4' to select LED 4");
  Serial.println("Press '+' to Increase delay for selected LED");
  Serial.println("Press '-' to Decrease delay for selected LED");
  Serial.println("Press '0' to turn OFF selected LED");
  Serial.println("Press '.' to turn OFF all LED's");
  
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
}

void closeAllLed()
{
  led1Active = false;
  led2Active = false;
  led3Active = false;
  led4Active = false;
  digitalWrite(led1,LOW);
  digitalWrite(led2,LOW);
  digitalWrite(led3,LOW);
  digitalWrite(led4,LOW);
}

void closeAllSelectedLED()
{ 
  if (led1Active)
  {
    led1Active = false;
    digitalWrite(led1,LOW);
  }  
  if (led2Active)
  {
    led2Active = false;
    digitalWrite(led2,LOW);
  }  
  if (led3Active)
  {
    led3Active = false;
    digitalWrite(led3,LOW);
  }  
  if (led4Active)
  {
    led4Active = false;
    digitalWrite(led4,LOW);
  }  
}
void blinker() 
{
  if(led1Active)
  {
    int led1status = digitalRead(led1);
    digitalWrite(led1,(led1status+1)%2);
  }
  if(led2Active)
  {
    int led2status = digitalRead(led2);
    digitalWrite(led2,(led2status+1)%2);
  }
  if(led3Active)
  {
    int led3status = digitalRead(led3);
    digitalWrite(led3,(led3status+1)%2);
  }
  if(led4Active)
  {
    int led4status = digitalRead(led4);
    digitalWrite(led4,(led4status+1)%2);
  }
}

void loop()
{
  current_time = millis();
  if (current_time - previous_time > interval)
  {
    blinker();
    previous_time = current_time;  
  }
  if (Serial.available() > 0)
  {
    input = Serial.read();
    switch (input)
    {
      case '1':
        {
          led1Active = !led1Active;
          break;
        }
      case '2':
        {
          led2Active = !led2Active;
          break;
        }
      case '3':
        {
           led3Active = !led3Active;
          break;
        }
      case '4':
        {
           led4Active = !led4Active;
          break;
        }
      case '0':
        {
           closeAllSelectedLED();
           break;
           
        }
      case '.':
        {
          closeAllLed();
          break;
        }
      case '+':
        {
          interval = interval - 100; 
          break;
        }
      case '-':
        {
          interval = interval + 100; 
          break;
        }
    }
  }
}
