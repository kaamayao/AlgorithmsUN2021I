#include <iostream>

int fibonacci_sum_squares_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current * current;
    }

    return sum % 10;
}

int last_digit(long long n){
	if(n<=1){
		return n;
	}
	long long previous = 0;
    long long current  = 1;
    long long suma = previous + current;

	
    for(int i=2; i<=n; i++ ){
    	long long tmp_previous = previous%10;
        previous = current%10;
        current = (tmp_previous + current)%10;
        suma = (suma + current*current)%10;
	}
    return suma;
}

long long last_digit_2(long long n){
	if(n<=1){
		return n;
	}
	n = n %60;
	long long previous = 0;
    long long current  = 1;
    long long suma = 0;

	
    for(int i=2; i<=n+1; i++ ){
    	long long tmp_previous = previous%10;
        previous = current%10;
        current = (tmp_previous + current)%10;
	}
    return (current*previous)%10;
}

int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << last_digit_2(n);
}
