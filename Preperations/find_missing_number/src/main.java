import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class main {
	/**
	 * https://www.educative.io/blog/crack-amazon-coding-interview-questions
	 */
    public int findMissingNumber(int[] input, int n) {
        //Note: input size is never zero.

        //Get sum of complete array (with missing number X)
        int sum = n * (n + 1);
        sum /= 2;

        for(int num : input) {
            sum -= num;
        }
        return sum;
    }

    @Test
    public void test() {
        int arr[] = {3, 7, 1, 2, 8, 4, 5};
        assertEquals(6, findMissingNumber(arr, 8));

        int arr2[] = {3, 7, 1, 2, 8, 4, 6};
        assertEquals(5, findMissingNumber(arr2, 8));

        int arr3[] = {1, 3};
        assertEquals(2, findMissingNumber(arr3, 3));

        int arr4[] = {1};
        assertEquals(2, findMissingNumber(arr4, 2));
    }
}
