#include<opencv/cv.hpp>   
#include<map>
#include<iostream>

using namespace std;
using namespace cv;

typedef struct
{
    int x;
    int y;
    string s;
}test_t;

int a1;
int a2;
string str;
int arr[10];
test_t t;
map<string, int> m;

//打印出學生資料，來驗證讀取文檔信息是否成功
void data_info_dump()
{
    cout << "a1:" << a1 << endl;
    cout << "a2:" << a2 << endl;
    cout << "str:" << str << endl;
    cout << "t.x:" << t.x << endl;
    cout << "t.y:" << t.y << endl;
    cout << "t.s:" << t.s << endl;
    cout << "curry:" << m["curry"] << endl;
    cout << "kobe:" << m["kobe"] << endl;
    cout << "james:" << m["james"] << endl;
    for (int i = 0; i < 10; i++)
    {
        cout << arr[i] << endl;
    }
}

int main(int argc, char** argv)
{
    FileStorage fs("test.yaml", FileStorage::READ); //填入讀操作
    a1 = (int)fs["int_data"];
    a2 = (int)fs["char_data"];
    str = (string)fs["string_data"];

    //讀入數組
    FileNode arr_node = fs["array_data"];
    FileNodeIterator fni = arr_node.begin(); 
    FileNodeIterator fniEnd = arr_node.end();
    int count = 0;
    for (; fni != fniEnd; fni++)
    {
        arr[count++] = (int)(*fni);
    }

    //讀入map
    FileNode map_node = fs["map_data"];
    m["curry"] = (int)map_node["curry"];
    m["james"] = (int)map_node["james"];
    m["kobe"] = (int)map_node["kobe"];

    //讀入結構體
    FileNode struct_node = fs["struct_data"];
    t.x = (int)struct_node["x"];
    t.y = (int)struct_node["y"];
    t.s = (string)struct_node["s"];

    data_info_dump();

    return 0;
}
