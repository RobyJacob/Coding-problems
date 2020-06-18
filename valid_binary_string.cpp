#include <iostream>

using namespace std;

int minimumMoves(string, int);

int main() {
    int d;
    string str;

    cin >> str;

    cin >> d;

    int result = minimumMoves(str, d);

    cout << result << endl;
}

int minimumMoves(string s, int d) {
    int change = 0, flag = 0;
    
    int loop_until = (int) (s.length() - (d-1));
    
    for (int i = 0; i < loop_until; i++) {
        for (int j = i; j < i+d; j++) {
            if (s[j] == '1') {
                flag = 1; 
                break;
            }
        }
        
        if (!flag) change++;
        flag = 0;
    }
    
    return change;
}