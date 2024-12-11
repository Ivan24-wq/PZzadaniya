#include <iostream>
#include <vector>
#include <limits>

using namespace std;

// Функция для нахождения максимального или минимального элемента среди упорядоченных строк
int findMinMax(const vector<vector<int>>& matrix, bool findMax, bool isSorted) {
    int minMaxVal = findMax ? numeric_limits<int>::min() : numeric_limits<int>::max();

    // Если строки отсортированы, пропускаем проверку на сортировку
    for (const auto& row : matrix) {
        // Если строки отсортированы, сразу ищем максимум или минимум
        if (isSorted) {
            int rowMinMaxVal = findMax ? row.back() : row.front();
            minMaxVal = findMax ? max(minMaxVal, rowMinMaxVal) : min(minMaxVal, rowMinMaxVal);
        }
        else {
            // Если строки не отсортированы, проверяем сортировку
            bool isSortedRow = true;
            for (size_t i = 1; i < row.size(); ++i) {
                if (row[i] < row[i - 1]) {
                    isSortedRow = false;
                    break;
                }
            }

            if (isSortedRow) {
                int rowMinMaxVal = findMax ? row.back() : row.front();
                minMaxVal = findMax ? max(minMaxVal, rowMinMaxVal) : min(minMaxVal, rowMinMaxVal);
            }
        }
    }

    return minMaxVal;
}

int main() {
    setlocale(LC_ALL, "RU");
    int n, m;
    cout << "Введите количество строк (n): ";
    cin >> n;
    cout << "Введите количество столбцов (m): ";
    cin >> m;

    vector<vector<int>> matrix(n, vector<int>(m));
    cout << "Введите элементы матрицы:" << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> matrix[i][j];
        }
    }

    // Предполагаем, что строки уже отсортированы, если это так
    bool isSorted = true;
    for (const auto& row : matrix) {
        for (size_t i = 1; i < row.size(); ++i) {
            if (row[i] < row[i - 1]) {
                isSorted = false;
                break;
            }
        }
        if (!isSorted) break;
    }

    cout << "Максимальный элемент среди упорядоченных строк: " << findMinMax(matrix, true, isSorted) << endl;
    cout << "Минимальный элемент среди упорядоченных строк: " << findMinMax(matrix, false, isSorted) << endl;

    return 0;
}