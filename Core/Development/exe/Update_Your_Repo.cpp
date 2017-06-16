









#include <direct.h>
#define GetCurrentDir _getcwd


#include <iostream>


#include <algorithm>
#include <iterator>

#include <vector>



using namespace std;

vector<string> split(const string& s, const string& delim, const bool keep_empty = true) {
    vector<string> result;
    if (delim.empty()) {
        result.push_back(s);
        return result;
    }
    string::const_iterator substart = s.begin(), subend;
    while (true) {
        subend = search(substart, s.end(), delim.begin(), delim.end());
        string temp(substart, subend);
        if (keep_empty || !temp.empty()) {
            result.push_back(temp);
        }
        if (subend == s.end()) {
            break;
        }
        substart = subend + delim.size();
    }
    return result;
}


std::string ReplaceString(std::string subject, const std::string& search,
                          const std::string& replace) {
    size_t pos = 0;
    while((pos = subject.find(search, pos)) != std::string::npos) {
         subject.replace(pos, search.length(), replace);
         pos += replace.length();
    }
    return subject;
}













int main() {


     char cCurrentPath[FILENAME_MAX];
      if (!GetCurrentDir(cCurrentPath, sizeof(cCurrentPath)))
     {
     return errno;
     }
     cCurrentPath[sizeof(cCurrentPath) - 1] = '\0'; /* not really required */

    string rootPath;

    const vector<string> words = split(cCurrentPath, "Core");
    copy(words.begin(), words.end(), ostream_iterator<string>(cout, "\n"));


    rootPath = words.at(0);



    string stringPath;


    string path;
    string path2;
    string rootPath2;






    path = "\"" + rootPath + "\\Core\\Python\\python.exe\" ";
    cout << path;
    path = "\"" + path + "\"" + rootPath + "\\Core\\Scripts\\Load.py" + "\"" + "\"" + "\ ";
    system(path.c_str());




    string goat = "?";
    cin >> goat;










    //string1 = "setx TESSDATA_PREFIX \"C:\\ImageScripter\\SystemFiles\\Tesseract\\Tesseract-OCR\"";
    //system(string1.c_str());

    //string1 = "setx Path \"C:\\ImageScripter\\SystemFiles\\Tesseract\\Tesseract-OCR\"";
    //system(string1.c_str());




    //string1 = "\"C:\\ImageScripw_handle = self.GetHandle(Attempts = attempts)ter\\SystemFiles\\Python\\python.exe\" \" C:\\ImageScripter\\SystemFiles\\Python\\Lib\\site-packages\\pytank\\GUI\\Main.py\"";
    //system(string1.c_str());







}
