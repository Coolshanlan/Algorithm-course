#include <iostream>
#include <string>
using namespace std;
class Node
{
public:
    Node *left;
    Node *right;
    Node *p;
    int data = 10;
};
int main()
{
    Node *ptr = new Node();
    Node *A = new Node();
    Node *B = new Node();
    Node *c = new Node();

    A->data = 10;
    B->data = 15;
    ptr->data = 20;
    c->data = 50;

    A->right = B;
    B->left = c;
    B->p = A;
    ptr = A->right;
    ptr = ptr->left;
    cout
        << A->right->data << endl
        << B->data << endl
        << ptr->data;
    system("pause");
    return 0;
}