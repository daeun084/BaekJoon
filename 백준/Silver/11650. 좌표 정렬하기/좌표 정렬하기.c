#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct arr{
  int x;
  int y;
}Arr;
Arr ary[100001];

int compare(Arr *a, Arr *b)
{
if(a->x > b->x) return 1;
else if(a->x < b->x) return -1;
else{
if(a->y > b->y) return 1;
else if(a->y < b->y) return -1;
else return 0;
}
}

int main(void){
int n;
scanf("%d", &n);

for(int i=0; i<n; i++){
    scanf("%d %d", &ary[i].x, &ary[i].y);
}
qsort(ary, n, sizeof(ary[0]), compare);


for(int i=0; i<n; i++){
    printf("%d %d\n", ary[i].x, ary[i].y);
}

    return 0;
}