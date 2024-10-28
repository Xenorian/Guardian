<template>
  <a-card 
    hoverable
    style="width: 300px"
    @click="clickCard"
    >
    <template #cover>
      <img
        alt="example"
        src="../../assets/jail.jpeg"
      />
    </template>

    <template #actions>
      <edit-outlined key="edit" @click.stop="editCard"/>
      <DeleteOutlined key="del" @click.stop="delCard"/>
    </template>

    <a-card-meta title="看守所" description="公安看守场景异常行为检测">
      <template #avatar>
        <AimOutlined />
      </template>
    </a-card-meta>
  </a-card>


  <el-dialog
    v-model="editDialogVisible"
    title="编辑规则领域"
    width="35%"
    style="padding: 1.5%;"
  >
    <CardForm />
  </el-dialog>

  <el-dialog
    v-model="delDialogVisible"
    :show-close="false"
    width="35%"
    style="padding: 1.5%;"
  >
    <template #header="{ close, titleId, titleClass }">
      <div class="my-header">
        <h4 :id="titleId" :class="titleClass"> <ExclamationCircleOutlined style="margin-right: 3%;color: #FAAD14"/> 提示</h4>
      </div>
    </template>

    <span>是否确认删除该领域？</span>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="delDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="delDialogVisible = false">
          确定
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts" setup>
import { SettingOutlined, EditOutlined, EllipsisOutlined,AimOutlined, DeleteOutlined, ExclamationCircleOutlined } from '@ant-design/icons-vue';
import { ref,reactive } from 'vue'
import { useRouter,useRoute } from 'vue-router';

import CardForm from './CardForm.vue'

const router = useRouter();
const route = useRoute();
const segments = route.path.split('/');
segments.pop(); // 移除最后一段
const newPath = segments.join('/') + '/field';

const editDialogVisible = ref(false)
const delDialogVisible = ref(false)

function editCard(){
  editDialogVisible.value = true
}

function delCard(){
  delDialogVisible.value = true
}

function clickCard(){
  router.push({ path: newPath })
}

const ruleFormRef = ref(null);
const rules = reactive({
  name: [
    { required: true, message: '请输入规则领域名称', trigger: 'blur' }
  ],
  describe: [
    { required: true, message: '请输入规则领域描述', trigger: 'blur' }
  ],
  cover: [
    { required: true, message: '请上传规则领域封面', trigger: 'change' }
  ]
});

const submitForm = (formEl) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      ElMessage.success('提交成功');
      // 这里可以添加提交表单的逻辑
    } else {
      ElMessage.error('请检查表单信息');
      return false;
    }
  });
};

const resetForm = (formEl) => {
  if (!formEl) return;
  formEl.resetFields();
};

</script>