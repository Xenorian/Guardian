<template>
  <div class="common-layout">
    <el-container>
      <el-header style="background-color: #01174B">
        <el-row :gutter="10" style="height: 100%;padding-right: 1%;padding-left: 1%;">
          <el-col :span="2" style="height: 100%;">

            <div class="headLogo" @click="goToHome" style="font-weight: 100;letter-spacing: 1.5px;">
              <img src="../assets/apertureWhite.png" style="height: 50%;margin-right: 5%;margin-left: 5%;">
              门神智能监管平台
            </div>

          </el-col>

          <el-col :span="1" :offset="1" @click="goToRule" class="headLogo">
            监管规则
          </el-col>

          <el-col :span="1" :offset="1" @click="gotToModel" class="headLogo">
            监管模型
          </el-col>

          <el-col :span="1" :offset="1" @click="gotToTask" class="headLogo">
            监管任务
          </el-col>

          <el-col :span="2" :offset="14" class="headUserLogo">
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

      <el-scrollbar height="95vh">
        <div style="width: 100%;">
          <el-main style="padding: 0;">
            <div class="banner">
              <div class="text-overlay">
                <div style="margin-top: 3%;margin-bottom: 1%;font-size: 58px;font-weight: 800;">浙江大学门神智能监管平台</div>
                <div style="margin-bottom: 3%;font-size: 28px;font-weight: 200;">
                  建立面向复杂服务监管的新型定义语言，多模态规范数据融合、<br>
                  违规事件智能识别技术，打造智能高效的服务监管体系。
                </div>

                <el-button @click="goToRule" type="primary" size="large" style="margin-bottom: 3%;width: 7%;">开始使用</el-button>
              </div>
            </div>

            <div class="content">
              <PartOne />
            </div>
          </el-main>
        </div>
      </el-scrollbar>

    </el-container>
  </div>
</template>

<script setup lang="ts">
import PartOne from '../components/main/PartOne.vue'
import { useRouter } from 'vue-router';
import avatar from '../assets/mainPage/avatar.png'

const router = useRouter();

function goToLogin(){
  router.push({ path: '/login' })
}

function goToHome(){
  router.push({ path: '/home' })
}

function goToRule(){
  router.push({ path: '/rule' })
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

.banner{
  object-fit: cover;
  height: 40%;
  width: 100%;

  background-image: url('../assets/headBanner.png');
  background-size: cover; /* 使背景图像覆盖整个容器 */
  background-position: center; /* 使背景图像居中 */
  background-repeat: no-repeat; /* 不重复背景图像 */
  display: flex;
  justify-content: left;
  align-items: center;
}

.text-overlay {
  color: white;
  text-align: left;
  width: 100%;

  padding: 10px;
  border-radius: 5px;
  margin-left: 10%
}

.content{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center; /* 垂直居中 */
  justify-content: left; /* 水平居中 */
  height: 100%; /* 根据你的需求调整高度 */
}
</style>