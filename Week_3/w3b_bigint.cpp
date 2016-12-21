// AUTHOR Vrushali M vmahajan@bu.edu

//#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef string BigInt;
typedef vector<int> Poly;

void correct_carries(Poly &r)
{
	int change = 1;
	while(change == 1)
	{
		change = 0;
		for(int i=0;i < r.size();i++)
		{
			if(r[i] > 9)
			{
			   r[i - 1] += r[i]/10;
			   r[i] = r[i]%10;
			   change = 1;
			}      	
		}
	}
}

BigInt multiply_int(const BigInt &a,const BigInt &b)
{
	Poly c;
	Poly d;
	Poly result_int;
	BigInt result_str;

	for(int i=0; i < a.size() ; i++)
	{   
		c.push_back(int(a[i] - '0'));	//'0' has the value of 0x30 which is = 48 in decimal
	}
	for(int i=0; i < b.size() ; i++)
	{
		d.push_back(int(b[i] - '0'));
	}
	for(int i = 0; i<(a.size() + b.size()); i++)
	{
		result_int.push_back(0);
	}
	for(int i = 0;i < a.size();i++)
	{
		for(int j = 0; j < b.size();j++)
		{       
		    result_int[i+j+1] += c[i]*d[j];
		}
	}
	correct_carries(result_int);
	for(int i=0;i < result_int.size();i++)
	{
		result_str += (char(result_int[i]) + '0');	//adding 48 back to make it the ascii value
	}
	/*for(int i = 0; i>result.size(); i++)
	{
	cout<<result[i];
	}*/
	//if()
	return result_str;
}


/*int main()
{
	BigInt A = "123456", B = "123456";
	BigInt c = multiply_int(A,B);
	cout<<c;
}*/
