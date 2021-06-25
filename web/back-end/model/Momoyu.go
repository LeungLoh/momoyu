package model

type Momoyu struct {
	ID       int    `gorm:"primary_key"`
	Title    string `gorm:"column:title"`
	Url      string `gorm:"column:url"`
	Subtitle string `gorm:"column:subtitle"`
	Website  string `gorm:"column:website"`
	Date     int    `gorm:"column:date"`
}

func (u *Momoyu) TableName() string {
	return "momoyu"
}
