package main

import (
	"io/ioutil"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_outputNumber(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		s    string
		want string
	}{
		{s: "1.345", want: "1000\n300\n40\n5\n"},
		{s: "1.345.679", want: "1000000\n300000\n40000\n5000\n600\n70\n9\n"},
	}
	for _, tt := range tests {
		t.Run(tt.s, func(t *testing.T) {
			rescueStdout := os.Stdout
			r, w, _ := os.Pipe()
			os.Stdout = w

			outputNumber(tt.s)
			w.Close()
			out, _ := ioutil.ReadAll(r)
			os.Stdout = rescueStdout

			assert.Equal(t, tt.want, string(out))

		})
	}
}
