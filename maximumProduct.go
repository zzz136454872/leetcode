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

func int_sum(inp []int) int {
    out:=0
    for _,v := range inp {
        out+=v
    }
    return out
}

func max(inp ...interface{}) interface{}{
    var list []interface{}
    if len(inp)==1 {
        list=inp[0].([]interface{})
    } else {
        list=inp
    }
    out:=list[0]
    for _,v := range list {
        switch out.(type) {
        case int:
            if out.(int)<v.(int) {
                out=v
            }
        case float32:
            if out.(float32)<v.(float32) {
                out=v
            }
        case float64:
            if out.(float64)<v.(float64) {
                out=v
            }
        default:
            fmt.Printf("type unknown: %T\n",out)
            return out
        }
    }
    return out
}

func maximumProduct(nums []int) int {
    max0:=-123456
    max1:=-123456
    max2:=-123456
    min0:= 123456
    min1:= 123456
    for _,num:=range(nums) {
        if num>=max0 {
            max2=max1
            max1=max0
            max0=num
        } else if num>=max1{
            max2=max1
            max1=num
        } else if num>=max2 {
            max2=num
        }
        if num<=min0 {
            min1=min0
            min0=num
        } else if num<=min1 {
            min1=num
        }
    }
    //fmt.Println(min0,min1)
    //fmt.Println(max0,max1,max2)
    return max(min0*min1*max0,max0*max1*max2).(int)
}

func main() {
    test()
    inp:=[]int{-1,-2,-3,-4}
    fmt.Println(maximumProduct(inp))
}

