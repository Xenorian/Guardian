<script setup lang="ts">
import MainPart from '../components/login/MainPart.vue'
</script>

<template>
  <div class="container">
    <MainPart class="MainPart" />
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  height: 100vh; /* 容器高度为视口高度 */
}

.MainPart {
  border-radius: 15px;
  box-shadow: 0px 10px 20px 0px rgba(0, 0, 0, 0.2);
  max-width: 40%;
  width: 100%; /* 确保内容宽度不超过 max-width */
  background-color: white; /* 可选：设置背景颜色 */
}
</style>