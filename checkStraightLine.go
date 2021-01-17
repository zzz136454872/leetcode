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

func check(a,b,c []int) bool {
    return (a[1]-b[1])*(c[0]-b[0])==(c[1]-b[1])*(a[0]-b[0])
}

func checkStraightLine(coordinates [][]int) bool {
    if len(coordinates)<=2 {
        return true
    }
    for i:=2;i<len(coordinates);i++ {
        if !check(coordinates[0],coordinates[1],coordinates[i]) {
            return false
        }
    }
    return true
}

func main() {
    test()
    coordinates:=[][]int{{1,1},{2,2},{3,4},{4,5},{5,6},{7,7}}
    fmt.Println(checkStraightLine(coordinates))
}
