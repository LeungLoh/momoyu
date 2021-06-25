package router

import (
	"back-end/api"
	"back-end/middleware"

	"github.com/gin-gonic/gin"
)

func NewRouter() *gin.Engine {
	r := gin.Default()
	r.Use(middleware.Cors())
	r.Use(middleware.Response())
	v1 := r.Group("/api/v1")
	v1.GET("hotlist", api.GetHotList)
	return r
}
