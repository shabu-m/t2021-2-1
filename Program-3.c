#include<stdio.h>
int main()
{
	int n,i,j;
	scanf("%d",&n);
	printf("input a = %d ",n);
	printf("\n");
	printf("output : ");
	if(n%2==0)
	{
		n=n-1;
		for(j=1,i=1;j<=n;i=i+2,j++)
  	{
	  	printf("%d ",i);
  	}
	}
	else
  {
  	for(j=1,i=1;j<=n;i=i+2,j++) 	
  	{ 	
  	  printf("%d ",i); 
  	 }
   }		 
}
