package main

import(
    "fmt"
    //"strings"
    //"sort"
)

var testMod=false;

func test() {
}

func lemonadeChange(bills []int) bool {
    log:=map[int]int{5:0,10:0}
    for _,bill:=range bills {
        switch bill {
        case 5:
            log[5]++
        case 10:
            if log[5]==0 {
                return false
            }
            log[5]--
            log[10]++
        case 20:
            if log[5]==0 {
                return false
            }
            if log[10]!=0 {
                log[10]--
                log[5]--
            } else if log[5]>=3 {
                log[5]-=3
            } else {
                return false
            }
        }
    }
    return true
}

func main() {
    if testMod {
        test()
    }
    inp:=[]int{10,10}
    fmt.Println(lemonadeChange(inp))
}
