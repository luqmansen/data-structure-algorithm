package main_test

import "testing"

func checkIfExist(arr []int) bool {
	if len(arr) < 2 || len(arr) > 500 {
		return false
	}
	// find even number, add to candidate
	candidate := make(map[int][]int)
	for idx, val := range arr {
		if val%2 == 0 {
			candidate[val/2] = []int{val, idx}
		}
	}

	for idx, val := range arr {
		val := val
		valueFromMap, ok := candidate[val]
		if ok {
			//make sure it's different number
			if valueFromMap[1] != idx {
				return true
			}
		}
	}
	return false

	//	first iteration, worst case n
	// second iteration worst case n
	// BigO = 2n = n
}

func Test_checkIfExist(t *testing.T) {
	type args struct {
		arr []int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "true",
			args: args{arr: []int{10, 2, 5, 3}},
			want: true,
		},
		{
			name: "true",
			args: args{arr: []int{7, 1, 14, 11}},
			want: true,
		},
		{
			name: "false",
			args: args{arr: []int{3, 1, 7, 11}},
			want: false,
		},
		{
			name: "false",
			args: args{arr: []int{-2, 0, 10, -19, 4, 6, -8}},
			want: false,
		},
		{
			name: "true",
			args: args{arr: []int{0, 0}},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := checkIfExist(tt.args.arr)
			if got != tt.want {
				t.Errorf("checkIfExist() = %v, want %v", got, tt.want)
			}
		})
	}
}
