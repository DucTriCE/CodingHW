#include <iostream>
#include <vector>
using namespace std;

int main (){
    int n, m;
    cin >> n >> m;
    vector<int> v1, v2;
    for (int i=0; i<n; i++){
        int x;
        cin >> x;
        v1.push_back(x);
    }
    for (int i=0; i<m; i++){
        int x;
        cin >> x;
        v2.push_back(x);
    }
    int j = m-1, temp = n;
    for (int i =temp-1; i>=0 ;i--){ 
        if(v2[j]>=v1[i]){
            n-=1;
            j--;
            if(j<0)break;
        }
        else continue;
    }
    cout << n;
}