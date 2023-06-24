#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> a;
    vector<int> b;  
    int na, nb, k, m;
    cin >> na >> nb >> k >> m;
    for (int i = 0 ; i < na ; i++){
        int temp;
        cin >> temp;
        a.push_back(temp);
    }
    for (int i = 0 ; i < nb ; i++){
        int temp;
        cin >> temp;
        b.push_back(temp);
    }
    if(a[k-1]<b[nb-m])cout<<"YES";
    else cout << "NO";
}