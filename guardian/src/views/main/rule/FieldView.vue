<template>
  <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
    <a-alert class="alert" description="支持???领域规则的可视化构建、编辑、查看、及管理" type="success" />

    <FieldRuleInfo />
    
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';

import FieldRuleInfo from '../../../components/rule/FieldRuleInfo.vue'
</script>

<style scoped>
.alert{
  margin-bottom: 1%
}
</style>