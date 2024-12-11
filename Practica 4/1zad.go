package main

import (
	"fmt"
	"math/big"
	"strings"
)

func print(s string) {
	k := 0
	for i := 0; i < len(s); i++ {
		if k == 8 {
			fmt.Print(" ")
			k = 0
		}
		k++
		fmt.Print(string(s[i]))
	}
	fmt.Println()
}

func ToDec(num string, base int) string {
	dec := 0
	multiplier := 1
	for i := len(num) - 1; i >= 0; i-- {
		if num[i] >= '0' && num[i] <= '9' {
			dec += int(num[i]-'0') * multiplier
		} else {
			dec += int(num[i]-'A'+10) * multiplier
		}
		multiplier *= base
	}
	return fmt.Sprintf("%d", dec)
}

func ToBin(num string) string {
	n, _ := new(big.Int).SetString(num, 10)
	s := ""
	for n.Cmp(big.NewInt(0)) > 0 {
		s = fmt.Sprintf("%d", n.Mod(n, big.NewInt(2))) + s
		n.Div(n, big.NewInt(2))
	}
	for len(s) < 32 {
		s = "0" + s
	}
	return s
}

func plas1(s []rune, t int) {
	if s[t] == '0' {
		s[t] = '1'
		return
	} else {
		s[t] = '0'
		plas1(s, t-1)
		return
	}
}

func creat(n string, m int) string {
	flag := false
	if n[0] == '-' {
		n = n[1:]
		flag = true
	}
	if m != 10 {
		n = ToDec(n, m)
	}
	n = ToBin(n)
	if flag {
		print(n)
		fmt.Println()
		for i := 0; i < len(n); i++ {
			if n[i] == '1' {
				n = n[:i] + "0" + n[i+1:]
			} else {
				n = n[:i] + "1" + n[i+1:]
			}
		}
		plas1([]rune(n), len(n)-1)
	}
	return n
}

func main() {
	var n string
	var m int
	fmt.Println("Введите число и его систему: ")
	fmt.Scan(&n, &m)
	fmt.Println()
	s := creat(n, m)
	print(s)
	fmt.Println("\n\nenter чтобы продолжить")
	fmt.Scan(&n)
}