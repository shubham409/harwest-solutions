#include <iostream>
#include <stack>
#include <vector>
#include <map>
#include <ostream>
#include <algorithm>
#include <type_traits>
#include <cstdlib>
using namespace std;
#define vectorofint  vector<int>
#define vectorofstring vector<string>
#define vectoroflong vector<long>
#define vectoroflonglong vector<long long>
#define input(x) cin>>x
#define print(x) cout<<x<<" "
#define println(x) cout<<x<<endl
#define newline cout<<endl;
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
int solve(vector<int> & obj){
    return -1;
}
string solve(string s1,string s2){
    string ans;
    for (int i = 0; i <s1.length() ; ++i) {
        ans.append(to_string((int)(s1[i])^(int)(s2[i])));
    }
    return ans;
}
int main() {
//    int t;
//    cin>>t;
//    loop(i,t) {
//        int n ;
//        input(n);
//        vector<int> vt(n);
//        loop(j,n){
//            input(vt[j]);
//        }
//        int ans=solve(vt);
//        println(ans);
//    }
    string s1;input(s1);
    string s2;input(s2);
    string ans = solve(s1,s2);
    println(ans);

    return 0;
}