package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	// 引数の数を確認
	if len(os.Args) != 3 {
		fmt.Println("Usage: go run add.go <num1> <num2>")
		return
	}

	// 引数を取得
	arg1 := os.Args[1]
	arg2 := os.Args[2]

	// 文字列から整数に変換
	num1, err1 := strconv.ParseFloat(arg1, 64)
	if err1 != nil {
		fmt.Printf("Error: %s is not a valid number.\n", arg1)
		return
	}

	num2, err2 := strconv.ParseFloat(arg2, 64)
	if err2 != nil {
		fmt.Printf("Error: %s is not a valid number.\n", arg2)
		return
	}

	// 加算結果を出力
	result := num1 + num2
	fmt.Println(result)
}
