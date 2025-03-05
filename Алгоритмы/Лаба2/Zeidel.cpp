#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <chrono>
using namespace std;
using namespace chrono;

// Точность вычисления
const double epsilon = 1e-4;

// Функция вывода матрица
void printMatrix(const vector<vector<double>>& A, const vector<double>& b) {
    cout << "Введенная матрица (A|b):" << endl;
    for (size_t i = 0; i < A.size(); ++i) {
        for (size_t j = 0; j < A[i].size(); ++j) {
            cout << fixed << setprecision(2) << setw(5) << A[i][j] << " ";
        }
        cout << "| ";
        cout << setw(5) << fixed << setprecision(2) << b[i] << " ";
        cout << endl;
    }
    cout << endl;
}

// Метод Зейделя
vector<double> Zeidel(const vector<vector<double>>& A, const vector<double>& b, int maxIteration = 10000) {
    int n = A.size();
    vector<double> x(n);
    vector<double> prevX(n);

    for (int iteration = 0; iteration < maxIteration; iteration++) {
        for (int i = 0; i < n; i++) {
            double sum = 0.0;
            for (int j = 0; j < n; j++) {
                if (j != i) {
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
        if (hasConverged) {
            break;
        }
        prevX = x;
    }
    return x;
}

int main() {
    setlocale(LC_ALL, "RU");

    // Матрица
    vector<vector<double>> A = {
        {3, 1, -1},
        {-2, 4, 1},
        {1, 1, 3}
    };

    vector<double> b = { -1, 5, -3 };

    // Вывод матрицы
    printMatrix(A, b);

    // Ответ
    auto start = high_resolution_clock::now();
    vector<double> solution = Zeidel(A, b);
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);

    
    cout << "Ответ: " << endl;
    cout << "Время выполнения алгоритма: " << duration.count() << " мкс\n";
    for (size_t i = 0; i < solution.size(); i++) {
        cout << " x" << i + 1 << " = " << fixed << setprecision(2) << solution[i] << endl;
    }

    return 0;
}