<template>
  <HeaderComponent />
  <BodyComponent />
</template>

<script>
import HeaderComponent from '@/layout/header/index.vue';
import BodyComponent from '@/layout/body/index.vue';

export default {
  name: 'MainPage',
  components: {
    HeaderComponent,
    BodyComponent,
  },
};
</script>
