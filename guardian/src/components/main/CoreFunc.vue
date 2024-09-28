<template>
  <el-row justify="space-between" :gutter="20">
    <el-col :span="6">

      <a-card hoverable class="custom-card">
        <div class="text1">定义监管规则</div>

        <div>
          <ul class="custom-list">
            <li>可视化定义复杂监管语言</li>
          </ul>
        </div>
      </a-card>

    </el-col>

    <el-col :span="6">
      <a-card hoverable class="custom-card">
        <div class="text1">验证模型效果</div>

        <div>
          <ul class="custom-list">
            <li>一键验证多模态大模型效果</li>
          </ul>
        </div>
      </a-card>

    </el-col>

    <el-col :span="6">
      <a-card hoverable class="custom-card">
        <div class="text1">创建监管任务</div>

        <div>
          <ul class="custom-list">
            <li>根据规则、模型、违规逻辑<br>创建任务</li>
          </ul>
        </div>
      </a-card>

    </el-col>

    <el-col :span="6">
      <a-card hoverable class="custom-card">
        <div class="text1">智能监管任务</div>

        <div>
          <ul class="custom-list">
            <li>违规事件自动可视化</li>
          </ul>
        </div>
      </a-card>

    </el-col>
  </el-row>
</template>

<script setup lang="ts">

</script>


<style scoped>
.custom-card{
  height: 100%;
}

.cover-container {
  display: flex;
  justify-content: left; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  width: 100%; /* 确保容器占满整个 cover 区域 */
  height: 100%; /* 确保容器占满整个 cover 区域 */

  margin-top: 15%;
}

.card-image {
  width: 25%;

  object-fit: cover;
  overflow: hidden;
}
  
.text1 {
  color: black;
  font-size: 32px;
  font-weight: 600;
  text-align: left;

  margin-top: 5%;
  margin-bottom: 10%;
  margin-left: 5%;
  margin-right: 20%;
  transition: color 0.25s ease; /* 添加渐变效果 */
}



.custom-list {
  list-style-type: none; /* 移除默认的列表样式 */
  padding-left: 0;
}

.custom-list li {
  font-size: 20px;
  font-weight: 400;

  position: relative;
  padding-left: 30px; /* 为点留出空间 */
  line-height: 2; /* 设置行高 */
  margin-bottom: 8px; /* 设置间距 */
}

.custom-list li::before {
  content: ''; /* 添加点 */
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%); /* 垂直居中 */
  width: 8px;
  height: 8px;
  background-color: #FFA500; /* 默认橙色 */
  border-radius: 50%; /* 使点呈圆形 */
  transition: background-color 0.3s ease; /* 添加渐变效果 */
}

.custom-card:hover .custom-list li::before {
  background-color: #409EFF; /* 鼠标悬停时变为蓝色 */
}

.custom-card:hover .text1 {
  color: #409EFF; /* 鼠标悬停时变为蓝色 */
}

::v-deep(.ant-card-body) {
  padding: 0;
  padding-top: 10%;
  padding-left: 10%;
  padding-bottom: 40px;
}

</style>