package api

import (
	"back-end/common"
	"back-end/model"
	"net/http"

	"github.com/gin-gonic/gin"
)

func GetHotList(ctx *gin.Context) {
	var res common.Result
	hotlist := make(gin.H)
	websites := []string{
		"douban",
		"zhihu",
		"weibo",
		"oschina",
	}

	for _, website := range websites {
		var result []model.Momoyu
		DB := model.DB.Model(&model.Momoyu{})
		DB.Where("website = ?", website).Order("date desc").Limit(20).Find(&result)
		hotlist[website] = result

	}
	res = common.Result{Httpcode: http.StatusOK, Msg: "Success", Data: hotlist}
	ctx.Set("Res", res)
	ctx.Next()
}
