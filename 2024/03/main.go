package main

import (
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var rawInput = ""

func getRawInput() string {
	if rawInput != "" {
		return rawInput
	}

	runProd := flag.Bool("prod", false, "")
	flag.Parse()

	fileName := "input.txt"
	if *runProd {
		fileName = "input-2.txt"
	}

	byteContents, _ := os.ReadFile(fileName)
	lines := strings.Split(string(byteContents), "\n")

	rawInput = strings.Join(lines[:len(lines)-1], "\n")
	return rawInput
}

func first() {
	sum := 0
	input := strings.Split(getRawInput(), "\n")
	for i := 0; i < len(input); i++ {
		input[i] = strings.ReplaceAll(input[i], "mul(", "")
		input[i] = strings.ReplaceAll(input[i], ")", "")
		split := strings.Split(input[i], ",")
		left, _ := strconv.Atoi(split[0])
		right, _ := strconv.Atoi(split[1])
		sum += left * right
	}

	fmt.Println(sum)
}

func second() {
	sum := 0
	isEnabled := true
	input := strings.Split(getRawInput(), "\n")
	for i := 0; i < len(input); i++ {
		if input[i] == "do()" {
			isEnabled = true
			continue
		} else if input[i] == "don't()" {
			isEnabled = false
			continue
		}

		input[i] = strings.ReplaceAll(input[i], "mul(", "")
		input[i] = strings.ReplaceAll(input[i], ")", "")
		split := strings.Split(input[i], ",")
		left, _ := strconv.Atoi(split[0])
		right, _ := strconv.Atoi(split[1])

		if isEnabled {
			sum += left * right
		}
	}

	fmt.Println(sum)
}

func main() {
	// first()
	second()
}
