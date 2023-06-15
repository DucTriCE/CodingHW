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
    int j=0, i=0;
    while(i!=v2.size()){
        if(v2[i]-y<=v1[j] && v2[i]+x>=v1[j]){
            vans.push_back(make_pair(j+1, i+1));
            j++;
            if(j==v1.size())break;
            i++;
        }else if(v2[i]-y<v1[j] && v2[i]+x<v1[j])i++;
        else{
            j++;
            if(j==v1.size())break;
        }
    }
    cout << vans.size() << endl;
    if(vans.size()!=0){
        for(int i=0; i<vans.size(); i++){
            cout << vans[i].first << " " << vans[i].second << endl;
        }
    }
}