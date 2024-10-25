<template>
  <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
    
    <div class="main">
      <el-row :gutter="20"> <!-- gutter 是列间距，可以根据需要调整 -->
        <el-col :span="5">
          <div class="grid-content bg-purple" style="margin-right: 10%;">
            <Form />
          </div>
        </el-col>
        <el-col :span="11">
          <div class="grid-content bg-purple-light">
            <div style="font-size: 25px;font-weight: 800;margin-bottom: 3%;">模型训练</div>

            <div class="mid">
              <a-card class="card" hoverable style="width: 240px">
                <template #cover>
                  <img src="../../../assets/test/1.png" alt="Card Image" class="card-image" />
                </template>
                <a-card-meta title="HOGRL">
                  <template #description>针对欺诈检测的高阶图表示学习模型</template>
                </a-card-meta>
              </a-card>

              <a-card class="card" hoverable style="width: 240px">
                <template #cover>
                  <img src="../../../assets/test/2.png" alt="Card Image" class="card-image" />
                </template>
                <a-card-meta title="GTAN">
                  <template #description>欺诈检测的半监督图神经网络模型</template>
                </a-card-meta>
              </a-card>

              <a-card class="card" hoverable style="width: 240px">
                <template #cover>
                  <img src="../../../assets/test/3.png" alt="Card Image" class="card-image" />
                </template>
                <a-card-meta title="待导入模型">
                  <template #description>添加模型描述</template>
                </a-card-meta>
              </a-card>
            </div>

            <div class="button-group">
              <el-button type="primary">模型导入</el-button>
              <el-button type="primary">模型管理</el-button>
            </div>

          </div>
        </el-col>
        <el-col :span="8">
          <div style="font-size: 25px;font-weight: 800;margin-bottom: 3%;">训练过程</div>
          <div style="font-size: 20px;font-weight: 500;margin-bottom: 3%;">实时训练输出</div>

          <div class="right">
            <img src="../../../assets/test/1.png" alt="Card Image" class="card-image" style="width: 70%;text-align: center;"/>
          </div>

          <div class="button-group">
            <el-button type="primary">启动训练</el-button>
            <el-button type="danger">中止训练</el-button>
            <el-button type="primary">保存至模型库</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';

import Form from '../../../components/model/form.vue'
</script>

<style scoped>
.alert{
  margin-bottom: 1%
}

.mid{
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: left; /* 水平居中 */
  height: 100%; /* 根据你的需求调整高度 */
  color: white;
  font-size: medium;
}

.right{
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  color: white;
  font-size: medium;
}

.card{
  margin-right: 3%;
  margin-left: 3%;
}

.button-group {
  margin: 3%;
  text-align: right;
}
</style>