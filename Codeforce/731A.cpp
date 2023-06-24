#include <iostream>
using namespace std;


int main(){
    string s;
    cin >> s;
    int ans=0;
    ans+=min(s[0]-'a', abs(s[0]-'z')+1);
    for(int i = 1; i < s.size() ; i++){
        if(s[i]=='a')ans+=min(s[i-1]-'a', 'z'-s[i-1]+1);
        else if(s[i]=='z')ans+=min(s[i-1]-'a'+1, 'z'-s[i-1]);
        else if(s[i-1]>s[i])ans+=min(s[i-1]-s[i], 'z'-s[i-1]+1+s[i]-'a');
        else ans+=min(s[i]-s[i-1], s[i-1]-'a'+'z'-s[i]+1);
    }
    cout << ans;
}