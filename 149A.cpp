#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int k;
    cin >> k;
    vector<int> v;
    for(int i=0; i<12; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    if(k==0)cout<<"0";
    else{
        sort(v.begin(), v.end(), greater<int>());
        for(int i=0; i<12; i++){
            k-=v[i];
            if(k<=0){
                cout << i+1;
                return 0; 
            }
        }
        cout << "-1";
    }
}