package main

import "testing"

func Test_matchSock(t *testing.T) {
	type args struct {
		n  int
		ar []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{name: "2", args: args{7, []int{1, 2, 1, 2, 1, 3, 2}}, want: 2},
		{name: "3", args: args{8, []int{1, 2, 1, 2, 1, 3, 2, 3}}, want: 3},
		{name: "0", args: args{6, []int{0, 1, 2, 3, 4, 5}}, want: 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := matchSock(tt.args.n, tt.args.ar); got != tt.want {
				t.Errorf("matchSock() = %v, want %v", got, tt.want)
			}
		})
	}
}
