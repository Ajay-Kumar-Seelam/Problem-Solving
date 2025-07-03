class Solution {
    public char kthCharacter(int k) {
   
    // convert the 1-based 'k' to a 0-based index
    int index = k - 1;

    // calculate the number of set bits
    // this will be the total number of times the character has been incremented
    int increments = 0;
        
    while (index > 0) {
        // find the largest power of 2 less than or equal to the current index
        // this represents the length of the string before the current char was generated
        long p = 1;
        while (p * 2 <= index) {
            p *= 2;
        }

        // since we must subtract p to find the parent index, it means our character
        // was in the second half of the string generation
        // so, we count an increment
        increments++;

        // subtract the largest power of two from the index
        index -= p;
    }
        
    // calculate the final character
    // start with 'a' and add the number of increments
    // use the modulo to handle the wrap-around from 'z' to 'a'
    // The result of ('a' + int) is an int, so we must cast it back to char
    return (char) ('a' + (increments % 26));   
    }
}