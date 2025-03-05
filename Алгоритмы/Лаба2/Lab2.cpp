#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <chrono>
using namespace std;
using namespace chrono;

const double epsilon = 1e-4;

// Метод Зейделя
vector<double> Zeidel(const vector<vector<double>>& A, const vector<double>& b, int maxIterations = 10000) {
    int n = A.size();
    vector<double> x(n, 0.0);
    vector<double> prevX(n, 0.0);

    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        for (int i = 0; i < n; ++i) {
            double sum = 0.0;
            for (int j = 0; j < n; ++j) {
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
        if (hasConverged) break;
        prevX = x;
    }
    return x;
}

// Метод Гаусса-Жордана
bool GaussJordan(vector<vector<float>>& matrix) {
    int n = matrix.size();
    int m = matrix[0].size();

    for (int col = 0; col < n; ++col) {
        int pivotRow = col;
        for (int i = col + 1; i < n; ++i) {
            if (fabs(matrix[i][col]) > fabs(matrix[pivotRow][col])) {
                pivotRow = i;
            }
        }

        if (fabs(matrix[pivotRow][col]) < 1e-9) {
            cerr << "Нет решения!\n";
            return false;
        }

        swap(matrix[col], matrix[pivotRow]);

        double pivot = matrix[col][col];
        for (int j = 0; j < m; ++j) {
            matrix[col][j] /= pivot;
        }

        for (int i = 0; i < n; ++i) {
            if (i != col) {
                double factor = matrix[i][col];
                for (int j = 0; j < m; ++j) {
                    matrix[i][j] -= factor * matrix[col][j];
                }
            }
        }
    }

    return true;
}

// Вывод матрицы
void printMatrix(vector<vector<float>>& matrix) {
    int k = matrix[0].size();
    for (const auto& row : matrix) {
        for (int g = 0; g < k; g++) {
            if (g == k - 1) {
                cout << " | ";
            }
            cout << setw(5) << fixed << setprecision(2) << row[g] << " ";
        }
        cout << endl;
    }
    cout << endl;
}


int main() {
    setlocale(LC_ALL, "RU");

    vector<vector<double>> A = {
        {3, 1, -1},
        {-2, 4, 1},
        {1, 1, 3}
    };
    vector<double> b = {-1, 5, -3};

    vector<vector<float>> matrix = {
        {3, 1, -1, -1},
        {-2, 4, 1, 5},
        {1, 1, 3, -3}
    };

    // Сравнение времени выполнения
    auto start1 = high_resolution_clock::now();
    vector<double> solutionZeidel = Zeidel(A, b);
    auto end1 = high_resolution_clock::now();
    auto durationZeidel = duration_cast<microseconds>(end1 - start1);

    cout << "Метод Зейделя:\n";
    cout << "Время выполнения: " << durationZeidel.count() << " мкс\n";
    for (size_t i = 0; i < solutionZeidel.size(); ++i) {
        cout << "x" << i + 1 << " = " << fixed << setprecision(2) << solutionZeidel[i] << endl;
    }
    cout << endl;

    auto start2 = high_resolution_clock::now();
    if (GaussJordan(matrix)) {
        auto end2 = high_resolution_clock::now();
        auto durationGauss = duration_cast<microseconds>(end2 - start2);

        cout << "Метод Гаусса-Жордана:\n";
        cout << "Время выполнения: " << durationGauss.count() << " мкс\n";

        cout << "Результирующая матрица:\n";
        printMatrix(matrix);

        cout << "Решения:\n";
        for (int i = 0; i < matrix.size(); ++i) {
            cout << "x" << i + 1 << " = " << matrix[i].back() << endl;
        }
    } else {
        cout << "Метод Гаусса-Жордана не смог найти решение.\n";
    }

    return 0;
}