<template>
  <div class="common-layout">
    <el-container>
      <el-header style="background-color: #01174B;min-height: 5vh;">
        <el-row :gutter="10" style="height: 100%;padding-right: 1%;padding-left: 1%;">
          <el-col :span="3" style="height: 100%;">

            <div class="headLogo" @click="goToHome" style="font-weight: 100;letter-spacing: 1.5px;">
              <img src="../assets/apertureWhite.png" style="height: 50%;margin-right: 5%;margin-left: 5%;">
              门神智能监管平台
            </div>

          </el-col>

          <el-col :span="1" :offset="1" @click="goToRule" class="headItem">
            监管规则
          </el-col>

          <el-col :span="1" :offset="1" @click="goToModel" class="headItem">
            监管模型
          </el-col>

          <el-col :span="1" :offset="1" @click="goToTask" class="headItem">
            监管任务
          </el-col>

          <el-col :span="2" :offset="13" class="headUserLogo">
            <el-dropdown>
              <span class="el-dropdown-link">
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
          </el-col>
        </el-row>
      </el-header>

      <div style="height: 95vh;">
        <RouterView />
      </div>

    </el-container>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import avatar from '../assets/mainPage/avatar.png'
import { RouterView } from 'vue-router'

const router = useRouter();

function goToLogin(){
  router.push({ path: '/login' })
}

function goToHome(){
  router.push({ path: '/home/intro' })
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
.headLogo {
  cursor: pointer;
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: left; /* 水平居中 */
  height: 100%; /* 根据你的需求调整高度 */
  color: white;
  font-size: medium;
}

.headItem {
  cursor: pointer;
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  height: 100%; /* 根据你的需求调整高度 */
  color: rgb(220, 220, 220);
  font-size: medium;

  background-color: transparent; /* 初始背景颜色 */
  transition: background-color 0.3s ease, color 0.3s ease; /* 平滑过渡效果 */
}

.headItem:hover {
  background-color: #1890FF; /* 悬停时的背景颜色 */
  color: white; /* 悬停时的文字颜色 */
}

.headUserLogo{
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: right; /* 水平居中 */
  height: 100%; /* 根据你的需求调整高度 */
  color: white;
  font-size: medium;
}

.el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
  outline: none;
}
</style>