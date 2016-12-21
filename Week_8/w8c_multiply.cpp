// AUTHOR Abhishek Shanbhag anshan@bu.edu
// AUTHOR Vrushali Mahajan vmahajan@bu.edu
// AUTHOR Ameya Apastamb ameyama@bu.edu
// AUTHOR Hari chhari@bu.edu
// AUTHOR Shreyas Joshi svmjoshi@bu.edu

#include<iostream>
#include<string>
#include<vector>
#include<fstream>


using namespace std;

typedef vector<vector<int>> int_matrix;
typedef vector<vector<double>> double_matrix;

int read_to_matrix(double_matrix &a, string file_name, int m, int n, char type)
{
	ifstream input_file;
	input_file.open(file_name);
	double temp;
	if(!(input_file.is_open()))
	{
		return 2;
	}
	try
	{		
		int i = 0, j = 0, count = 0;
		while((input_file >> temp))
		{
			//cout<<temp<<endl;
			if(count >= m*n)
			{
				return 3;
			}
			if(j == n)
			{
				i++;
				a[i].push_back(temp);
				count++;
				j = 1;
			}
			else
			{
				if(tolower(type) == 'i')
				{
					if(double(int(temp)) != temp)
					{
						return 3;
					}
				}
				a[i].push_back(temp);
				j++;
				count++;
			}
		}
		if(count<(m*n-1))
		{
			return 3;
		}
		cout<<temp<<endl;
		input_file.close();
	}
	catch(...)
	{
		return 3;
	}
	return 0;
}

void print_matrix(const double_matrix &a)
{
	for(int i = 0; i<a.size(); i++)
	{
		for(int j = 0; j<a[i].size(); j++)
		{
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}
}

int multiply_mat(double_matrix &a, double_matrix &b, double_matrix &c)
{
	double_matrix ans(a.size(), vector<double>(b[0].size()));
	try
	{	
		for(int i = 0; i<a.size(); i++)
		{
			for(int j = 0; j<b[0].size(); j++)
			{
				double sum = 0;
				for(int k = 0; k<b.size(); k++)
				{
					sum+= a[i][k] * b[k][j];
				}
				c[i].push_back(sum);
			}
		}
		return 0;
	}
	catch(...)
	{
		return 4;
	}
}

int write_matrix(string file_name, double_matrix c, char type)
{
	try
	{
		ofstream output_file;
		output_file.open(file_name);
		if(!(output_file.is_open()))
		{		
			return 4;
		}
		for(int i = 0; i<c.size(); i++)
		{
			string line;
			if(tolower(type) == 'i')
			{
				line = to_string(int(c[i][0]));
			}
			else if(tolower(type) == 'd')
			{
				line = to_string(c[i][0]);
			}
			line.append(" ");
			for(int j = 1; j<c[0].size(); j++)
			{
				if(tolower(type) == 'i')
				{
					line.append(to_string(int(c[i][j])));
				}
				else if(tolower(type) == 'd')
				{
					line.append(to_string(c[i][j]));
				}
				line.append(" ");
			}
			line.append("\n");
			output_file << line;
		}
		output_file.close();
		return 0;
	}
	catch(...)
	{
		return 4;
	}
}


int main(int argc, char const* argv[])
{
	int m,n,l,x;
	string file_a;
	string file_b;
	string file_c;
	string type = argv[1];
	if(!((type == "double") || (type == "int")))
	{
		return 1;
	}
	if(argc == 6)
	{
		try
		{
			m = stoi(argv[2]);
			n = stoi(argv[2]);
			l = stoi(argv[2]);
			if(m < 1)
			{
				return 1;
			}				
			file_a = argv[3];
			file_b = argv[4];
			file_c = argv[5];
		}
		catch(...)
		{
			return 1;
		}
	}
	else if(argc == 8)
	{
		try
		{
			m = stoi(argv[2]);
			n = stoi(argv[3]);
			l = stoi(argv[4]);
			if((m < 1) || (n < 1) || (l < 1))
			{
				return 1;
			}
			file_a = argv[5];
			file_b = argv[6];
			file_c = argv[7];
		}
		catch(...)
		{
			return 1;
		}
	}
	else 
	{
		return 1;
	}
	double_matrix a(m);
	double_matrix b(n);
	double_matrix c(m);
	x = read_to_matrix(a, file_a, m, n, argv[1][0]);
	if(x != 0)
	{
		return x;
	}
	x = read_to_matrix(b, file_b, n, l, argv[1][0]);
	if(x != 0)
	{
		return x;
	}	
	x = multiply_mat(a, b, c);
	if(x != 0)
	{
		return x;
	}	
	x = write_matrix(file_c, c, argv[1][0]);
	if(x != 0)
	{
		return x;
	}
	return 0;
}
