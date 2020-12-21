package main

import(
    "fmt"
    //"strings"
    //"sort"
)

var testMod=false;

func test() {
}

func min(a int,b int) int {
    if a>b {
        return b
    }
    return a
}

func minCostClimbingStairs(cost []int) int {
    log:=make([]int, len(cost))
    log[0]=cost[0]
    log[1]=cost[1]
    for i:=2;i<len(cost);i++ {
        log[i]=min(log[i-1],log[i-2])+cost[i]
    }
    l:=len(cost)
    return min(log[l-1],log[l-2])
}

func main() {
    test()
    cost :=[]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
    fmt.Println(minCostClimbingStairs(cost))
}
