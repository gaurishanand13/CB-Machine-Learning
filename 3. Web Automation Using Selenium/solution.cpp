#include<iostream>
#include<cmath>
#include<vector>
#include<string.h>
#include<utility>
#include<set>
#include<algorithm>
#include<queue>
#include<unordered_map>
#include<stack>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        if(n==0 || k==0){
            cout<<0<<endl;
            continue;
        }
        else{
            if(n==k){
                if(n%2==0){
                    cout<<n<<endl;
                }
                else{
                    cout<<(n+1)<<endl;
                }
            }
            else if(n>k){
                int total_count = (n/2);
                if(total_count>=k){
                    cout<<k<<endl;
                }
                else{
                    if(n%2==0){
                        cout<<total_count<<endl;
                    }
                    else{
                        if((total_count+1)<=k){
                            cout<<total_count+1<<endl;
                        }
                        else{
                            cout<<total_count<<endl;
                        }
                    }
                }
            }
            else{
                int total_count = (k/2);
                if(total_count>=n){
                    cout<<n<<endl;
                }
                else{
                    if(k%2==0){
                        cout<<total_count<<endl;
                    }
                    else{
                        if((total_count+1)<=n){
                            cout<<total_count+1<<endl;
                        }
                        else{
                            cout<<total_count<<endl;
                        }
                    }
                }
            }
        }
    }
}