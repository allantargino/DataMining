from __future__ import print_function
import math


def print_table(table, n, m):
    for i in range(0, n):
        for j in range(0, m):
            print(table[i][j], end='\t')
        print()


def get_idf(table, n, m):
    df = []
    for j in range(0, m):
        df_t = 0
        for i in range(0, n):
            if(table[i][j] > 0):
                df_t += 1
        df_t = math.log(n / df_t, 2)
        df.append(df_t)
    return df


def get_tf_idf(table, n, m, idf):
    for j in range(0, m):
        for i in range(0, n):
            table[i][j] = table[i][j] * idf[j]
    return table


table = [[10, 2, 0, 0, 1], [10, 0, 1, 0, 5], [0, 0, 0, 3, 0]]
n = len(table)
m = len(table[0])

print("absolut:")
print_table(table, n, m)

idf = get_idf(table, n, m)
tf_idf = get_tf_idf(table, n, m, idf)

print("\n")
print("tf-idf:")
print_table(tf_idf, n, m)
