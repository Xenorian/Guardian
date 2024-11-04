<template>
  <el-form 
    style="width: 70%;margin: auto;"
    label-position="left"
    label-width="auto"
    >
    <el-form-item label="选择模态" required>
      <el-select v-model="mode" placeholder="请选择">
        <el-option label="文本" value="text"></el-option>
      </el-select>
    </el-form-item>

    <el-divider content-position="left">配置属性</el-divider>

    <el-form-item label="规则ID" required>
      <el-input v-model="ruleId" placeholder="规则ID - 自动生成" disabled></el-input>
    </el-form-item>
    <el-form-item label="规则文本" required>
      <el-col :span="20">
        <el-input v-model="ruleText" placeholder="规则文本"></el-input>
      </el-col>
      <el-col :span="3" :offset="1">
        <el-button type="primary">AI生成事件</el-button>
      </el-col>
    </el-form-item>
    <!-- <el-form-item label="test">
      <el-input v-model="test" placeholder="test"></el-input>
    </el-form-item> -->

    <el-divider content-position="left">配置事件</el-divider>
    <EventGraph />

    <!-- <el-divider content-position="left">配置时序</el-divider>
    <el-link type="primary">查看/编辑时序</el-link> -->
  </el-form>
</template>
  
<script setup>
import { ref } from 'vue';
import EventGraph from './EventGraph.vue';

const mode = ref('');
const ruleId = ref('');
const ruleText = ref('');
const test = ref('');
</script>

<style scoped>
/* Add any additional styles here */
</style>