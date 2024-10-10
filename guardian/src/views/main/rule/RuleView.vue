<template>
  <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
    <a-alert class="alert" message="欢迎使用门神智能监管平台" description="建立面向复杂服务监管的新型定义语言，多模态规范数据融合、违规事件智能识别技术，打造智能高效的服务监管体系。" type="info" />

    <div style="font-size: x-large;font-weight: 600;margin: 1%;margin-left: 0">
      规则领域
    </div>

    <div class="cards">
      <p v-for="item in 20" :key="item" class="cards-item"> <FieldCard /> </p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';
import { HomeOutlined } from '@ant-design/icons-vue';
import { useRouter, RouterView } from 'vue-router'
import FieldCard from '../../../components/rule/FieldCard.vue'

interface Route {
  path: string;
  breadcrumbName: string;
  children?: Array<{
    path: string;
    breadcrumbName: string;
  }>;
}

const basePath = ''
const routes = ref<Route[]>([
  {
    path: 'home',
    breadcrumbName: 'Home',
  },
  {
    path: 'rule',
    breadcrumbName: '监管规则',
  },
])


</script>

<style scoped>
.alert :deep(.ant-alert-message){
  font-weight: bold;
  font-size: 22px;
}

.alert :deep(.ant-alert-description){
  font-weight: 400;
  font-size: 18px;
}

.site-layout-content {
  min-height: 280px;
  padding: 24px;
  background: #fff;
}
#components-layout-demo-top .logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(255, 255, 255, 0.3);
}
.ant-row-rtl #components-layout-demo-top .logo {
  float: right;
  margin: 16px 0 16px 24px;
}

[data-theme='dark'] .site-layout-content {
  background: #141414;
}

.cards{
  display: flex;
  flex-wrap: wrap;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  color: white;
  font-size: medium;
}

.cards-item{
  margin: 1%
}
</style>