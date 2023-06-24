#include <iostream>
#include <vector>
using namespace std;
 
int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    vector<int> v;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    int pos=0, i=1, ma=v[0], mi=v[0], ans=1, temp;
    while(i!=v.size()){
        if(v[i]>v[i-1]){
            if(v[i]-mi>1){
                mi=ma;
                ma=v[i];
                ans=max(ans, i-pos);
                pos=temp;
                temp=i;
            }else{
                temp=i;
                ma=v[i];
            }
        } else if(v[i]<v[i-1]){
            if(ma-v[i]>1){
                ma=mi;
                mi=v[i];
                ans=max(ans, i-pos);
                pos=temp;
                temp=i;
            }else{
                temp=i;
                mi=v[i];
            } 
        }
        i++;
        if(i==v.size())ans=max(ans, i-pos);
    }
    cout << ans;
}