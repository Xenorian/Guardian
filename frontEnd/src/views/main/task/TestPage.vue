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
            <div class="midHead" style="margin-bottom: 3%;margin-right: 5%;">
              <el-row :gutter="20">
                <el-col :span="5">
                  <div style="font-size: 25px;font-weight: 800;">任务运行</div>
                </el-col>
                <el-col :span="4" :offset="15" class="d-flex">
                  <el-text type="success">任务完成</el-text>
                  <CheckCircleTwoTone twoToneColor="#52c41a" style="margin-left: 3%;margin-top: 2%"/>
                </el-col>
              </el-row>
            </div>

            <div class="mid">  
              <midPart />
            </div>

          </div>
        </el-col>

        <el-col :span="8">
          <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">违规数量</div>
          <div class="text">
            <el-text class="mx-1">违规告警总数:<span class="alert-count">2</span></el-text>
            <el-text class="mx-1">违规规则数:&emsp;<span class="alert-count">2</span></el-text>
          </div>
          
          <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">违规规则</div>
          <div class="text">
            <el-text class="mx-1 dot-before">服务提供者必须告知服务消费者数据存储期限            </el-text>
            <el-text class="mx-1 dot-before">服务提供者必须告知联系信息</el-text>
          </div>

          <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">告警记录</div>
          <el-scrollbar height="300px">
            <div class="text">
              <el-text class="mx-1" size="large" type="info">违规内容:</el-text>
              <el-text class="mx-1" type="danger">users shall grant Studios the permanent,irrevocable,non-exclusive right to use the content and contributions posted by the users.            </el-text>
              <el-text class="mx-1" size="large" type="info">违规条约:</el-text>
              <el-text class="mx-1">服务提供者必须告知服务消费者数据存储期限            </el-text>
            </div>

            <div class="text">
              <el-text class="mx-1" size="large" type="info">违规内容:</el-text>
              <el-text class="mx-1" type="danger">users shall grant Studios the permanent,irrevocable,non-exclusive right to use the content and contributions posted by the users.            </el-text>
              <el-text class="mx-1" size="large" type="info">违规条约:</el-text>
              <el-text class="mx-1">服务提供者必须告知联系信息            </el-text>
            </div>
          </el-scrollbar>
          
        </el-col>
      </el-row>
    </div>
    
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref,reactive } from 'vue';
import {CheckCircleTwoTone} from '@ant-design/icons-vue';
import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus';

import Form from '../../../components/task/form.vue'
import { uploadImageURL } from '@/utils/api'

import midPart from '@/components/task/uploadAndDisplay.vue'
</script>

<style scoped>
.text {
  border: 1px solid #dddcdc; /* 添加细线边框 */
  border-radius: 8px;
  display: flex;
  align-items: flex-start; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  flex-direction: column;
  margin-bottom: 3%;
}

.boardered{
  border: 1px solid #dddcdc; /* 添加细线边框 */
  border-radius: 8px;
}

.mx-1{
  margin: 2%;
  margin-left: 5%;
  align-self: start;
}

.dot-before::before {
  content: '•'; /* 插入一个圆点 */
  margin-right: 10px; /* 控制圆点和文本之间的间隔 */
  color: #333; /* 圆点的颜色 */
}

.alert-count {
  margin-left: 50px; /* 调整这个值以控制间隔大小 */
}

.alert{
  margin-bottom: 1%
}

.mid{
  height: 100%; /* 根据你的需求调整高度 */
  font-size: medium;
  width: 100%;
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

.d-flex{
  display: flex;
  align-items: center;
  justify-content: right;
}
</style>