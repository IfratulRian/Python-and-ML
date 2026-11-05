#include<bits/stdc++.h>
using namespace std;
#define O_amay_BHaloBashe_Nai() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define endl '\n'
#define ll long long
#define all(v) v.begin(),v.end()
#define pb push_back
#define MAX 1000001
#define MOD 998244353
#define in insert 
// string yy = "YES";
// string nn = "NO";
#define yy cout<<"YES"<<endl;
#define nn cout<<"NO"<<endl;

const int MAXA = 1e6 + 5;

void solve(){
    int m,n;
    cin>>n>>m;
    //vector<vector<int>>adj(n+1,vector<int>(n+1));
    vector<int>adj[n+1];
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        // adj[u][v]=1;
        // adj[v][u]=1;
        adj[u].pb(v);
        adj[v].pb(u);
    }
    // for(int i=1;i<n+1;i++){
    //     cout<<i<<" ->";
    //     for(int j=0;j<n+1;j++){
    //         if(adj[i][j]==1)cout<<' '<<j;
    //         // else cout<<endl;
    //     }
    //     cout<<endl;
    // }
    for(int i=1;i<=n;i++){
        // cout<<i<<" ->";
        // for(auto x:adj[i]){
        //     cout<<' '<<x;
        // }
        // cout<<endl;
        cout<<adj[i].size()<<' ';
    }
}

int main(){
    O_amay_BHaloBashe_Nai();
    //solve();
    int t;
    t=1;
    //cin>>t;
    while(t--){
        solve();
    }
    return 0;
}