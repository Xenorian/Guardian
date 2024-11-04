<template>
  <el-row :gutter="20" justify="space-between">
    <el-col :span="6">
      <div style="font-size: x-large;font-weight: 600;margin: 1%;">
        领域规则库
      </div>
    </el-col>

    <el-col :span="6" :offset="12">
      <div class="button-group">
        <el-button type="primary" @click="handleAddRule">新增规则</el-button>
        <el-button type="primary" :disabled="notAbleToCreateTask">创建任务</el-button>
      </div>
    </el-col>
  </el-row>

  <el-table :data="tableData" style="width: 100%;margin: 1%;font-size: medium"
  @selection-change="handleSelectionChange" show-header 
  :header-cell-style="{fontSize: '14px', backgroundColor: '#f8f8f8',color:'#333'}"
  v-loading="loading">
    <el-table-column type="selection" :selectable="selectable" width="55" />
    <el-table-column fixed prop="index" label="规则序号" width="150" />
    <el-table-column prop="id" label="规则ID" width="120" />
    <el-table-column prop="text" label="规则文本" />
    <!-- <el-table-column prop="city" label="City" width="120" />
    <el-table-column prop="address" label="Address" width="600" />
    <el-table-column prop="zip" label="Zip" width="120" /> -->
    <el-table-column fixed="right" label="操作" width="200">
      <template #default>
        <el-button link type="primary" size="large" @click="handleClick">
          编辑
        </el-button>
        <el-button link type="danger" size="large">删除</el-button>
      </template>
    </el-table-column>
  </el-table>


  <el-pagination
    background
    layout="total, sizes, prev, pager, next, jumper"
    :total="total"
    :page-size="pageSize"
    :current-page="currentPage"
    :page-sizes="[10, 20, 30, 50]"
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
    style="justify-content: right; /* 水平 */"
  />

  <el-dialog
    v-model="showAddRuleForm"
    title="新增规则"
    width="1000"
  >
    <AddRuleForm />    

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="showAddRuleForm = false">Cancel</el-button>
        <el-button type="primary" @click="handleSubmit">
          Confirm
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts" setup>
import {ref ,onMounted } from 'vue'
import {getFieldRule} from '@/utils/api'
import AddRuleForm from '@/components/rule/AddRuleForm.vue'
import { ElMessageBox } from 'element-plus'

const showAddRuleForm = ref(false)
const handleAddRule = () => {
  showAddRuleForm.value = true
}
const handleSubmit = async() => {
  loading.value = true
  await fetchData()
  loading.value = false
  showAddRuleForm.value = false
}

const loading = ref(true)
const tableData = ref<any[]>([]);
const fetchData = async () => {
  try {
    const response = await getFieldRule(); // 替换为实际的端点
    tableData.value = response; // 假设后端返回的数据是一个数组
  } catch (error) {
    console.error('There was an error fetching the data!', error);
  }
};

const handleClick = () => {
  console.log('click')
}

const multipleSelection = ref([])
const notAbleToCreateTask = ref(true)
const selectable = (row) => ![1, 2].includes(row.id)
const handleSelectionChange = (val) => {
  multipleSelection.value = val
  if(multipleSelection.value.length >= 1){
    notAbleToCreateTask.value = false
  }else{
    notAbleToCreateTask.value = true
  }
}

const total = tableData.length
const pageSize = ref(10)
const currentPage = ref(1)
const handleSizeChange = (newPageSize) => {
  pageSize.value = newPageSize
}
const handleCurrentChange = (newPage) => {
  currentPage.value = newPage
  // 这里可以调用你的分页请求函数
  console.log(`当前页码 ${newPage}`)
}

onMounted(async () => {
  await fetchData();
  // console.log(tableData); // 在数据获取后打印 tableData
  loading.value = false
});
</script>

<style scoped>
.button-group {
  text-align: right;
}
</style>