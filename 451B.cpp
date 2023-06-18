#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    int start=-1, end=-1;
    vector<int> v, v1;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
        v1.push_back(x);
    }
    sort(v1.begin(), v1.end());
    for(int i=0; i<n; i++){
        if(v[i]!=v1[i]){
            start=i;
            break;
        }
    }
    for(int i=n-1; i>=0; i--){
        if(v[i]!=v1[i]){
            end=i;
            break;
        }
    }
    if(start==end)cout << "yes" << endl << "1 1";
    else{
        for(int i=end; i>=start; i--){
            if(v[i]!=v1[end-i+start]){
                cout << "no";
                return 0;
            }
        }
        cout << "yes" << endl << start+1 << " " << end+1;
    }
}