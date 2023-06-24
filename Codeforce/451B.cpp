#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    int start=-1, end=-1;
    vector<int> v, v1;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
        v1.push_back(x);
    }
    sort(v1.begin(), v1.end());
    for (int i = 0; i < n; i++) {
        if (start == -1 && v[i] != v1[i])start = i;
        if (v[i] != v1[i])end = i;
    }   
    if(start==end)cout << "yes" << endl << "1 1";
    else if(is_sorted(v.begin()+start, v.begin()+end+1, greater<int>())==true){
        cout << "yes" << endl << start+1 << " " << end+1;
    }else cout << "no";
}