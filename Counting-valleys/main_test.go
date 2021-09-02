package main

import "testing"

func Test_countingValleys(t *testing.T) {
	tests := []struct {
		s    string
		want int32
	}{
		{s: "DDUUDDUDUUUD", want: 2},
		{s: "UDDDUDUU", want: 1},
	}
	for _, tt := range tests {
		t.Run("", func(t *testing.T) {
			if got := countingValleys(0, tt.s); got != tt.want {
				t.Errorf("countingValleys() = %v, want %v", got, tt.want)
			}
		})
	}
}
