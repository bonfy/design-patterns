package main

import (
	"fmt"
)

type Component interface {
	Operation() string
}

type ConcreteComponent struct {
}

func (self *ConcreteComponent) Operation() string {
	return "I am component!"
}

type ConcreteDecoratorA struct {
	component Component
}

func (self *ConcreteDecoratorA) Operation() string {
	return "<A>" + self.component.Operation() + "</A>"
}

type ConcreteDecoratorB struct {
	component Component
}

func (self *ConcreteDecoratorB) Operation() string {
	return "<B>" + self.component.Operation() + "</B>"
}

func main() {
	decorator := &ConcreteDecoratorB{&ConcreteDecoratorA{&ConcreteComponent{}}}
	result := decorator.Operation()

	fmt.Println(result)
}
