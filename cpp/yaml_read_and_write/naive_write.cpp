#include <opencv/cv.hpp>
#include <map>

using namespace std;
using namespace cv;

typedef struct
{
    int x;
    int y;
    string s;
}test_t;


int main(int argc, char** argv)
{
    FileStorage fs("test.yaml", FileStorage::WRITE); //填入寫操作

    //測試數據
    int a1 = 2;
    char a2 = -1;
    string str = "hello mother fucker!";
    int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
    test_t t = { 3,4,"hi fucker" };
    map<string, int> m;
    m["kobe"] = 100;
    m["james"] = 99;
    m["curry"] = 98;

    //寫入文檔操作,先寫標註在寫數據
    fs << "int_data" << a1;
    fs << "char_data" << a2;
    fs << "string_data" << str;

    //寫入數組
    fs <<"array_data"<< "["; //數組開始
    for (int i = 0; i < 10; i++)
    {
        fs << arr[i];
    }
    fs << "]"; //數組結束

    //寫入結構體
    fs << "struct_data" << "{"; //結構體開始
    fs << "x" << t.x;
    fs << "y" << t.y;
    fs << "s" << t.s;
    fs << "}";  //結構結束


    //map的寫入 
    fs << "map_data" << "{";  //map的開始寫入
    map<string, int>::iterator it = m.begin();
    for (; it != m.end(); it++)
    {
        fs << it->first << it->second;
    }
    fs << "}";  //map寫入結束


    return 0;
}
