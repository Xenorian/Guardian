<template>
  <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
    <a-alert class="alert" description="支持看守所领域规则的可视化构建、编辑、查看、及管理" type="success" />

    <el-tabs v-model="activeName" class="demo-tabs">
      <el-tab-pane label="规则库" name="Rule">
        <FieldRuleInfo />
      </el-tab-pane>

      <el-tab-pane label="术语库" name="Term">
        <FieldTermInfo />
      </el-tab-pane>
    </el-tabs>
    
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';

import FieldRuleInfo from '../../../components/rule/FieldRuleInfo.vue'
import FieldTermInfo from '../../../components/rule/FieldTermInfo.vue'

const activeName = ref('Rule')

</script>

<style scoped>
.alert{
  margin-bottom: 1%
}
</style>