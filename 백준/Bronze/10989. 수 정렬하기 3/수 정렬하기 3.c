#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
int n, ary[10001]={0}, num;
scanf("%d", &n);

for(int i=0; i<n; i++){
scanf("%d", &num);
ary[num]++;
}

for(int i=0; i<10001; i++){
if(ary[i]==0) continue;

for(int j=0; j<ary[i]; j++)
printf("%d\n", i);

}
    return 0;
}
