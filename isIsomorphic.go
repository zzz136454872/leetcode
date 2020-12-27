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

func isIsomorphic(s string, t string) bool {
    if len(s)!=len(t) {
        return false
    }
    log1:=map[byte]byte{}
    log2:=map[byte]byte{}
    for i:=0;i<len(s);i++ {
        c1:=log1[s[i]]
        c2:=log2[t[i]]
        if c1==0 && c2==0 {
            log1[s[i]]=t[i]
            log2[t[i]]=s[i]
        } else if c1==0 || c2==0 {
            return false
        } else if c1==t[i] && c2==s[i] {
            continue
        } else {
            return false
        }
    }
    return true
}

func main() {
    test()
    s:="aba"
    t:="baa"
    fmt.Println(isIsomorphic(s,t))
}
