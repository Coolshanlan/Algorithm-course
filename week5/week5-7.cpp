#include <iostream>
using namespace std;

int max(int a, int b)
{
	if (a > b)
		return a;
	else
		return b;
}
int main()
{
	int M = 0;
	cout << "Length:";
	cin >> M;
	int p[M + 1];
	cout << "Length of price (1 to " << M << ")";
	for (int i = 1; i <= M; i++)
	{
		cin >> p[i];
	}
	int r[M + 1];
	p[0] = 0;
	r[0] = 0;
	for (int i = 1; i <= M; i++)
	{
		int total = -9999999;
		int j = 1;
		while (i >= j)
		{
			total = max(total, p[j] + r[i - j]);
			j++;
		}
		r[i] = total;
	}
	cout << r[M];
	system("pause");
}
