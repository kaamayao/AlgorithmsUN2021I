#include <iostream>
#include <vector>
using std::vector;

long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    long long sum = 0;

    long long current = 0;
    long long next  = 1;

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current;
        }

        long long new_current = next;
        next = next + current;
        current = new_current;
    }

    return sum % 10;
}

int last_digit(long long m, long long n){
	if(n<=1){
		return n;
	}
	long long current = 0;
    long long next  = 1;
    long long suma = 0;

	
    for(int i=0; i<=n; i++ ){
    	if(i>=m){
        	suma = (suma + current)%10;
		}
    	long long new_current = next%10;
        next = (next+current)%10;
        current = new_current;
        
	}
    return suma;
}


int main() {
    long long from, to;
    std::cin >> from >> to;
    std::cout << last_digit(from, to) << '\n';
}
