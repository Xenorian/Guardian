<template>
  <a-layout class="layout">
    <a-layout-content style="padding: 0px 50px;">

      <a-breadcrumb :routes="routes" style="padding-top: 1%;padding-bottom: 1%;">
        <template #itemRender="{ route, routes, paths }">
          <span v-if="routes.indexOf(route) === routes.length - 1">
            {{ route.breadcrumbName }}
          </span>
          <router-link v-else :to="`${basePath}/${paths.join('/')}`">
            {{ route.breadcrumbName }}
          </router-link>
        </template>
      </a-breadcrumb>
      
      <RouterView />
    </a-layout-content>

  </a-layout>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';
import { HomeOutlined } from '@ant-design/icons-vue';
import { useRouter, RouterView } from 'vue-router'

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

<style>
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
</style>