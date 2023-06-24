#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n, x;
    long long ans=0;
    cin >> n >> x;
    vector<long long> v;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    sort(v.begin(), v.end());
    for(int i=0; i<v.size(); i++){
        ans+=(x*v[i]);
        if(x!=1)x--;
    }
    cout << ans;
}