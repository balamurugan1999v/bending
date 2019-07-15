#include <iostream>
#include<string.h>
using namespace std;

int main() {
	int ij[100],d,a1=1,i,j,n,c;
	char a[100][100],b[100][100],temp[100];
	for(i=0;i<2;i++)
	cin>>a[i];
	for(i=0;i<2;i++)
	{
		d=0;a1=0;
		for(j=0;a[i][j]!='#';j++)
		{
			b[i][j]=a[i][j];
		}
		j++;
		for(;1;j++)
		{
			if(a[i][j]=='\0')
			break;
			else if(a[i][j]=='#')
			{
				d=a1+d;
				a1=0;
				break;
			}
			c=(int)a[i][j];
			a1=a1*10+c;
		}
		ij[i]=d;
	}
	(ij[0]>ij[1])?strcpy(temp,b[0]):strcpy(temp,b[1]);
	cout<<temp;
		return 0;
}
