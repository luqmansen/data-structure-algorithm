package main

import (
	"reflect"
	"testing"
)

func Test_mergeSorted(t *testing.T) {
	type args struct {
		arr1 []int
		arr2 []int
	}
	tests := []struct {
		args args
		want []int
	}{
		{args: args{
			arr1: []int{1, 3, 5, 7},
			arr2: []int{2, 4, 6, 8},
		}, want: []int{1, 2, 3, 4, 5, 6, 7, 8}},
	}
	for _, tt := range tests {
		t.Run("", func(t *testing.T) {
			if got := mergeSortedArray(tt.args.arr1, tt.args.arr2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("mergeSortedArray() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_mergesort(t *testing.T) {
	tests := []struct {
		param []int
		want  []int
	}{
		{param: []int{7, 4, 3, 2, 1, 5, 6},
			want: []int{1, 2, 3, 4, 5, 6, 7},
		},
	}
	for _, tt := range tests {
		t.Run("", func(t *testing.T) {
			mergesort(tt.param)
			if !reflect.DeepEqual(tt.param, tt.want) {
				t.Errorf("mergesort() = %v, want %v", tt.param, tt.want)
			}
		})
	}
}
