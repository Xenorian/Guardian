import { reactive, computed,ref } from 'vue'
import { defineStore } from 'pinia'

export const useTaskFormStore = defineStore('taskForm', () => {
  // 使用 reactive 定义状态对象，便于其字段都可以是可响应的
  const taskForm = reactive({
    name: '',
    description: '',
    rule: '',
    model: '',
    threshold: '0.85',
    maxLen: '512',
    topP: '1.0'
  });

  const formValid = reactive({
    val: false
  })

  // 动作：清空 taskForm 的所有字段
  function clearTaskForm() {
    taskForm.name = '';
    taskForm.description = '';
    taskForm.rule = '';
    taskForm.model = '';
    // taskForm.threshold = '';
    // taskForm.maxLen = '';
    // taskForm.topP = '';
    formValid.val=false;
  }

  // 动作：设置 taskForm 的字段，保证每个参数都是可选的
  function setTaskForm(data = {}) {
    Object.keys(data).forEach(key => {
      if (key in taskForm) {
        taskForm[key] = data[key];
      }
    });
  }

  function setFormValid(valid : boolean){
    formValid.val = valid
  }

  return { taskForm,formValid, clearTaskForm, setTaskForm,setFormValid };
});
