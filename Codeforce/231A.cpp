#include <iostream>
#include <vector>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    int ans=n;
    while(n!=0){
        int a, b, c;
        cin >> a >> b >> c;
        if(a+b+c<2)ans--;
        n--;
    }
    cout << ans;
}