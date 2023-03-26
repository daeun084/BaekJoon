#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
int m, n, count=0;
scanf("%d %d", &m, &n);

//에라토스테네스의 체
int *ary = (int*)malloc(sizeof(int)*(n+1));
for(int i=2; i<=n; i++)
ary[i]=i;

for(int i=0; i<=n; i++){
    //이미 0으로 지우면 건너뛰기
    if(ary[i]==0) continue;

    //가능한 배수 모두 0으로 지우기
    for(int j=2*i; j<=n; j+=i){
        ary[j]=0;
    }
}

int i;
for(i=m; i<=n; i++){
    if(ary[i]!=0)
        printf("%d\n", ary[i]);
}
    return 0;
}
