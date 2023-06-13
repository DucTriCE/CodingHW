#include <iostream>
#include <vector>
using namespace std;

int main(){
    int mi = 9999999999, ma = -1;
    int n;
    cin >> n;
    vector<vector<int>> v(n);
    for(int i = 0 ; i < n; i++){
        int a, b;
        cin >> a >> b;
        v[i].push_back(a);
        v[i].push_back(b);
        if(a<mi)mi=a;
        if(b>ma)ma=b;
    }
    for(int i = 0 ; i < n ; i++){
        if(v[i][0]==mi && v[i][1]==ma){
            cout << i+1;
            return 0;
        }
    }
    cout << "-1";
}