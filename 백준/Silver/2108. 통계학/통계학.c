#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int compare1(void* a, void* b)
{
    if(*(int*)a > *(int*)b)
        return 1;
    if(*(int*)a == *(int*)b)
        return 0;
    return -1;
}


int main(void) {

int n, cnt[8001]={0};
scanf("%d", &n);
double p1=0;  

int *ary = (int*)malloc(sizeof(int)*n);

for(int i=0; i<n; i++){
scanf("%d", &ary[i]);

p1+=ary[i];
}

//1.산술평균
p1/=n;
if((int)(p1*10)%10>=5 && p1>0) p1+=1;
else if((int)(p1*10)%10<=-5) p1-=1;
printf("%d\n", (int)p1); 


//2.중앙값
qsort(ary, n, sizeof(int), compare1);
printf("%d\n", ary[(n-1)/2]);


//3.최빈값
for(int i=0; i<n; i++)
cnt[ary[i]+4000]++;

int max=cnt[0], index=0;
for(int i=0; i<8001; i++){
  if(cnt[i]>max){
    max=cnt[i];
    index=i;
}}

for(int i=index+1; i<8001; i++){
  if(cnt[i]==max) {
    index=i;
    break;
  }
}   
printf("%d\n", index-4000);

//4.범위
printf("%d\n", ary[n-1]-ary[0]);

	return 0;

}