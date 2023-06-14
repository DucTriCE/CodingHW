#include <iostream>
#include <vector>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    vector<int> v1, v2;
    vector<pair<int, int>> vans;
    int n, m, x ,y;
    cin >> n >> m >> x >> y;
    for (int i=0; i<n; i++){
        int x;
        cin >> x;
        v1.push_back(x);
    }
    for (int i=0; i<m; i++){
        int x;
        cin >> x;
        v2.push_back(x);
    }
    int i=v2.size()-1;
    while(i>=0){
        int j = v1.size()-1;
        cout << v2[i] << " " << v1[j] << endl;
        if(v2[i]-x==v1[j] || v2[i]+y==v1[j]){
            vans.push_back(make_pair(i+1, j+1));
            v1.pop_back();
            i--;
            if(v1.empty())break;
        }
        else i--;
    }
    cout << vans.size() << endl;
    for(int i=0; i<vans.size(); i++){
        cout << vans[i].first << " " << vans[i].second << endl;
    }
}