package conf

import (
	"back-end/model"
	"back-end/util"
	"fmt"
)

func Init() {

	// 设置日志级别
	util.BuildLogger("info")

	// 连接数据库
	username := "root"       //账号
	password := "199746"     //密码
	host := "42.193.131.171" //数据库地址，可以是Ip或者域名
	port := 3306             //数据库端口
	Dbname := "momoyu"       //数据库名
	timeout := "10s"         //连接超时，10秒
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8&parseTime=True&loc=Local&timeout=%s", username, password, host, port, Dbname, timeout)
	model.Database(dsn)
}
