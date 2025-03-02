#include <iostream>
#include<vector>
#include<cmath>
#include <iomanip>
#include <chrono>
using namespace std;
using namespace chrono;
//Точность вычисления
const double epsilon = 1e-4;

// Метод зейделя
vector<double> Zeidel(const vector<vector<double>> & A, const vector<double> & b, int maxIterarion = 10000){
    int n = A.size();
    vector<double> x(n);
    vector<double> prevX(n);

    for(int iteration = 0; iteration < maxIterarion; iteration++){
        for(int i = 0; i < n; i++){
            double sum = 0.0;
            for(int j = 0; j < n; j++){
                if( j != i){
                    sum += A[i][j] * x[j];
                }
            }
            x[i] = (b[i] - sum) / A[i][i];
        }
        bool hasConverged = true;
        for (int i = 0; i < n; ++i) {
            if (fabs(x[i] - prevX[i]) > epsilon) {
                hasConverged = false;
                break;
            }
        }
        if(hasConverged){
            break;
        }
        prevX = x;
    }
    return x;
}

int main(){
    setlocale(LC_ALL, "RU");

    //Матрица
    vector<vector<double>> A = {
        {3, 1, -1},
        {-2, 4, 1},
        {1, 1, 3}

    };

    vector<double> b = {
        {-1, 5, -3}
    };

    //Нахождение ответа
    auto start = high_resolution_clock::now();
    vector<double> solution = Zeidel(A, b);
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    cout << "Ответ: " << endl;
    cout << "Время выполнения алгоритма: " << duration.count() << "мкс \n";
    for (size_t i = 0; i < solution.size(); i++) {
        cout << " x" << i + 1 << " = " << fixed << setprecision(2) << solution[i] << endl;
    }
    return 0;
}