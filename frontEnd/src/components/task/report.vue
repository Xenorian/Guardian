<template>
  <div>
    <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">违规数量</div>
    <div class="text-1">
      <el-text class="mx-1">违规告警总数: <span class="alert-count">{{ alertCnt }}</span></el-text>
      <el-text class="mx-1">违规规则总数: <span class="alert-count">{{ alertRuleCnt }}</span></el-text>
    </div>

    <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%">违规规则</div>

    <div class="text-2">
      <div v-for="(rule, index) in alertRules" :key="index" style="width: 100%;margin-top: 1%">
        <el-text class="mx-1 dot-before"> {{ rule }} </el-text>
      </div>

      <div v-if="alertRules.length === 0" class="mx-1">无违规规则</div>
    </div>

    <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">告警记录</div>
    <div class="text">
      <el-scrollbar height="300px" style="width: 100%;">
        <div v-if="alertsContents.length === 0" class="mx-1">无告警记录</div>

        <div v-for="(alert, index) in alertsContents" :key="index" class="text">
          <el-text class="mx-1" size="large" type="info">违规内容:</el-text>
          <el-image 
            :src="alert.img" 
            alt="Alert Image" 
            style="width: 80%;margin-left: 10%;margin-right: 10%"
            :preview-src-list="srcList"
            :initial-index="index"
            />
          <el-text class="mx-1" size="large" type="info">违规条约:</el-text>
          <el-text class="mx-1">{{ alert.rule }}</el-text>
          <el-text class="mx-1" size="large" type="info">违规描述:</el-text>
          <el-text class="mx-1" type="danger">{{ alert.description }}</el-text>
        </div>
      </el-scrollbar>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineProps, ref, computed,onMounted,watch } from 'vue';

import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus';
import { uploadImageURL,getImgList,uploadVideoURL,getVideoList,BASE_URL,delThings,imgInference } from '@/utils/api'
import { useTaskFormStore } from '@/stores/taskForm';
import { useAPIResponseStore } from '@/stores/apiResponse'
const { taskForm,ruleData,formValid } = useTaskFormStore();
const { apiResponse } = useAPIResponseStore();

const loading = ref(true)
const alertCnt = ref(0)
const alertRuleCnt = ref(0)
const alertRules = ref([])
const alertsContents = ref([])

const ruleID2ruleText = ref({})

const srcList = ref([])

watch(apiResponse, () => {
  loading.value = true
  alertCnt.value = 0
  alertRuleCnt.value = 0
  alertRules.value = []
  alertsContents.value = []
  ruleID2ruleText.value = {}

  for(let i=0;i<ruleData.value.length;i++){
    ruleID2ruleText[ruleData.value[i].id] = ruleData.value[i].text
  }

  if(apiResponse.data !== undefined){
    for (let i = 0; i < apiResponse.data.data.length; i++) {
      if( apiResponse.data.data[i].result !== 'NO'){
        continue
      }

      alertCnt.value += 1
      alertRuleCnt.value = 1
      alertRules.value = [ruleID2ruleText[taskForm.rule]]
      const content = {
        'img': 'data:image/png;base64,' + apiResponse.data.data[i].photo_base64,
        'description': apiResponse.data.data[i].description,
        'rule': ruleID2ruleText[taskForm.rule]
      }
      alertsContents.value.push(content)
      srcList.value.push('data:image/png;base64,' + apiResponse.data.data[i].photo_base64)
    }
  }

  loading.value = false
}, { deep: true });
</script>


<style scoped>
.text-1 {
  border: 1px solid #dddcdc; /* 添加细线边框 */
  border-radius: 8px;
  display: flex;
  align-items: flex-start; /* 垂直居中 */
  justify-content: flex-start; /* 水平居中 */
  flex-direction: column;
  margin-bottom: 3%;
}

.text-2 {
  border: 1px solid #dddcdc; /* 添加细线边框 */
  border-radius: 8px;
  display: flex;
  align-items: flex-start; /* 垂直居中 */
  justify-content: flex-start; /* 水平居中 */
  flex-direction: column;
  margin-bottom: 3%;

  min-height: 100px;
}

.text {
  border: 1px solid #dddcdc; /* 添加细线边框 */
  border-radius: 8px;
  display: flex;
  align-items: flex-start; /* 垂直居中 */
  justify-content: flex-start; /* 水平居中 */
  flex-direction: column;
  margin-bottom: 3%;

  min-height: 200px;
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