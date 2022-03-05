import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class main {
    public String runLengthEncoding(String input) {
        if(input == null || input.length() == 0)
            return "";

        char[] inputCharArray = input.toCharArray();

        StringBuilder sb = new StringBuilder();

        char prevChar = 0;
        int counter = 0;

        for(char c : inputCharArray) {
            if(c == prevChar) {
                //Same char
                counter++;
            }
            else {
                //Different char
                if (prevChar != 0) {
                    sb.append(counter).append(prevChar);
                }
                prevChar = c;
                counter = 1;
            }
        }

        sb.append(counter).append(prevChar);
        return sb.toString();
    }

    @Test
    public void testSolution() {
        assertEquals("4a2b1c", runLengthEncoding("aaaabbc"));
        assertEquals("1c", runLengthEncoding("c"));
        assertEquals("1c1a", runLengthEncoding("ca"));
        assertEquals("4a", runLengthEncoding("aaaa"));
        assertEquals("", runLengthEncoding(""));
        assertEquals("", runLengthEncoding(null));
    }
}
