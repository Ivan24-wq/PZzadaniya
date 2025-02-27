#include <iostream>
#include <vector>
#include<iomanip>
#include <cmath>
using namespace std;
// Функция вывода матрицы

void printMatrix(vector<vector<double>>& matrix){
    for(const auto& row : matrix){
        for(double value : row){
            cout << setw(10) << fixed << setprecision(4) << value << " ";
        }
        cout << endl;
    }
    cout << endl;
}

// Гаусса-Жордана
bool Gaussjordann(vector<vector<double>>& matrix){
    int n = matrix.size(); //Строки
    int m = matrix[0].size();  //Строки

    // Строка с максимальным элементом
    for(int col = 0; col < n; col++){
        int pivotRow = col;
        for(int i = col + 1; i < n; i++){
            if(fabs(matrix[i][col]) > fabs(matrix[pivotRow][col])){
                pivotRow = i;
            }
        }
        if(fabs(matrix[pivotRow][col]) < 1e-9){
            cerr << "Нет решения!";
            return false;
        }
        swap(matrix[col], matrix[pivotRow]); // Менякм текущую строку со строкой главного элемента
        double pivot = matrix[col][col];
        for(int j = 0; j < m; j++){
            matrix[col][j] /= pivot;
        }

        // Обращаем остальные элементы в 0
        for(int h = 0; h < n; h++){
            if( h != col){
                double factor = matrix[h][col];
                for(int t = 0; t < m; t++){
                    matrix[h][t] = - factor * matrix[col][t];
                }
            }
        }
    }
    return true;
}
int main(){
    setlocale(LC_ALL, "RU");
}