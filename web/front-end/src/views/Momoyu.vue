<template>
  <div>
    <el-row :gutter="30">
      <el-col
        :span="6"
        v-for="(articles, website, index) in result"
        :key="index"
      >
        <el-card>
          <div class="hot-title-name">
            <svg class="icon" aria-hidden="true">
              <use :xlink:href="'#icon-' + website"></use>
            </svg>
            <span class="hot-title-name">{{ getwebsite(website) }}</span>
          </div>
          <div class="hot-content">
            <ul>
              <li
                v-for="(article, index) in articles"
                :index="index"
                :key="index"
              >
                <a :href="article.Url" target="_blank" :title="article.Title">
                  <span>{{ index + 1 }}.</span>
                  <span>{{ article.Title }}</span>
                  <span>{{ article.Subtitle }}</span>
                </a>
              </li>
            </ul>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
    
<script>
import { gethotlist } from "../api/index";
export default {
  data() {
    return {
      result: {},
      websites: {
        douban: "豆瓣",
        zhihu: "知乎",
        oschina: "开源中国",
        weibo: "微博",
      },
      icon: "#icon-douban",
    };
  },
  mounted() {
    this.getresult();
  },
  methods: {
    getresult() {
      gethotlist().then((res) => {
        if (res.status != 200) {
          this.$message.error(res.error);
        } else {
          this.result = res.data;
        }
      });
    },
    getwebsite: function (val) {
      return this.websites[val];
    },
  },
};
</script>
<style >
.el-card {
  background-color: #1f2025;
  border-color: #1f2025;
  margin-top: 30px;
  margin-bottom: 30px;
  word-break: break-all;
}

.hot-title-name {
  height: 30px;
  padding: 0 8px 0 20px;
  margin-right: 7px;
  margin-bottom: 30px;
  overflow: auto;
}

.hot-title-name span {
  display: inline-block;
  line-height: 30px;
  vertical-align: top;
  text-align: center;
  font-weight: bolder;
  font-size: 20px;
  color: #aaa;
  cursor: pointer;
  margin-left: 5px;
}

.hot-content {
  height: 320px;
  padding: 0 8px 0 20px;
  margin-right: 7px;
  overflow: auto;
}

.hot-content li a span:first-of-type {
  padding-right: 3px;
}

.hot-content li:first-of-type a span:first-of-type {
  color: #cc3939;
}

.hot-content li:nth-of-type(2) a span:first-of-type {
  color: #de6b30;
}

.hot-content li:nth-of-type(3) a span:first-of-type {
  color: #cc984f;
}

.hot-content ul {
  list-style: none;
}

.hot-content span {
  margin-left: 10px;
  /* max-width: 400px; */
  word-break: break-all;
}
.hot-content li a span:first-of-type {
  width: 40px;
}

.hot-content li a span:nth-of-type(2) {
  width: 400px;
}

.hot-content li a span:nth-of-type(3) {
  width: 100px;
}

.hot-content a {
  width: 100%;
  line-height: 1.3em;
  color: #666666;
  display: flex;
  justify-content: start;
}
.hot-content a:link {
  text-decoration: none;
  color: inherit;
  transition: color 0.1s;
  width: 100%;
  line-height: 1.3em;
  cursor: pointer;
  color: #aaaaaa;
}

.hot-content::-webkit-scrollbar {
  width: 5px;
  height: 8px;
}

.hot-content:hover ::-webkit-scrollbar-track {
  border-radius: 10px;
  background-color: transparent;
}

/*定义滑块 内阴影+圆角*/
.hot-content:hover::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background-color: #18191e;
}
</style>