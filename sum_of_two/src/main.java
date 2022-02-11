import org.testng.annotations.Test;

import java.util.HashSet;

import static org.testng.AssertJUnit.*;

public class main {
    /**
     * Determine if sum of two integers is equal to the given value
     * https://www.educative.io/blog/crack-amazon-coding-interview-questions
     * @param arr
     * @return
     */
    public boolean solution(int[] arr, int targetSum) {
        HashSet<Integer> hashSet = new HashSet<>();

        for(int n : arr) {
            int targetNum = targetSum - n;
            if(hashSet.contains(targetNum)) {
                System.out.println("Target sum: " + targetSum + " Found: " + n + "+" + targetNum);
                return true;
            }

            hashSet.add(n);
        }

        return false;
    }

    @Test
    public void test() {
        int arr[] = {5, 7, 1, 2, 8, 4, 3};
        int targetSum = 10;
        assertTrue(solution(arr, targetSum));


        int arr2[] = {5, 1, 2, 8, 4, 3};
        int targetSum2 = 10;
        assertTrue(solution(arr2, targetSum2));

        int arr3[] = {5, 1, 2, 4, 3};
        int targetSum3 = 10;
        assertFalse(solution(arr3, targetSum3));
    }
}
