// g++ sinperiodamp.cpp -o sin]periodamp.o
#include <iostream>
#include <cmath>
using namespace std;

double round4(double var)
{  double value;
    if (var < 0){
          value = (int)(var * 10000 - 0.00005);
        }
      else{
            value = (int)(var * 10000 + 0.0005);
        }
      return (double)value / 10000;
}

int main (){
double PI=3.14159265;
double a,p,t, rad,sr,aspr;
// (t)theta rad(radian) sr(sine result)
// aspr (amplitude * sine (period*t))
  cout << "\nInput an amplitude : ";
  cin>>a;
  cout<<"\nInput a period : ";
  cin>>p;
  cout <<"Theta\tsin(t)\t*sin(pt) \n";
  for ( t=0 ; t<=360 ; t = t + 15 )
  {
    rad = t * (PI / 180);
    sr= sin(rad);
    aspr = a*sin(p*rad);
    cout<<t<<"\t"<<round4(sr)<<"\t"<<aspr<<"\n";
  }
  return 0;
}
