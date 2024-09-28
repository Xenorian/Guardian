<template>
  <el-row justify="space-between" :gutter="80">
    <el-col :span="6">
      <a-card hoverable class="applicationCard">
        <template #cover>
          <div class="image-container">
            <img src="../../assets/mainPage/medical.jpg" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text-underlay">医疗健康</div>
      </a-card>
    </el-col>

    <el-col :span="6">
      <a-card hoverable class="applicationCard">
        <template #cover>
          <div class="image-container">
            <img src="../../assets/mainPage/electricity.png" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text-underlay">电力能源</div>
      </a-card>
    </el-col>

    <el-col :span="6">
      <a-card hoverable class="applicationCard">
        <template #cover>
          <div class="image-container">
            <img src="../../assets/mainPage/device.png" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text-underlay">电力设备</div>
      </a-card>
    </el-col>

    <el-col :span="6">
      <a-card hoverable class="applicationCard">
        <template #cover>
          <div class="image-container">
            <img src="../../assets/mainPage/cityManagement.jpg" alt="Card Image" class="card-image" />
          </div>
        </template>
        
        <div class="text-underlay">城市管理</div>
      </a-card>
    </el-col>
  </el-row>
</template>

<style scoped>
.image-container {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 100%;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease-in-out;
  overflow: hidden;
}

.image-container:hover .card-image {
  transform: scale(1.15);
}
  
.text-underlay {
  color: black;
  font-size: 28px;
  font-weight: 400;
  text-align: center;
}
</style>