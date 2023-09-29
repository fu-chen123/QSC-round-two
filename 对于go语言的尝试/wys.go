//位运算
package main

import "fmt"

func main()  {
	var a int = 60
	var b int = 13
	fmt.Println(a&b)  //与
	fmt.Println(a|b)  //或
	fmt.Println(a^b)  //异或
	fmt.Println(a<<2)  //二进制位前进两位
	fmt.Println(a>>3)  //后退三位
}