#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  unsigned long long int maxNumber = 0LL;
  unsigned long long int maxSecondNumber = 0LL;
  unsigned long long int aux = 0LL;
  auto start = chrono::high_resolution_clock::now();

  for (int i = 0; i < n; ++i) {
    cin >> aux;
    if(maxNumber < aux){
      maxSecondNumber = maxNumber;
      maxNumber = aux;
    } else if(maxSecondNumber < aux){
      maxSecondNumber = aux;
    }
  }

  unsigned long long int maxProductUltraFast = maxNumber * maxSecondNumber;
  
  auto stop = chrono::high_resolution_clock::now();
  auto ms_int = chrono::duration_cast<chrono::milliseconds>(stop - start);
  auto reading_time = ms_int.count();

  cout << "Result using Ultra Fast method: " << maxProductUltraFast << endl;
  cout << "Execution time: " << ms_int.count() << " ms" << endl;

  return 0;
}
