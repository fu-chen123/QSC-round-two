package main


/*	var mark int = 90
	var garde string = "A"

	switch mark {
	case 90: garde = "A"
	case 80 : garde = "B"
	default : garde = "C"
	fmt.Println(garde,mark)*/

import "fmt"

func main()  {
	var mark int = 90
	var garde string ="a"

	switch  {
	case mark==90:
		garde = "a"
	case mark==80 :
		garde = "b"
	default :
		garde = "c"
	fmt.Println(mark,garde)
		
	}
}