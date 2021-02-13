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
    if len(inp)==1 {
        list:=inp[0]
        switch list.(type) {
        case []int:
            out:=list.([]int)[0]
            for _,v := range list.([]int)[1:] {
                if out<v {
                    out=v
                }
            }
            return out
        case []float32:
            out:=list.([]float32)[0]
            for _,v := range list.([]float32)[1:] {
                if out<v {
                    out=v
                }
            }
            return out
        case []float64:
            out:=list.([]float64)[0]
            for _,v := range list.([]float64)[1:] {
                if out<v {
                    out=v
                }
            }
            return out
        default:
            fmt.Printf("type unknown: %T\n",list)
        }
    }
    out:=inp[0]
    for _,v := range inp {
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

func findDisappearedNumbers(nums []int) []int {
    n:=len(nums)
    for _,num:=range(nums) {
        nums[(num-1)%n]+=n
    }
    out:=[]int{}

    for i,v:=range(nums) {
        if v<=n {
            out=append(out,i+1)
        }
    }
    return out
}

func main() {
    test()
    inp:=[]int{4,3,2,7,8,2,3,1}
    fmt.Println(findDisappearedNumbers(inp))
}
