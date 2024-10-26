<template>
  <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
    
    <div class="main">
      <el-row :gutter="20"> <!-- gutter 是列间距，可以根据需要调整 -->
        <el-col :span="5">
          <div class="grid-content bg-purple" style="margin-right: 10%;">
            <Form />
          </div>
        </el-col>
        <el-col :span="11">
          <div class="grid-content bg-purple-light">
            <div class="midHead" style="margin-bottom: 3%;margin-right: 5%;">
              <el-row :gutter="20">
                <el-col :span="5">
                  <div style="font-size: 25px;font-weight: 800;">任务运行</div>
                </el-col>
                <el-col :span="4" :offset="15" class="d-flex">
                  <el-text type="success">任务完成</el-text>
                  <CheckCircleTwoTone twoToneColor="#52c41a" style="margin-left: 3%;margin-top: 2%"/>
                </el-col>
              </el-row>
            </div>

            <div class="mid">
              <el-input
                v-model="textarea"
                style="width: 100%;margin-right: 3%;"
                autosize
                type="textarea"
                placeholder="Please input"
              />
            </div>

            <div class="button-group">
              <el-button>监管数据上传</el-button>
              <el-button type="primary">开始运行</el-button>
            </div>

          </div>
        </el-col>
        <el-col :span="8">
          <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">违规数量</div>
          <div class="text">
            <el-text class="mx-1">违规告警总数:<span class="alert-count">2</span></el-text>
            <el-text class="mx-1">违规规则数:&emsp;<span class="alert-count">2</span></el-text>
          </div>
          
          <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">违规规则</div>
          <div class="text">
            <el-text class="mx-1 dot-before">服务提供者必须告知服务消费者数据存储期限            </el-text>
            <el-text class="mx-1 dot-before">服务提供者必须告知联系信息</el-text>
          </div>

          <div style="font-size: 20px;font-weight: 800;margin-bottom: 3%;">告警记录</div>
          <el-scrollbar height="300px">
            <div class="text">
              <el-text class="mx-1" size="large" type="info">违规内容:</el-text>
              <el-text class="mx-1" type="danger">users shall grant Studios the permanent,irrevocable,non-exclusive right to use the content and contributions posted by the users.            </el-text>
              <el-text class="mx-1" size="large" type="info">违规条约:</el-text>
              <el-text class="mx-1">服务提供者必须告知服务消费者数据存储期限            </el-text>
            </div>

            <div class="text">
              <el-text class="mx-1" size="large" type="info">违规内容:</el-text>
              <el-text class="mx-1" type="danger">users shall grant Studios the permanent,irrevocable,non-exclusive right to use the content and contributions posted by the users.            </el-text>
              <el-text class="mx-1" size="large" type="info">违规条约:</el-text>
              <el-text class="mx-1">服务提供者必须告知联系信息            </el-text>
            </div>
          </el-scrollbar>
          
        </el-col>
      </el-row>
    </div>
    
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';
import {
  CheckCircleTwoTone
} from '@ant-design/icons-vue';
import Form from '../../../components/task/form.vue'

const textarea = ref(`At Studios, we value the contributions of our users and understand that they are the lifeblood of our community. We recognize that users generate a significant amount of content, which includes posts, comments, and other entries. It is essential to note that users are solely responsible for the content they post and the information they share within our platform.
By participating in our community, users agree to hold Studios harmless from any legitimate claims that may arise from third parties due to a user's culpable violation of their obligations. This means that users must ensure that their contributions do not infringe upon the rights of others, including copyright, trademark, or privacy rights.
While Studios does not claim ownership of the content entered by users, we do require certain rights to use and manage this content. Users grant Studios a permanent, irrevocable, non-exclusive right to use, reproduce, modify, adapt, publish, translate, create derivative works from, distribute, and display the content and contributions posted by users on our platform.
This license allows Studios to maintain and improve the platform, ensure the integrity of the community, and provide a consistent and engaging experience for all users. It also enables us to promote and market our services, which may include showcasing user-generated content as part of our promotional efforts.
Users take full responsibility for the content and entries they post. Users agree to release Studios from any legitimate claims from third parties arising from a culpable violation of the users'obligations.Studios explicitly does not claim content entered by users as its own. However, users shall grant Studios the permanent,irrevocable,non-exclusive right to use the content and contributions posted by the users.
We take the security of user data seriously and implement appropriate technical and organizational measures to protect against unauthorized access, disclosure, alteration, or destruction of personal data. While no system can guarantee complete security, we continually strive to enhance our security measures to protect your information.
Our privacy policy may change from time to time to reflect updates in our services or changes in the law. We will notify users of any material changes to this policy by posting the updated policy on our platform and, where appropriate, by sending a notification to the email address associated with your account.
`)

</script>

<style scoped>
.text {
  border: 1px solid #dddcdc; /* 添加细线边框 */
  border-radius: 8px;
  display: flex;
  align-items: flex-start; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  flex-direction: column;
  margin-bottom: 3%;
}

.boardered{
  border: 1px solid #dddcdc; /* 添加细线边框 */
  border-radius: 8px;
}

.mx-1{
  margin: 2%;
  margin-left: 5%;
  align-self: start;
}

.dot-before::before {
  content: '•'; /* 插入一个圆点 */
  margin-right: 10px; /* 控制圆点和文本之间的间隔 */
  color: #333; /* 圆点的颜色 */
}

.alert-count {
  margin-left: 50px; /* 调整这个值以控制间隔大小 */
}

.alert{
  margin-bottom: 1%
}

.mid{
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: left; /* 水平居中 */
  height: 100%; /* 根据你的需求调整高度 */
  color: black;
  font-size: medium;
}

.right{
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  color: white;
  font-size: medium;
}

.card{
  margin-right: 3%;
  margin-left: 3%;
}

.button-group {
  margin: 3%;
  text-align: right;
}

.d-flex{
  display: flex;
  align-items: center;
  justify-content: right;
}
</style>