//Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
//只要后面比前面大的都行。这是最简单的方法，stack可解，用python解了一遍。
// Input: [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
//              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
// class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit=0;
        for(int i=1; i<prices.length;i++){
            if (prices[i-1]<prices[i]){
                maxProfit+=(prices[i]-prices[i-1]);
            }
        }
        return maxProfit;
    }
}