<template>
  <a-layout class="layout" style="width: 100%;">
    <a-layout-content style="padding: 0px 50px;">

      <bread style="margin: 1%;"/>
      
      <router-view />

    </a-layout-content>

  </a-layout>
</template>

<script lang="ts" setup>
import { defineComponent, ref } from 'vue';
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import bread from '../../../components/BreadCrumbRoute.vue'

</script>

<style scoped>

</style>