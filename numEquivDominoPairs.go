package main

import(
    "fmt"
    //"strings"
    "sort"
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

func numEquivDominoPairs(dominoes [][]int) int {
    for i:=0;i<len(dominoes);i++ {
        if dominoes[i][0]>dominoes[i][1] {
            tmp:=dominoes[i][0]
            dominoes[i][0]=dominoes[i][1]
            dominoes[i][1]=tmp
        }
    }
    less:=func(i,j int) bool {
        if dominoes[i][0]!=dominoes[j][0] {
            return dominoes[i][0]<dominoes[j][0]
        }
        return dominoes[i][1]<dominoes[j][1]
    }
    sort.Slice(dominoes,less)
    out:=0
    same:=func(i,j int) bool {
        return dominoes[i][0]==dominoes[j][0] &&
            dominoes[i][1]==dominoes[j][1]
        }
    for i:=0;i<len(dominoes); {
        j:=i+1
        //fmt.Println(i,out)
        for j<len(dominoes)&&same(i,j) {
            j++
        }
        tmp:=j-i
        out+=(tmp-1)*tmp/2
        i=j
    }
    return out
}

func main() {
    test()
    dominoes:=[][]int{{2,1},{5,4},{3,7},{6,2},{4,4},{1,8},{9,6},{5,3},{7,4},{1,9},{1,1},{6,6},{9,6},{1,3},{9,7},{4,7},{5,1},{6,5},{1,6},{6,1},{1,8},{7,2},{2,4},{1,6},{3,1},{3,9},{3,7},{9,1},{1,9},{8,9}}
    fmt.Println(numEquivDominoPairs(dominoes))
}
