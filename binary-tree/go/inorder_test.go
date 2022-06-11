package main

import (
	"reflect"
	"testing"
)

func Test_inOrderTraversalIter(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "123",
			args: args{
				root: &TreeNode{Val: 1, Right: &TreeNode{Val: 2}, Left: &TreeNode{Val: 3}},
			},
			want: []int{2, 1, 3},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := inOrderTraversalIter(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("inOrderTraversalIter() = %v, want %v", got, tt.want)
			}
		})
	}
}
