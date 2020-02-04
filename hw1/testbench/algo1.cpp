#include <iostream>
using namespace std;

void algo1(int n){
    int out_loop = 0;
    int in_loop = 0;
    int sum = 0;
    for (int i = n; i > 0; i--){
        cout << "Outer loop" << endl;
        for (int j = i+1; j <= n; j++){
            cout << "Inner loop" << endl;
            sum = sum + j;
            cout << i << " " << sum << endl;
            in_loop += 1;
        }
        out_loop += 1;
    }
    cout << "\n" << endl;
    cout << "n = " << n << endl;
    cout << "Outer loop ran: " << out_loop << " times" << endl;
    cout << "Inner loop ran: " << in_loop << " times" << endl;
    return;
}

void algo2(int n){
    int loop = 0;
    int sum = 0;
    for (long int i = 2; i <= n; i = i*i){
        cout << "loop" << endl;
        sum = sum + 1;
        cout << i << " " << sum << endl;
        loop += 1;
    }
    cout << endl;
    cout << "n = " << n << endl;
    cout << "loop ran " << loop << " times" << endl;
    return;
}


int main(){
    int input = 20;
    //algo1(input);
    algo2(input);

    return 0;
}
