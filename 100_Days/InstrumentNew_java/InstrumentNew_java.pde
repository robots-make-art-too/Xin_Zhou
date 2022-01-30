//scale(x) pitch(y)
import processing.sound.*;

TriOsc triOsc;
int scale, pitch;
int[] pitchList = {53,106,159};;
int[] scaleList = {90,180,270};;

void setup(){
  size(640,320,P2D);
  triOsc = new TriOsc (this);
}

void draw(){
  scale = pitchSort(mouseX,scaleList);
  pitch = pitchSort(mouseY,pitchList);
  triOsc.play(midiToFreq(scale,pitch), 0.8);
  println(scale,pitch);
}

float midiToFreq(int s, int p) {
    return(pow(2,(s / 12.0))) * 440  * p;
}

int pitchSort(int num,int[] list){
  int p=-20;
  for (int i=0;i<list.length;i++){
    if(num<list[i]){
      p = list[i];
      break;
    }
      p = list[i];
  }
  return p;
}
