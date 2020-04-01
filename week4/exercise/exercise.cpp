#include <iostream>
#include <string>
using namespace std;
string to_int(string num)
{
    int len = num.size();
    for (int i = 0; i < len; i++)
    {
        if (num[0] == '0')
        {
            num = num.substr(1, num.size());
        }
        else
            return num;
    }
    return "0";
}
string plusnum(string num1, string num2)
{
    int maxlen = max(num1.size(), num2.size());
    int c = 0;
    int num1_n = 0;
    int num2_n = 0;
    int plus_n = 0;
    string plus_num = "";
    for (int i = 0; i < maxlen; i++)
    {
        if (i >= num1.size())
        {
            num1_n = 0;
        }
        else
        {
            num1_n = num1[num1.size() - 1 - i] - '0';
        }
        if (i >= num2.size())
        {
            num2_n = 0;
        }
        else
        {
            num2_n = num2[num2.size() - 1 - i] - '0';
        }
        plus_n = num1_n + num2_n + c;
        c = plus_n / 10;
        plus_n = plus_n % 10;
        plus_num = to_string(plus_n) + plus_num;
    }
    plus_num = (c == 0 ? "" : "1") + plus_num;
    return plus_num;
}
string subnum(string num1, string num2)
{
    int maxlen = max(num1.size(), num2.size());
    int c = 0;
    int num1_n = 0;
    int num2_n = 0;
    int sub_n = 0;
    string sub_num = "";
    for (int i = 0; i < maxlen; i++)
    {
        if (i >= num1.size())
        {
            num1_n = 0;
        }
        else
        {
            num1_n = num1[num1.size() - 1 - i] - '0';
        }
        if (i >= num2.size())
        {
            num2_n = 0;
        }
        else
        {
            num2_n = num2[num2.size() - 1 - i] - '0';
        }
        num1_n -= c;
        if (num2_n > num1_n)
        {
            num1_n = 10 + num1_n;
            c = 1;
        }
        else
        {
            c = 0;
        }
        sub_n = num1_n - num2_n;
        sub_num = to_string(sub_n) + sub_num;
    }
    return sub_num;
}
string paddingzero(string *num, int len, bool pre)
{
    for (int i = 0; i < len; i++)
    {
        if (pre)
            *num = "0" + *num;

        else
            *num = *num + "0";
    }
    return *num;
}
string karatsuba(string num1, string num2)
{
    if (num1.size() < num2.size())
    {
        string tmp = num1;
        num1 = num2;
        num2 = tmp;
    }
    if (min(num1.size(), num2.size()) <= 1)
    {
        return to_string(stoi(num1) * stoi(num2));
    }
    int maxlen = max(num1.size(), num2.size());
    paddingzero(&num1, maxlen - num1.size(), 1);
    paddingzero(&num2, maxlen - num2.size(), 1);
    int maxlen_2 = maxlen / 2;
    string x = num1.substr(0, maxlen - maxlen_2);
    string y = num1.substr(maxlen - maxlen_2, maxlen);
    string w = num2.substr(0, maxlen - maxlen_2);
    string z = num2.substr(maxlen - maxlen_2, maxlen);
    string xw = karatsuba(x, w);
    string yz = karatsuba(y, z);
    string plus_xw_yz = subnum(subnum(karatsuba(plusnum(x, y), plusnum(w, z)), xw), yz);
    paddingzero(&xw, maxlen_2 * 2, 0);
    paddingzero(&plus_xw_yz, maxlen_2, 0);
    string final_num = plusnum(plusnum(xw, yz), plus_xw_yz);
    return final_num;
}
int main()
{
    string num1 = "";
    string num2 = "";
    string ans = "";
    cout << "number1:";
    cin >> num1;
    cout << "number2:";
    cin >> num2;
    ans = to_int(karatsuba(num1, num2));
    cout << ans;
    system("pause");
}