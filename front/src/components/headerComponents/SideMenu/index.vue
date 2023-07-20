<template>
    <div class="side-menu">
      <div class="app-menu">
        <div class="side-menu-nav">
          <div v-if="menuData && menuData.length > 0">
            <router-link v-for="link in menuData.slice(0, 6)" :key="link.id" class="side-menu__link" :to="link.url">
              {{ link.title }}
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <button class="side-menu-icon">
        <div class="icon-line"></div>
        <div class="icon-line"></div>
        <div class="icon-line"></div>
    </button>
</template>

<script>
import axios from 'axios';

const token = 'Token <USER-TOKEN>';

export default {
  name: 'SideMenu',
  methods: {
    toggleClassMenu() {
      this.myMenu.classList.add('side-menu--animatable');
      if (!this.myMenu.classList.contains('side-menu--visible')) {
        this.myMenu.classList.add('side-menu--visible');
      } else {
        this.myMenu.classList.remove('side-menu--visible');
      }
    },
    OnTransitionEnd() {
      this.myMenu.classList.remove('side-menu--animatable');
    },
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
  mounted() {
    this.myMenu = document.querySelector('.side-menu');
    this.oppMenu = document.querySelector('.side-menu-icon');
    this.myMenu.addEventListener('transitionend', this.OnTransitionEnd, false);
    this.oppMenu.addEventListener('click', this.toggleClassMenu, false);
    this.myMenu.addEventListener('click', this.toggleClassMenu, false);
  },
  data() {
    return {
      menuData: [],
    };
  },
  created() {
    this.fetchMenuData();
  },
};
</script>
