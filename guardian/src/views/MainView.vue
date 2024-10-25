<template>
  <a-layout class="layout" style="height: 100vh;">
    <a-layout-header style="padding-left: 1%;">
      <div class="logo" @click="goToHome" style="font-weight: 100;letter-spacing: 1.5px;width: 20%;">
        <img src="../assets/apertureWhite.png" style="height: 50%;margin-right: 5%;margin-left: 5%;">
        数字服务智能监管支撑工具
      </div>

      <a-menu
        theme="dark"
        mode="horizontal"
        v-model:selectedKeys="selectedKeys"
        style="width: 50%;"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1" @click="goToRule">监管规则</a-menu-item>
        <a-menu-item key="2" @click="goToModel">监管模型</a-menu-item>
        <a-menu-item key="3" @click="goToTask">监管任务</a-menu-item>
      </a-menu>

      <el-dropdown class="headUserLogo">
        <span class="el-dropdown-link" style="outline: none;">
          <el-avatar
            :src="avatar"
          />
        </span>

        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="goToLogin">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </a-layout-header>

    <a-layout-content style="padding: 0 0">


    <el-scrollbar class="scrollbar">
      <div class="content">
        <RouterView />
      </div>
    </el-scrollbar>

    </a-layout-content>


    <!-- <a-layout-footer style="text-align: center">
      Guardian ©2024
    </a-layout-footer> -->
  </a-layout>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';
import avatar from '../assets/mainPage/avatar.png'
import { useRouter, RouterView } from 'vue-router'

const selectedKeys = ref<string[]>(['0'])
const router = useRouter();

router.beforeEach((to, from, next) => {
  if (to.path.includes('/home/intro')) {
    selectedKeys.value = ['0']
  }else if (to.path.includes('/home/rule')){
    selectedKeys.value = ['1']
  }else if (to.path.includes('/home/model')){
    selectedKeys.value = ['2']
  }else if (to.path.includes('/home/task')){
    selectedKeys.value = ['3']
  }

  next();
});

function goToLogin(){
  router.push({ path: '/login' })
}

function goToHome(){
  router.push({ path: '/home/intro' })
  selectedKeys.value = ['0']
}

function goToRule(){
  router.push({ path: '/home/rule' })
}

function goToModel(){
  router.push({ path: '/home/model' })
}

function goToTask(){
  router.push({ path: '/home/task' })
}

</script>

<style scoped>

.logo {
  float: left;
  display: flex;
  width: 12%;
  height: 100%;
  cursor: pointer;
  flex-wrap: nowrap;

  align-items: center; /* 垂直居中 */
  justify-content: left; /* 水平居中 */

  color: white;
  font-size: medium;
}

.logo img {
  height: 100%;
}

.ant-row-rtl #components-layout-demo-top .logo {
  float: right;
  margin: 16px 0 16px 24px;
}

.headUserLogo{
  cursor: pointer;
  color: var(--el-color-primary);

  align-items: center;
  outline: none;
  
  position: relative;
  left: 98%;
  top: -80%;
}
</style>