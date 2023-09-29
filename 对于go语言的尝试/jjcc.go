package main
//算术运算
import "fmt"

func main()  {
	var a int =1
	var b int =2
	var c int
	c=a+b
	a++
	b--
	fmt.Printf("%d\n",c)
	if (b>a){
		fmt.Printf("b>a")
	}
	num:=0
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(num)
}