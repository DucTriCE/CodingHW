#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main (){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    while(n--){
        string s;
        cin >> s;
        stack<char> operators, brackets;
        for(int i=0; i<s.size(); i++){
            if(s[i]=='(')brackets.push(s[i]);
            else if(s[i]==')'){
                brackets.pop();
                cout << operators.top();
                operators.pop();
            }
            else if(s[i]>='a' && s[i]<='z')cout<<s[i];
            else operators.push(s[i]);
        }
        cout << endl;
    }
}