#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n, check=0;
    vector<int> v, v1, vans(2);
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
        v1.push_back(x);
    }
    sort(v1.begin(), v1.end());
    for(int i=0; i<n; i++){
        if(v1[i]!=v[i]){
            check++;
            if(check<=2)vans.push_back(i+1);
            else{
                cout << "no";
                return 0;
            } 
        }
    }
    cout << "yes" << endl;
    cout << vans[0]<< " " << vans[1];
}