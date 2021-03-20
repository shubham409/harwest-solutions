#include <iostream>
#include <stack>
#include <vector>
#include <map>
#include <ostream>
#include <algorithm>
#include <type_traits>
#include <cstdlib>
#include <sstream>
#include <stdio.h>
using namespace std;
#define vectorofint  vector<int>
#define vectorofstring vector<string>
#define vectoroflong vector<long>
#define vectoroflonglong vector<long long>
#define input(x) cin>>x
#define print(x) cout<<x<<" "
#define println(x) cout<<x<<endl
#define newline() cout<<endl;
#define loop(i,n) for(int i=0; i<n; i++)

template<typename first,typename second, typename input>
map<first,second> counter( input & obj ){
    map<first,second>ans;
    for(first i : obj){
        ans[i]++;
    }
    return ans;
}
void show(){
//    parameter pack in cpp
}
template<typename arg,typename ...args>
void show(arg var,args... vars){
    cout<< var<<" " ;
    show(vars...);
}
//int solve(vector<int> & obj){
//    return -1;
//}
void solve(vector<int > &v){
    sort(v.begin(),v.end());
    for (int x: v){
        print(x);
    }
    newline();
}
string solve(string s1,string s2){
    return "";
}
int stringtoint(const char *s){
//    1. using string stream apllicable to int float and double etc
    stringstream mystream(s);
    int ans;
    mystream>>ans;
    return ans;
//    2. using stoi cpp style atoi  (c style legacy clss to convert char array to int )
//    int stoi (const string&  str, size_t* index = 0, int base = 10);
    int a=stoi(s);
//    3.use sscanf c style
    int c;
    sscanf(s,"%d",&c);
//
}
int main() {
    int t;
    input(t);
//    loop(i,t) {
//        int n ;
//        input(n);
        vector<int> vt(t);
        loop(j,t){
            input(vt[j]);
        }
        solve(vt);
//        println(ans);
//    }


    return 0;
}