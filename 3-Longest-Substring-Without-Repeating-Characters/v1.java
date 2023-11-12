class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;

        int front = 0;
        int back = 0;

        String current = s.substring(back, front+1);
        int currentBest = current.length();


        while (front + 1 < s.length()) {
            front += 1;
            if (current.indexOf(s.charAt(front)) == -1) {
                current = s.substring(back, front+1);
                currentBest = Math.max(currentBest, current.length());
            } else {
                back = Math.min(front, s.indexOf(s.charAt(front), back) + 1);
                current = s.substring(back, front+1);
            }
        }

        System.out.println(currentBest);

        return currentBest;
    }
}
