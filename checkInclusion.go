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

func checkInclusion(s1 string, s2 string) bool {
    if len(s2)<len(s1) {
        return false
    }
    table1:=make([]int, 26)
    count:=0
    for _,l := range s1 {
        table1[l-'a']++
        if table1[l-'a']==1 {
            count++
        }
    }

    for i:=0;i<len(s1);i++ {
        table1[s2[i]-'a']--
        if table1[s2[i]-'a']==0 {
            count--
        } else if table1[s2[i]-'a']==-1 {
            count++
        }
    }

    if count==0 {
        return true
    }

    fmt.Println(table1,count)

    for i:=0;i<len(s2)-len(s1);i++ {
        table1[s2[i]-'a']++
        if table1[s2[i]-'a']==0 {
            count--
        } else if table1[s2[i]-'a']==1 {
            count++
        }
        table1[s2[i+len(s1)]-'a']--
        if table1[s2[i+len(s1)]-'a']==0 {
            count--
        } else if table1[s2[i+len(s1)]-'a']==-1 {
            count++
        }
        fmt.Println(table1,count)
        if count==0 {
            return true
        }
    }
    return false
}

func main() {
    test()
    s1:="abc"
    s2:="bbbca"
    fmt.Println(checkInclusion(s1,s2))
}
