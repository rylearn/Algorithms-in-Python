#include <string.h>
#include <iostream>
using std::cout;
using std::endl;

int dice_sum_combos(int num_faces, int num_dice, int sum) {
    int dp_table[num_dice + 1][sum + 1];
    memset(dp_table, 0, sizeof(dp_table));

    for (int i = 1; i <= num_faces && i <= sum; ++i) {
        dp_table[1][i] = 1;
    }

    for (int i = 2; i <= num_dice; ++i) {
        for (int j = 1; j <= sum; ++j) {
            for (int k = 1; k <= num_faces && k < j; ++k) {
                dp_table[i][j] += dp_table[i - 1][j - k];
            }
        }
    }

    return dp_table[num_dice][sum];
}

int main() {
    cout << dice_sum_combos(6, 2, 5) << endl;
    return 0;
}
