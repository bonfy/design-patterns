package singleton

// Singleton Struct
type Singleton struct{}

var instance *Singleton

// GetInstance Return the only instance
func GetInstance() *Singleton {
	return instance
}
