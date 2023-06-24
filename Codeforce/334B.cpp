#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    set<int> stx, sty;
    set<pair<int,int>> stp;
    vector<pair<int,int>> v;
    for(int i=0; i<8; i++){
        int x,y;
        cin >> x >> y;
        stx.insert(x);
        sty.insert(y);
        stp.insert(make_pair(x,y));
        v.push_back(make_pair(x,y));
    }
    if(stx.size()!=3||sty.size()!=3||stp.size()!=8){
        cout << "ugly";
    }else{
        set<int>::iterator it = stx.begin();
        set<int>::iterator it2 = sty.begin();
        int x2=*++it, y2=*++it2;
        for(int i=0; i<8; i++){
            if(v[i].first==x2 && v[i].second==y2){
                cout << "ugly";
                return 0;
            }
        }
        cout << "respectable";
    }
}