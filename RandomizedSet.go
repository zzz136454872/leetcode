package main

import (
	"fmt"
	//"strings"
	//"sort"
	"math/rand"
	"time"
)

var testMod = false

func test() {

}

func int_min(inp ...int) int {
	out := inp[0]
	for _, v := range inp {
		if out > v {
			out = v
		}
	}
	return out
}

func int_sum(inp []int) int {
	out := 0
	for _, v := range inp {
		out += v
	}
	return out
}

func max(inp ...interface{}) interface{} {
	if len(inp) == 1 {
		list := inp[0]
		switch list.(type) {
		case []int:
			out := list.([]int)[0]
			for _, v := range list.([]int)[1:] {
				if out < v {
					out = v
				}
			}
			return out
		case []float32:
			out := list.([]float32)[0]
			for _, v := range list.([]float32)[1:] {
				if out < v {
					out = v
				}
			}
			return out
		case []float64:
			out := list.([]float64)[0]
			for _, v := range list.([]float64)[1:] {
				if out < v {
					out = v
				}
			}
			return out
		default:
			fmt.Printf("type unknown: %T\n", list)
		}
	}
	out := inp[0]
	for _, v := range inp {
		switch out.(type) {
		case int:
			if out.(int) < v.(int) {
				out = v
			}
		case float32:
			if out.(float32) < v.(float32) {
				out = v
			}
		case float64:
			if out.(float64) < v.(float64) {
				out = v
			}
		default:
			fmt.Printf("type unknown: %T\n", out)
			return out
		}
	}
	return out
}

type RandomizedSet struct {
	table []int
	loc   map[int]int
}

func Constructor() RandomizedSet {
	rand.Seed(time.Now().Unix())
	return RandomizedSet{table: []int{}, loc: map[int]int{}}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.loc[val]; ok {
		return false
	}
	this.loc[val] = len(this.table)
	this.table = append(this.table, val)
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	if _, ok := this.loc[val]; !ok {
		return false
	}
	id := this.loc[val]
	this.table[id] = this.table[len(this.table)-1]
	this.loc[this.table[id]] = id
	this.table = this.table[:len(this.table)-1]
	delete(this.loc, val)
	return true
}

func (this *RandomizedSet) GetRandom() int {
	return this.table[rand.Intn(len(this.table))]
}

func main() {
	test()
	// ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
	// [[],[1],[2],[2],[],[1],[2],[]]
	r := Constructor()
	r.Insert(1)
	r.Remove(2)
}
