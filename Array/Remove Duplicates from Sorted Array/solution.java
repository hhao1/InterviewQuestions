//Two pointer
//思路：前后两个指针，i慢于j，最后去重的结果在list的最前面
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length==0) return 0;
        int i=0;
        for (int j=1;j<nums.length;j++){
            if (nums[i]!=nums[j]){
                i++;
                nums[i]=nums[j];
            }
        }
        return i+1;
}
}