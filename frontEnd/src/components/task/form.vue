<template>
  <el-form
    ref="ruleFormRef"
    style="max-width: 600px"
    :model="taskForm"
    label-width="auto"
    label-position="left"
    class="demo-ruleForm"
    :size="formSize"
    status-icon
    v-loading="loading"
  >
    <el-form-item class="formItem" label="任务名称" prop="name" required>
      <el-input v-model="taskForm.name" />
    </el-form-item>

    <el-form-item class="formItem" label="任务描述" prop="description">
      <el-input v-model="taskForm.description" type="textarea" />
    </el-form-item>

    <el-form-item class="formItem" label="规则设置" prop="rule" required>

      <el-select
        v-model="taskForm.rule"
        placeholder="please select"
      >
        <el-option
          v-for="item in modelOptions"
          :key="item.id"
          :label="item.label"
          :value="item.id"
        />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="选择模型" prop="model" required>
      <el-select v-model="taskForm.model" placeholder="please select">
        <el-option label="监管领域模型" value="1" />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="Threshold" prop="threshold" required>
      <el-input v-model="taskForm.threshold" />
    </el-form-item>

    <el-form-item class="formItem" label="Maximum Length" prop="maxLen" required>
      <el-input v-model="taskForm.maxLen" />
    </el-form-item>

    <el-form-item class="formItem" label="Top P" prop="topP" required>
      <el-input v-model="taskForm.topP" />
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref,onMounted,watch } from 'vue'
import type { ComponentSize, FormInstance, FormRules } from 'element-plus'

import {getFieldRule} from '@/utils/api'
import { useTaskFormStore } from '@/stores/taskForm';
const { taskForm,ruleData, clearTaskForm,setFormValid } = useTaskFormStore();

const formSize = ref<ComponentSize>('default')
const ruleFormRef = ref<FormInstance>()


const loading = ref(true)

const fetchData = async () => {
  try {
    const response = await getFieldRule(); // 替换为实际的端点
    ruleData.value = response; // 假设后端返回的数据是一个数组
  } catch (error) {
    console.error('There was an error fetching the data!', error);
  }
};

const modelOptions = ref<any[]>([]);

onMounted(async () => {
  clearTaskForm()

  await fetchData();
  // console.log(tableData); // 在数据获取后打印 tableData
  loading.value = false
  modelOptions.value = []
  for(const item of ruleData.value){
    modelOptions.value.push({id: item['id'],label: item['text']})
  }
  // console.log(modelOptions.value)
});

// 监控表单数据变化
watch(taskForm, () => {
  if (ruleFormRef.value) {
    ruleFormRef.value.validate((valid) => {
      // formValid.value = valid;
      // 在这里可以添加更多的操作
      setFormValid(valid)
    });
  }
}, { deep: true });
</script>

<style scoped>
.formItem{
  margin-bottom: 8%
}
</style>