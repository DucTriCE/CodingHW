#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int main (){
    while(1){
        int n;
        cin >> n;
        if(n==0)return 0;
        vector<int> v, v1;
        for(int i=0; i<n; i++){
            int x;
            cin >> x;
            v.push_back(x);
            v1.push_back(x);
        }
        cout << "OK";
        stack<int> s;
        sort(v1.begin(), v1.end());
        int j=0;
        for(int i=0; i<v.size(); i++){
            if(v[i]!=v[j])s.push(v[i]);
            else j++;
        }
        while(v1[j]==s.top() && s.empty()==false){
            s.pop();
            j++;
        }
        if(s.empty()!=true)cout << "no";
        else cout << "yes";
        cout << endl;
    }
}