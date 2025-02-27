#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
using namespace std;

// Функция для вывода матрицы
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

// Метод Гаусса-Жордана
bool GaussJordan(vector<vector<float>>& matrix) {
    int n = matrix.size();    
    int m = matrix[0].size(); 

    for (int col = 0; col < n; col++) {
        // Найти строку с максимальным элементом в текущем столбце
        int pivotRow = col;
        for (int i = col + 1; i < n; i++) {
            if (fabs(matrix[i][col]) > fabs(matrix[pivotRow][col])) {
                pivotRow = i;
            }
        }

        
        if (fabs(matrix[pivotRow][col]) < 1e-9) {
            cerr << "Нет решения!\n";
            return false;
        }

        
        swap(matrix[col], matrix[pivotRow]);

        // Приведение ведущего элемента к 1
        double pivot = matrix[col][col];
        for (int j = 0; j < m; j++) {
            matrix[col][j] /= pivot;
        }

        
        for (int i = 0; i < n; i++) {
            if (i != col) {
                double factor = matrix[i][col];
                for (int j = 0; j < m; j++) {
                    matrix[i][j] -= factor * matrix[col][j];
                }
            }
        }
    }

    return true;
}

int main() {
    
    vector<vector<float>> matrix = {
        {5, 1, -1, -5},
        {-1, 3, -1, 5},
        {1, -2, 4, 1}
    };

    cout << "Введённая матрица:\n";
    printMatrix(matrix);

    
    if (GaussJordan(matrix)) {
        cout << "Vетода Гаусса-Жордана:\n";
        printMatrix(matrix);

        cout << "Ответ:\n";
        for (int i = 0; i < matrix.size(); i++) {
            cout << "x" << i + 1 << " = " << matrix[i].back() << endl;
        }
    } else {
        cout << "Нет решений!\n";
    }

    return 0;
}
