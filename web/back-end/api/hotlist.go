package api

import (
	"back-end/common"
	"back-end/model"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func GetHotList(ctx *gin.Context) {
	var res common.Result
	hotlist := make(gin.H)
	websites := []string{
		"weibo",
		"douban",
		"oschina",
	}

	for _, website := range websites {
		var result []model.Momoyu
		DB := model.DB.Model(&model.Momoyu{})
		DB.Where("website = ?", website).Order("date desc").Limit(20).Find(&result)
		for index, value := range result {
			count, _ := strconv.ParseFloat(value.Subtitle, 32)
			if count > 10000 {
				result[index].Subtitle = fmt.Sprintf("%.2f 万", count/10000)
			} else if count > 1000 {
				result[index].Subtitle = fmt.Sprintf("%.2f 千", count/1000)
			}

		}
		hotlist[website] = result

	}
	res = common.Result{Httpcode: http.StatusOK, Msg: "Success", Data: hotlist}
	ctx.Set("Res", res)
	ctx.Next()
}
