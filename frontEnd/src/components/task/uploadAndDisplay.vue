<template>
  
  <el-tabs v-model="activeName" class="tabs" style="width: 100%; margin-bottom: 10%" v-loading="loading">
    <el-tab-pane label="视频样本" name="Video">
      <el-carousel v-if="videos && videos.length > 0"
          trigger="click" 
          style="width: 100%;height: 40%;"
          indicator-position="outside"
          arrow="always"
          type="card"
          :autoplay=false
          :cardScale=0.5
          :loop=false
          :initial-index="0"
          :limit="1"
        >
        <el-carousel-item v-for="(src, index) in videos" :key="index">
          <video 
            controls
            style="height: 100%;max-width: 100%;"
            :src="src"
          />
        </el-carousel-item>
      </el-carousel>

      <div v-else class="placeholder" style="text-align: center;">
        暂无样本，请上传
      </div>
    </el-tab-pane>

    <el-tab-pane label="图片样本" name="Image">
      <div class="upload-img">
        <el-carousel v-if="images && images.length > 0"
          trigger="click" 
          style="width: 100%;height: 20%;"
          indicator-position="outside"
          arrow="always"
          type="card"
          :autoplay=false
          :cardScale=0.5
          :loop=false
          @change="handleImageChange" 
          :initial-index="0"
        >
          <el-carousel-item v-for="(src, index) in images" :key="index">
            <img :src="src" :alt="'Image ' + (index + 1)" class="carousel-image"/>
          </el-carousel-item>
        </el-carousel>

        <div v-else class="placeholder" style="text-align: center;">
          暂无样本，请上传
        </div>
      </div>

    </el-tab-pane>
  </el-tabs>

  <div v-if="activeName === 'Image'" class="button-group">
    <el-upload
      :action="uploadImageURL"
      :before-upload="beforeImgUpload"
      :on-success="handleSuccess"
      :on-error="handleError"
      ref="upload"
      style="margin-right: 10px;"
      :show-file-list=false
    >
      <el-button type="default">上传图片样本</el-button>
    </el-upload>

    <el-button type="danger" @click="delSomething" :disabled="images.length==0">删除该图片样本</el-button>
    <el-button type="primary" @click="_imgInference" :disabled="images.length==0 || !formValid.value">开始运行</el-button>
  </div>

  <div v-if="activeName === 'Video'" class="button-group">
    <el-upload
      :action="uploadVideoURL"
      :before-upload="beforeVideoUpload"
      :on-success="handleSuccess"
      :on-error="handleError"
      ref="upload"
      style="margin-right: 10px;"
      :show-file-list=false
    >
      <el-button type="default" :disabled="videos.length>=1">上传视频样本</el-button>
    </el-upload>

    <el-button type="danger" @click="delSomething" :disabled="videos.length==0">删除该视频样本</el-button>
    <el-button type="primary" @click="_videoInference" :disabled="videos.length!=1 || !formValid.value">开始运行</el-button>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed,onMounted } from 'vue';

import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus';
import { uploadImageURL,getImgList,uploadVideoURL,getVideoList,BASE_URL,delThings,imgInference,videoInference } from '@/utils/api'
import { useTaskFormStore } from '@/stores/taskForm';
import { useAPIResponseStore } from '@/stores/apiResponse'
const { taskForm,formValid } = useTaskFormStore();
const { apiResponse } = useAPIResponseStore();

const loading = ref(true)

const activeName = ref('Image')
const images = ref([])
const videos = ref([])

const fetchImgList = async () => {
  try {
    const response = await getImgList(); // 替换为实际的端点
    const array = []
    for (let i = 0; i < response.length; i++) {
      array.push(BASE_URL + response[i]);
    }
    images.value = array.reverse()
    // console.log(images.value)
  } catch (error) {
    console.error('There was an error fetching the data!', error);
  }
};
const fetchVideoList = async () => {
  try {
    const response = await getVideoList(); // 替换为实际的端点
    const array = []
    for (let i = 0; i < response.length; i++) {
      array.push(BASE_URL + response[i]);
    }
    videos.value = array.reverse()
    // console.log(images.value)
  } catch (error) {
    console.error('There was an error fetching the data!', error);
  }
};

const result = ref({})
const delSomething = async() => {
  if(activeName.value == 'Image'){
    result.value = await delThings(images.value[currentImageIndex.value])
  }else{
    result.value = await delThings(videos.value[currentVideoIndex.value])
  }

  // console.log(result)
  if(result.value.status == 'success'){
    ElMessage.success('删除成功')
  }else{
    ElMessage.error(`删除失败: ${result.value.message}`);
  }

  loading.value = true
  await fetchImgList()
  await fetchVideoList()
  loading.value = false
}

const _imgInference = async() => {
  try {
    loading.value = true
    
    if(apiResponse.data){
      delete apiResponse.data
    }

    const response = await imgInference(taskForm.rule); // 替换为实际的端点
    apiResponse.data = JSON.parse(response.data)
    loading.value = false
  } catch (error) {
    console.error('There was an error when generate inference response', error);
    loading.value = false
  }
}

const _videoInference = async() => {
  try {
    loading.value = true
    
    if(apiResponse.data){
      delete apiResponse.data
    }

    const response = await videoInference(taskForm.rule,videos.value[0]); // 替换为实际的端点
    apiResponse.data = JSON.parse(response.data)
    loading.value = false
  } catch (error) {
    console.error('There was an error when generate inference response', error);
    loading.value = false
  }
}

const currentImageIndex = ref(0)
const currentVideoIndex = ref(0)
// 处理轮播变化的函数
const handleImageChange = (newIndex) => {
  currentImageIndex.value = newIndex
}
const handleVideoChange = (newIndex) => {
  currentVideoIndex.value = newIndex
}

// 处理上传成功
const handleSuccess = async(response, file) => {
  // console.log('Upload success:', response, file);
  ElMessage.success('上传成功')
  loading.value = true
  await fetchImgList()
  await fetchVideoList()
  loading.value = false
};

// 处理上传错误
const handleError = (err, file) => {
  console.error('Upload error:', err, file);
  ElMessage.error(`上传失败: ${err.message}`);
};

// 上传前检查
const beforeImgUpload = (file) => {
  const isJPGorPNG = file.type === 'image/jpeg' || file.type === 'image/png';
  const isLt5M = file.size / 1024 / 1024 < 5;

  if (!isJPGorPNG) {
    ElMessage.error('只能上传 JPG 或 PNG 文件!');
  }
  if (!isLt5M) {
    ElMessage.error('文件大小不能超过 5MB!');
  }else{
    loading.value = true
  }

  return isJPGorPNG && isLt5M;
};

// 视频

// 上传前检查
const beforeVideoUpload = (file) => {
  const isVideoType =
    file.type === 'video/mp4' || file.type === 'video/avi' || file.type === 'video/mov';
  const isLt50M = file.size / 1024 / 1024 < 100;

  if (!isVideoType) {
    ElMessage.error('只能上传 mp4、avi 或 mov 格式的视频!');
  }
  if (!isLt50M) {
    ElMessage.error('视频大小不能超过 100MB!');
  }else{
    loading.value = true
  }

  return isVideoType && isLt50M;
};

onMounted(async () => {
  await fetchImgList()
  await fetchVideoList()
  loading.value = false
});
</script>

<style scoped>
.upload-img{
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  flex-direction: column;
}

.carousel-image {
  width: auto;
  height: 90%;
  opacity: 0.5; /* 设置非选中图片的不透明度 */
  transition: opacity 0.3s;
  margin-left: 20%;
}

.el-carousel__item.is-active .carousel-image {
  opacity: 1; /* 设置选中图片的不透明度 */
}

.button-group {
  display: flex;     /* 使用 Flexbox 布局 */
  justify-content: flex-end;  /* 将按钮组整体右对齐 */
  align-items: center; /* 在垂直方向上居中对齐 */
}

:deep(.el-upload-list){
  margin: 0;
}
</style>