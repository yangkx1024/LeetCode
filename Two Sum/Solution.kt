class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = HashMap<Int, Int>()
        nums.forEachIndexed { index, i ->
            if (map.containsKey(i)) {
                return intArrayOf(map[i]!!, index)
            } else {
                map[target - i] = index
            }
        }
        return IntArray(0)
    }
}

fun main(args: Array<String>) {
    val array = intArrayOf(2, 7, 11, 15)
    val target = 9
    val result = Solution().twoSum(array, target)
    println(result.joinToString())
}