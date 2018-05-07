package singleton

type singleton struct{}

var instance *singleton

// GetInstance Return the only instance
func GetInstance() *singleton {
	return instance
}
