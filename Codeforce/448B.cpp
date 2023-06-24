#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    string s, t;
    cin >> s >> t;
    map<char, int> sm, tm;
    bool check=true;
    for(int i=0; i<s.size(); i++)sm[s[i]]++;
    for(int i=0; i<t.size(); i++)tm[t[i]]++;
    for(auto i=tm.begin(); i!=tm.end(); i++){
        if(sm[i->first]<i->second){
            check=false;
            break;
        }
    }
    if(t.size()>s.size() || check==false)cout << "need tree";
    else if(t.size()==s.size())cout << "array";
    else{
        int j=0;
        for(int i=0; i<s.size(); i++){
            if(s[i]==t[j])j++;
            else continue;
        }
        if(j==t.size())cout<<"automaton";
        else cout << "both";
    }
}
