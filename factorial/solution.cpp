#include <bits/stdc++.h>
using namespace std;

int factorial(int n) {
    // base case
    // this means factorial of 1 is 1 
    if ( n == 1) {
        return 1;
    }
    // the reccurence relation of factorial is:- 
    return n * factorial(n-1);
}

int main() {
    int n;
    cin >> n;

    cout << factorial(n) << endl;
}