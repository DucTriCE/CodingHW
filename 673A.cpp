#include <iostream>
using namespace std;

int main(){
    int n, ans=0;
    cin >> n;
    if(n==0){
        cout << 15;
        return 0;
    }
    for(int i = 0 ; i < n ; i++){
        int temp;
        cin >> temp;
        if(abs(ans-temp)<=15)ans+=temp-ans;
    }
    if(ans+15<=90)ans+=15;
    else ans=90;
    cout << ans;
}