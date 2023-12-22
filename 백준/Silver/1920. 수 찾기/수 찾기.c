#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare(void* a, void* b)
{
    if(*(int*)a > *(int*)b)
        return 1;
    if(*(int*)a == *(int*)b)
        return 0;
    return -1;
}

int search(int *ary, int n, int num){
int low=0, mid, high=n-1;

while(low<=high){
    mid = (low+high)/2;
    if(ary[mid]==num) return 1;
    else if(ary[mid]<num)
    low=mid+1;
    else if(ary[mid]>num)
    high = mid-1;
}
return 0;
}

int main(void){
int n1, n2, num;

scanf("%d", &n1);
int *ary = (int*)malloc(sizeof(int)*n1);
for(int i=0; i<n1; i++)
scanf("%d", &ary[i]);

qsort(ary, n1, sizeof(int), compare);

scanf("%d", &n2);
for(int i=0; i<n2; i++){
    scanf("%d", &num);
    printf("%d\n", search(ary, n1, num));
}

    return 0;
}
