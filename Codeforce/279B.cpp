#include <iostream>
#include <vector>
using namespace std;

int main (){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n, t, sum=0, ans=0;
    cin >> n >> t;
    vector<int> v, v1(n+1, 0);
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    for(int i=1; i<=n; i++){
        v1[i]=(v1[i-1]+v[i-1]);
    }
    int j=0, i=1;
    while(i!=v1.size()){
        sum=v1[i]-v1[j];
        if(sum<=t){
            ans = max(ans, i-j);
            i++;
        }else j++;
    }
    cout << ans;
}