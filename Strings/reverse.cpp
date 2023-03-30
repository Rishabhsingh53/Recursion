#include <bits/stdc++.h>
using namespace std;

void reverse(string &str,int i,int j) {
    if (i > j) {
        return ;
    }
    swap(str[i],str[j]);
    i++;
    j--;
    reverse(str,i,j);
}


int main() {
    string str = "rishabh";

    cout << "Given string is:\t" << str<< endl;
    reverse(str,0,str.length()-1);
    cout << "String after processing \t" << str << endl;
}


// h e l l o 
// 