package main

import(
    "fmt"
    //"strings"
    //"sort"
)

var testMod=false;

func test() {

}

func int_min(inp... int) int {
    out:=inp[0]
    for _,v := range inp {
        if out>v {
            out=v
        }
    }
    return out
}

func minCostClimbingStairs(cost []int) int {
    log:=make([]int, len(cost))
    log[0]=cost[0]
    log[1]=cost[1]
    for i:=2;i<len(cost);i++ {
        log[i]=int_min(log[i-1],log[i-2])+cost[i]
    }
    l:=len(cost)
    return int_min(log[l-1],log[l-2])
}

func main() {
    test()
    cost :=[]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
    fmt.Println(minCostClimbingStairs(cost))
}
