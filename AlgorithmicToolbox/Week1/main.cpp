#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <bits/stdc++.h>

using namespace std;

long long maxPairwiseProduct(const vector<unsigned long long int>& numbers) {
  long long max_product = 0LL;
  long long aux_product = 0LL;
  int n = numbers.size();

  for (int first = 0; first < n; ++first) {
    for (int second = first + 1; second < n; ++second) {
      aux_product =  (long long) numbers[first] * numbers[second];
      if ( max_product < aux_product)  {
        max_product = aux_product;
      }
    }
  }
  return max_product;
}

long long maxPairwiseProductList(vector<unsigned long long int>& numbers){
  sort(numbers.begin(), numbers.end());
  return numbers[numbers.size()-1]*numbers[numbers.size()-2];
}

long long maxPairwiseProductFast(vector<unsigned long long int>& numbers){  
  long long n = numbers.size();
  int index1 = 0;
  int index2 = 0;
    
  for(int i= 1; i < n; i++){
    if(numbers[i] > numbers[index1]){
      index1 = i;
    }
  }
    
  for(int i= 1; i < n; i++){
    if(i!=index1 && numbers[i]>numbers[index2]){
      index2 = i;
    }
  } 
    
  return numbers[index1]*numbers[index2];
}

int main() {
  int n;
  cin >> n;
  unsigned long long int maxNumber = 0LL;
  unsigned long long int maxSecondNumber = 0LL;
  unsigned long long int aux = 0LL;
  vector <unsigned long long int> numbers (n);

  auto start = chrono::high_resolution_clock::now();

  for (int i = 0; i < n; ++i) {
    cin >> numbers[i];;
    if(maxNumber < numbers[i]){
      maxSecondNumber = maxNumber;
      maxNumber = numbers[i];
    } else if(maxSecondNumber < numbers[i]){
      maxSecondNumber = numbers[i];
    }
  }

  unsigned long long int maxProductUltraFast = maxNumber * maxSecondNumber;
  
  auto stop = chrono::high_resolution_clock::now();

  auto ms_int = chrono::duration_cast<chrono::milliseconds>(stop - start);
  auto reading_time = ms_int.count();

  cout << "Result using Ultra Fast method: " << maxProductUltraFast << endl;
  cout << "Execution time: " << ms_int.count() << " ms" << endl;

  cout << endl;

  start = chrono::high_resolution_clock::now();
  cout << "Result using Fast method: " << maxPairwiseProductFast(numbers) << endl;
  stop = chrono::high_resolution_clock::now();
  ms_int = chrono::duration_cast<chrono::milliseconds>(stop - start);
  cout << "Execution time: " << reading_time + ms_int.count() << " ms" << endl;

  cout << endl;
  
  start = chrono::high_resolution_clock::now();
  cout << "Result using List method: " << maxPairwiseProductList(numbers) << endl;
  stop = chrono::high_resolution_clock::now();
  ms_int = chrono::duration_cast<chrono::milliseconds>(stop - start);
  cout << "Execution time: " << reading_time + ms_int.count() << " ms" << endl;

  cout << endl;

  start = chrono::high_resolution_clock::now();
  cout << "Result using naive method: " << maxPairwiseProduct(numbers) << endl;
  stop = chrono::high_resolution_clock::now();
  ms_int = chrono::duration_cast<chrono::milliseconds>(stop - start);
  cout << "Execution time: " << reading_time + ms_int.count() << " ms" << endl;
  return 0;
}
