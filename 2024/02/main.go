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

	fileName := "test.txt"
	if *runProd {
		fileName = "input.txt"
	}

	byteContents, _ := os.ReadFile(fileName)
	lines := strings.Split(string(byteContents), "\n")

	rawInput = strings.Join(lines[:len(lines)-1], "\n")
	return rawInput
}

func numsArraysInput() [][]int {
	nums := [][]int{}
	lines := strings.Split(getRawInput(), "\n")
	for i := 0; i < len(lines); i++ {
		strNums := strings.Split(lines[i], " ")
		localNums := make([]int, len(strNums))
		for j := 0; j < len(strNums); j++ {
			num, err := strconv.Atoi(strNums[j])
			if err != nil {
				panic(err)
			}

			localNums[j] = num
		}
		nums = append(nums, localNums)
	}

	return nums
}

func first() {
	lines := numsArraysInput()
	safeCount := 0
	for i := 0; i < len(lines); i++ {
		isCorrect := true
		direction := 1
		if lines[i][0] > lines[i][1] {
			direction = -1
		}
		for j := 1; j < len(lines[i]); j++ {
			line := lines[i]
			diff := line[j-1] - line[j]
			absDiff := max(diff, -diff)
			if absDiff < 1 || absDiff > 3 {
				isCorrect = false
				break
			}

			if diff > 0 && direction > 0 {
				isCorrect = false
				break
			}
			if diff < 0 && direction < 0 {
				isCorrect = false
				break
			}
		}

		if isCorrect {
			safeCount++
		}
	}

	fmt.Printf("Correct count is %d\n", safeCount)
}

func verifyRow(row []int) bool {
    badCount := 0
	for j := 1; j < len(row); j++ {
		diff := row[j-1] - row[j]
		absDiff := max(diff, -diff)
		if absDiff < 1 || absDiff > 3 {
			badCount++
		}

		if diff > 0 {
			badCount++
		}
	}

    if badCount == 0 {
        return true
    }

    badCount = 0
	for j := 1; j < len(row); j++ {
		diff := row[j-1] - row[j]
		absDiff := max(diff, -diff)
		if absDiff < 1 || absDiff > 3 {
			badCount++
		}

		if diff < 0 {
			badCount++
		}
	}
    return badCount == 0
}

func second() {
	lines := numsArraysInput()
	safeCount := 0
	for i := 0; i < len(lines); i++ {
        if verifyRow(lines[i]) {
			safeCount++
            continue
		}

        for j := 0; j < len(lines[i]); j++ {
            temp := []int{}
            temp = append(temp, lines[i][0:j]...)
            temp = append(temp, lines[i][j+1:len(lines[i])]...)
            if verifyRow(temp) {
                safeCount++
                break
            }
        }
	}

	fmt.Printf("Correct count is %d\n", safeCount)
}

func main() {
	first()
	second()
}
