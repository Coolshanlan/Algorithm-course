#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define A 5.99898687687768768767686798
#define B 0.77774758979798798798798403

int main() {
  float a = A * 11 * 11 * 11 * 11 * 11 * 11 /
            (A * B * A * B * A * B * A * B * A * B * A * B);
  float b = 11 / (A * B);
  float c = A * b * b * b * b * b * b;
  printf("%.20f\n", a);
  printf("%.20f", c);
}