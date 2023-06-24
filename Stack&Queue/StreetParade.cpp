#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    while(cin>>n){
        vector<int> v(n);
        stack<int> s;
        if(n==0)return 0;
        for(int i=0; i<n; i++)cin>>v[i];
        vector<int> v1 = v;
        sort(v1.begin(), v1.end());
        int j=0, i=0;
        while(i!=v.size()){
            if(v1[j]==v[i]){
                j++;
                i++;
            }
            else if(!s.empty()&&s.top()==v1[j]){
                j++;
                s.pop();
            }
            else {
                s.push(v[i]);
                i++;
            }
        }
        while(!s.empty()&&v1[j]==s.top()){
            j++;
            s.pop();
        }
        if(!s.empty())cout<<"no";
        else cout << "yes";
        cout << endl;
    }
}