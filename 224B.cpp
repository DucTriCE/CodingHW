#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(){
    int n, k, left = 0, right;
    cin >> n >> k;
    vector<int> v(n), vans;
    for(int i = 0 ; i < n ; i++)cin>>v[i];
    set<int> st, st1;
    for(int i = 0 ; i < n ; i++){
        st.insert(v[i]);
        if(st.size()<=k){
            vans.push_back(v[i]);
            right = i;
            if(st.size()==k)break;
        }
    }
    if(st.size()<k){
        cout << "-1 -1";
        return 0;
    }
    for(int i = vans.size()-1 ; i >=0 ; i--){
        st1.insert(vans[i]);
        if(st1.size()<=k){
            left = i;
            if(st1.size()==k)break;
        }
    }
    cout << left + 1 << " " << right+1;
}