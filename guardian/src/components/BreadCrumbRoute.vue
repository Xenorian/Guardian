<template>
  <a-breadcrumb separator="/">
    <a-breadcrumb-item v-for="(route, index) in breadcrumbRoutes" :key="index">
      <router-link v-if="index !== breadcrumbRoutes.length - 1" :to="route.path">
        {{ route.breadcrumbName }}
      </router-link>
      <span v-else>
        {{ route.breadcrumbName }}
      </span>
    </a-breadcrumb-item>
  </a-breadcrumb>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// 获取当前路径的面包屑项
const breadcrumbRoutes = computed(() => {
  const matched = route.matched.filter(record => record.meta && record.meta.breadcrumbName)
  return matched.map((record) => ({
    path: record.path,
    breadcrumbName: record.meta.breadcrumbName,
  }))
})

</script>