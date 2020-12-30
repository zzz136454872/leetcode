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

type heap []int

func (list *heap) adjust(loc int) {
    maxLoc:=loc
    if 2*loc<len(*list)&&(*list)[2*loc]>=(*list)[maxLoc] {
        maxLoc=2*loc
    }
    if 2*loc+1<len(*list)&&(*list)[2*loc+1]>(*list)[maxLoc] {
        maxLoc=2*loc+1 
    }
    if maxLoc!=loc {
        tmp:=(*list)[loc]
        (*list)[loc]=(*list)[maxLoc]
        (*list)[maxLoc]=tmp
        list.adjust(maxLoc)
    }
}

func (list *heap) heapfy() {
    last:=len(*list)/2
    for i:= last;i>=0;i-- {
        list.adjust(i)
    }
}

func (list *heap) push(val int) {
    idx:=len(*list)
    *list=append(*list,val)
    for idx>0 {
        father:=idx/2
        if (*list)[father]<(*list)[idx] {
            tmp:=(*list)[father]
            (*list)[father]=(*list)[idx]
            (*list)[idx]=tmp
        } else {
            break
        }
        idx=father
    }
}

func (list *heap) pop() int {
    l:=len(*list)
    out:=(*list)[0]
    (*list)[0]=(*list)[len(*list)-1]
    (*list)=(*list)[:l-1]
    list.adjust(0)
    return out
}

func lastStoneWeight(stones []int) int {
    s:=heap(stones)
    s.heapfy()
    var t1,t2 int 
    for len(s)>2 {
        t1=s.pop()
        t2=s.pop()
        if t1!=t2 {
            s.push(t1-t2)
        }
    }
    t1=s.pop()
    if len(s)==0 {
        return t1
    }
    t2=s.pop()
    if t1==t2 {
        return 0
    }
    return t1-t2
}

func main() {
    test()
    inp:=[]int{2,7,4,1,8,1}
    fmt.Println(lastStoneWeight(inp))
}
