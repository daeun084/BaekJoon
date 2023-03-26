#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int fun1(int k){//소수찾기
if(k==1) return 0;
if(k==2) return 1;
if(k==3) return 1;

for(int i=2; i<=k/2; i++){
if(k%i==0)
    return 0;
}
    return 1;
}

int fun2(int k){
int tmp = k;
int plus = 0;
while(1){
plus+=tmp%10;
tmp/=10;

if(tmp==0) break;

plus *=10;
}

if(plus==k)return 1;
else return 0;
}

int main(void){
int n;
scanf("%d", &n);
int k=n;

while(1){
if(1==fun2(k) &&fun1(k)==1 ){
    printf("%d\n", k);
    return 0;
}
else k+=1;
}
}