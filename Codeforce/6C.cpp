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
    int x=0, i=v.size()-1;
    while(i>=0){
        if(v[i]>x){
            if(v[i]>i){
                n-=i;
                break;
            }else x=v[i];
        }
        if(x>0)n-=1;
        x--;
        i--;
    }
    cout << n;
}
