#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(void){
int n, com, result=0, k;
scanf("%d", &n);
scanf("%d", &com);
int **ary =(int**)malloc(sizeof(int*)*com);

for(int i=0; i<com; i++){
ary[i]= (int*)malloc(sizeof(int)*2);
scanf("%d %d", &ary[i][0], &ary[i][1]);
}

for(int i=0; i<com; i++){
if(ary[i][0]*ary[i][1]!=1){

if(ary[i][0]==1){
    k = ary[i][1];
    for(int p=0; p<com; p++)
    for(int t=0; t<2; t++){
        if(k==ary[p][t])
        ary[p][t]=1;
    }
result++;
i=-1;
}
else if(ary[i][1]==1){
k = ary[i][0];
for(int p=0; p<com; p++)
    for(int t=0; t<2; t++){
        if(k==ary[p][t])
        ary[p][t]=1;
    }
result++;
i=-1;
}

}}

printf("%d\n", result);

return 0;
}