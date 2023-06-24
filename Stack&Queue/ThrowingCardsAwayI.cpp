#include <iostream>
#include <queue>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n, c;
    while(cin >> n >> c){
        if(n==0&&c==0)return 0;
        cout << "Case 1:" << endl;
        queue<int> q;
        for(int i=1; i<=n; i++)q.push(i);
        for(int i=0; i<c; i++){
            string s;
            cin >> s;
            if(s[0]=='N'){
                cout 
            }
        }
    }
}