#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    vector<pair<int,int>> v;
    for(int i=0; i<n; i++){
        int x,y;
        cin >> x >> y;
        v.push_back(make_pair(x,y));
    }
}