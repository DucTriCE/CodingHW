#include <iostream>
#include <vector>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    vector<int> v;
    for (int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    int sereja=0, dima=0, i = 0, left=0, right=n-1;
    while(i!=v.size()){
        int temp=max(v[left], v[right]);
        if(v[left]>=v[right])left++;
        else right--;
        if(i%2==0)sereja+=temp;
        else dima+=temp;
        i++;
    }
    cout << sereja << " " << dima;
}