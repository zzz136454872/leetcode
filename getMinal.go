package main

import (
     "fmt"
)

func min(a,b int) int {
    if a>b {
        return b
    }
    return a
}

func getMinal(nums []int) int {
	if len(nums) <= 1 {
		return 0
	}
	end := -1
	start := -1
	for i := len(nums) - 1; i > 0; i-- {
		if nums[i] < nums[i-1] {
			end = i
			break
		}
	}
	if -1 == end { // 原始数组有序， 非降序
		return 0
	}
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			start = i
			break
		}
	}
	newStart := start
	newEnd := end
	for ;newStart >= 0; newStart -- {
		if nums[newStart] <= nums[end] {
			break
		}
	}
	if newStart == -1 { // 删除的连续自数组是从下标0开始的一部分
		return end
	}
	for ; newEnd <= len(nums) - 1; newEnd++ {
		if nums[newEnd] >= nums[start] {
			break
		}
	}
	if newEnd == len(nums) { //  删除的数组是数组的最后一部分
		return len(nums) - start - 1
	}
	return min(end - newStart - 1, newEnd - start - 1)
}

func main() {
    nums:=[]int{1,2,1000,-1000,3,4}
    fmt.Println(getMinal(nums))
}
