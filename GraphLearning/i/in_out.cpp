#include <bits/stdc++.h>
using namespace std;

int main() {
	int n,m;
	cin>>n>>m;
    //creating adj matrix, to see which vertex is connected with which vertex 
	vector<vector<int>>adj(n+1,vector<int>(n+1));
	for(int i=0;i<m;i++){
	    int u,v;
	    cin>>u>>v;
	    adj[u][v] = 1;
	    adj[v][u] = 1;
	}
	for(int i=1;i<=n;i++){
	    for(int j=1;j<=n;j++){
	        cout<<adj[i][j]<<' ';
	    }
	    cout<<"\n";
	}
}
