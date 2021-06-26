<template>
  <div>
    <el-row :gutter="20">
      <el-col
        :span="8"
        v-for="(articles, website, index) in result"
        :key="index"
      >
        <el-card>
          <div>
            <div>{{ website }}</div>
            <div>
              <ul>
                <li
                  v-for="article in articles"
                  :index="article.Title"
                  :key="article.Title"
                >
                  <a href="{{article.Url}}">
                    <span>{{ article.Title }}</span>
                  </a>
                </li>
              </ul>
            </div>
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
      test: {
        test1: [
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
        ],
        test2: [
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
        ],
        test3: [
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
          { title: "123", url: "123", subtitle: "123" },
        ],
      },
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
          console.log(res);
          this.result = res.data;
        }
      });
    },
  },
};
</script>
<style >
.el-card {
  min-width: 600;
  margin-right: 20px;
  transition: all 0.5s;
  /* background: red; */
}
</style>