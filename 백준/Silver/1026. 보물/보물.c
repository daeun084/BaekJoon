#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
int n, result=0;
scanf("%d", &n);
int *a =(int*)malloc(sizeof(int)*n);
int *b = (int*)malloc(sizeof(int)*n);

for(int i=0; i<n; i++)
scanf("%d", &a[i]);
for(int i=0; i<n; i++)
scanf("%d", &b[i]);

//a 오름차순, b내림차순 정렬 후 곱하기

for(int i=0; i<n; i++)
for(int j=n-1; j>i; j--){
if(a[j]<a[j-1]){
    int tmp = a[j];
    a[j] = a[j-1];
    a[j-1]=tmp;
}
if(b[j]>b[j-1]){
    int tmp=b[j];
    b[j]=b[j-1];
    b[j-1]=tmp;
}

}

for(int i=0; i<n; i++)
result+=a[i]*b[i];

printf("%d\n", result);



return 0;
}