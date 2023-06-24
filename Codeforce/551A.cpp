#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    vector<int> v, v1;
    map<int, int> mp;
    cin >> n;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
        v1.push_back(x);
    }
    sort(v1.begin(), v1.end(), greater<int>());
    int curr=v1[0], diff=1, temp=0;
    for(int i=0; i<n; i++){
        if(v1[i]<curr){
            diff+=i-temp;
            temp=i;
        }
        mp[v1[i]]=diff;
        curr=v1[i];
    }
    for(int i=0; i<n; i++)cout<<mp[v[i]]<<" ";
}