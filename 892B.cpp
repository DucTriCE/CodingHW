#include <iostream>
#include <vector>
using namespace std;

int main (){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n; 
    cin >> n;
    vector<int> v;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    int left=0, right=n-1;
    if(n==1)cout << "1 0";
    else{
        while(left<=right){
            if(v[left]>v[right]){
                v[left]-=v[right];
                right--;
                if(left==right){
                    right++;
                    break;
                }
            } else if(v[right]>v[left]){
                v[right]-=v[left];
                left++;
                if(left==right){
                    left--;
                    break;
                }
            } else{
                left++;
                right--;
                if(left==right){
                    right++;
                    break;
                }else if(left>right){
                    left--;
                    right++;
                    break;
                }
            }
        }
        cout << left+1 << " " << n-right;
    }
}
