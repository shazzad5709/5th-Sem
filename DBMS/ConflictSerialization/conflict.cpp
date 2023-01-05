#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    bool conflict=true;
    string line[10];
    // string trans[10];
    ifstream f;
    f.open("input.txt");
    int k=0;
    while(f)
    {
        getline(cin, line[k++]);        
    }
    bool xwrite=false, ywrite=false;
    for(int i=0; i<k; i++)
    {
        if(line[i][3]=='X' && line[i][0]=='w')
            xwrite=true;
        else if(line[i][3]=='Y' && line[i][0]=='w')
            ywrite=true;
    }
    if(xwrite)
    {
        
    }

}