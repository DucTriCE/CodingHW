#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n, w;
    cin >> n >> w;
    vector<int> v;
    for(int i=0; i<2*n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    sort(v.begin(), v.end());
    float minboy = (float)v[n]/2, mingirl=v[0];
    float m = min(minboy, mingirl);
    cout << fixed << setprecision(10) << min((float)w,3*n*m);
}