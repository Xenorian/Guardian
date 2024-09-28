<template>
  <el-row justify="space-between" :gutter="40">
    <el-col :span="6">

      <a-card hoverable class="custom-card">
        <template #cover>
          <div class="cover-container">
            <img src="../../assets/mainPage/TechAdv1.png" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text1">监管语言</div>

        <div>
          <ul class="custom-list">
            <li>总结监管规则规律</li>
            <li>构建多模态监管语言</li>
            <li>一致性验证</li>
          </ul>
        </div>
      </a-card>

    </el-col>

    <el-col :span="6">
      <a-card hoverable class="custom-card">
        <template #cover>
          <div class="cover-container">
            <img src="../../assets/mainPage/TechAdv2.png" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text1">识别算法</div>

        <div>
          <ul class="custom-list">
            <li>多模态规则与数据融合机制</li>
            <li>视频与信息流的事件识别算法</li>
            <li>违规事件识别与定位算法研制</li>
          </ul>
        </div>
      </a-card>

    </el-col>

    <el-col :span="6">
      <a-card hoverable class="custom-card">
        <template #cover>
          <div class="cover-container">
            <img src="../../assets/mainPage/TechAdv3.png" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text1">场景自适应</div>

        <div>
          <ul class="custom-list">
            <li>监管算法迁移学习机制</li>
            <li>监管规则自监督表征学习算法</li>
            <li>多任务监管场景适配框架</li>
          </ul>
        </div>
      </a-card>

    </el-col>

    <el-col :span="6">
      <a-card hoverable class="custom-card">
        <template #cover>
          <div class="cover-container">
            <img src="../../assets/mainPage/TechAdv4.png" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text1">自动化平台</div>

        <div>
          <ul class="custom-list">
            <li>可视化监管语言定义工具</li>
            <li>自动化违规识别平台系统</li>
            <li>多服务场景示范应用</li>
          </ul>
        </div>
      </a-card>

    </el-col>
  </el-row>
</template>

<script setup lang="ts">

</script>


<style scoped>
.cover-container {
  display: flex;
  justify-content: center; /* 水平居中 */
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
  text-align: center;

  margin-bottom: 10%;
  transition: color 0.25s ease; /* 添加渐变效果 */
}



.custom-list {
  list-style-type: none; /* 移除默认的列表样式 */
  padding-left: 10%;
}

.custom-list li {
  font-size: 20px;
  font-weight: 400;

  position: relative;
  padding-left: 20px; /* 为点留出空间 */
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
.custom-card{
  min-width: 340px;
}
.custom-card:hover .custom-list li::before {
  background-color: #409EFF; /* 鼠标悬停时变为蓝色 */
}

.custom-card:hover .text1 {
  color: #409EFF; /* 鼠标悬停时变为蓝色 */
}

::v-deep(.ant-card-body) {
  padding: 0;
  padding-bottom: 40px;
}

</style>