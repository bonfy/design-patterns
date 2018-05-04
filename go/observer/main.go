package main

import (
	"fmt"
)


type Subject interface {
	Attach(observer Observer)
	// Detach(observer Observer)
	Notify()

}

type Observer interface {
	Update(state string)
}

type ConcreteSubject struct{
	observers []Observer
	State      string
}

func (self *ConcreteSubject) Attach(observer Observer) {
	self.observers = append(self.observers, observer)
}


func (self *ConcreteSubject) Notify() {
	for _, observer := range self.observers {
		observer.Update(self.State)
	}
}

type ConcreteObserver struct {
	name string
	state string
}

func (self *ConcreteObserver) Update(state string) {
	self.state = state
	fmt.Printf("%s State change: %s\n", self.name, self.state)
}

func main()  {
	subject := &ConcreteSubject{}
	subject.Attach(&ConcreteObserver{name:"observer-1"})
	subject.Attach(&ConcreteObserver{name:"observer-2"})
	subject.Attach(&ConcreteObserver{name:"observer-3"})

	subject.State = "New State..."
	subject.Notify()
}