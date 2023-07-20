<template>
    <div class="space-x__body">
        <div class="space-x__body-left">
            <button class="main-button__get-start">
                Начать путешествие
            </button>
            <div class="main-button__corner-1"></div>
            <div class="main-button__corner-2"></div>
        </div>
        <div class="space-x__body-right">
            <MainInfoCard />
        </div>
    </div>
</template>

<script>
import MainInfoCard from '../../components/bodyComponents/MainInfoCard/index.vue';

export default {
  name: 'BodyComponent',
  components: {
    MainInfoCard,
  },
};
</script>
