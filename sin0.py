// g++ sin0.cpp -o sin0.o
#include <iostream>
#include <cmath>
//using namespace std;
int main (){
double PI=3.14159265
double t, result=0;// theta
  for ( t=0 ; t<=260 ; t = t + 15 )
  {
  result = sin(t);
    cout <<t<<"\t"<< result<<endl;

  }
  return 0;
}
