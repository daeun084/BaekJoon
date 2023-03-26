#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(void) {
int n,m,i,j;
scanf("%d %d", &n, &m);

int **ary = (int**)malloc(sizeof(int*)*2);

ary[0]=(int*)malloc(sizeof(int)*n);
ary[1]=(int*)malloc(sizeof(int)*n); //누적합 기재

for(int k=0; k<n;k++ ){
  scanf("%d", &ary[0][k]);
}
ary[1][0]=ary[0][0];
for(int k=1; k<n; k++){
  ary[1][k] = ary[1][k-1]+ary[0][k];
}

while(m-- >0){
scanf("%d %d", &i, &j);

printf("%d\n", ary[1][j-1]-ary[1][i-2]);
}

}