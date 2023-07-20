<template>
    <div class="space-x__header">
        <NavMenu />
        <SideMenu />
    </div>
</template>

<script>
import NavMenu from '../../components/headerComponents/NavMenu/index.vue';
import SideMenu from '../../components/headerComponents/SideMenu/index.vue';

export default {
  name: 'HeaderComponent',
  components: {
    NavMenu,
    SideMenu,
  },
};
</script>
