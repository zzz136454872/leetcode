/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_int_star(int *list, int len) {
  for (int i = 0; i < len; i++)
    printf("%d ", list[i]);
  putchar('\n');
}

void print_int_2star(int **matrix, int row, int col) {
  for (int i = 0; i < row; i++)
    print_int_star(matrix[i], col);
}

void print2(int **mat, int row, int col, int x, int y) {
  for (int i = 0; i < row; i++)
    if (mat[i][y] != 0)
      mat[i][y] = 12356;
  for (int j = 0; j < col; j++)
    if (mat[x][j] != 0)
      mat[x][j] = 12356;
}

void setZeroes(int **matrix, int matrixSize, int *matrixColSize) {
  for (int i = 0; i < matrixSize; i++) {
    for (int j = 0; j < matrixColSize[0]; j++)
      if (matrix[i][j] == 0)
        print2(matrix, matrixSize, matrixColSize[0], i, j);
  }
  for (int i = 0; i < matrixSize; i++) {
    for (int j = 0; j < matrixColSize[0]; j++)
      if (matrix[i][j] == 12356)
        matrix[i][j] = 0;
  }
}

int main() {
  int x = 3;
  int **matrix = (int **)malloc(x * sizeof(int *));
  for (int i = 0; i < x; i++)
    matrix[i] = (int *)malloc(x * sizeof(int));
  for (int i = 0; i < x; i++)
    for (int j = 0; j < x; j++)
      matrix[i][j] = 1;
  int cols[3] = {3, 3, 3};
  matrix[1][1] = 0;
  setZeroes(matrix, 3, cols);
  print_int_2star(matrix, x, x);
  return 0;
}
