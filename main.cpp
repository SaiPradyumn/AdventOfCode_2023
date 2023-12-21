#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int process_line(string line){
    int dig1 = -1;
    int dig2 = 0;
    for(int i = 0; i < line.length(); i++){
        if(isdigit(line[i])){
            if(dig1 == -1){
                char st = line[i];
                dig1 = st-'0';
                //cout<<dig1;
            }
                char st = line[i];
                dig2 = st-'0';

        }
    }
//    if(dig1 == -1 || dig2 == -1){
//        return 0;
//    }

    return dig1*10 + dig2;
}


int main() {
    fstream fin;
    fin.open("../input_1.txt", ios::in);
    int answer = 0;
    if(fin.is_open()){
        cout<<"file open";
        string line;
        int line_sum = 0;
        while(getline(fin,line)){
            line_sum = process_line(line);
            answer += line_sum;
        }
        cout<<answer;
    }else{
        cout<<"Error opening file!!";
    }

    return 0;
}
