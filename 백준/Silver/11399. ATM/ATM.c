#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

int mul(int *ary, int n){
int result=0;
for(int i=0; i<n; i++)
for(int j=0; j<=i; j++)
result+=ary[j];

    return result;
}

int main(void){
int n, result;
scanf("%d", &n);
int *ary = (int*)malloc(sizeof(int)*n);

for(int i=0; i<n; i++)
scanf("%d", &ary[i]);

for(int i=0; i<n; i++)
for(int j=n-1; j>i; j--){
    if(ary[j]<ary[j-1]){
        int tmp = ary[j];
        ary[j]=ary[j-1];
        ary[j-1] = tmp;
    }
}
result= mul(ary, n);
printf("%d\n", result);
free(ary);
return 0;
}