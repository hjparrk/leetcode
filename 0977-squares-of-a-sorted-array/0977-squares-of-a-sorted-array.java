class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int n = nums.length;
        int[] answer = new int[n];
        int left = 0, right = n - 1;
        
        for (int i = n - 1; i >= 0; i--) {
            
            int square;
            
            // abs(left) > abs(right)
            if(Math.abs(nums[left]) < Math.abs(nums[right])) {
                square = (int) Math.pow(nums[right], 2);
                right --;
            } 
            // abs(left) <= abs(right)
            else {
                square = (int) Math.pow(nums[left], 2);
                left ++;
            }
            
            answer[i] = square;
        }
        
        return answer;
    }
}