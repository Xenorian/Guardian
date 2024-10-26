<template>
  <el-form
    ref="ruleFormRef"
    style="max-width: 600px"
    :model="ruleForm"
    label-width="auto"
    label-position="left"
    class="demo-ruleForm"
    :size="formSize"
    status-icon
  >
    <el-form-item class="formItem" label="任务名称" prop="name" required>
      <el-input v-model="ruleForm.name" />
    </el-form-item>

    <el-form-item class="formItem" label="任务描述" prop="description">
      <el-input v-model="ruleForm.description" type="textarea" />
    </el-form-item>

    <el-form-item class="formItem" label="规则设置" prop="rule" required>

      <el-select
        v-model="ruleForm.rule"
        multiple
        placeholder="please select"
      >
        <el-option
          v-for="item in modelOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="选择模型" required>
      <el-select v-model="ruleForm.model" placeholder="please select">
        <el-option label="文本监管领域模型" value="1" />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="Threshold" prop="threshold" required>
      <el-input v-model="ruleForm.threshold" />
    </el-form-item>

    <el-form-item class="formItem" label="Maximum Length" prop="maxLen" required>
      <el-input v-model="ruleForm.maxLen" />
    </el-form-item>

    <el-form-item class="formItem" label="Top P" prop="topP" required>
      <el-input v-model="ruleForm.topP" />
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { ComponentSize, FormInstance, FormRules } from 'element-plus'

const formSize = ref<ComponentSize>('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive({
  name: '',
  description: '',
  rule: '',
  model: '',
  threshold:'0.85',
  maxLen: '512',
  topP: '1.00',
})
const modelOptions = [
  {
    value: '1',
    label: '服务提供者必须告知服务消费者数据存储期限',
  },
  {
    value: '2',
    label: '服务提供者必须告知联系信息',
  },
]
</script>

<style scoped>
.formItem{
  margin-bottom: 8%
}
</style>