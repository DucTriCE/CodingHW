    #include <iostream>
    #include <vector>
    using namespace std;

    int main (){
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        int n;
        cin >> n;
        while(n!=0){
            string s;
            cin >> s;
            if(s.size()<=10)cout<<s;
            else cout << s[0] << s.size()-2 << s[s.size()-1];
            n--; cout << endl;
        }
    }