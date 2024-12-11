#include <iostream>
#include <vector>
using namespace std;

// Функция для вывода матрицы
void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int element : row) {
            cout << element << " ";
        }
        cout << endl;
    }
}

// Функция циклической перестановки квадратов
void rotateSquares(vector<vector<int>>& matrix, int n) {
    int half = n / 2; // Размер подматрицы (половина матрицы)
    
    for (int i = 0; i < half; ++i) {
        for (int j = 0; j < half; ++j) {
            // Сохранение значений квадратов
            int topLeft = matrix[i][j];
            int topRight = matrix[i][j + half];
            int bottomRight = matrix[i + half][j + half];
            int bottomLeft = matrix[i + half][j];

            // Циклический сдвиг
            matrix[i][j + half] = topLeft;            // Верхний левый → Верхний правый
            matrix[i + half][j + half] = topRight;    // Верхний правый → Нижний правый
            matrix[i + half][j] = bottomRight;        // Нижний правый → Нижний левый
            matrix[i][j] = bottomLeft;                // Нижний левый → Верхний левый
        }
    }
}

int main() {
    int n;

    cout << "Введите размер матрицы (четное число): ";
    cin >> n;

    if (n % 2 != 0) {
        cout << "Размер матрицы должен быть четным!" << endl;
        return 1;
    }

    // Инициализация матрицы
    vector<vector<int>> matrix(n, vector<int>(n));
    cout << "Введите элементы матрицы:" << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    cout << "Исходная матрица:" << endl;
    printMatrix(matrix);

    // Циклическая перестановка
    rotateSquares(matrix, n);

    cout << "Матрица после циклической перестановки:" << endl;
    printMatrix(matrix);

    return 0;
}
