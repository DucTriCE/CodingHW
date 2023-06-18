#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (){
    int n, a, b, ans=0;
    cin >> n >> a >> b;
    vector<int> v;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    sort(v.begin(), v.end(), greater<int>());
    cout << v[a-1]-v[a];
}