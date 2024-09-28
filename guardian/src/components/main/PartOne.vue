<template>
  <div class="text-overlay">
    <div style="margin-top: 8vh;margin-bottom: 8vh;font-size: 45px;font-weight: 600;">应用领域</div>
  </div>

  <AppField style="width: 65%;"/>

  <div class="text-overlay">
    <div style="margin-top: 8vh;margin-bottom: 8vh;font-size: 45px;font-weight: 600;">核心技术</div>
  </div>

  <CoreTech style="width: 65%;"/>

  <div class="text-overlay">
    <div style="margin-top: 10vh;margin-bottom: 10vh;font-size: 45px;font-weight: 600;">技术优势</div>
  </div>

  <TechAdv style="width: 65%;"/>

  <div class="text-overlay">
    <div style="margin-top: 10vh;margin-bottom: 10vh;font-size: 45px;font-weight: 600;">平台功能</div>
  </div>

  <CoreFunc style="width: 65%;margin-bottom: 10%;" />

</template>
  
<script setup lang="ts">
  import AppField from './AppField.vue'
  import CoreTech from './CoreTech.vue'
  import TechAdv from './TechAdv.vue'
  import CoreFunc from './CoreFunc.vue';
</script>