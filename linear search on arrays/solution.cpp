#include <bits/stdc++.h>
using namespace std;

int search(int arr[],int len,int ele) {
    if (len == 0) {
        return 0;
    }
    if (ele == arr[0]) {
        return 1;
    } 
    else {
        return search(arr+1,len-1,ele);
    }
}

int main() {
    int arr[] = {1,2,3,4,5};
    int len = sizeof(arr)/sizeof(arr[0]);
    int ele = 40;
    
    if (search(arr,len,ele)) {
        cout << "Element found" << endl;
    }
    else{
        cout << "element not found" << endl;
    }
}