
import java.util.HashMap;

class Solution {
    public int totalFruit(int[] fruits) {
        int n = fruits.length;
        HashMap<Integer, Integer> fruitCounts = new HashMap<>();
        int windowStart = 0, maxLength = 0;

        for (int windowEnd = 0; windowEnd < n; windowEnd++) {
            fruitCounts.put(fruits[windowEnd], fruitCounts.getOrDefault(fruits[windowEnd], 0) + 1);

            while (fruitCounts.size() > 2) {
                fruitCounts.put(fruits[windowStart], fruitCounts.get(fruits[windowStart]) - 1);
                if (fruitCounts.get(fruits[windowStart]) == 0) {
                    fruitCounts.remove(fruits[windowStart]);
                }
                windowStart++;
            }

            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }

        return maxLength;
    }
}

