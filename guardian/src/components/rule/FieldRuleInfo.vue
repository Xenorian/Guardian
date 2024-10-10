<template>
  <el-row :gutter="20" justify="space-between">
    <el-col :span="6">
      <div style="font-size: x-large;font-weight: 600;margin: 1%;">
        领域规则库
      </div>
    </el-col>

    <el-col :span="6" :offset="12">
      <div class="button-group">
        <el-button type="primary">新增规则</el-button>
        <el-button type="primary" :disabled="notAbleToCreateTask">创建任务</el-button>
      </div>
    </el-col>
  </el-row>

  <el-table :data="tableData" style="width: 100%;margin: 1%;font-size: medium"
  @selection-change="handleSelectionChange" show-header 
  :header-cell-style="{fontSize: '14px', backgroundColor: '#f8f8f8',color:'#333'}">
    <el-table-column type="selection" :selectable="selectable" width="55" />
    <el-table-column fixed prop="date" label="规则序号" width="150" />
    <el-table-column prop="name" label="规则ID" width="120" />
    <el-table-column prop="state" label="规则文本" />
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

</template>

<script lang="ts" setup>
import {ref} from 'vue'

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

const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Home',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Office',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Home',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Office',
  },
]

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
</script>

<style scoped>
.button-group {
  text-align: right;
}
</style>