package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Data struct {
	A int
	S string
}

func main() {

	// 1行読み込む
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	line := scanner.Text()
	chars := strings.Split(line, " ")

	//最後に受け取る値を数値に変換し、mに格納
	var m int
	m, _ = strconv.Atoi(chars[len(chars)-1])

	data := []Data{}
	var a int
	var s string
	len := len(chars) - 1

	for _, ch := range chars[0:len] {
		elements := strings.Split(ch, ":")

		a, _ = strconv.Atoi(elements[0])
		s = elements[1]

		ele := Data{A: a, S: s}
		data = append(data, ele)
	}

	sort.SliceStable(data, func(i, j int) bool { return data[i].A < data[j].A })

	fmt.Println(data)
	fmt.Println(m)

}
