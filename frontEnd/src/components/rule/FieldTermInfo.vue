<template>
  <el-row :gutter="20" justify="space-between">
    <el-col :span="7">
      <div class="container">
        <div class="vocabulary-list">
          词汇列表
        </div>
        <div class="button-group">
          <el-button type="primary" :disabled="notAbleToAdd">批量导入</el-button>
          <el-button type="primary" :disabled="notAbleToDel">批量删除</el-button>
        </div>
      </div>

      <el-tree
        style="max-width: 600px;font-size: medium;margin-top: 3%;"
        :props="props"
        :data="data"
        show-checkbox
        @check-change="handleCheckChange"
        class="custom-tree"
      />
    </el-col>

    <el-col :span="15" :offset="2">
      <div class="vocabulary-list">
        词汇图片
      </div>
    </el-col>
  </el-row>

</template>

<script lang="ts" setup>
import {ref} from 'vue'
import type Node from 'element-plus/es/components/tree/src/model/node'

const notAbleToAdd = ref(true)
const notAbleToDel = ref(true)

const props = {
  children: 'children',
  label: 'label',
}

interface Tree {
  label: string
  children?: Tree[]
}

const handleCheckChange = (
  data: Tree,
  checked: boolean,
  indeterminate: boolean
) => {
  console.log(data, checked, indeterminate)
}

const data: Tree[] = [
  {
    label: 'Level one 1',
    children: [
      {
        label: 'Level two 1-1',
        children: [
          {
            label: 'Level three 1-1-1',
          },
        ],
      },
    ],
  },
  {
    label: 'Level one 2',
    children: [
      {
        label: 'Level two 2-1',
        children: [
          {
            label: 'Level three 2-1-1',
          },
        ],
      },
      {
        label: 'Level two 2-2',
        children: [
          {
            label: 'Level three 2-2-1',
          },
        ],
      },
    ],
  },
  {
    label: 'Level one 3',
    children: [
      {
        label: 'Level two 3-1',
        children: [
          {
            label: 'Level three 3-1-1',
          },
        ],
      },
      {
        label: 'Level two 3-2',
        children: [
          {
            label: 'Level three 3-2-1',
          },
        ],
      },
    ],
  },
]

</script>

<style scoped>
.button-group {
  text-align: right;
}
.container {
  display: flex;
  align-items: center; /* 垂直居中对齐 */
}
.vocabulary-list {
  font-size: x-large;
  font-weight: 600;
  margin: 1%;
  padding-left: 15px;
  position: relative;
}

.vocabulary-list:before {
  content: "";
  display: block;
  width: 4px;
  height: 24px;
  background: linear-gradient(180deg, #165DFF 0%, #6B97FC 100%);
  border-radius: 0 2px 2px 0;
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
}

.button-group {
  margin-left: auto; /* 将按钮组推到最右边 */
}
.el-button {
  margin-left: 20px; /* 按钮之间的间距 */
}
.el-button:first-child {
  margin-left: 0; /* 第一个按钮没有左边距 */
}

:deep(.el-tree-node) .el-checkbox{
  margin-left: 5px; /* 调整这个值来增加勾选框和文字间的间距 */
  margin-right: 10px;
}

:deep(.el-tree-node){
  margin-top: 1.5%;
}
</style>