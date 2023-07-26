#include <iostream>
#include <vector>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    int x=0;
    while(n!=0){
        string s;
        cin >> s;
        if(s[1]=='+')x++;
        else x--;
        n--;
    }
    cout << x;
}