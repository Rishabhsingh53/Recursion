#include <bits/stdc++.h>
using namespace std;

bool binarySearch(int arr[],int start,int end,int ele) {
    if (start > end) {
        return false;
    }
    int mid = (start) + (end-start) / 2;

    if (ele == arr[mid]) {
        return true;
    }
    else if (ele > arr[mid]) {
        return binarySearch(arr,mid+1,end,ele);
    }
    else {
        return binarySearch(arr,start,mid,ele);
    }
}

int main() {
    int arr[10] = {1,2,3,4,5,6,7,8,9};
    int size = sizeof(arr)/sizeof(arr[0]);
    int ele = 90;
    if (binarySearch(arr,0,size-1,ele)) {
        cout << "found";
    }
    else {
        cout << "not found";
    }
} 
