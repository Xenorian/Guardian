import { reactive, computed,ref } from 'vue'
import { defineStore } from 'pinia'

export const useAPIResponseStore = defineStore('apiResponse', () => {
  // 使用 reactive 定义状态对象，便于其字段都可以是可响应的
  const apiResponse = reactive({});

  return { apiResponse };
});
