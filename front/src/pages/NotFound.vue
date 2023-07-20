<template>
    <div class="to-main">
        <router-link class="nav-menu__logo" to="/">
            <img src="../assets/img/logo.png" alt="Logo">
            <div class="corner-logo__1"></div>
            <div class="corner-logo__2"></div>
            <div class="corner-logo__3"></div>
            <div class="corner-logo__4"></div>
        </router-link>
    </div>
    <div>
        <h1>Страница не найдена</h1>
        <p>Извините, запрошенная страница не существует.</p>
    </div>
  </template>

<script>
export default {
  name: 'NotFound',
};
</script>

<style scoped>
.to-main {
    display: inline-flex;
    top: 1%;
    position: relative;
}

h1 {
    font-size: 2cm;
    color: aliceblue;
}

p {
    font-size: 1cm;
    color: brown;
}
</style>
