package main

import "fmt"
func main()  {
	var a bool =true
	var b bool = false
	fmt.Println(a&&b)  //与门
	fmt.Println(a||b)  //或门
	fmt.Println(!(a&&b))  //非门
}