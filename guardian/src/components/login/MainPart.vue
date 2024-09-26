<template>
  <el-row class="content">
    <!--el-col 列： -->
    <el-col :span="10" :xs="0" class="content-left">
      <img src="/src/assets/LeftBanner.jpg" alt="Left Banner" style="width: 100%; height: 100%;">
    </el-col>
    <el-col :span="14" :xs="24" class="content-right" style="text-align:center;">
      <div class="loginContent" style="margin-left: 20%;margin-right: 20%;">
        <div class="loginContentTop" style="margin-top: 30%;">
          <div class="header">
            <div class="fontSize">登录</div>
          </div>
          <!-- <span class="introduce">全球最大的代码托管平台</span> -->
        </div>

        <div class="loginContentForm" style="margin-top: 10%;">
          <div class="loginMethods">
            <el-tabs>
              <el-tab-pane
                label="账号密码登录"
                class="toLogin"
              >
                <!-- loginForm: 表单数据对象-->
                <el-form :model="loginForm">
                  <el-form-item label="" prop="username">
                    <el-input
                      placeholder="用户名"
                      v-model="loginForm.username"
                      inline-message
                      size="large"
                      :prefix-icon="User"
                    ></el-input>
                  </el-form-item>
                  <el-form-item label="" prop="password">
                    <el-input
                      placeholder="密码"
                      show-password
                      v-model="loginForm.password"
                      inline-message
                      size="large"
                      :prefix-icon="Lock"
                    ></el-input>
                  </el-form-item>
                </el-form>

              </el-tab-pane>
            </el-tabs>
          </div>
        </div>

        <div class="loginContentButton">
          <div class="buttonTop" style="margin-top: 5%;margin-bottom: 5%">
            <el-link type="primary" :underline="false">
              <span style="font-size: 16px">忘记密码</span>
            </el-link>
          </div>

          <el-button type="primary" size="large" class="loginButton" @click="login" style="width: 40%;"> 登录 </el-button>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router';

const router = useRouter();

const loginForm = ref({
  username: '',
  password: ''
})

function login() {
  alert('OK')
}
</script>

<style scoped>
.loginContent{
  margin-left: 20%;
}

.fontSize{
  font-size: xx-large;
}
</style>