<template>
  <div style="position: relative;width: 100%;height:100%">
    <div ref="container" style="background-color: rgb(242, 247, 250);"> </div>

    <transition name="fade">
      <el-cascader-panel
        v-if="showCascader"
        :options="relationOptions"
        v-model="selectedOption"
        @change="onCascaderChange"
        style="background-color: white;"
        :style="{ width: 'fit-content', position: 'absolute', left: `${cascaderPosition.x}px`, top: `${cascaderPosition.y}px`,boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)'}"
      />
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Graph } from '@antv/x6';

const container = ref<HTMLDivElement | null>(null);
let graph: Graph
const relationOptions = [
  {
    value: '关系',
    label: '关系',
    children: [
      { value: '与', label: '与' },
      { value: '或', label: '或' },
      { value: '非', label: '非' },
    ],
  },
  {
    value: '事件',
    label: '事件',
    children: [
      { value: '对象 行为', label: '对象 行为' },
      { value: '对象 行为 对象', label: '对象 行为 对象' },
      { value: '行为 对象', label: '行为 对象' },
    ],
  },
];

const selectedRelation = ref<string[]>([]);
const selectedEvent = ref<string[]>([]);

const showCascader = ref(false)
const selectedOption = ref([] as string[])
const cascaderPosition = ref({ x: 0, y: 0 })

const onCascaderChange = (value: string[]) => {
  if (value.length > 0 && graph.getSelectedCells().length > 0) {
    const selectedNode = graph.getSelectedCells()[0]
    if (selectedNode) {
      selectedNode.attr('label/text', value.join('/'))
    }
    showCascader.value = false
  }
}

onMounted(() => {
  if (!container.value) return;

  graph = new Graph({
    container: container.value,
    autoResize: true,
    height: 500,
    grid: true,
    interacting: {
      nodeMovable: false, // 禁止节点拖动
    },
    panning: {
      enabled: true,
      // modifiers 默认为空，这意味着不需要特殊键结合使用，例如使用 shift 可表示 "按住 Shift 键拖动"
    }
  });

  const startNode = graph.addNode({
    x: 40,
    y: 200,
    width: 80,
    height: 40,
    label: '关系 / 或',
    attrs: {
      body: {
        fill: '#ffffff', // 背景颜色
        stroke: '#e0e0e0', // 边框颜色
        strokeWidth: 1, // 边框宽度
        rx: 10, // 圆角半径
        ry: 10, // 圆角半径
      },
    },
  });

  const eventNode1 = graph.addNode({
    x: 200,
    y: 120,
    width: 120,
    height: 40,
    label: '事件 / 对象',
  });

  const eventNode2 = graph.addNode({
    x: 200,
    y: 280,
    width: 120,
    height: 40,
    label: '事件 / 对象',
  });

  const personNode1 = graph.addNode({
    x: 380,
    y: 120,
    width: 80,
    height: 40,
    label: '人员',
  });

  const personNode2 = graph.addNode({
    x: 380,
    y: 280,
    width: 80,
    height: 40,
    label: '人员',
  });

  graph.addEdge({
    source: { cell: startNode, anchor: { name: 'right', args: { dx: 10, dy: 0 } } },
    target: { cell: eventNode1, anchor: { name: 'left', args: { dx: -10, dy: 0 } } },
    connector: { name: 'rounded' }, // 可选：使用圆角连接器
  });

  graph.addEdge({
    source: { cell: startNode, anchor: { name: 'right', args: { dx: 10, dy: 0 } } },
    target: { cell: eventNode2, anchor: { name: 'left', args: { dx: -10, dy: 0 } } },
    connector: { name: 'rounded' }, // 可选：使用圆角连接器
  });

  graph.addEdge({
    source: eventNode1,
    target: personNode1,
    attrs: {
      line: {
        stroke: '#999',
      },
    },
  });

  graph.addEdge({
    source: eventNode2,
    target: personNode2,
    attrs: {
      line: {
        stroke: '#999',
      },
    },
  });

  graph.on('node:click', ({ e, x, y, node }) => {
    // 使用鼠标事件的 x 和 y 来定位下拉框
    // 获取节点的包围盒相对于画布的坐标
    const bbox = node.getBBox()
    // 将画布内的局部坐标转换为全局视口坐标
    const pan = graph.translate(); // 获取当前的平移偏移量

    cascaderPosition.value = {
      x: bbox.x + pan.tx,
      y: bbox.y + pan.ty + node.getSize().height + 5,
    }

    showCascader.value = true
    e.stopPropagation() // 防止事件冒泡影响
  })

  graph.on('blank:mousedown', ({ e }) => {
    showCascader.value = false
  })

  // 下拉框改变事件处理
  const onCascaderChange = (value: string[]) => {
    // 更新当前选中的节点的标签
    // 注意：你需要一种方式来跟踪哪个节点被点击了
    // 这里仅作为示例，实际上你需要根据实际情况来更新节点
    const selectedNode = graph.getSelectedCells()[0]; // 假设只选中了一个节点
    if (selectedNode) {
      selectedNode.setLabel(value.join('/'));
    }
    showCascader.value = false; // 关闭下拉框
  };

});
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.custom-node {
  border-radius: 5px;
  background-color: #673ab7;
  border: 1px solid #512da8;
  color: #673ab7;
  padding: 5px;
  text-align: center;
  font-size: 12px;
}
</style>