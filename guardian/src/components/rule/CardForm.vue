<template>
  <el-form 
    :model="form" 
    :rules="rules" 
    ref="ruleFormRef" 
    label-width="auto" 
    label-position="right" 
    size="large">

    <div style="padding: 2%; padding-right: 15%; margin-top: 2%;">
      <el-form-item label="规则领域名称" prop="name">
        <el-input v-model="form.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="规则领域描述" prop="describe">
        <el-input v-model="form.describe" autocomplete="off" type="textarea" />
      </el-form-item>
      <el-form-item label="规则领域封面" prop="cover">
        <el-input v-model="form.cover" autocomplete="off" />
      </el-form-item>
    </div>
    
    <el-form-item class="button-container">
      <el-button type="primary" @click="submitForm(ruleFormRef)">提交</el-button>
      <el-button @click="resetForm(ruleFormRef)">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { ElMessage } from 'element-plus';

const form = reactive({
  name: '',
  describe: '',
  cover: ''
});

const rules = reactive({
  name: [
    { required: true, message: '请输入规则领域名称', trigger: 'blur' }
  ],
  describe: [
    { required: true, message: '请输入规则领域描述', trigger: 'blur' }
  ],
  cover: [
    { required: true, message: '请上传规则领域封面', trigger: 'change' }
  ]
});

const ruleFormRef = ref(null);

const submitForm = (formEl) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      ElMessage.success('提交成功');
      // 这里可以添加提交表单的逻辑
    } else {
      ElMessage.error('请检查表单信息');
      return false;
    }
  });
};

const resetForm = (formEl) => {
  if (!formEl) return;
  formEl.resetFields();
};
</script>

<style scoped>
.button-container {
  display: flex;
  flex-direction: column;
  margin-right: 5%;
}
</style>