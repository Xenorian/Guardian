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
    <el-form-item class="formItem" label="监管模型领域" prop="field" required>
      <el-select v-model="ruleForm.field" placeholder="please select">
        <el-option label="欺诈检测" value="1" />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="对齐策略" prop="align" required>
      <el-select v-model="ruleForm.align" placeholder="please select">
        <el-option label="异构监管模型对齐与聚合" value="1" />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="测试数据集" prop="testDataset" required>
      <el-select v-model="ruleForm.testDataset" placeholder="please select">
        <el-option label="Yelp评论数据集" value="1" />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="监管模型选择" required>
      <el-select
        v-model="ruleForm.model"
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

    <el-form-item class="formItem" label="优化器" prop="optimizer" required>
      <el-select v-model="ruleForm.optimizer" placeholder="please select">
        <el-option label="Adam" value="1" />
      </el-select>
    </el-form-item>

    <el-form-item class="formItem" label="学习率" prop="lr" required>
      <el-input v-model="ruleForm.lr" />
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { ComponentSize, FormInstance, FormRules } from 'element-plus'

interface RuleForm {
  field: string
  align: string
  testDataset: string
  optimizer: string
  model:string
  lr: string
}

const formSize = ref<ComponentSize>('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  field: '',
  align: '',
  testDataset: '',
  optimizer: '',
  lr: '0.001',
  model: '',
})

const locationOptions = ['Home', 'Company', 'School']

const modelSelected = ref([])
const modelOptions = [
  {
    value: 'HOGRL',
    label: 'HOGRL',
  },
  {
    value: 'GTAN',
    label: 'GTAN',
  },
  {
    value: 'RGTAN',
    label: 'RGTAN',
  }
]
</script>

<style scoped>
.formItem{
  margin-bottom: 8%
}
</style>