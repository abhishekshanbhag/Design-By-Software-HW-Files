#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;
typedef vector<double> Poly;
typedef string BigInt;

Poly multiply_poly(const Poly &v, const Poly &w)
{
	Poly result;
	Poly a = v;
	Poly b = w;
	int n = a.size();
	int k = b.size();
	if(n > k || k == n)
	{
		int n1 = (n + k) - 1;
		for(int i = 0; i < n1; i++)
		{
		  double y = 0;
		  for(int j = 0; j < k; j++)
		  {
			if( j > i )
			{
				j = k;
			}
			else if(((i - j) > n))
			{
				j++;
				y += b[j] * a[i - j];
			}
			else
			{
				y += b[j] * a[i - j];
			}
		  }
			result.push_back(y);
		}
	}
	else if(k > n)
	{
		int n1 = (k + n) -1;
		for(int i = 0; i < k; i++)
		{
		  double y = 0;
		  for(int j = 0; j < n; j++)
		  {
			if( j > i )
			{
				j = n;
			}
			else if(((i - j) > k))
			{
				j++;
				y += b[j] * a[i - j];
			}
			else
			{
				y += b[j] * a[i - j];
				
			}
		  }
			result.push_back(y);
		}
	}
	
	
	return result;
}
void print_poly(const Poly &s)
{
	//cout<< endl <<"Polynomial : ";
	for(int i = 0; i<s.size(); i++)
		{
			cout<<s[i]; 
		}
	cout<<endl;
}

Poly convert_to_poly(BigInt &x)
{	
	Poly result;
	BigInt a = x; 
	int n = a.length();
	//int d = atoi(a.c_str());
	for(int i = 0; i < n; i = i + 1)
	{
		string t;
		t = a[i];
		int d = atoi(t.c_str());
		cout<<a[i]<<"";
		result.push_back(d);
	}
	print_poly(result);
	return result;
}
int main()
{	
	BigInt x,y;
	cin >> x;
	Poly a = convert_to_poly(x);
	cin >> y;
	Poly b = convert_to_poly(y);

	Poly result = multiply_poly(a,b);
	cout << "Multiplication"<< endl;
	print_poly(result);
	cout<<endl;

	return 0;
}
