//条件语句
package main

import "fmt"
func main()  {
	var a int = 20
	if a!=20 {
		fmt.Println("y")


	} else {
		fmt.Println("n")
	}

	var mark int = 90
	var garde string = "A"

	switch mark {
	case 90: garde = "A"
	case 80 : garde = "B"
	default : garde = "C"
	fmt.Println(garde,mark)
		
	}
}