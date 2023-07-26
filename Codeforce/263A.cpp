#include <iostream>
#include <vector>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    vector<vector<int>> v(5, vector<int>(0,0));
    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++)cout << v[i][j];
    }
}