#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    vector<int> v;
    set<int> st;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
        st.insert(x);
    }
    sort(v.begin(), v.end(), greater<int>());
    int ans=1, temp=1;
    for(int i=1; i<n; i++){
        if(v[i]==v[i-1])ans=max(ans,++temp);
        else temp=1;
    }
    cout << ans << " " << st.size();
    //Use map[x]++ and store in a max variable in input loop
}