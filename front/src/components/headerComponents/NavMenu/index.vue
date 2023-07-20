<template>
    <div class="nav-menu">
      <router-link class="nav-menu__logo" to="/">
        <img src="../../../assets/img/logo.png" alt="Logo">
        <div class="corner-logo__1"></div>
        <div class="corner-logo__2"></div>
        <div class="corner-logo__3"></div>
        <div class="corner-logo__4"></div>
      </router-link>
      <div v-if="menuData && menuData.length > 0">
        <router-link v-for="link in menuData.slice(0, 6)" :key="link.id" class="nav-menu__link" :to="link.url">
          {{ link.title }}
        </router-link>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

const token = 'Token <USER-TOKEN>';

export default {
  name: 'NavMenu',
  data() {
    return {
      menuData: [],
    };
  },
  created() {
    this.fetchMenuData();
  },
  methods: {
    fetchMenuData() {
      axios.get('http://localhost:8000/api/menu/', {
        headers: { Authorization: token },
      })
        .then((response) => {
          this.menuData = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
