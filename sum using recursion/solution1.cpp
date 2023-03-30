#include <bits/stdc++.h>
using namespace std;

int SuM(int arr[],int len) {
    if (len == 0) {
        return 0;
    }
    return arr[0] + SuM(arr+1,len-1);
}

int main() {
    int arr[] = {1,2,3,4,5};
    int len = sizeof(arr) / sizeof(arr[0]);
    cout << SuM(arr,len);
}
