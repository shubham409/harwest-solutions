#include <iostream>
#include <stack>
#include <vector>
#include <map>
#include <ostream>
#include <algorithm>
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

int solve(vector<int> & obj){
    map<int,int>count=counter<int,int ,vector<int>>(obj);
    vectorofint sorted = vector(obj);
    sort(sorted.begin(),sorted.end());
    for (int x:sorted){
        if(count[x]==1)
            return (find(obj.begin(),obj.end(),x)-obj.begin())+1;
    }
    return -1;
}
int main() {
    int t;
    cin>>t;
    loop(i,t) {
        int n ;
        input(n);
        vector<int> vt(n);
        loop(j,n){
            input(vt[j]);
        }
        int ans=solve(vt);
        println(ans);
    }
    return 0;
}
