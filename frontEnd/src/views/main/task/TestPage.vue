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

                <el-col v-if="apiResponse.data" :span="4" :offset="15" class="d-flex">
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
          <report />
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
import report from '@/components/task/report.vue'

import { useAPIResponseStore } from '@/stores/apiResponse'
const { apiResponse } = useAPIResponseStore();
</script>

<style scoped>
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

.d-flex{
  display: flex;
  align-items: center;
  justify-content: right;
}
</style>