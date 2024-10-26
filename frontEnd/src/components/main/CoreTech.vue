<template>
  <el-row justify="space-between">
    <el-col :span="5">
      <div class="item">
        <img class="icon" src="../../assets/mainPage/coreTechnology1.png">
        <div class="text-1">复杂监管场景规则定义</div>
        <div class="text-2">基于多模态规范数据的<br>服务监管语言</div>
      </div>
    </el-col>

    <el-col :span="1" class="item">
      <img class="array" src="../../assets/mainPage/array.png">
    </el-col>

    <el-col :span="5">
      <div class="item">
        <img class="icon" src="../../assets/mainPage/coreTechnology2.png">
        <div class="text-1">多模态违规事件识别</div>
        <div class="text-2">基于多模态规范融合与<br>违规分析算法</div>
      </div>
    </el-col>

    <el-col :span="1" class="item">
      <img class="array" src="../../assets/mainPage/array.png">
    </el-col>

    <el-col :span="5">
      <div class="item">
        <img class="icon" src="../../assets/mainPage/coreTechnology3.png">
        <div class="text-1">监管算法自动化适应</div>
        <div class="text-2">基于智能服务监管软件平台<br>和示范应用模型</div>
      </div>
    </el-col>
  </el-row>
</template>

<style scoped>


.array{
  width: 100%;
  height: 30%;
}

.item{
  display: flex;
  flex-direction: column;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */

  color: white;
  font-size: medium;
}

.icon {
  width: 35%;
  object-fit: cover;
}
  
.text-1 {
  color: black;
  font-size: 28px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 2%
}

.text-2{
  color: black;
  font-size: 20px;
  font-weight: light;
  text-align: center;
}
</style>