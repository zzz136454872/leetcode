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

func int_max(inp... int) int {
    out:=inp[0]
    for _,v := range inp {
        if out<v {
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

func candy(ratings []int) int {
    log1:=make([]int,len(ratings))
    log2:=make([]int,len(ratings))
    log1[0]=1
    log2[len(ratings)-1]=1
    for i:=1;i<len(log1);i++ {
        if ratings[i]>ratings[i-1] {
            log1[i]=log1[i-1]+1
        } else {
            log1[i]=1
        }
    }
    for i:=len(ratings)-2;i>=0;i-- {
        if ratings[i]>ratings[i+1] {
            log2[i]=log2[i+1]+1
        } else {
            log2[i]=1
        }
    }
    for i:=0;i<len(log1);i++ {
        log1[i]=int_max(log1[i],log2[i])
    }
    return int_sum(log1);
}

func main() {
    test()
    inp:=[]int{1,2,2}
    fmt.Println(candy(inp))
}
