<template>
  <div v-for="(card, index) in infoCardData" :key="index" :class="'info-card__' + (index + 1)">
    <div class="info-card">
      <h3 class="info-card__text">
          {{ card.top }}
          <div class="info-card__number">
              {{ card.middle_number }}
              <span v-if="card.middle_text" class="info-card__year">
                  {{ card.middle_text }}
              </span>
          </div>
          {{ card.bottom }}
      </h3>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const token = 'Token <USER-TOKEN>';

export default {
  name: 'MainInfoCard',
  data() {
    return {
      infoCardData: [],
    };
  },
  created() {
    this.fetchInfoCardData();
  },
  methods: {
    fetchInfoCardData() {
      axios.get('http://localhost:8000/api/infocard/', {
        headers: { Authorization: token },
      })
        .then((response) => {
          this.infoCardData = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
