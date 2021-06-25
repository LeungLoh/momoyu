package main

import (
	"back-end/conf"
	"back-end/router"
)

func main() {
	conf.Init()
	app := router.NewRouter()
	app.Run(":7000") // 监听并在 0.0.0.0:8080 上启动服务
}
